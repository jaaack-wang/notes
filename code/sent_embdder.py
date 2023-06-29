import pandas as pd
import plotly.express as px
from sklearn.manifold import TSNE
from knn import knn_train, find_closest_centroids
from sentence_transformers import SentenceTransformer, util


class SentenceEmbedder:
    
    def __init__(self, sentences, model_name="all-MiniLM-L6-v2"):
        self.sentences = sentences
        self.model = SentenceTransformer(model_name)
        self.sent_embds = self.encode(sentences)
        self.sent_pairs_with_score = []
        self.__centroids = None
        self.sent_knn_class = dict()
        
    def encode(self, text):
        return self.model.encode(text)
    
    def _t_sne_embeddings(self, embds=None, dim=2, perplexity=None):
        if embds is None:
            embds = self.sent_embds
        
        if perplexity is None:
            perplexity = n // 2
        
        tsne = TSNE(n_components=dim, perplexity=perplexity)
        X = tsne.fit_transform(embds)
        return X
    
    def t_sne_2d(self, perplexity=None, labels=None):
        
        n = len(self.sent_embds)            
        X = self._t_sne_embeddings(perplexity=perplexity)
        df = pd.DataFrame(X).rename(columns={0:'x', 1:'y'})
        
        if not labels:
            labels = list(map(str, range(1, n+1)))
        
        df = df.assign(label=labels)
        df = df.assign(text=self.sentences)
        
        fig = px.scatter(df, x='x', y='y', 
                         color='label', 
                         hover_data=['text'], 
                         labels={'color': 'label'},
                         title = '2-d t-SNE visualization')
        fig.show()
        
    def sort_similar_sentences(self, sim_func=util.cos_sim, 
                               reverse=True, output=True):
        
        scores = sim_func(self.sent_embds, self.sent_embds)
        
        n = len(scores)
        self.sent_pairs_with_score = []
        
        for i in range(n-1):
            for j in range(i+1, n):
                s1, s2 = self.sentences[i], self.sentences[j]
                self.sent_pairs_with_score.append([s1, s2, scores[i, j]])
        
        self.sent_pairs_with_score.sort(key=lambda x: x[-1], 
                                        reverse=reverse)
        
        if output:
            return self.sent_pairs_with_score
    
    def top_n_similar_sentence_pairs(self, n):
        if not self.sent_pairs_with_score:
            self.sort_similar_sentences(output=False)
        
        return self.sent_pairs_with_score[:n]
    
    
    def __get_knn_class(self, sentences, idx):
        
        out = dict()
        for ix, c in enumerate(idx):
            key = f"Class {c}"
            if key not in out:
                out[key] = [sentences[ix]]
            else:
                out[key].append(sentences[ix])
        
        return out
        
    
    def train_knn(self, k, X=None, 
                  max_iters=10, print_loss=False):
        
        if X is None:
            X = self.sent_embds
        
        self.__centroids, idx, loss = knn_train(X, k, max_iters, 
                                                print_loss=print_loss)
        self.sent_knn_class = self.__get_knn_class(self.sentences, idx)
    
    def classify_knn(self, sentences, class_only=False):
        if self.__centroids is None:
            raise RuntimeError("Please train a knn classifier" \
                              "first by calling self.train_knn(k)")
        
        if isinstance(sentences, str):
            sentences = [sentences]
        
        embd = self.encode(sentences)
        idx, _ = find_closest_centroids(embd, self.__centroids)
        
        if class_only:
            return idx
        return self.__get_knn_class(sentences, idx)
