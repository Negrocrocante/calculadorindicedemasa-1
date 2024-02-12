nombre= input("introduce tu nombre:")
apellido = input("introduce tu apellido:")
edad= int(input("introduce tu edad:"))

def imc(estatura, peso):
   
 return peso / estatura**2

    
peso = float(input("escribe tu peso (kg):"))
estatura = float(input("escriba su estatura(m):"))
indice = imc(estatura,peso)
print("tu nombre:"  + nombre.title()) 
print("tu apellido:" + apellido.title())
print(" tu edad es:" + str(edad) + "años" )
print("su IMC es: {}".format(indice))


