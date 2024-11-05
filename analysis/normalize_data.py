import numpy as np
from sklearn.preprocessing import StandardScaler

def normalize_data(*args):
    scaler = StandardScaler()
    normalized_data = []
    for data in args:
        data_np = np.array(data) 
        normalized_data.append(scaler.fit_transform(data_np.reshape(-1, 1)).flatten())
    return normalized_data