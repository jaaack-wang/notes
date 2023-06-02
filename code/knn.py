import numpy as np


def random_centroid(X, k, seed=1):
    np.random.seed(seed)
    idx = np.random.permutation(len(X))
    return X[idx[:k]]


def find_closest_centroids(X, centroid):
    k, m = centroid.shape[0], X.shape[0]
    idx = np.zeros(m, dtype=np.int16)
    loss = 0
    
    for i in range(m):
        dst = np.sum(np.square(centroid - X[i]), axis=1)
        idx[i] = np.argmin(dst)
        loss += np.min(dst)
    
    loss /= m    
    return idx, loss


def update_centroids(X, idx, k):
    m, n = X.shape
    centroids = np.zeros((k, n))
    
    for j in range(k):
        points = [i for i, x in enumerate(idx) if x == j]
        centroids[j] = np.mean(X[points], axis=0)
    
    return centroids


def knn_train(X, k, max_iters=10, seed=1, print_loss=False):
    centroids = random_centroid(X, k, seed)
    prev_loss = float("inf")
    
    for i in range(max_iters):
        idx, loss = find_closest_centroids(X, centroids)
        centroids = update_centroids(X, idx, k)
        
        if abs(loss - prev_loss) < 1e-8:
            break
        else:
            prev_loss = loss
        
        if print_loss:
            print(f"Iter: {i+1}; Loss: {loss}")
        
    return centroids, idx, loss
