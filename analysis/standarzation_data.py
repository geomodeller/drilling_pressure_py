import numpy as np
from sklearn.preprocessing import MinMaxScaler

def standarzation_data(*args):
    scaler = MinMaxScaler()
    standarzatied_data = []
    for data in args:
        data_np = np.array(data) 
        standarzatied_data.append(scaler.fit_transform(data_np.reshape(-1, 1)).flatten())
    return standarzatied_data