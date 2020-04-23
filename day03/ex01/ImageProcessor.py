import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImageProcessor:
    @staticmethod
    def load(path):
        img = mpimg.imread(path)
        print(*img.shape)
        return img

    @staticmethod
    def display(array):
        plt.imshow(array)
        plt.show()