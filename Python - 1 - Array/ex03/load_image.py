import numpy as np
from PIL import Image


def ft_load(path: str) -> list[list]:
    if not isinstance(path, str):
        raise ValueError("The 'path' parameter must be a string.")
        
    if not path.endswith(".jpg") and not path.endswith(".jpeg"):
        raise ValueError("The 'path' parameter must be a JPG or JPEG file.")
    
    try:
        data = Image.open(path)
    except FileNotFoundError:
        raise ValueError("The file does not exist.")
    
    np_data = np.array(data)
    
    print(f"The shape of image is: {np_data.shape}")
    
    return np_data.tolist()

