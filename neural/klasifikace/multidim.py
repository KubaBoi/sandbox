import sklearn.datasets
import sklearn.model_selection
import sklearn.metrics
import matplotlib.pyplot as plt
import numpy as np

# Definování funkce sign
def sign(x):
    return 0 if x < 0 else 1

# GENEROVÁNÍ DAT
data, classes = sklearn.datasets.make_blobs(
    n_samples=1000,
    n_features=10,
    centers=2,
    random_state=42
)
data = np.hstack([data, np.ones((data.shape[0],1))])

train_data, test_data, train_classes, test_classes = sklearn.model_selection.train_test_split(data, classes, test_size=0.15)

# TRÉNINK PERCEPTRONU
weights = np.random.RandomState(42).uniform(-2, 2, 11)
old_weights = None
while (weights != old_weights).any():
    old_weights = weights
    for instance, target in zip(train_data, train_classes):
        prediction = sign(instance @ weights)
        weights = weights + (target - prediction) * instance

# TEST
predictions = [sign(instance @ weights) for instance in test_data]
print(f'Přesnost: {sklearn.metrics.accuracy_score(test_classes, predictions)}')