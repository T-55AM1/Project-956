numero_secreto = 777 #constante

print(
"""
+================================+
| Vienvenido a my juego          |
|adivina o queda atrapado        |
|¿cual es el numero secreto?     |
+================================+
""")
while  True: #condicion de bucle
    num = int(input("pon un numero..."))

    if num == numero_secreto: #primer if
         print("felicidades eres libre")
         break
    else: #si no se cumple el if
         print("jas jas, atrapado,vuelve a intentarlo...")
   
        
           

       
    
