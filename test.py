import numpy as np

mask = np.random.choice((0, 1), size=(3, 2, 3), replace=True, p=[0.5, 0.5])
print(mask)
