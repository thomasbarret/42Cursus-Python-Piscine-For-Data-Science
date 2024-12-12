from load_image import ft_load
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def zoom_image(image, start_x, start_y, size):
    """
    Zoom into the image by slicing it around a specified region.

    Parameters:
        image (np.ndarray): The original image as a NumPy array.
        start_x (int): Starting X coordinate for slicing.
        start_y (int): Starting Y coordinate for slicing.
        size (int): Width and height of the zoomed area.

    Returns:
        np.ndarray: The zoomed (cropped) image.
    """
    return image[start_y:start_y + size, start_x:start_x + size]


def display_image(image):
    """
    Display an image using matplotlib.

    Parameters:
        image (np.ndarray): The image to display.
    """
    try:
        matplotlib.use('TkAgg')
        plt.imshow(image, cmap="gray")
        plt.colorbar()
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.show()
    except KeyboardInterrupt:
        plt.close()


if __name__ == "__main__":
    try:
        image_path = "animal.jpeg"
        image = np.array(ft_load(image_path))

        if image.ndim == 3:
            grayscale_image = np.mean(image, axis=2).astype(int)
        else:
            grayscale_image = image

        print(grayscale_image)

        start_x = 453  # Custom starting X coordinate
        start_y = 100  # Custom starting Y coordinate
        zoom_size = 400  # Zoom size (both width and height)

        start_x = min(start_x, grayscale_image.shape[1] - zoom_size)
        start_y = min(start_y, grayscale_image.shape[0] - zoom_size)

        zoomed_image = zoom_image(
            grayscale_image,
            start_x=start_x, start_y=start_y,
            size=zoom_size
        )
        print(f"New shape after slicing: ({zoom_size}, {zoom_size}, 1) "
              f"or ({zoom_size}, {zoom_size})")

        print(zoomed_image)

        display_image(zoomed_image)

    except Exception as e:
        print(f"An error occurred: {e}")
