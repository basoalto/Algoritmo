from os import system
system("cls")


pasajeros=  [None]*198
asientos = []
for i in range(198):
    if i < 9:
        asientos.append(f"💺 0{i+1}")
    else:
        asientos.append(f"💺 {i+1}")
#MIS FUNCIONES
def menu():
    print("""
1. Ver asientos disponibles
2. Comprar pasaje
3. Eliminar una reserva de pasaje
4. Ver listado de pasajeros
5. Total ganancias
6. Salir
    """)
def pausa():
    input("Presione una tecla para continuar....")
def Mi_Error(texto):
    print( texto )
def comprar():
    while True: 
        nroasi = int(input('cantidad de pasajes que necesita comprar: '))
        print("Seleccione su asiento")
        print("*******************************************\n")
        verasientos()
        print("\n*******************************************")
        precios()
        if nroasi>=1:
            for i in range(nroasi):
                asi=input("Ingrese el asiento: ")
                if asi.isnumeric():
                    asi=int(asi)
                if asi>=1 and asi<=198:
                   rut= list (map(int, input().split()))
                   asientos[asi-1]=f"⛔"
                   pasajeros[asi-1]=rut
                else:
                    Mi_Error("Debe ser un número entero entre 1 y 198")
        break
def precios():
    print('''
Los precios de los asientos son los siguientes:
• Asiento común, $60.000 pesos. 💺 1 al 17
• Espacio adicional para piernas, $80.000 pesos. 💺 18 al 27
• No reclina, $50.000 pesos. 💺 28 al 45
    ''')          
def verasientos():
    for i in range(0,194,4):
        print(f"{asientos[i]}|{asientos[i+1]}      {asientos[i+2]}|{asientos[i+3]}")       
        print(f"{asientos[196]}|{asientos[197]}")

def verpasajeros():
    for i in range(198):
        if pasajeros[i]!=None:
            pasajeros.sort()
            print(f"{i+1} rut= {pasajeros[i]}")
    pausa()
def cancelar():
    while True:
        num=input("Ingrese número de asiento a cancelar o presione 's' para salir: ")
        if num=="s":
            return #finaliza la funcion
        if num.isnumeric():
            num=int(num)
            if num>=1 and num<=45:
                if num < 9:
                    asientos[num-1]=f"💺 0{num}"
                else:
                    asientos[num-1]=f"💺 {num}"
                pasajeros[num-1]=None
                break
        Mi_Error("Debe ingresar el número del asiento")
def ganancias():
    cuenta=0
    for item in pasajeros:
        if item!=None:
            cuenta +=1
    print(f"Ganancias Totales {cuenta*4000}")
    pausa()
# MI PROGRAMA PRINCIPAL
while True:
    system("cls")
    menu()
    op = input("Ingrese una opción: ")
    if op == "1":
        verasientos()
        pausa()
    elif op=="2":
        comprar()
    elif op=="3":
        cancelar()
    elif op=="4":
        verpasajeros()
    elif op=="5":
        ganancias()
    else:
        print("Opción no válida!!!")
        pausa()