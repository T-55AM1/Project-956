#millas a kilometros lo que hice
milla = 1.6
kilometro = 1
kilometro *= milla
print(kilometro)
milla /= kilometro
print(milla)
#solucion real
kilometros = 12.25
millas = 7.38
km_a_milles = millas * 1.6
millas_a_km = kilometros / 1.6
print("km a millas: ", km_a_milles)
print("millas a km: ", millas_a_km)
print("Redondeos")
print("km a millas: ", round(km_a_milles, 2), "km")
print("millas a km: ", round(millas_a_km, 2), "millas")
