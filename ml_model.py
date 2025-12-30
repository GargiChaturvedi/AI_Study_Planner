import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([
    [1, 5, 3, 5],
    [2, 4, 2, 4],
    [5, 3, 2, 3],
    [7, 2, 1, 2],
    [10, 1, 1, 1]
])

y = np.array([9, 8, 6, 4, 2])

model = LinearRegression()
model.fit(X, y)

def predict_priority(days_left, difficulty, time_required, user_priority):
    features = np.array([[days_left, difficulty, time_required, user_priority]])
    return round(model.predict(features)[0], 2)
