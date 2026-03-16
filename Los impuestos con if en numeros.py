entrada = float(input("introduce el impuesto: "))

if entrada < 85528:
	wow = entrada * 0.18 - 556.02
else:
	wow = (entrada - 85528) * 0.32 + 14839.02

if wow < 0.0:
	wow = 0.0

wow = round(wow, 0)
print("el impuesto es:", wow, "moneditas")
