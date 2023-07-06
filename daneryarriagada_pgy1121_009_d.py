import funciones as fn

while True:
    opc = fn.menu()
    if opc == 1:
        fn.Ventrada()
    if opc == 2:
        fn.VerE()
    if opc == 3:
        print(fn.ListRut)
    if opc == 4:
        fn.pagototal()
    if opc == 5:
        fn.salir()
        break            