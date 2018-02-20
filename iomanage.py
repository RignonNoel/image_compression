import pickle
import os

class IOManage:
    """This class help you save matrix image in a file text"""

    _path = None

    def __init__(self, path):
        self._path = path

    # writre in the file
    def set_file(self, data):
        # destroy file if exist
        self.del_file()
        # open file
        with open(self._path, 'wb') as file:
            try:
                my_pickler = pickle.Pickler(file)
                my_pickler.dump(data)
            except EOFError:
                print(EOFError.message)

    # read a file
    def get_file(self):
        matrix = []
        with open(self._path, 'rb') as file:
            try:
                my_depickler = pickle.Unpickler(file)
                matrix = my_depickler.load()
            except EOFError:
                print(EOFError.message)

        return matrix


    # destroy a file
    def del_file(self):
        if(os.path.isfile(self._path)):
            os.rmdir(self._path)
        else:
            print("the file matrix.txt not exist")
