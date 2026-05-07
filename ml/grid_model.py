from sklearn.ensemble import RandomForestClassifier

class GridModel:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, voltage, current, load):
        return self.model.predict([[voltage, current, load]])[0]