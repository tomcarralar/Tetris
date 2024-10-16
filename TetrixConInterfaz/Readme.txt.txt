Deslizator II - Juego con Interfaz Gráfica
Descripción
Este proyecto implementa la segunda versión del juego Deslizator, una aplicación de tablero que utiliza una Interfaz Gráfica de Usuario (GUI) desarrollada con la librería wxPython. Es una continuación de la primera práctica en la que el juego se ejecutaba en un entorno de texto. En esta ocasión, se ha diseñado una versión orientada a ventanas con varios controles interactivos para mejorar la experiencia del usuario.

Funcionalidades Implementadas
1. Estado Gráfico del Tablero
	- El tablero del juego se muestra de manera gráfica en todo momento. Cada vez que ocurre un cambio en el juego (movimientos, caídas de bloques, etc.), la interfaz se actualiza para reflejar el estado actual del tablero.
2. Lectura de Archivos de Entrada
	- El programa permite que el usuario seleccione un archivo que contiene las jugadas iniciales del juego mediante un control de entrada. Este archivo sigue el mismo formato que en la práctica anterior. No es posible comenzar a jugar hasta que se haya seleccionado y leído el archivo de entrada.
3. Configuración de Filas
	- El número de filas del tablero se puede modificar desde la interfaz, con un control dedicado para este ajuste. Si se cambia el número de filas durante una partida, el juego se reinicia automáticamente.
4. Iniciar Nueva Partida
	- El usuario puede iniciar una nueva partida en cualquier momento utilizando un botón dedicado en la interfaz.
5. Lista de Jugadas
	- Se muestra una lista con todas las jugadas realizadas hasta el momento en la partida actual, permitiendo al usuario seguir el progreso del juego.
6. Puntuación
	- La puntuación actual del jugador se muestra en la interfaz y se actualiza a medida que se realizan jugadas.
7. Realizar Jugadas
	- El usuario puede ingresar una jugada manualmente escribiendo el código de la jugada en un cuadro de texto dentro de la interfaz. Las jugadas son procesadas y reflejadas en el tablero gráfico.
8. Otras funcionalidades implementadas
	- Indicación de jugadas mediante el ratón: El usuario puede mover los bloques en el tablero utilizando el ratón, haciendo clic y arrastrando para indicar la dirección del movimiento (izquierda o derecha).
	- Animación de movimientos y caídas: Los movimientos de los bloques y sus caídas se animan, brindando una experiencia visual más fluida.
	- Adaptación al tamaño de ventana: La interfaz gráfica se adapta al tamaño de la ventana si esta se redimensiona, ajustando el tamaño de los bloques y el tablero en consecuencia.

Requisitos Técnicos
	Librería wxPython: Todo el desarrollo de la GUI está basado en la librería wxPython. 
	Para ejecutar el proyecto, asegúrate de tener instalada esta librería: "pip install wxPython"

Ejecución 
Para ejecutar el juego, simplemente ejecuta el archivo principal desde una terminal o un entorno de desarrollo como Visual Studio Code: "python main.py"
	- Una vez esto deberás abrir con el menú "abir fichero" uno de los archivos que se adjuntan como "examen_.txt"
