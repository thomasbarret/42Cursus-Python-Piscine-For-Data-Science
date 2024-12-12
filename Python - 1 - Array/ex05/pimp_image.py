import numpy as np
from load_image import ft_load
import matplotlib
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """
    Inverts the colors of the image by subtracting each pixel value from 255.

    Parameters:
        array (np.ndarray): The input image array.

    Returns:
        np.ndarray: The color-inverted image array.
    """
    return [[255 - pixel for pixel in row] for row in array]


def ft_red(array) -> np.ndarray:
    """
    Applies a red filter by zeroing out the green and blue channels.

    Parameters:
        array (np.ndarray): The input image array.

    Returns:
        np.ndarray: The red-filtered image array.
    """
    red_array = [[[pixel[0], 0, 0] for pixel in row] for row in array]
    return red_array


def ft_green(array) -> np.ndarray:
    """
    Applies a green filter by zeroing out the red and blue channels.

    Parameters:
        array (np.ndarray): The input image array.

    Returns:
        np.ndarray: The green-filtered image array.
    """
    green_array = [[[0, pixel[1], 0] for pixel in row] for row in array]
    return green_array


def ft_blue(array) -> np.ndarray:
    """
    Applies a blue filter by zeroing out the red and green channels.

    Parameters:
        array (np.ndarray): The input image array.

    Returns:
        np.ndarray: The blue-filtered image array.
    """
    blue_array = [[[0, 0, pixel[2]] for pixel in row] for row in array]
    return blue_array


def ft_grey(array) -> np.ndarray:
    """
    Converts the image to grayscale by averaging the red,
    green, and blue channels.

    Parameters:
        array (np.ndarray): The input image array.

    Returns:
        np.ndarray: The grayscale image array.
    """
    grey_array = [[int(sum(pixel) / 3) for pixel in row] for row in array]
    return grey_array


if __name__ == "__main__":
    image_path = "landscape.jpg"
    array = np.array(ft_load(image_path))

    print(f"The shape of image is: {np.array(array).shape}")
    print(array)

    original_image = array
    inverted_image = ft_invert(array)
    red_image = ft_red(array)
    green_image = ft_green(array)
    blue_image = ft_blue(array)
    grey_image = ft_grey(array)

    filters = [
        original_image,
        inverted_image,
        red_image,
        green_image,
        blue_image,
        grey_image
    ]
    titles = ["Original", "Invert", "Red", "Green", "Blue", "Grayscale"]

    for i, img in enumerate(filters):
        try:
            matplotlib.use('TkAgg')
            plt.figure()
            if titles[i] == "Grayscale":
                plt.imshow(img, cmap="gray")
            else:
                plt.imshow(img)
            plt.title(titles[i])
            plt.show()
        except KeyboardInterrupt:
            plt.close()
            break
