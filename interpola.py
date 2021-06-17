import scipy.interpolate

#Valores de referencia
x = [1,6,19,37,50]
y = [4500, 8750, 11685, 7420, 19850]

#Solicita número del mes en el que deseamos realizar la previsión
numero= input("Introduce el mes de previsión: ")

#try/except para controlar si se introduce un carácter no válido
try:
    y_interp = scipy.interpolate.interp1d(x, y)
    print (y_interp(numero))
except:
    print ("Por favor, debes introducir un número entero válido, entre 1 y 50")
