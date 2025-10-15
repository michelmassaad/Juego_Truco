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

¡Claro\! Ahora que ofreces múltiples archivos, la sección de "Cómo Jugar" debe ser una guía clara para que el usuario elija el archivo correcto para su sistema operativo.

Aquí tienes una versión mucho más clara y detallada, lista para copiar y pegar en tu `README.md`.

-----

## 🎮 ¿Cómo Jugar?

¡No necesitas instalar nada\! Sigue los pasos para tu sistema operativo y empieza a jugar en segundos.

1.  **Ve a la página de [Releases](https://www.google.com/search?q=https://github.com/michelmassaad/Juego_Truco/releases/latest) para descargar el juego.**
2.  Busca el archivo que corresponda a tu sistema operativo a continuación:

-----

### 🪟 Para Windows

Tienes dos opciones. **Te recomendamos descargar el archivo `.zip`** para evitar advertencias de seguridad.

1.  Descarga el archivo `1-JuegoTruco-windows.zip`.
2.  Haz clic derecho sobre el archivo y selecciona **"Extraer todo..."** para descomprimirlo en una carpeta.
3.  ¡Listo\! Abre la nueva carpeta y haz doble clic en `JuegoTruco.exe` para jugar.

*(Alternativa: puedes descargar `2-JuegoTruco-windows.exe` directamente, pero es probable que Windows muestre una advertencia de seguridad que deberás ignorar.)*

-----

###  Para macOS

1.  Descarga el archivo `3-JuegoTruco-macos.zip`.
2.  Haz doble clic en el archivo `.zip` para descomprimirlo. Se creará la aplicación `JuegoTruco.app`.
3.  **Importante:** La primera vez que lo abras, es posible que macOS te impida hacerlo. Haz **clic derecho** sobre `JuegoTruco.app` y selecciona **"Abrir"**. Te aparecerá una ventana de confirmación donde podrás volver a hacer clic en "Abrir". Solo necesitas hacer esto una vez.
4.  ¡A jugar\!

-----

### 🐧 Para Linux (Ubuntu/Debian)

Te recomendamos descargar el archivo `.zip`.

1.  Descarga el archivo `4-JuegoTruco-linux.zip`.
2.  Descomprime el archivo donde prefieras.
3.  Abre una terminal en la carpeta donde descomprimiste el juego.
4.  Dale permisos de ejecución al archivo con el siguiente comando:
    ```bash
    chmod +x JuegoTruco
    ```
5.  ¡Listo\! Ejecuta el juego desde la terminal con `./JuegoTruco` o haciendo doble clic sobre el archivo.

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
