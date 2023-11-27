import sklearn.datasets
import sklearn.model_selection
import sklearn.metrics
import matplotlib.pyplot as plt
import numpy as np

# Definování funkce sign
def sign(x):
    return 0 if x < 0 else 1

# GENEROVÁNÍ DAT
data, classes = sklearn.datasets.make_blobs(n_samples=100, n_features=2, centers=2, random_state=42)

# TRÉNINK PERCEPTRONU
# Inicializace vah
weights = np.random.RandomState(42).uniform(-2, 2, 2)

# Opakování až do konvergence
old_weights = None
while (weights != old_weights).any():
    old_weights = weights

    # pro každou instanci v datech
    for instance, target in zip(data, classes):
        # predikce výstupu perceptronu
        prediction = sign(instance @ weights)
        # aktualizace vah
        weights = weights + (target - prediction) * instance

# VYKRESLENÍ
slope = - weights[0] / weights[1]
plt.scatter(data[:,0], data[:,1], c=classes)
plt.plot(
    [data.min(axis=0)[0], data.max(0)[0]],
    [slope * data.min(axis=0)[0], slope * data.max(axis=0)[0]],
    c='r')
plt.show()