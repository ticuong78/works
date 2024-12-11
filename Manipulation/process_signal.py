import pandas as pd
import numpy as np

important_number = np.pow(2, 13)

def process_signal(file_path: str):
    # Read data from files
    data = np.fromfile(file_path, dtype=np.uint8)

    # Calculate len of data and split into chunks
    len_of_data = len(data)
    slices = [data[i : i + important_number] for i in range(0, len_of_data, important_number)]

    # bit-padding the last chunk
    pad_set = [np.uint8(0) for i in range(0, important_number - len(slices[-1]))]
    slices[-1] = np.concatenate((slices[-1], pad_set))

    # Initialize result array
    result = np.array(object=[], dtype=np.uint16)

    # Summing chunks and store it in "result" array
    for slice in slices:
        if len(result) < important_number:
            result = slice
        else:
            result += slice

    # normalize data
    normalized_result = (result - result.min()) / (result.max() - result.min())

    return normalized_result
