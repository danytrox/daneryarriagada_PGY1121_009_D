import time
import os
import numpy as np



def menu ():
    print("""MENU
1. Comprar entradas
2. Mostrar ubicaciones disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir
    """)
    opc = Vopc()
    return opc
ListPago=[]

def pagototal():
     total = 0
     for x in range(len(ListPago)):
          x= ListPago[x]
          total = total + x
     os.system("cls")
     print("el total de ganancias de hoy es: ",total)
     time.sleep(2)
     os.system('cls')

          

def Vfila():
    while True:
        try:
            fila = int(input("Ingrese una fila (1-10)"))
            if fila in (1,2,3,4,5,6,7,8,9,10):
                print("fila correcta")
                return fila
            else:
                print("opc ingresada fuera de rango ")
        except:
            print("Error!!! porfavor ingresar numeros no letras")

def Vcolumnas():
    while True:
        try:
            columnas = int(input("Ingrese una columnas (1-10)"))
            if columnas in (1,2,3,4,5,6,7,8,9,10):
                print("columnas correcta")
                return columnas
            else:
                print("opc ingresada fuera de rango ")
        except:
            print("Error!!! porfavor ingresar numeros no letras")

ListRut=[]
ListEnt = []
ListFila =[]
ListColumna=[]

def Ventrada():
    while True:
        try:
                    rut = Vrut()
                    if rut not in ListRut:
                        ListRut.append(rut)
                        VerE()             
                        comprar()
                        return

        except:
            print("ERROR! intente nuevamente ")

    
def comprar():
            con1 = 0
            while True:
                x = int(input("cuantas entradas quiere comprar ?"))
                if x in (1,2,3):
                    pago = 0
                    while True:
                            if x <= con1:
                                    ListPago.append(pago)
                                    return
                            fila = Vfila()
                            columna= Vcolumnas()
                            if concierto[fila-1][columna-1]== 0:
                                concierto[fila-1][columna-1] = 1
                                ListFila.append(fila)
                                ListColumna.append(columna)             
                                con1+=1
                                if fila in (1,2):
                                    print ("has comprado una entrada Platinum(120000): ")
                                    pago = 120000 + pago
                                elif fila in (3,4,5):
                                    print("has comprado una entrada Gold(80000): ")
                                    pago = 80000+pago
                                elif fila in (6,7,8,9,10):
                                    print("has comprado una entrada Silver: ")
                                    pago= 50000+pago   
                            else:
                                print("este lugar esta ocupado ")
                else:
                    print("valor maximo para un usuario es 3 ")
                        
                    
                       
            

                    


concierto = np.zeros((100,10),int)

def VerE():
    os.system("cls")
    for x in range (10):
        print ("fila",x+1,": ", end=(" "))
        for y in range(10):
            print(concierto[x][y], end=" ")  

        print()
    print("columnas   1 2 3 4 5 6 7 8 9 10")
    time.sleep(2)

def Vopc():
    while True:
        try:
            opc = int(input("seleccione una opcion (1-5) : " ))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("opc no valida porfavor poner entre 1 a 5 ")

        except:
            print("ERROr! intente nuevamente ")

def Vopc2():
    while True:
        try:
            opc = int(input("seleccione una opcion (1-5) : " ))
            if opc in (1,2,3):
                return opc
            else:
                print("opc no valida porfavor poner entre 1 a 5 ")

        except:
            print("ERROr! intente nuevamente ")

def Vrut():
    while True:
        try:
            os.system("cls")
            rut = int(input("Ingrese su numero de rut : "))
            if len(str(rut))== 7 or len(str(rut))==8:
                return rut
            else:
                print(" numero de rut debe tene al menos 7 digitos y no superar los 8..")
        except:
            print("rut no valido")
























































































































































def salir():
     time.sleep(2)
     print(":c")
     return