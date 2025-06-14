import pickle
import os
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class DataAnalysisAgent:
    def __init__(self, name, message_bus, monitor, model_path="model.pkl"):
        self.name = name
        self.message_bus = message_bus
        self.monitor = monitor
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        if os.path.exists(self.model_path):
            with open(self.model_path, "rb") as f:
                return pickle.load(f)
        return LinearRegression()

    def save_model(self):
        with open(self.model_path, "wb") as f:
            pickle.dump(self.model, f)

    def handle_task(self, task):
        task_type = task.get("type")
        if task_type == "regression_request":
            x_data = np.array(task["data"]["x"]).reshape(-1, 1)
            y_data = np.array(task["data"]["y"])
            self.model.fit(x_data, y_data)
            self.save_model()
            prediction = self.model.predict([[4]])[0]
            from math import sqrt
            mse = mean_squared_error(y_data, self.model.predict(x_data))
            accuracy = sqrt(mse)
            return f"Regression complete. Prediction: {prediction:.2f}, RMSE: {accuracy:.2f}"
        return None

