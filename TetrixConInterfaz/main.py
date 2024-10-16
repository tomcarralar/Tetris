# Tomás Carretero Alarcón   DNI: 04640646M 

import wx
import time
# la librería os solo la utilizo para que al abrir el fichero se ponga automáticamente en la dirección del archivo. 
import os
from wx.core import Dialog, MessageBoxCaptionStr, OK, OK_DEFAULT, YES_NO

CH_PANT = ord('#')  # Inicio secuencia caracteres pantalla
CH_FICH = ord('A')  # Inicio secuencia caracteres fichero (mayúsculas)
CH_FIL = ord('A')   # Inicio secuencia caracteres que representan filas
CH_COL = ord('0')   # Inicio secuencia caracteres que representan columnas

# La clase M es la del marco principal que contiene todos los elementos
class M(wx.Frame):
    # begin wxGlade: M.__init__ : generado automáticamente por wxGlade, comento principalemente lo añadido por mi a mayores
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE | wx.FULL_REPAINT_ON_RESIZE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((737, 543))
        self.SetTitle("Deslizator2")

        # self.passa no permitirá que se pinte el tablero hasta introuducir el archivo. 
        self.passa = False

        sizer = wx.BoxSizer(wx.HORIZONTAL)

        der = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(der, 1, wx.ALL | wx.EXPAND, 2)

        abrir = wx.BoxSizer(wx.HORIZONTAL)
        der.Add(abrir, 1, wx.ALL | wx.EXPAND, 2)

        # self.open referencia al bonton para abir el fichero 
        self.open = wx.Button(self, wx.ID_ANY, "Abrir Fichero")
        der.Add(self.open, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 2)

        # self.restart referencia al botón para comenzar de nuevo la partida
        self.restart = wx.Button(self, wx.ID_ANY, "Nueva partida")
        der.Add(self.restart, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 2)

        # self.boton_filas referencia al botón que a su vez llama al diálogo que contiene el espin de filas
        self.boton_filas = wx.Button(self, wx.ID_ANY, "Cambiar filas")
        der.Add(self.boton_filas, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 2)

        # self.numfil es la variable que contiene el número de filas con el que se está jugando, inicialmente 12
        self.numfil = 12

        sizer_5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Lista de jugadas:"), wx.HORIZONTAL)
        der.Add(sizer_5, 7, wx.ALL | wx.EXPAND, 2)

        # self.list_jugadas es una lista que contine las jugadas indicadas por el usuario y es lo que muestra la ListBox (self.out_jugadas)
        self.list_jugadas = []   

        self.out_jugadas = wx.ListBox(self, wx.ID_ANY, choices=self.list_jugadas)
        sizer_5.Add(self.out_jugadas, 1, wx.ALL | wx.EXPAND, 2)

        self.puntos = wx.StaticText(self, wx.ID_ANY, "Puntos =", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.puntos.SetFont(wx.Font(14, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        der.Add(self.puntos, 0, wx.ALL | wx.EXPAND, 2)

        izq = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(izq, 2, wx.ALL | wx.EXPAND, 2)

        # self.panel, seferencia al panel donde se muestra el estado del tablero. 
        self.panel = wx.Panel(self, wx.ID_ANY)
        izq.Add(self.panel, 1, wx.EXPAND, 0)

        self.SetSizer(sizer)

        self.Layout()
        
        # A partir de aqui están los enlaces para los eventos con sus respectivas funciones

        self.Bind(wx.EVT_BUTTON, self.on_abrir, self.open)
        self.Bind(wx.EVT_BUTTON, self.on_newgame, self.restart)
        self.Bind(wx.EVT_BUTTON, self.change_filas, self.boton_filas)
        self.Bind(wx.EVT_LISTBOX, self.on_volver_jugada, self.out_jugadas)
        self.panel.Bind(wx.EVT_PAINT, self.dibujarcuadrado)
        self.panel.Bind(wx.EVT_LEFT_DOWN, self.position)
        self.panel.Bind(wx.EVT_LEFT_UP, self.iod)

        self.update_draw()
        # end wxGlade

    # método que al recibir el evento de botón derecho soltado, escribe en self.jug la jugada del usuario
    def iod (self, event):
        y = event.GetPosition()

        if self.x[0] < y[0]: 
            self.jug = str(self.filchar+self.colchar+">")
        elif self.x[0] == y[0]: 
            self.jug = "---"
        else: 
            self.jug = str(self.filchar+self.colchar+"<")
        self.on_jugada_con_raton(self.jug)

    # método que al recibir el evento de bontón derecho clicado sobre el panel detecta la fila (self.filchar)
    # pero también el la columna (self.colchar) del bloque selecionado.
    def position (self,event):
        self.x = event.GetPosition()

        for i in range(self.numfil):
            if self.x[1] < (i+1)*self.alto: 
                self.filchar = chr(65+i)
                break
        for j in range(10):
            if self.x[0] < ((j+1)*self.ancho + self.letras): 
                self.colchar = chr(48+j)
                break    

    # Función que se ejecuta al pulsar el botón de abrir fichero y depliega un FileDialog para que el usuario lo seleccione.    
    def on_abrir(self, event):
        msg = "Selecione el fichero de jugadas"
        defdir = os.getcwd()
        wilcard = "Archivos de texto(.txt)|*.txt"
        diag = wx.FileDialog(self, msg, defdir, "", wilcard)
        resp = diag.ShowModal()

        if resp == wx.ID_OK:
            # guardo la ruta del fichero en self.name, por si el usuario quisiera restaurar la partida
            self.name = diag.GetPath()
            try: 
                # self.passa solo sera True si se ejecutan todas las instrucciones siguiente, esto es si es un fichero válido. 
                self.passa = False
                fichero = open(self.name)                                            
                self.todotext = fichero.readlines()
                fichero.close()
                # Creación del objeto de clase Tablero 
                self.tab = Tablero(self.name, self.numfil)
                self.tab.ins_fila()
                self.passa = True
                self.update_draw()
            except:
                self.passa = False 
                self.in_name.Clear()
                event.Skip()
        event.Skip()

    # Método que responde al pulsar el botón de nueva partida y restaura la misma. 
    def on_newgame(self, event):  # wxGlade: M.<event_handler>
        self.out_jugadas.Clear()
        self.list_jugadas = []
        self.puntos.SetLabel("Puntos = ")
        self.tab = Tablero(self.name, self.numfil)
        self.update_draw()
        self.tab.ins_fila()
        self.update_draw()
        event.Skip()
    # Metodo dervida del anterior pero sin insertar la fila, para evitar problemas al ser llamado por la función caida_animada() y no evento. 
    def on_newgame_sin_evento(self):
        self.out_jugadas.Clear()
        self.list_jugadas = []
        self.puntos.SetLabel("Puntos = ")
        self.tab = Tablero(self.name, self.numfil)
        self.update_draw()
        self.tab.ins_fila()
        self.update_draw()

    # Método que responde ante el evento generado al pulsar el botón de cambiar filas, llamando a otro método que despliega el digalogo.
    def change_filas(self, event):
        self.on_cambio_filas()

    def on_cambio_filas(self): 
        # creo una referencia al dialogo de las filas
        dlg_filas = Ruleta(self)
        # Muestro el diálogo y con un condicional, solo si devulve un cambio de filas, entonces obtengo el nuevo número y ejecuto la nueva partida. 
        if dlg_filas.ShowModal() != wx.ID_CANCEL:
            self.numfil = dlg_filas.numero()
            self.on_newgame_sin_evento()
            self.update_draw()
    # Método que responde a la llamada del método que transcribe la jugada del usuario que no es otro que self.iod()
    def on_jugada_con_raton(self, jug):
        # Meto la jugada en la función correspondiente de la primera practica para que esta la evalue.
        x = self.tab.jugada(jug)
        # Si la función devuelve 0 (bloque se puede desplazar lateralmente) o 1 (bajar sin tocar), entonces se ejecuta la instrucción
        if x == 0 or x == -1: 
            self.update_draw()      #acutlizo el panel para que se vea el movimiento
            self.out_jugadas.Insert(jug, len(self.list_jugadas))    # Acutualizo la ListBox así como su lista de jugadas
            self.list_jugadas.append(jug)
            # seguir es una v. local que impide salir de la bajada de bloques hasta que hayan bajado todos y se haya eliminado toda fila completa
            seguir = True
            while seguir:
                # mueve es otra v. local que hace que se ejecute el bucle hasta que nigún bloque pueda bajar más. 
                mueve = True
                while mueve == True:
                    mueve = False
                    # Desde la penúltima fila a la primera se comprueba, si estas contienen bloques que deban bajar. 
                    for fil_or in range(self.numfil-2, -1, -1):
                        # w es otra v. local que solo será True cuando en la fila que se mira, baje un bloque, caso en el que se actualiza el tablero.
                        w = self.tab.caida_animada(fil_or)
                        if w:
                            mueve = True
                            self.update_draw()
                # Una vez hayan bajado los bloques, compruebo si se puede eliminar alguna fila, caso en que se hace y se acutaliza el contador.        
                lis, punt = self.tab.eliminacion()
                self.puntos.SetLabel("Puntos = " + str(punt))
                seguir = len(lis) > 0

                if seguir: # si se cummple, se ha eliminado una fila y hay que bajar los bloques. 
                    self.update_draw()
                else: # caso contrario, se comprueba si la fila 0 contiene bloques, en cuyo caso la partida termina, pero da opción de comenzar de nuevo
                    if self.tab.lleno() == True: 
                        finjug = wx.MessageDialog(self,"Ha perdido", caption = "Mensaje", style = wx.YES_NO)
                        finjug.SetYesNoLabels("Play again", "Salir")
                        resp = finjug.ShowModal()
                        if resp == wx.ID_YES: 
                            self.on_newgame_sin_evento()
                            return 
                        else: exit()
            # Una vez eliminadas todas las filas completas y bajados todos los bloques, se inserta la fila para la proxima jugada.             
            self.tab.ins_fila()
            self.update_draw()
            #print(self.tab)
        return 
    # Método para gestionar la caida sin animación, y en el que la jugada se metía por teclado, lo mantego por si acaso diera fallo lo otro pero es lo mismo
    def on_jugada(self, event):  # wxGlade: M.<event_handler>
        
        jug = str(self.in_jugada.GetValue())
        self.in_jugada.Clear()
        #print(jug)
        x = self.tab.jugada(jug)
        if x == 0: 
            self.out_jugadas.Insert(jug, len(self.list_jugadas))
            self.list_jugadas.append(jug)
            seguir = True
            while seguir:
                fil_ori = self.numfil-2
                
                while fil_ori >=0:
                    x = False
                    x = self.tab.caida_animada(fil_ori)
                    fil_ori2 = fil_ori
                    
                    if x == True and fil_ori != 10: 
                        fil_ori +=1
                        while x == True:
                            self.update_draw()
                            fil_ori2 += 1 
                            x = self.tab.caida_animada(fil_ori2)

                    fil_ori = fil_ori - 1
                        
                lis, punt = self.tab.eliminacion()
                self.puntos.SetLabel("Puntos = " + str(punt))
                seguir = len(lis) > 0
                if seguir:
                    self.update_draw()
            if self.tab.lleno() == True: 
                finjug = wx.MessageDialog(self,"Ha perdido", caption = "Mensaje", style = wx.YES_NO)
                finjug.SetYesNoLabels("Play again", "Salir")
                resp = finjug.ShowModal()
                if resp == wx.ID_YES: 
                    self.on_newgame_sin_evento()
                    event.Skip()
                    
                else: exit()
            self.tab.ins_fila()
            self.update_draw()
            #print(self.tab)
        event.Skip()

    # Método que responde a la pulsación de una de las jugadas, restaurando el tablero a la situaicón del tablero tras esta:
    def on_volver_jugada(self, event):  # wxGlade: M.<event_handler>
        # obtengo la posición ocupada por la jugada selecionada en la lista
        last = self.out_jugadas.GetSelection()
        # creo una varaible local (lista) para guardar las jugadas que deben permanecer y la relleno
        lista = []
        for i in range(last+1):
            lista.append(self.list_jugadas[i])
        # vuelvo a crear el tablero, ya que hay que restaurar la partida. 
        self.tab = Tablero(self.name, self.numfil)
        # hago que el código de la primera practica ejecute las jugadas hasta la seleccionada pero sin nada de interfaz. 
        for rt in range(last + 1):
            self.tab.ins_fila()
            jug = self.list_jugadas[rt]
            self.tab.jugada(jug)
            seguir = True
            while seguir:
                self.tab.caida()
                lis, punt  = self.tab.eliminacion()
                seguir = len(lis) > 0
        # restauro los puntos a los que correspondan así como también limpio la lista de jugadas para después poner la copia que está en "lista"
        self.puntos.SetLabel("Puntos = " + str(punt))
        self.list_jugadas = []
        self.out_jugadas.Clear()
        for i in lista: 
            self.out_jugadas.Insert(i, len(self.list_jugadas))
            self.list_jugadas.append(i)
        # Inserto la fila correspondiente a la jugada siguiente y acutalizo ahora sí el panel. 
        self.tab.ins_fila()
        self.update_draw()
        event.Skip()
    # el panel se encuentra relacionado con este método que lo que hace es llamar al método draw que imprime el el tablero en todo momento
    def dibujarcuadrado (self, event): 
        self.draw(wx.PaintDC(self.panel))
    # otro método que hace lo mismo que el anterior pero esta vez no reacciona a un evento sino a una llamada de otra función
    def update_draw(self): 
        self.draw(wx.ClientDC(self.panel))
    # método que imprime el estado del tablero en el panel: 
    def draw(self, DC):
        # self.passa solo permite que se imprima en el panel cuando se haya abirto el fichero. 
        if self.passa == True:
            self.letras = 30 # espacio reservado para el indicador de filas
            # cada bloque unitario tendrá un ancho y alto que se calculan:
            self.ancho = (DC.GetSize().GetWidth()-self.letras)/10 
            self.alto = (DC.GetSize().GetHeight()-12)/self.numfil
            self.grey = DC.SetBrush(wx.Brush(wx.Colour('grey')))
            DC.Clear() # borro lo que contenga el panel
            # Pinto las letras correspondientes a las filas, así como los número de las columnas
            for i in range (self.numfil+1):
                DC.DrawText(chr(65+i), 10, (i+0.4)*self.alto)
                if i == (self.numfil): 
                    for j in range (0,10):
                        DC.DrawText(str(j), (j+0.4)*self.ancho+self.letras, i*self.alto-2)
            # Pinto el estado del tablero, recorriendo bloque a bloque este por filas y columnas
            for i in range (self.numfil):
                j = 0
                while j < 10: #utilizo un while para poder modificar la columna ya que un bloque puede no ser unitario. 
                    x = self.tab.compro(i,j) # Compruebo si en la casilla hay un bloque: 
                    if x == -1:  # sino lo hay paso a la siguiente casilla, caso contrario se pinta del color y tamaño correspondiente. 
                        j += 1
                    elif x[1] == 0:
                        self.azul = DC.SetBrush(wx.Brush(wx.Colour('blue')))
                        DC.DrawRoundedRectangle(j*self.ancho+self.letras, i*self.alto, self.ancho*x[0], self.alto, 8)
                        if x[0] > 1: j = j + x[0]   #cunado el bloque ocupe más de una casilla, se pasa al proximo bloque, no casilla. 
                        else: j += 1
                    elif x[1] == 1:
                        self.red = DC.SetBrush(wx.Brush(wx.Colour('red')))
                        DC.DrawRoundedRectangle(j*self.ancho+self.letras, i*self.alto, self.ancho*x[0], self.alto, 8)
                        if x[0] > 1: j = j + x[0] 
                        else: j += 1
                    elif x[1] == 2:
                        self.grey = DC.SetBrush(wx.Brush(wx.Colour('grey')))
                        DC.DrawRoundedRectangle(j*self.ancho+self.letras, i*self.alto, self.ancho*x[0], self.alto, 8)
                        if x[0] > 1: j = j + x[0] 
                        else: j += 1
                    else: j+=1

            time.sleep(0.1)    #tiempo entre pintada y pintada para crear la "animación"                    

# Ruelta es el nombre del dialogo personalizdo que contiene el mecanismo de cambio de filas.  
class Ruleta(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Ruleta.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle(u"Número de filas")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)
    
        self.spin_filas = wx.SpinCtrl(self, wx.ID_ANY, "12", min=5, max=24)
        sizer_1.Add(self.spin_filas, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 2)

        sizer_2 = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self.button_APPLY = wx.Button(self, wx.ID_APPLY, "")
        sizer_2.AddButton(self.button_APPLY)

        self.button_CANCEL = wx.Button(self, wx.ID_CANCEL, "")
        sizer_2.AddButton(self.button_CANCEL)

        sizer_2.Realize()

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.SetEscapeId(self.button_CANCEL.GetId())

        self.Bind(wx.EVT_BUTTON, self.appy_cerrar, self.button_APPLY)

        self.Layout()
    
    # Cuando se pulse el btón apply también debe desaparecer el recuadro
    def appy_cerrar(self, event): 
        self.Destroy()
        
    # Función que al ser llamada devuelve el número de filas selecionado por el usuario
    def numero (self):
        return self.spin_filas.GetValue()

def ciclo(lis):
    while True:
        for elem in lis:
            yield elem

class Bloque(object):
        """ Representa un bloque. Propiedades: fila, columna inicial, final y valor (color) """
        def __init__(self, fil, col0, col1, val):
            self.fil = fil
            self.col0 = col0
            self.col1 = col1
            self.val = val            # Es un entero positivo (0, 1, ...)
            self.n = col1 - col0 + 1  # Tamaño del bloque

        # Desplazamiento de un bloque
        def desplazar(self, dx, dy):
            self.fil += dy
            self.col0 += dx
            self.col1 += dx

        # Para depuración
        def __repr__(self):
            return f"{self.col0}-{self.col1},{self.fil}:{self.val}"

        def __str__(self):
            return chr(self.val+CH_PANT)*(4*self.n-1)

        
class Tablero(object):
    """ Representa el estado del Tablero en un momento dado """

    # Se pasa como parámetros el nombre de ficheros de filas entrantes
    # y el número de filas del tablero (las columnas son siempre 10)
    def __init__(self, nomfich, numfil):
        # Lectura de fichero de filas entrantes
        with open(nomfich) as fich:
            self.entrada = ciclo(fich.read().splitlines())
        # Propiedades/Atributos: Tamaño del tablero y puntuación
        self.nfil = numfil
        self.ncol = 10
        self.ptos = 0
        # El tablero se representa como una lista de filas,
        # cada fila es una lista de Bloques. Usamos compresión de listas
        self.dat = [[] for _ in range(numfil)]

    # ************** OPERACIONES PRINCIPALES ********************
    # ¡función propia! recibe como parámetros la fila y col de una celda y devuelve:
    def compro(self, fil, i):
        i = self.index_bloque(self.dat[fil], i)
        
        if i < 0:
            return -1       # -1 sino es una posición de bloque

        b = self.dat[fil][i]

        r = [(b.col1 -b.col0 + 1) , b.val]
        return r    # la cantidad de celdas que ocupa el bloque, así como también el color que tiene

    # Comprueba si hay bloques en la primera fila (fin de partida)
    def lleno(self):
        return len(self.dat[0]) > 0

    # Asigna una nueva fila de bloques en la parte superior del tablero
    def ins_fila(self):
        # Nueva linea de texto (formato fichero) que indica los bloques
        linea = next(self.entrada)
        self.dat[0] = [Bloque(0, c0, c1, val) for (c0, c1, val) in self.bloques_en_linea(linea)]

    # Traduce jugada (string) y la efectúa si es correcta. Valores devueltos:
    # -3 -> Sintaxis errónea
    # -2 -> El bloque no puede desplazarse
    # -1 -> No hay bloque en esa posición
    #  0 -> Jugada válida
    def jugada(self, jug):
        if len(jug) != 3:
            return -3
        # No hace movimiento
        if jug == '---':
            return 0
        # Obtener fila y columna
        fil = ord(jug[0]) - CH_FIL
        col = ord(jug[1]) - CH_COL
        # Fuera de rango
        if fil < 0 or fil >= self.nfil or col < 0 or col >= self.ncol:
            return -3
        # Indice del bloque en esa columna
        i = self.index_bloque(self.dat[fil], col)
        # No es una posición de bloque
        if i < 0:
            return -1
        b = self.dat[fil][i]
        # Comprobar si se puede desplazar
        if jug[2] == '<':            
            if i == 0:
                # Caso de bloque situado más a la izquierda
                if b.col0 == 0:  # Pegado a borde
                    return -2
                # Lo movemos al borde
                b.desplazar(-b.col0, 0)
            else:
                ba = self.dat[fil][i - 1]  # Bloque anterior
                db = b.col0 - ba.col1 - 1    # Espacio entre bloques
                if db == 0:  # Pegado a nuestro bloque
                    return -2
                # Lo movemos de forma que se "pegue" al bloque anterior
                b.desplazar(-db, 0)
        elif jug[2] == '>':
            if i == len(self.dat[fil])-1:
                # Caso de bloque situado más a la derecha
                if b.col1 == self.ncol-1:  # Pegado a borde
                    return -2
                # Lo movemos al borde
                b.desplazar(self.ncol-b.col1-1, 0)
            else:
                bs = self.dat[fil][i + 1]  # Bloque siguiente
                db = bs.col0 - b.col1 - 1    # Espacio entre bloques
                if db == 0:  # Pegado a nuestro bloque
                    return -2
                # Lo movemos de forma que se "pegue" al bloque siguiente
                b.desplazar(db, 0)
        else:
            return -3
        return 0

    # ¡Función propia!: Similar a la de Vaca, pero esta recibe como parámetro la fila y hace un movimiento de tan solo un bloque hacia abajo
    # en caso de ser posible, además devueve False si en esa fila no cae ningún bloque y true en caso contrario
    def caida_animada(self, fil_ori):
        mueve = False
        # Se recorren los bloques de la fila
        # Cuidado: Como es posible que durante el bucle modifiquemos la composición
        # de la fila, el bucle trabaja sobre una copia de la fila ([:])
        for b in self.dat[fil_ori][:]:
            # Se comprueban huecos en filas inferiores
            fil_des = pos_hueco = -1
            for i in range(fil_ori+1, self.nfil):
                ph = self.pos_ins_bloque(self.dat[i], b) # -1 sino se puede bajar más
                if ph == -1:
                    break
                pos_hueco = ph
                if self.compro(fil_ori + 1, b.col0) and self.compro(fil_ori+1, b.col1) == -1:
                    fil_des = fil_ori + 1
                else: fil_des == -1
                
            # Si hay descenso, mover el bloque
            if fil_des > -1:
                mueve = True
                self.dat[fil_ori].remove(b)
                self.dat[fil_des].insert(pos_hueco, b)
                b.desplazar(0, fil_des - fil_ori)

        return mueve


    # Se hacen caer los bloques recorriendo las filas desde la penúltima
    # a la primera (de "abajo" a "arriba")
    def caida(self):
        for fil_ori in range(self.nfil-2, -1, -1):
            # Se recorren los bloques de la fila
            # Cuidado: Como es posible que durante el bucle modifiquemos la composición
            # de la fila, el bucle trabaja sobre una copia de la fila ([:])
            for b in self.dat[fil_ori][:]:
                # Se comprueban huecos en filas inferiores
                fil_des = pos_hueco = -1
                for i in range(fil_ori+1, self.nfil):
                    ph = self.pos_ins_bloque(self.dat[i], b)
                    if ph == -1:
                        break
                    pos_hueco = ph
                    fil_des = i
                # Si hay descenso, mover el bloque
                if fil_des > -1:
                    self.dat[fil_ori].remove(b)
                    self.dat[fil_des].insert(pos_hueco, b)
                    b.desplazar(0, fil_des - fil_ori)

    # Elimina las filas completas, detectando si se produce una "reacción en cadena"
    # Devuelve la lista de bloques borrados
    def eliminacion(self):
        lis = []
        reaccion_cadena = False
        inc_ptos = 0
        for fil in range(self.nfil):
            if self.fila_completa(self.dat[fil], self.ncol):
                if self.fila_mismo_color(self.dat[fil]):
                    reaccion_cadena = True
                    break
                lis += self.borra_fila(fil)
                hay_borrado = True
                inc_ptos += self.ncol
        if reaccion_cadena:
            for fil in range(self.nfil):
                # Suma de las longitudes de todos los bloques de la fila,
                # usando una enumeración mediante la sintaxis (.. for .. in ..)
                inc_ptos += sum((b.n for b in self.dat[fil]))
                lis += self.borra_fila(fil)
        self.ptos += inc_ptos
        return lis, self.ptos

    def __str__(self):
        return self.tab2txt()

    def __repr__(self):
        return self.tab2txt()

    # ************** OPERACIONES AUXILIARES ********************

    # Se define como método aparte para que pueda sobrescribirse en clases derivadas
    # Devuelve la lista de bloques borrados
    def borra_fila(self, fil):
        lis = self.dat[fil]
        self.dat[fil] = []
        return lis

    # Iterador sobre todos los bloques del tablero, implementado mediante corutina/generador
    def iter_bloques(self):
        for fila in self.dat:
            for b in fila:
                yield b

    # Devuelve una tupla (columna inicial, final y valor/color) por cada bloque que
    # aparece en la línea de texto (formato fichero). Implementado mediante corutina/generador
    @staticmethod
    def bloques_en_linea(lin):
        i, n, c_ant = 0, 0, ' '
        for c in lin:
            if c != c_ant:
                if c_ant != ' ':
                    yield (i-n, i-1, ord(c_ant.upper())-CH_FICH)
                c_ant = c
                n = 1
            else:
                n += 1
            i += 1
        if c_ant != ' ':
            yield (i-n, i-1, ord(c_ant.upper())-CH_FICH)

    # Busca en la lista el bloque que contiene esa columna
    # Devuelve su índice en la lista o -1 si no existe
    @staticmethod
    def index_bloque(lis, col):
        i = 0
        for b in lis:
            if b.col0 <= col <= b.col1:
                return i
            i += 1
        return -1

    @staticmethod
    def pos_libre(lis, blo):
        i = blo.fil - 1
        for b in lis:
            if b.col0 > blo.col1: 
                break
            i -= 1
                
        return i if i==0 or lis[i-1].col < blo.col0 else -1

    # Devuelve la posición donde se debería insertar un bloque
    # si existe un hueco para él (o -1 si no se puede insertar)
    @staticmethod    
    def pos_ins_bloque(lis, blo):
        # Búsqueda del primer bloque totalmente posterior al nuestro
        i = 0
        for b in lis:
            if b.col0 > blo.col1:
                break
            i += 1
        # Si existe colisión, es con el bloque anterior al posterior
        return i if i == 0 or lis[i-1].col1 < blo.col0 else -1

    # Comprueba si una fila está completa
    @staticmethod
    def fila_completa(fila, numcol):
        if len(fila) == 0:
            return False
        # Comprobación de que los bloques inicial y final cubren los extremos 
        if fila[0].col0 != 0 or fila[-1].col1 != numcol-1:
            return False
        # Comprobación de que todos los bloques están "pegados"
        # Ver https://docs.python.org/3/library/functions.html#zip
        for (b1, b2) in zip(fila, fila[1:]):
            if b1.col1+1 != b2.col0:
                return False
        return True

    # Comprueba si en una fila completa todos los bloques son del mismo color
    # Ver https://docs.python.org/3/library/functions.html#all
    # Ver https://docs.python.org/3/library/functions.html#map
    # Ver https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
    @staticmethod
    def fila_mismo_color(fila):
        return all(map(lambda b: b.val == fila[0].val, fila[1:]))

    # Traducción de fila a texto
    def fil2txt(self, letra, fila):
        ca = 0
        lin = letra+' '
        for b in fila:
            lin += '|   '*(b.col0-ca) + '|' + str(b)
            ca = b.col1+1
        lin += '|   '*(self.ncol-ca) + '|\n'
        return lin
            
    # Traducción de tablero a texto
    def tab2txt(self):
        sep = '  ' + '---'.join(['+']*(self.ncol+1)) + '\n'
        ejey = [chr(i+CH_FIL) for i in range(self.nfil)]
        ejex = '    ' + '   '.join([chr(i+CH_COL) for i in range(self.ncol)]) + '\n'
        return sep + sep.join([self.fil2txt(*p) for p in zip(ejey, self.dat)]) + sep + ejex

# end of class M

class MyApp(wx.App):
    def OnInit(self):
        self.Marco = M(None, wx.ID_ANY, "")
        self.SetTopWindow(self.Marco)
        self.Marco.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
