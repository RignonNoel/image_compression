from compressor import Compressor
from iomanage import IOManage

compressor = Compressor("static/test_2.png")

# new_matrice = compressor.minify(11)
# compressor.render(new_matrice, "test.png")

# test file save
new_matrice = compressor.get_matrice()
# print(new_matrice)
ioflux = IOManage("static/matrix.txt")

#ioflux.set_file(new_matrice)
print(ioflux.get_file())



