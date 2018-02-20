from compressor import Compressor

compressor = Compressor("static/test_1023.png")

new_matrice = compressor.minify(11)
compressor.render(new_matrice, "test.png")
