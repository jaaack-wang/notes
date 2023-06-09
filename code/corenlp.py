'''
- Author: Zhengxiang (Jack) Wang 
- GitHub: https://github.com/jaaack-wang
- Website: https://jaaack-wang.eu.org
'''
from stanfordcorenlp import StanfordCoreNLP
import json


class CoreNLP:
    
    def __init__(self, props, local_host='http://localhost', port=9999,
                 whitespace_based=False, split_hyphen=False, step=5000):
        
        self._nlp = StanfordCoreNLP(local_host, port)
        self.props = props
        if whitespace_based: 
            self.props['tokenize.whitespace'] = 'true'
        else:
            self.props['tokenize.whitespace'] = 'false'
        if split_hyphen:
            self.props['tokenize.options'] = "splitHyphenated=true"
        else:
            self.props['tokenize.options'] = "splitHyphenated=false"
        self._step = step
        self._text = ''
        self._has_percent = False
    
    def _annotating(self, text):
        '''Annotating given text based on preset properties (annotating setups).'''
        try:
            annotated_text = self._nlp.annotate(text, properties=self.props)
            return json.loads(annotated_text)
        
        except Exception as e:
            print("\033[32mTokenizingError: \033[0m", e)
            if "Expecting value: line 1 column 1 (char 0)" in str(e):
                
                print("Trying to re-do the process by narrowing the slicing steps by 500. Was: %i. Now: %i" 
                 % (self._step, int(self._step * 0.75)))
                self._step = int(self._step * 0.75)
                return
            
    def _text_annotating(self, text):
        
        self._text = text
        annotated_text = []
        if len(text) <= 100000:
            annotated_text.append(self._annotating(text))
        else:
            tokens = text.split()
            for i in range(0, len(tokens), self._step):
                sub_text = ' '.join(tokens[i: i + self._step])
                rturn = self._annotating(sub_text)
                if rturn:
                    annotated_text.append(rturn)
                else:
                    return 
                
        return annotated_text
    
    def get_annotated_text(self, text):
        '''Auto-adjust the slicing steps when needed to get the final annotated text.'''
        
        annotated_text = []
        while not annotated_text:
            annotated_text = self._text_annotating(text)
            if self._step == 0:
                print("Text cannot be annotated. Please check whether if it has spaces or if" \
                      "it contains special symbols that cannot be annotated via server.")
                break
            
        self._step = 5000
        return annotated_text


class stanfordAnnotator(CoreNLP):
    
    def __init__(self, local_host='http://localhost', port=9999,
                 whitespace_based=True, split_hyphen=False, step=5000):
        props = {'annotators': 'tokenize,ssplit,pos,lemma', 'outputFormat': 'json'}
        super().__init__(props, local_host, port, whitespace_based, split_hyphen, step)
               
    def get_tks_with_pos(self, text, out_str=True):
        annotated_text = self.get_annotated_text(text)
        pos, tks = [], []
        try:
            for t in annotated_text:
                for s in t['sentences']:
                    for token in s['tokens']:
                        pos.append(token['pos'])
                        tks.append(token['originalText'])
            
            if out_str:
                return " ".join([f"{t}_{p}" for t, p in zip(tks, pos)])
            return tks, pos
            
        except Exception as e:
            print(e)
