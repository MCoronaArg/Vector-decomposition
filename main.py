import math
def preguntar():
   global ax,ay,az,bx,by,bz,cx,cy,cz,mod

   #Ingreso de variables
   print("Ingrese 2 puntos de la recta de accion del vector.\nPunto Partida: ")
   ax = float(input("Ax: "))
   ay = float(input("Ay: "))
   az = float(input("Az: "))

   print("Punto de llegada: ")
   bx = float(input("Bx: "))
   by = float(input("By: "))
   bz = float(input("Bz: "))

   print("Fuerza del vector: ")
   mod = float(input("Modulo: "))

   #Armo el vector
   cx = float(bx-ax)
   cy = float(by-ay)
   cz = float(bz-az)

def calculo():
    global adj1,op1,hip1,adj2,op2,hip2,fx,fy,fz,fxy,cuadrante

    #Triangulacion 1 plano XY
    adj1 =float(abs(cx))
    op1 = float(abs(cy))
    hip1 = float(math.sqrt(op1**2+adj1**2))

    #Triangulacion R3
    adj2 = hip1
    op2 = float(abs(cz))
    hip2 = float(math.sqrt(op2**2+adj2**2))

    #Fuerzas triangulacion R3
    fz = float(mod*(op2/hip2))
    fxy = float(mod*(adj2/hip2))

    #Fuerzas triangulacion plano XY
    fx = float(fxy*(adj1/hip1))
    fy = float(fxy*(op1/hip1))

    #Devuelvo la fuerza descompuesta con sus correctos signos
    print("\nFuerzas resultantes: ")

    if cx >= 0 and cy >= 0 and cz >= 0:
        cuadrante = 1
        print("Fx: ", abs(fx))
        print("Fy: ", abs(fy))
        print("Fz: ", abs(fz))

    elif cx >= 0 and cy <= 0 and cz >= 0:
        cuadrante = 2
        print("Fx: ", abs(fx))
        print("Fy: ", -abs(fy))
        print("Fz: ", abs(fz))

    elif cx <= 0 and cy <= 0 and cz >= 0:
        cuadrante = 3
        print("Fx: ", -abs(fx))
        print("Fy: ", -abs(fy))
        print("Fz: ", abs(fz))

    elif cx <= 0 and cy >= 0 and cz >= 0:
        cuadrante = 4
        print("Fx: ", -abs(fx))
        print("Fy: ", abs(fy))
        print("Fz: ", abs(fz))

    elif cx >= 0 and cy >= 0 and cz <= 0:
        cuadrante = 5
        print("Fx: ", abs(fx))
        print("Fy: ", abs(fy))
        print("Fz: ", -abs(fz))

    elif cx >= 0 and cy <= 0 and cz <= 0:
        cuadrante = 6
        print("Fx: ", abs(fx))
        print("Fy: ", -abs(fy))
        print("Fz: ", -abs(fz))

    elif cx <= 0 and cy <= 0 and cz <= 0:
        cuadrante = 7
        print("Fx: ", -abs(fx))
        print("Fy: ", -abs(fy))
        print("Fz: ", -abs(fz))

    elif cx <= 0 and cy >= 0 and cz <= 0:
        cuadrante = 8
        print("Fx: ", -abs(fx))
        print("Fy: ", abs(fy))
        print("Fz: ", -abs(fz))

preguntar()
calculo()

