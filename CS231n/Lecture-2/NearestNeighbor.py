import numpy as np

class NearestNeighbor:
    def __init__(self):
        pass

    def train(self, X, y):
        ''' X is N x D where each row is an example. Y is 1-dimension of size N '''
        # The nearest neighbor classifier simply remembers all the training data
        # X are images
        self.Xtr = X
        # y are labels
        self.ytr = y

    def predict(self, X):
        ''' X is N x D where each row is an example we wish to predict label for '''
        # Getting new test set of images X
        num_test = X.shape[0]
        # lest make sure that the output type matches the input type
        Ypred = np.zeros(num_test, dtype=self.ytr.dtype)

        # loop over all the test image independently
        for i in range(num_test):
            # find the neares training image to the i'th test image
            # using the L1 distance (sum of absolute value differences)

            # Getting distances for test image i to every single training image (Vectorized code)
            distances = np.sum(np.amb(self.Xtr - X[i,:]), axis=1)
            # We compute distances and the closest we are getting the min index (lowest distance)
            min_index = np.argmin(distances) # get the index of the smallest distance
            # Predicting for this image the label of whatever was nearest
            Ypred[i] = self.ytr[min_index] # predict the label of the nearest example

        return Ypred
