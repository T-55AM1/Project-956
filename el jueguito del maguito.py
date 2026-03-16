numero_secreto = 777

print(
"""
+================================+
| Vienvenido a my juego          |
|adivina o queda atrapado        |
|¿cual es el numero secreto?     |
+================================+
""")
while  True:
    num = int(input("pon un numero..."))

    if num == numero_secreto:
         print("felicidades eres libre")
         break
    else:
         print("jas jas, atrapado,vuelve a intentarlo...")
   
        
           

       
    
