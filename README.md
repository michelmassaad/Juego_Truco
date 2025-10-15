# Juego de Truco Argentino 🃏

[](https://www.python.org/) [](https://www.pygame.org/) [](https://www.google.com/search?q=)

¡Bienvenido al Truco Argentino\! Un clásico juego de cartas desarrollado en Python con Pygame, donde te enfrentarás a un oponente controlado por la computadora.

Este proyecto fue creado como trabajo práctico para la materia **Programación I** de la **Tecnicatura Universitaria en Programación** en la **UTN-FRA**.

-----

## ✨ Características Principales

  * **Partidas Clásicas:** Juega partidas a 15 o 30 puntos.
  * **Oponente con IA:** Elige entre dos dificultades:
      * 🤖 **Aleatorio:** Un oponente impredecible que juega sus cartas al azar y siempre acepta los desafíos de envido.
      * 🧠 **Inteligente:** Un oponente más estratégico que juega su carta más alta para ganar la mano y solo canta envido si tiene buenos puntos.
  * **Lógica de Truco Completa:** Desafía a la máquina con Truco, Retruco y Vale 4.
  * **Historial de Partidas:** Tu nombre y puntaje se guardan automáticamente en un archivo `.csv` para llevar un registro de tus hazañas.

-----

## 🎮 ¿Cómo Jugar? (¡La forma fácil\!)

¡No necesitas instalar nada\! Descarga el ejecutable y empieza a jugar en segundos.

1.  **[Haz clic aquí para ir a Releases](https://github.com/michelmassaad/Juego_Truco/releases)**.
2.  Busca la última versión (`Latest`) y descarga el archivo `.exe`.
3.  Descomprime el archivo donde quieras.
4.  ¡Listo\! Ejecuta el archivo `Juego_Truco.exe` y a jugar.

-----

## 🚀 Para Desarrolladores

Si quieres modificar el código o simplemente ejecutarlo desde la fuente, sigue estos pasos.

### Ejecutar desde el código fuente

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/michelmassaad/Juego_Truco.git
    cd Juego_Truco
    ```
2.  **Instala las dependencias:**
    ```bash
    pip install pygame
    ```
3.  **Ejecuta el juego:**
    ```bash
    python main.py
    ```

### Crear tu propio ejecutable

Puedes compilar tu propia versión del juego usando **PyInstaller**.

1.  **Instala PyInstaller:**
    ```bash
    pip install pyinstaller
    ```
2.  **Ejecuta el comando de compilación desde la raíz del proyecto:**
    ```bash
    pyinstaller --onefile --windowed --add-data "cartas;cartas" --add-data "audio;audio" --add-data "archivos;archivos" main.py
    ```
3.  Tu nuevo ejecutable estará en la carpeta `dist/`.

-----

## 📈 Estado del Proyecto

  * ✅ Lógica completa de **Truco**, **Retruco** y **Vale 4**.
  * ✅ Elección de oponente y puntaje máximo.
  * ✅ Sistema de historial de puntajes funcionales.
  * 🚧 **Lógica del Envido:** En desarrollo (parcialmente implementada).

-----

## 🛠️ Tecnologías Utilizadas

Este proyecto fue construido aplicando los siguientes conceptos y herramientas:

  * **Lenguaje:** Python
  * **Librería Gráfica:** Pygame para la interfaz, manejo de eventos, imágenes y sonidos.
  * **Paradigma:** Programación Funcional.
  * **Estructuras de Datos:** Uso intensivo de listas, diccionarios y tuplas para gestionar la lógica del juego.
  * **Manejo de Archivos:** Lectura y escritura de archivos `.csv` para la persistencia de datos.
