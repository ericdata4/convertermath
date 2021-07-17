# a program which can only be used by the gang

import numpy as np
import math

def converter1(): # Parameterform in Normalform
    a = []
    b = []
    c = []

    print("-+-+-+-+ PARAMETERFORM IN NORMALFORM UMWANDELN -+-+-+-+")
    print("Ortsvektor OA: ")
    for i in range(3):
            a.append(float(input(f"{i + 1}. Koordinate: ")))
    print("Orsvektor OA: " , a)
    print("-.-.-.-.-.-.")    

    for i in range(3):
        b.append(float(input(f"{i + 1}. Koordinate: ")))
    print("Richtungsvektor AB: ", b)
    print("-.-.-.-.-.-.")


    print("Richtungsvektor OB: ")
    for i in range(3):
        c.append(float(input(f"{i + 1}. Koordinate: ")))
    print("Richtungsvektor AC: ", c)

    print("Geradengleichung in Parameterform: ")
    print(f"       |{a[0]}|       |{b[0]}|       |{c[0]}|")
    print(f"E:X =  |{a[1]}| + r * |{b[1]}| + s * |{c[1]}|")
    print(f"       |{a[2]}|       |{b[2]}|       |{c[2]}|")

    print("Geradengleichung in Normalform: ")

    # Kreuz = a[1] * b[2] - a[2] * b[1],a[2] * b[0] - a[0] * b[2],a[0] * b[1] - a[1] * b[0]

    print(f"      |     |{a[0]}| |   " , "|" ,b[1] * c[2] - b[2] * c[1],"|")           #|{c[0]}|")
    print(f"E:X = | x - |{a[1]}| | * " , "|" ,b[2] * c[0] - b[0] * c[2],"|")           #|{c[1]}|")
    print(f"      |     |{a[2]}| |   " , "|" ,b[0] * c[1] - b[1] * c[0],"|")           #|{c[2]}|")

def converter2(): #Normalform in Koordinatenform
    print("-+-+-+-+ NORMALFORM IN KOORDINATENFORM UMWANDELN -+-+-+-+")
    a = []
    b = []

    for i in range(3):
        a.append(float(input(f"{i + 1}. Koordinate des Ortsvektor: ")))
    print("Ortsvektor: " , a)
    print("-.-.-.-.-.-.")

    
    for i in range(3):
        b.append(float(input(f"{i + 1}. Koordinate des Normalenvektors: ")))
    print("Normalenvektor: " , b)
    print("-.-.-.-.-.-. Ebenengleichung in Normalform -.-.-.-.-.-.")

    print(f"      |     |{a[0]}|   " "|"  ,b[0], "|")   
    print(f"E:X = | x - |{a[1]}| * " "|"  ,b[1], "|")     
    print(f"      |     |{a[2]}|   " "|"  ,b[2], "|")

    print("-.-.-.-.-.-. Normalengleichung in Koordinatenform -.-.-.-.-.-. ")

    print(b[0] , "x + ", b[1], "y +", b[2], "z" " =", a[0]*b[0]+a[1]*b[1]+a[2]*b[2])

def converter3():

    print("-+-+-+-+ KOORDINATENFORM IN PARAMETERFORM UMWANDELN -+-+-+-+")
    a = float(input("X-Wert?: ")) #f
    b = float(input("Y-Wert?: ")) #g
    c = float(input("Z-Wert?: ")) #h
    d = float(input("Summe-Wert?: ")) #i

    print("------  Gleichung in Koordinatenform ------ ")
    print(a,"x + ", b,"y +", c,"z" " =" , d)

    print("------  Gleichung in Parameterform ------ ")

    print(f"       |{d/a}|       |{0 - d/a}|   |{0 - d/a}|")
    print(f"E:X =  |{0}| + r *   |{d/b}| + s * |{0}|")
    print(f"       |{0}|         |{0}|         |{d/c}|")

    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

def converter4(): # Parameterform in Koordinatenform # UNSUCESSFUL BUILD
  
    print("Aufbau der Parameterform: ")

    print("E:x = OA + r * AB + s * AC")

    a = []
    b = []
    c = []
    
    print("Ortsvektor OA: ")
    for i in range(3):
        a.append(float(input(f"{i + 1}. Koordinate: ")))
    print("Ortsvektor: " , a)
    print("-.-.-.-.-.-.")


    print("Richtungsvektor AB: ")
    for i in range(3):
        b.append(float(input(f"{i + 1}. Koordinate: ")))
    print("Richtungsvektor AB: ", b)
    print("-.-.-.-.-.-.")


    print("Richtungsvektor AC: ")
    for i in range(3):
        c.append(float(input(f"{i + 1}. Koordinate: ")))
    print("Richtungsvektor AC: ")

    print("Geradengleichung in Parameterform: ")
    print(f"       |{a[0]}|       |{b[0]}|         |{c[0]}|")
    print(f"E:X =  |{a[1]}| + r * |{b[1]}| + s *   |{c[1]}|")
    print(f"       |{a[2]}|       |{b[2]}|         |{c[2]}|")

    print("-.-.-.-.-.-. Parameterform in Koordinatenform -.-.-.-.-.-. ")
    # das was auf der linken Seite rauskommt ist korrekt, das was wiederum auf der rechten Seiten kommt, ist nicht korrekt
    # alternativ würde ich hier einfach das so umschreiben, dass es von parameterform in normalform erstmal übergeht
    # und danach dann erst von normalform in koordintanform

    print(b[1] * c[2] - b[2] * c[1] , "x + ", b[2] * c[0] - b[0] * c[2], "y +", b[0] * c[1] - b[1] * c[0], "z" " =", (a[1] * b[1] * c[2] - b[2] * c[1] + a[2] * b[2] * c[0] - b[0] * c[2] + a[2]* b[0] * c[1] - b[1] * c[0]))
  

def converter5(): # Koordinatenform in Parameterform # viele lösungen
    print("Bei dieser Umwandlung können unterschiedliche Ergebnisse entstehen. Das bedeudet, mehrere Gleichungen können die korrekte Umwandlung der Ausgangsgleichug sein.")
    a = float(input("X-Wert?: "))
    b = float(input("Y-Wert?: "))
    c = float(input("Z-Wert?: "))
    d = float(input("Summe-Wert?: "))

    print("------  Gleichung in Koordinatenform ------ ")
    print(a,"x + ", b,"y +", c,"z" " =" , d)

    print("------  Gleichung in Parameterform ------ ")

    print(f"       |{d/a}|       |{0 - d/a}|   |{0 - d/a}|")
    print(f"E:X =  |{0}| + r *   |{d/b}| + s * |{0}|")
    print(f"       |{0}|         |{0}|         |{d/c}|")


def converter6(): # NORMALFORM IN PARAMETERFORM # viele lösungen
    a = []
    b = []

    print("Bei dieser Umwandlung können verschiedene Ergebnisse entsehen, die alle jedoch die selbe Ebene beschreiben!")

    for i in range(3):
        a.append(float(input(f"{i + 1}. Koordinate des Ortsvektor: "))) 
    print("Ortsvektor: " , a)
    print("-.-.-.-.-.-.")

    
    for i in range(3):
        b.append(float(input(f"{i + 1}. Koordinate des Normalenvektors: ")))
    print("Normalenvektor: " , b)
    print("-.-.-.-.-.-. Ebenengleichung in Normalform -.-.-.-.-.-.")

    print(f"      |     |{a[0]}|   " "|" ,b[0], "|")   
    print(f"E:X = | x - |{a[1]}| * " "|" ,b[1], "|")     
    print(f"      |     |{a[2]}|   " "|" ,b[2], "|")

    print("-.-.-.-.-.-. Normalengleichung in Parameterform -.-.-.-.-.-. ")

    print(f"       |{a[0]}|         |{b[0] *  0}|         |{b[1] *  1}|")
    print(f"E:X =  |{a[1]}| + r  *  |{b[2] * -1}| + s  *  |{b[0] * -1}|")
    print(f"       |{a[2]}|         |{b[1] *  1}|         |{b[2] *  0}|")


def Kreuprodukt():
    a = [int(input("X-Koordinate: ")),
         int(input("Y-Koordinate: ")),
         int(input("Z-Koordinate: "))]

    print("Vektor a:", a)

    b = [int(input("X-Koordinate: ")),
         int(input("Y-Koordinate: ")),
         int(input("Z-Koordinate: "))]

    print("Vektor b:", b)

    Kreuz = a[1] * b[2] - a[2] * b[1],a[2] * b[0] - a[0] * b[2],a[0] * b[1] - a[1] * b[0]

    print("Das Kreuzprodukt dazu lautet: " , Kreuz)

def converter8(): # Winkel zwischen Gerade und Gerade

    print("-+-+-+-+-+- Winkelberechnung zwischen Gerade und Gerade -+-+-+-+-+-")
    print("Um den winkel zweier Geraden im dreidimensionalen Raum zu berechnen, muss der Winkel zwischen den zwei Richtungsvektoren bestimmt werden")


    rx1 = float(input("X- Wert (Richtungsvektor #1): "))
    ry1 = float(input("Y- Wert (Richtungsvektor #1): "))
    rz1 = float(input("Z- Wert (Richtungsvektor #1): "))

    rx2 = float(input("X- Wert (Richtungsvektor #2): "))
    ry2 = float(input("Y- Wert (Richtungsvektor #2): "))
    rz2 = float(input("Z- Wert (Richtungsvektor #2): "))

    rich1 = [rx1, ry1, rz1]
    rich2 = [rx2, ry2, rz2]

    # Winkel Berechnung: Skalarprodukt durch die Beträge und davon dann den Cosinus

    skala = rich1[0] * rich2[0] + rich1[1] * rich2[1] + rich1[2] * rich2[2]

    b_von_r1 = math.sqrt(rich1[0]**2 + rich1[1]**2 + rich1[2]**2) 
    b_von_r2 = math.sqrt(rich2[0]**2 + rich2[1]**2 + rich2[2]**2)

    angle1 = math.acos((skala / (b_von_r1 * b_von_r2)))
    angle = math.degrees(angle1)


    if angle > 90:
        angle = 180 - angle
    else:
        pass

    print(angle)

def converter9(): # Winkel zwischen Gerade und Ebene
    print("-+-+-+-+-+- Winkel zwischen Gerade und Ebene ausrechnen -+-+-+-+-+-")
    a = []
    b = []

    print("Definiere den Richtungsvektor der Gerade!")

    #for i in range(3):
        #a.append(float(input(f"{i + 1}. Koordinate: "))) # ignorier das hier
        #print("Richtungsvektor der Geraden: ", a)

    rx = float(input("X- Wert (Gerade): "))
    ry = float(input("Y- Wert (Gerade): "))
    rz = float(input("Z- Wert (Gerade): "))

    print("Der Richtungsvektor lautet: ","[", rx ,",", ry, ",", rz,"]",)

    ans = str(input("Ist der Normalenvektor der Ebene gegeben? (y/n)"))

    if ans == "y" or ans == "Y":
        print("Definiere den Normalenvektor der auf deiner Ebene steht!")
        nx = float(input("X- Wert (Normalenvektor): "))
        ny = float(input("Y- Wert (Normalenvektor): "))
        nz = float(input("Z- Wert (Normalenvektor): "))

        print("Der Normalenvektor lautet: ","[", rx ,",", ry, ",", rz,"]",)

    else: 
        print("Richtungsvektor der Ebene (Richtungsvektor) #1: ")
        V1 = [float(input("X- Wert (#1): ")), float(input("Y- Wert (#1): ")), float(input("Z- Wert (#1): "))]

        print("Richtungsvektor der Ebene (Richtungsvektor) #2: ")
        V2 = [float(input("X- Wert (#2): ")), float(input("Y- Wert (#2): ")), float(input("Z- Wert (#2): "))]

        nx = V1[1] * V2[2] - V1[2] * V2[1]
        ny = V1[2] * V2[0] - V1[0] * V2[2]
        nz = V1[0] * V2[1] - V1[1] * V2[0]

        print("Der Normalenvektor lautet: ","[", rx ,",", ry, ",", rz,"]",)
        
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

    norm = [nx, ny, nz]
    rich = [rx, ry, rz]

    # Winkel Berechnung: Skalarprodukt durch die Beträge und davon dann den Cosinus

    skala = norm[0] * rich[0] + norm[1] * rich[1] + norm[2] * rich[2]

    b_von_r1 = math.sqrt(norm[0]**2 + norm[1]**2 + norm[2]**2) 
    b_von_r2 = math.sqrt(rich[0]**2 + rich[1]**2 + rich[2]**2)

    angle1 = math.acos((skala / (b_von_r1 * b_von_r2)))
    angle = math.degrees(angle1)

    if angle > 90:
        angle = 180 - angle
    else:
        pass

    print("Der Winkel zwischen Richtungsvektor und Normalenvektor beträgt",angle,"°")

def converter10():   # Winkel zwischen Ebene und Ebene
    print("-+-+-+-+- Winkelberechnung zwischen Ebene und Ebene -+-+-+-+-")
    print("Um den Winkel zwischen den beiden Ebenen zu berechnen, muss der Winkel zwischen den zwei Normalenvektoren bestimmt werden")
    ans = str(input("Sind die Normalenvektoren für #1 und #2 gegeben? (y/n)"))

    if ans == "y" or ans == "yes":
        nx1 = float(input("X- Wert (Normalenvektor #1): "))
        ny1 = float(input("Y- Wert (Normalenvektor #1): "))
        nz1 = float(input("Z- Wert (Normalenvektor #1): "))

        nx2 = float(input("X- Wert (Normalenvektor #2): "))
        ny2 = float(input("Y- Wert (Normalenvektor #2): "))
        nz2 = float(input("Z- Wert (Normalenvektor #2): "))

        norm1 = [nx1, ny1, nz1]
        norm2 = [nx2, ny2, nz2]

    # Winkel Berechnung: Skalarprodukt durch die Beträge und davon dann den Cosinus

        skala = norm1[0] * norm2[0] + norm1[1] * norm2[1] + norm1[2] * norm2[2]

        b_von_r1 = math.sqrt(norm1[0]**2 + norm1[1]**2 + norm1[2]**2) 
        b_von_r2 = math.sqrt(norm2[0]**2 + norm2[1]**2 + norm2[2]**2)
        # angle_arccos = (skala/(b_von_n + b_von_r))
        
        angle1 = math.acos((skala / (b_von_r1 * b_von_r2)))
        angle = math.degrees(angle1)

        if angle > 90:
            angle = 180 - angle
        else:
            pass

        print("Der Winkel beträgt", angle , "°!")

    elif ans == "n" or ans == "N":
        print("Berechne zuerst die zwei Vektoren, die orthogonal zu jeweils einer Ebene stehen")
        print("Benutze dazu das Kreuzprodukt Modul!")
        pass
        

def converter11():

    print("-+-+- Lineare Abhängigkeit zweier Vektoren -+-+-")

    a1 = float(input("X-Wert: (Richtungsvektor #1)"))
    a2 = float(input("Y-Wert: (Richtungsvektor #1)"))
    a3 = float(input("Z-Wert: (Richtungsvektor #1)"))
    print("[",a1, ",", a2, ",", a3,"]")

    b1 = float(input("X-Wert: (Richtungsvektor #2)"))
    b2 = float(input("Y-Wert: (Richtungsvektor #2)"))
    b3 = float(input("Z-Wert: (Richtungsvektor #2)"))
    print("[",b1, ",", b2, ",", b3,"]")

    a = [a1, a2, a3] 
    b = [b1, b2, b3]

    print("---------------------------------------------------------")

    if a1 % b1 == a2 % b2 == a3 % b3:
        print("Die Vektoren " , a, "und", b , "sind linear abhängig!")

    else:
        print("Die Vektoren" , a , "und" , b , "sind nicht linear abhängig!")


def converter12():
    # Lineare Abhängigkeit von drei Vektoren untersuchen
   
    print("-+-+- Komplanarität von drei Vektoren untersuchen -+-+-")

    a1 = float(input("X-Wert: (Vektor #1)"))
    a2 = float(input("Y-Wert: (Vektor #1)"))
    a3 = float(input("Z-Wert: (Vektor #1)"))
    print("[",a1, ",", a2, ",", a3,"]")

    b1 = float(input("X-Wert: (Vektor #2)"))
    b2 = float(input("Y-Wert: (Vektor #2)"))
    b3 = float(input("Z-Wert: (Vektor #2)"))
    print("[",b1, ",", b2, ",", b3,"]")

    c1 = float(input("X-Wert: (Vektor #3)"))
    c2 = float(input("Y-Wert: (Vektor #3)"))
    c3 = float(input("Z-Wert: (Vektor #3)"))
    print("[",c1, ",", c2, ",", c3,"]")

    a = [a1, a2, a3] 
    b = [b1, b2, b3]
    c = [c1, c2, c3] 

    print("------------------------------------------------------")

while True:
    print("(1) = PARAMETERFORM IN NORMALFORM")
    print("(2) = NORMALFORM IN KOORDINATENFORM")
    print("(3) = KOORDINATENFORM IN PARAMETERFORM")
    print("(4) = PARAMETERFORM IN KOORDINATENFORM (UNSUCCESFUL BUILD - tobi fix das, guck bei converter4 ")
    print("(5) = KOORDINATENFORM IN PARAMETERFORM")
    print("(6) = NORMALFORM IN PARAMETERFORM")
    print("(7) = KREUZPRODUKT BERECHNEN")
    print("(8) = WINKEL ZWISCHEN GERADE UND GERADE")
    print("(9) = WINKEL ZWISCHEN EBENE UND GERADE")
    print("(10) = WINKEL ZWISCHEN EBENE UND EBENE")
    print("(11) = Lineare Abhängigkeit untersuchen")
    print("(12) = Komplanarität untersuchen")

    answer = str(input("UMWANDLER WÄHLEN: "))
    
    if answer == "1":
        converter1()
        

    elif answer == "2":
        converter2()
        

    elif answer == "3":
        converter3()
        

    elif answer == "4":
        converter4()
      

    elif answer == "5":
        converter5()
        

    elif answer == "6":
        converter6()
        

    elif answer == "7":
        Kreuprodukt()
        

    elif answer == "8":
        converter8()
        

    elif answer == "9":
        converter9()
        

    elif answer == "10":
        converter10()
        

    elif answer == "11":
        converter11()
        

    elif answer == "12":
        converter12()
        

    else:
        print("Bitte wähle eine Zahl zwischen 1-12!")
        