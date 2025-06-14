import numpy as np
from model import PredictiveModel

def generate_dummy_data(samples=100):
    # Generate some linear data: y = 2x + noise
    X = np.random.rand(samples, 1) * 100
    y = 2 * X.flatten() + np.random.randn(samples) * 5
    return X, y

def train_and_save_model():
    X, y = generate_dummy_data()
    model = PredictiveModel()
    model.train(X, y)
    model.save()
    print("Model trained and saved as model.pkl")

if __name__ == "__main__":
    train_and_save_model()
