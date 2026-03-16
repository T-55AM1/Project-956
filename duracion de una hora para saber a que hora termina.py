hora = int(input("hora:"))
mins = int(input("minutos:"))
dura = int(input("duracion:"))
mins = mins + dura
hora = hora + mins // 60
mins = mins % 60
hora = hora % 24
print("finaliza a las:", hora,":", mins, sep='')

