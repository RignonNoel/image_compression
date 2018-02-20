from PIL import Image

class Compressor:
    """This class is used to compress image"""

    _width = None
    _height = None
    _path = None

    def __init__(self, path_image):
        self._path = path_image

        image = Image.open(self._path)
        self._width, self._height = image.size

    def get_matrice(self):
        """Return an array that represent the image"""
        image = Image.open(self._path)
        pixels = image.load()

        matrice = self.create_empty_matrice(self._width, self._height)

        for id_line in range(self._width):
            for id_column in range(self._height):
                matrice[id_column][id_line] = pixels[id_line, id_column]

        return matrice

    def minify(self, size_bloc):
        """
        Minify the image to a new size
        :param size_bloc: The size of the bloc used to make an average
        :return: A new image minified
        """
        assert self._width % size_bloc == 0, "'size_bloc' need to be a denominator of the image's width"
        assert self._height % size_bloc == 0, "'size_bloc' need to be a denominator of the image's height"

        new_width = self._width // size_bloc
        new_height = self._height // size_bloc
        new_matrice = self.create_empty_matrice(new_width, new_height)

        matrice = self.get_matrice()

        for column in range(new_width):
            for line in range(new_height):
                block = self.crop(matrice, line*size_bloc, column*size_bloc, size_bloc, size_bloc)
                new_matrice[line][column] = self.block_average(block)

        return new_matrice

    def crop(self, matrice, line, column, width, height):
        """
        Crop/cut a part of a matrice
        :param matrice: The matrice we want to cut
        :param position_x: The position in x of the part we want to cut
        :param position_y: The position in y of the part we want to cut
        :param width: The width of the part we want to cut
        :param height: The height of the part we want to cut
        :return: The sub-matrice cutted from the original
        """
        block = self.create_empty_matrice(width, height)
        for id_line in range(width):
            for id_column in range(height):
                block[id_line][id_column] = matrice[line + id_line][column + id_column]

        return block

    @staticmethod
    def create_empty_matrice(width, height):
        """
        Create an empty matrice of the given dimension
        :param width: The width of the new matrice
        :param height: The height of the new matrice
        :return: A new emply matrice (None inside)
        """
        matrice = [None] * height
        for line in range(height):
            matrice[line] = [None] * width
        return matrice

    @staticmethod
    def block_average(block):
        """
        Return the average value of a matrice
        :param block: The matrice you want to average
        :return: An average value
        """
        total = [0, 0, 0]
        count = 0
        for line in block:
            for elem in line:
                count += 1
                total[0] += elem[0]
                total[1] += elem[1]
                total[2] += elem[2]

        total[0] = int(total[0]/count)
        total[1] = int(total[1]/count)
        total[2] = int(total[2]/count)

        return tuple(total)

    @staticmethod
    def render(matrice, new_path):
        """
        Create a new image from a matrice
        :param matrice: The matrice we want to render
        :param new_path: The path to save the new image
        :return: A new image
        """
        height = len(matrice)
        width = len(matrice[0])

        image = Image.new('RGB', (width, height))
        pixels = image.load()

        for line in range(height):
            for column in range(width):
                pixels[column, line] = matrice[line][column]

        image.save(new_path)
