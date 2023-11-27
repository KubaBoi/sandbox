import sklearn.datasets
import sklearn.model_selection
import sklearn.metrics
import matplotlib.pyplot as plt
import numpy as np

# Definování funkce sign
def sign(x):
    return 0 if x < 0 else 1

data, classes = sklearn.datasets.make_blobs(
    n_samples=10,
    n_features=2,
    centers=[[-1,0.4],[1,0.6]],
    cluster_std=0.8,
    random_state=82
)
plt.scatter(data[:,0], data[:,1], c=classes)
plt.show()

# TRÉNINK PERCEPTRONU
# Inicializace vah
weights = np.random.RandomState(42).uniform(size=2)

# Opakování až do konvergence
weights_changed = True
while weights_changed:
    weights_changed = False
    # pro každou instanci v datech
    for instance, target in zip(data, classes):
        # predikce výstupu perceptronu
        prediction = sign(instance @ weights)
        # aktualizace vah
        weights_new = weights + (target - prediction) * instance

        # vykreslení změny
        if (weights != weights_new).any():
            slope = - weights[0] / weights[1]  # vypočítání sklonu
            plt.figure(figsize=(8, 5))
            plt.plot(
                [data.min(axis=0)[0], data.max(0)[0]],
                [slope * data.min(axis=0)[0], slope * data.max(axis=0)[0]],
                c='r')  # vykreslení dělící nardoviny
            plt.plot([0, weights[0]],[0, weights[1]], c='black')  # vykreslení normály
            plt.scatter(data[:,0], data[:,1], c=classes)  # vykreslení dat
            plt.scatter(instance[0], instance[1], c='g')  # vykreslení chybně klasifikované instance
            plt.plot([0, instance[0]], [0, instance[1]], c='g', alpha=0.4)  # vykreslení instančního vektoru
            plt.plot(
                [weights[0], weights[0] + (target - prediction) * instance[0]],
                [weights[1], weights[1] + (target - prediction) * instance[1]],
                c='g', alpha=0.4)  # vykreslení instančního vektoru z normály
            plt.plot(
                [0, weights[0] + (target - prediction) * instance[0]],
                [0, weights[1] + (target - prediction) * instance[1]],
                c='c', alpha=0.4)  # vykreslení nové normály
            slope_new = - weights_new[0] / weights_new[1]  # výpočet sklonu nové přímky
            plt.plot(
                [data.min(axis=0)[0], data.max(0)[0]],
                [slope_new * data.min(axis=0)[0], slope_new * data.max(axis=0)[0]],
                c='r', alpha=0.2)  # vykreslení dělící nadroviny
            plt.axis('equal')
            plt.ylim(-2,4)
            plt.show()

        weights_changed = weights_changed or (weights != weights_new).any()
        weights = weights_new

# VYKRESLENÍ KONEČNÝCH VAH
slope = - weights[0] / weights[1]
plt.figure(figsize=(8, 5))
plt.scatter(data[:,0], data[:,1], c=classes)
plt.plot(
    [data.min(axis=0)[0], data.max(0)[0]],
    [slope * data.min(axis=0)[0], slope * data.max(axis=0)[0]],
    c='r')
plt.show()