"""
def showAnimal(name,n_legs):
    print(f"El animal {name} tiene {n_legs} patas.")

showAnimal("Gato",18)

def functionArgumentos(lista):
    print(len(lista))

listaArgumentos=["Gato","Perro","Cachorro","Caballo","Ballena","Cangrejo",4,4,4,4,0,6]
functionArgumentos(listaArgumentos)

def SumaResta(x,y):
    return (x+y,x-y)
print(SumaResta(10,20))


def Multiplicacion(x,y):
    return(x*y)

def Modulus(x,y):
    return(x%y)

def FunComplex(Multiplicacion,Modulus,num1,num2):
    return(Multiplicacion(num1,num2),Modulus(num1,num2))

print(FunComplex(Multiplicacion,Modulus,100,20))
"""
"""
def login(name,email="Sin determinar"):
    print(f"Bienvenido {name} {email}")

login("Juan")
login("Juan","kenaa@example.com")
"""
"""
def SumaIterada(number):
    suma=0
    i=0
    while i<=number:
        suma=suma+i
        i=i+1
    return suma
    
print(SumaIterada(10))
print(SumaIterada(100))
"""
#Funciones anónimas
#Funciones lambda
"""
Cuadrado=lambda parametro: parametro**2
print(Cuadrado(5))
print(Cuadrado(25))
"""
"""
#Funcion lambda que retorna un boolean
Mayorque999=lambda num: num>999
print(Mayorque999(10))
"""
"""
mult=lambda num1,num2:num1*num2

print(mult(20,15))
"""
