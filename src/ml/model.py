import pickle
from sklearn.linear_model import LinearRegression

class PredictiveModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def save(self, path="model.pkl"):
        with open(path, "wb") as f:
            pickle.dump(self.model, f)

    def load(self, path="model.pkl"):
        with open(path, "rb") as f:
            self.model = pickle.load(f)
