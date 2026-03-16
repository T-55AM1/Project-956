año = int(input("dime el año: "))

if año < 1582:
	print("No encontrado en el calendario gregoriano")
else:
	if año % 4 != 0:
		print("año comun")
	elif año % 100 != 0:
		print("año bisiesto")
	elif año % 400 != 0:
		print("año comun")
	else:
		print("año bisiesto")
