# Tomás Carretero Alarcón   DNI: 04640646M 
import re
# He diseñado el Delizator de tal modo que todos los pasos se relaizan sobre una matriz (tablero) que solo contiene las letras y luego otra matriz (m) que es la que tiene el formato pedido.

def imprimir (tablero):                     #procedimineto para imprimir por pantalla la matriz que sea enviada como parámetro
    for i in range (len(tablero)):
        for j in range(len(tablero[0])):
            print(tablero[i][j], end="")
        print("")


def siguiente (tablero):                    #creación de tablero con la primera ya insertada la primera fila del fichero. 
    for i in range(f):
        tablero.append([])
        for j in range (c):
            if i == 0: 
                tablero[i].append(text[j:j+1])
            else: tablero[i].append(" ")
    return tablero


def siguiente2(tablero):                    #modificación del tablero para introducir las posteriores jugadas. 
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if i==0: tablero[i][j] = (text[j:j+1])
    return tablero
    

def jugada (tablero):                              #esta función se encarga pedir la jugada hasta que sea una de las opciones y devuelve el array con la jugada 
    correcta = False
    jug = [1,2,3]  
    while correcta == False:
        cad = input("Introduzca jugada o --- o FIN: ")
        

        if re.search(pattern,cad) or cad == "---" or cad == "FIN":
            correcta = True
                
            for i in range(3):                      #separo los caracteres en un array para acutar en función de su contenido.
                jug[i] = cad[i:i+1]

            x = jug[2]
            if x == "-": correcta = True
            else: 
                if x == "N": correcta = True
                else: 
                    w = (Dict[str(jug[0])])             #Asigno respectivamente en w y k la fila y comuna selecionada en la jugada. 
                    k = int(jug[1])
                    
                    if tablero[w][k] == " " or x == "N": print("No hay ningún bloque en esa celda"); correcta = False
                    else:
                        if x == "<": 
                            while k > 0 and tablero[w][k] == tablero[w][k-1]: 
                                k -=1

                            if tablero[w][k-1] == " ": correcta = True
                            else: print("El bloque no puede moverse en esa dirección"); correcta = False
                        else: 
                            if x == ">": 
                                while (k+1) < len(tablero[w]) and tablero[w][k] == tablero[w][k+1]: 
                                    k +=1
                                    
                                if (k+1) < len(tablero[w]) and tablero[w][k+1] == " ": correcta = True
                                else: print("El bloque no puede moverse en esa dirección"); correcta = False
                            else:
                                if x == "N": correcta = True          
        else: print("Error de sintaxis en jugada")
        
    return jug
    

def latera (jug, tablero):                  #esta función se encarga de aplicar la jugada del usuario. 

    if jug[2] != "-":                     
        w = (Dict[str(jug[0])])             #Asigno respectivamente en w y k la fila y comuna selecionada en la jugada. 
        k = int(jug[1])
    
        if (jug[2] == "<") and tablero[w][k] != " " and (jug[1] != "0"):    #no tiene sentido mover un bloque que ya está a la izquierda del todo, ni tampoco mover un espacio.
                                #El recuento de letras que forman el bloque está en bloc  
            i=k; bloc = 1       #El esta ocasion utilizare la variable i para moverme en busca de más letras que formen el bloque selecionado en caso de existir. 

            while tablero[w][k] == tablero[w][i-1]: # Incremento las letras que forman el bloque a partir de la letra selecionada hacia la izquierda, si se trata de un mismo bloque. 
                bloc +=1
                i-=1

            inic = i            #Guardo la posición de más a la izquierda del bloque en la variable inic

            while (i) > 0 and tablero[w][i-1] == " ": #Descubir cual va a ser la nueva posición de la letra que más a la izquierda esté en el bloque. 
                i-=1

            if tablero[w][i] == " ":    #solo habrá movimeinto si a la izquierda del bloque hay al menos un espacio: 
                pos = i                 #La variable pos gurada la posición con espacio más a la izquieda del bloque
                i = k + 1               #Incremento en uno la posición introducida por el jugador para conocer las letras que forman el bloque hacia la derecha. 
                
                while i < 9 and tablero[w][k] == tablero[w][i]: #Calculo el nº total de letras que forman el bloque y el más alejado del moviento. 
                    bloc +=1
                    i+=1

                k = inic

                for j in range(bloc):                       #Procedo a mover el bloque, de tal modo que se cambia el espacio más a la izquierda por la primera letra que fomra el bloque. 
                    tablero[w][pos] = tablero[w][k]
                    if k != (pos) : tablero[w][k] = " "     #Sólo se borra el contenido, si no coindiden las celdas de copiar y borrar. 
                    k +=1; pos +=1

                i = pos - bloc          #pongo la variable i en la nueva primera posición del bloque una vez movido. 

                if i >= 0 and tablero[w][i] == tablero[w][i-1]:     #Si el bloque de la izquieda tiene la misma letra, cambio dichos bloques. 

                    if tablero[w][i] == "A" or tablero[w][i] == "B": 
                        p=0   #Como cambio los bloques de la izquierda puede haber otro bloque con la misma letra y con la p evito que se fusionen estos. 
                        while i >=0 and tablero[w][i] == tablero[w][i-1]:
                            c = tablero[w][i]; i-=1

                            if tablero[w][i] == c and p%2==0: 
                                while tablero[w][i] == c: tablero[w][i] = (tablero[w][i]).lower(); i-=1
                            else:
                                while tablero[w][i] == c: tablero[w][i]=(tablero[w][i]).upper(); i-=1 
                            i+=1;p+=1                           

                    if tablero[w][i] == "a" or tablero[w][i] =="b":
                        p=1
                        while i >=0 and tablero[w][i] == tablero[w][i-1]:
                            c = tablero[w][i]; i-=1

                            if tablero[w][i] == c and p%2==0: 
                                while tablero[w][i] == c: tablero[w][i] = (tablero[w][i]).lower(); i-=1
                            else:
                                while tablero[w][i] == c: tablero[w][i]=(tablero[w][i]).upper(); i-=1 
                            i+=1;p+=1
        
        if (jug[2] == ">") and tablero[w][k] != " " and (jug[1] != "9"):    #No se puede mover el ultimo bloque hacia la derecha ni tampoco mover un espacio. 
            i=k; bloc = 1   #Inicializo la variable i con la posición selecionada por el usuario y la de bloques con 1 representando las letras que forman el bloque 

            while tablero[w][i] == tablero[w][i+1]:     #Cuento las letras que forman el bloque hacia la derecha. 
                bloc +=1
                i+=1
            inic = i
            i+=1           #incremento en uno la variable i para posicionarme a la derecha del bloque. 

            if tablero[w][i] == " ":    #solo si hay espacios a la derecha del bloque podrás haber movimiento. 

                while i < 10 and tablero[w][i] == " ":  
                    i+=1
                
                pos = i - 1        #La variable i después del bucle anterior contiene el valor de la celda más alejada del movimiento, el cual guardo en pos. 
                
                i = k           #De nuevo reasigna a i el valor de la letra selecionado por el usuario y en el siguiente termino de contar las letras que forman el bloque. 
                while tablero[w][i] == tablero[w][i-1]:
                    bloc +=1
                    i-=1

 

                for j in range(bloc):      #hago el movimiento copiando el contenido de la letra más a la izquierda en el espacio de más a la derecha. 
                    tablero[w][pos]= tablero[w][inic]

                    if inic != pos: tablero[w][inic] = " "

                    inic -= 1
                    pos -= 1

                i = pos + bloc      #Mismo sistema que antes para evitar que se fusionen dos bloques distintos.  

                if i < 9 and tablero[w][i] == tablero[w][i+1] : 

                    if tablero[w][i] == "A" or tablero[w][i] == "B": 
                        p=0
                        while i < 9 and tablero[w][i] == tablero[w][i+1]:
                            c = tablero[w][i]; i+=1
                            if tablero[w][i] == c and p%2==0: 
                                while tablero[w][i] == c: tablero[w][i] = (tablero[w][i]).lower(); i+=1
                            else:
                                while tablero[w][i] == c: tablero[w][i]=(tablero[w][i]).upper(); i+=1 
                            i-=1;p+=1

                    if tablero[w][i] == "a" or tablero[w][i] =="b":
                        p=1
                        while i < 9 and tablero[w][i] == tablero[w][i+1]:

                            c = tablero[w][i]; i+=1

                            if tablero[w][i] == c and p%2==0: 
                                while tablero[w][i] == c: tablero[w][i] = (tablero[w][i]).lower(); i+=1
                            else:
                                while tablero[w][i] == c: tablero[w][i]=(tablero[w][i]).upper(); i+=1 
                            i-=1;p+=1

    return tablero
    
    
def free (tablero, fil):        #Función llamada por bajadaporfilas para conocer cual es la fila más abajo hasta la que puede bajar. 
    num = fil
    for fil2 in range(fil,len(tablero)):    #se recoren todas las filas a partir de la recibica como parámetro. 
        free = "T"              #La variable free indica si la fila está vacia con 'T' o tiene alguna letra 'F'
        for j in range(len(tablero[0])):
            if tablero[fil2][j] != " ": free = "F"

        if free == "T": num = fil2      #Sólo si la fila está completamente vacía, num (variable que se devulve) sarará a valer dicho valor. 

    return num


def bajadaporfilas(tablero):            #Para evitar vueltas, con esta función bajo por filas todo lo posible hasta solo quedar espaios por encima de la ultima fila introducida. 
        fil = len(tablero) - 1
        while fil >= 0:                             #El bucle se recorre de la ultima fila (L) a la primera (A)
            if espacios(tablero, fil) == False:     #Sólo si espacios es False encontes se podrá la fila en cuestión podrá bajar. El nombre da lugar a confusión, ir al metodo espaicos para entenderlo. 
                num = free(tablero,fil)

                if num != fil:
                    for j in range(len(tablero[0])):
                        tablero[num][j] = tablero[fil][j]
                        tablero[fil][j] = " " 
            fil -=1

        return tablero


def espacios (tablero,fil):         #Función que recibe el tablero y una fila y pone devuelve False si esta está vacia y True en caso contrario
    sigue = True; j=0
    while sigue == True and j<10:
        if tablero[fil][j] != " ": sigue = False
        j+=1
    return sigue

def bajadaporbloques(t, modificacion):  #Función que recibe el tablero que reapunta con 't' y devulve este con la bajada completa de los bloques y también una variable booleana positiva si algún bloque ha bajado 

    i = (len(t)-1); modificacion = False    #Se debe recorrer el tablero de abajo a arriba y en principio no se relaiza ninguna modificación. 

    while i != 0: 
        j = 0
        while j < len((t[i])):      #Estando en la fila i, la recorro para ver si pueden bajar bloques, en cuyo caso bajarían. 

            letras = 1
            datos = False; k = j
            espacios = 0    #Son los espacios disponibles
            while datos == False and k < 10:    #solo sirve para comprobar que la fila de arriba no esté vacía
                if t[i-1][k] != " ": datos = True
                else: k +=1

            j = k       #Al salir del bucle anterior tengo la posición donde hay letra y no espacio en la fila anterior, esta posición es la que me interesea pues los espacios no deben bajar sólo las letras. 

            if j < len(t[i]) and t[i][j] == " " and datos == True:

                inic = j    #Guardo en la variable inic el valor de la priemra letra que forma el bloque que debe caer. 

                while j < 10 and t[i][j] == " ": # Cuenta el numero de espacios disponibles para que caigan letras, a partir de la posición inic
                    espacios += 1
                    j +=1

                r = inic + 1    #La variable r valdrá inic + 1 para ver si el bloque contiene más de una letra. 

                while r < (len(t[i])) and t[i-1][inic] == t[i-1][r]:    #Cuenta el numero de letras que forma el bloque
                    r = r+1; letras +=1
                
                if t[i-1][inic] != t[i-1][inic-1] and espacios >= letras or (inic == 0 and letras == 1 and tablero[i-1][inic+1]!= tablero[i][inic]): #Para bajar, el bloque no debe estar formado por letras a la izquierda de inic y además o bien espaciso es mayor que letras o bien se trata de un bloque con solo una letra. 
                    
                    n=0
                    while n<letras and (inic+n)<len(t[i]):      #Hago la bajada del bloque, teniendo en cuenta que si al bajar, mi bloque tiene la misma letra que el de la izquierda tengo que cambiar a mayusculas o minusculas según proceda
                        
                        if t[i][inic-1] == t[i-1][inic+n]:
                            if ord(t[i][inic-1]) > 95: t[i][(inic + n)] = (t[i-1][(inic + n)]).upper()
                            elif ord(t[i][inic-1]) < 68: t[i][(inic + n)] = (t[i-1][(inic + n)]).lower()
                        else:
                            t[i][(inic + n)] = t[i-1][(inic + n)]

                        t[i-1][inic + n] = " "
                        modificacion = True
                        n += 1

                    
                    while (inic+n)<len(t[i]) and t[i][inic+n] == t[i][inic]: #Si al bajar el bloque, a la derecha de este hay un bloque con la misma letra debo cambiar a mayusculas o minusculas todos los bloques de la derecha según proceda. 
                            if ord(t[i][inic+n]) > 96:

                                while (inic+n)<10 and t[i][inic+n] == t[i][inic]:
                                    t[i][(inic + n)] = (t[i][(inic + n)]).upper()
                                    n+=1
                                inic = inic + n

                            elif ord(t[i][inic+n]) < 68:
                                while (inic+n)<10 and t[i][inic+n] == t[i][inic]:
                                    t[i][(inic + n)] = (t[i][(inic + n)]).lower()
                                    n+=1
                                inic = inic + n

                            
                    j = inic + letras   #En caso de haber bajado un bloque j pasa a ser inic + las letras que lo forman. 
                else: j= k + 1          #Sino ha podido bajar se incrementa en 1 para buscar en esa misma fila un bloque que si que pueda bajar. 
            else: j = k + 1             #Si la celda t[i][j] no es un espaico no puede bajar y busca uno más a la derecha que si que pueda.

        i -= 1

    return t, modificacion

def filacompleta(tablero, i):           #función booleana llamada por otra función para saber la fila enviada como parámetro debe ser eliminada, al tener todo letras.

    cambiar = True
    j = 0
    while j < (len(tablero[i])):
        if ord(tablero[i][j]) == 32:    #ascii del espacio = 32, por lo que si alguno coincide no se debe eliminar la fila 
            cambiar = False

        j += 1

    return cambiar

def samecolor (tablero, i):             #función boolena que devulve True cuando se debe producir la reación en cadena y False en caso contrario
    j = 0; same = True; c = (tablero [i][0]).lower(); c2 = (tablero[i][0]).upper() 

    while j < (len(tablero[i])):
        if c != tablero [i][j] and c2 != tablero[i][j]: same = False
        j +=1

    return same

def eliminar_filas(tablero, cont, modificacion):      #Función que se encarga de comprobar si una fila está completa y en este caso eliminarlo, también relaiza en su caso la reacción en cadena. 
    i = (len(tablero) - 1)              #Además también devuelve el total de puntos por la eliminación de las filas.  
    while i != 0: 
        
        cambiar = filacompleta(tablero, i)
        
        if cambiar == True:
            modificacion = True
            j=0
            if samecolor(tablero, i) == True: 
                k = len(tablero) -1
                while k >= 0: 
                    j = 0
                    while j < (len(tablero[i])): 
                        if (tablero[k][j] != " "): cont +=1
                        tablero[k][j] = " "
                        j += 1

                    k -= 1
                i = 1
                modificacion = False
            else:    
                while j < (len(tablero[i])): 
                    tablero[i][j] = " "
                    j += 1
                    cont +=1 

        i -= 1

    return tablero, cont, modificacion

def creacion_matriz_interfaz():         # creación de la matriz interfaz para el usuario (la pedida): 
    m = []; col = 21; filas = 26; w = 0

    Dict = {0:" ", 1:" A |", 3:" B |", 5:" C |", 7:" D |", 9:" E |", 11:" F |", 13:" G |", 15:" H |", 17:" I |", 19:" J |", 21:" K |", 23:" L |", 25:"  "}

    for i in range (filas):

        m.append([])

        for j in range(col):

            if i == 25 and j>1 and j%2==0:      #Indicador del numero de la columna. 
                m[i].append(w)
                w+=1

            elif j == 0:                        #Indicador de la fila con su letra correspondiente o sino el formato de la matriz pedido. 
                if i%2==1: 
                    m[i].append(Dict[i])
                else: m[i].append("   +")

            else:                               #Resto de la matriz según se pedia que fuese, rellenado las celdas de las jugadas con tres espacios. 
                if i%2==0 and j%2==1: m[i].append("---")
                elif j%2==0: 
                    if i%2==0 or i==0 or i==26: m[i].append("+")
                    else: m[i].append("|")
                else: m[i].append("   ")

    return m

def rellenar_m(tablero, m):                     #Función que devuelve la matriz interfaz usuario rellena en función del contenido del tablero. 
    w = 0
    for i in range (1,(len(m)-1)):              #Este bucle se encarga de rellenar los límites entre las letras de los bloques así como entre los propios bloques. 
        k = 0
        if i % 2 == 1:
            for j in range(1,(len(m[0])-2)):
                if k < (len(tablero[0])-1) and j%2 == 1: 

                    if tablero[w][k] == tablero [w][k+1] and tablero[w][k] != " ": 
                        if tablero[w][k] == "a" or tablero [w][k]== "A": m[i][j+1] = "#"
                        elif tablero[w][k] == "b" or tablero [w][k]== "B": m[i][j+1] = "$"
                    else: m[i][j+1] = "|"
                    k +=1
                
            w += 1
                        
    w = 0
    for i in range(1,(len(m))-1):           #Este buble rellena con # o $ según el contenido del tablero. 
        k = 0
        if i % 2 == 1:
            for j in range(1,(len(m[0]))):
                if k < len(tablero[0]) and j%2 == 1:
                    if tablero [w][k] == "a" or tablero[w][k] == "A": m[i][j] = "###" 
                    elif tablero [w][k] == "b" or tablero [w][k]== "B": m [i][j] = "$$$"
                    elif tablero [w][k] == " ": m[i][j]="   "
                    k += 1
            w += 1

    return m


tablero = []        
m = creacion_matriz_interfaz()      #Llamada a la función para crear la matriz interfaz usuario. 
jug = [1,2,3]                       #Creación del array para tener la jugada en cachos. 
Dict = { "A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "-":"-"}
c = 10        
f = 12
q = 0
pattern = r"[A-L][0-9][<,>]"        #Creación de la plantilla que debe seguir la jugada introducida para ser valida. 
cont = 0                            #Inicializa el contador de puntos en 0. 
vacia=True                          #Varibale booleana que llevará el buble principal de la ejecución, solo termina el progrma si esta vale False. 

name = input("Introduzca la dirección y el nombre del fichero") 
fichero = open(name)                                            
todotext = fichero.readlines()                                  #Creo un array, del cual cada componente es una liena del fichero. 
fichero.close()
i = 0
while i < len(todotext):                                        #Fuerzo a que da componente del vecotr solo tenga 10 caracteres. 
        todotext[i] = (todotext[i])[0:10]
        i +=1
mododesarrollador = False                                     #El modo desarrollador imprime la matriz tablero en lugar de la interfaz, solo puede ser cambiado desde el código. 

while vacia == True:

            text = todotext[q]
            if(jug[1]==2):tablero = siguiente(tablero)          #La primera jugada crea la matriz tablero. 
            else:tablero = siguiente2(tablero)                  #Pone el en parte más arriba de la matriz, los bloques leidos desde el fichero.  
            print("1. INSERCION FILA")
            if mododesarrollador == True:  imprimir(tablero)    #Imprime por pantalla la matriz para que el usuario introduzca la jugada deseada.
            else: 
                m = rellenar_m(tablero, m)
                imprimir(m)

            print("Su puntuación acutal es de ", cont ," puntos.")

            jug = jugada(tablero)                                      #Llamada a la función jugada. 
            if jug [2] != "N":                                  #Si el usuraio introujo fin, entonces no se introduce y se asigna la condición para terminar la partida. 
                tablero = latera(jug, tablero)      

                print("2. MOVIMIENTO")
                
                if mododesarrollador == True:  imprimir(tablero)
                else: 
                    m = rellenar_m(tablero, m)
                    imprimir(m)

                tablero = bajadaporfilas(tablero)               #Bajo por filas la matriz.
                
                r=0
                modificacion = True

                while modificacion == True:                     #Bajada por bloques y eliminación una vez hayan todos bajado, al eliminar puede que un bloque. 
                    
                    tablero, modificacion = bajadaporbloques(tablero, modificacion)
                    
                    if (modificacion == False): 

                        print("3. CAÍDA: ")
                        if mododesarrollador == True:  imprimir(tablero)
                        else: 
                            m = rellenar_m(tablero, m)
                            imprimir(m)
                        
                        tablero, cont, modificacion = eliminar_filas(tablero, cont, modificacion)
                        print("4. ELIMINACIÓN: ")
                        if mododesarrollador == True:  imprimir(tablero)
                        else: 
                            m = rellenar_m(tablero, m)
                            imprimir(m)
                        
                        tablero = bajadaporfilas(tablero)       #Bajo todas las filas hasta su máximo. 


                q +=1                                           #Incremento en 1 para coger la siguiente fila de bloques del programa. 
                
                if espacios(tablero, 0) != True: vacia = False  #Si una vez acabada la jugada, y bajado bloques y eliminados filas, la fila A no está vacía el jugador pierde y la partida finaliza
                if q >= len(todotext): q = 0                     #Si se llega al final del fichero se vuelve a coger la primera fila. 
            else: vacia = False
            

