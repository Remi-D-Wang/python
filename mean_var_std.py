import numpy as np

def calculate(list):
    if len(list)!=9:
        raise ValueError('List must contain nine numbers.')
    # Convert the list to array
    arr = np.array(list).reshape(3,3)
    # mean, variance, standard deviation, max, min, and sum
    # Row
    mean_row = np.mean(arr, axis=1)
    var_row = np.var(arr, axis=1)
    std_row = np.std(arr, axis=1)
    max_row = np.max(arr, axis=1)
    min_row = np.min(arr, axis=1)
    sum_row = np.sum(arr, axis=1)

    # Column
    mean_c = np.mean(arr, axis=0)
    var_c = np.var(arr, axis=0)
    std_c = np.std(arr, axis=0)
    max_c = np.max(arr, axis=0)
    min_c = np.min(arr, axis=0)
    sum_c = np.sum(arr, axis=0)

    # Flatten
    flat_arr = arr.flatten()
    mean_f = np.mean(flat_arr)
    var_f = np.var(flat_arr)
    std_f = np.std(flat_arr)
    max_f = np.max(flat_arr)
    min_f = np.min(flat_arr)  
    sum_f = np.sum(flat_arr)


    calculations = {
        'mean':[mean_c.tolist(),mean_row.tolist(),mean_f],
        'variance':[var_c.tolist(),var_row.tolist(),var_f],
        'standard deviation':[std_c.tolist(),std_row.tolist(),std_f],
        'max':[max_c.tolist(),max_row.tolist(),max_f],
        'min':[min_c.tolist(),min_row.tolist(),min_f],
        'sum':[sum_c.tolist(),sum_row.tolist(),sum_f]
    }


    return calculations
    
