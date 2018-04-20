from compressor import Compressor

compressor = Compressor("static/test.png")

print('')
print("====================")
print("=      MATRICE     =")
print("====================")
print('')
matrice = compressor.get_matrice()
for line in matrice:
    print(line)

print('')
print("====================")
print("=       ARRAY      =")
print("====================")
print('')
print(compressor.get_array())
