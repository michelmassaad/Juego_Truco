# Juego de Truco Argentino

¡Bienvenido al clásico juego de cartas argentino, el Truco, implementado en Python con Pygame!

Este proyecto te permite jugar una partida de Truco contra la computadora. Podrás cantar envido, truco, y poner a prueba tus habilidades en este emocionante juego de ingenio y engaño.

![Captura de pantalla del juego](https://i.imgur.com/tuqgI8a.png)  <!-- Reemplazar con una captura de pantalla real si es posible -->

## ¿Cómo Jugar?

Tienes dos maneras de disfrutar del juego:

### Opción 1: Usando el Ejecutable (Windows)

La forma más sencilla de jugar. No necesitas instalar nada.

1.  Ve a la sección de **Releases** en este repositorio de GitHub.
2.  Descarga el archivo `Truco.exe` de la última versión.
3.  Haz doble clic en el archivo `Truco.exe` y ¡a jugar!

### Opción 2: Ejecutando desde el Código Fuente

Si eres un desarrollador o prefieres ejecutarlo desde el código, sigue estos pasos.

#### Prerrequisitos

-   Tener instalado Python 3.x en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
-   Tener `pip` (el gestor de paquetes de Python) disponible.

#### Pasos

1.  **Clona o descarga este repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio
    ```
    *(Reemplaza `tu-usuario/tu-repositorio` con la URL real de este repositorio)*

2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    El único requisito es Pygame.
    ```bash
    pip install pygame
    ```

4.  **Ejecuta el juego:**
    ```bash
    python main.py
    ```

## Para Desarrolladores: Crear tu Propio Ejecutable

Si has hecho cambios en el código y quieres compilar tu propia versión del archivo `.exe`, puedes hacerlo usando **PyInstaller**.

1.  **Instala PyInstaller:**
    ```bash
    pip install pyinstaller
    ```

2.  **Ejecuta el comando de compilación:**
    Abre una terminal en la raíz del proyecto y ejecuta el siguiente comando:

    ```bash
    # Para Windows
    pyinstaller --onefile --windowed --add-data "cartas;cartas" --add-data "audio;audio" --add-data "archivos;archivos" main.py

    # Para macOS o Linux
    pyinstaller --onefile --windowed --add-data "cartas:cartas" --add-data "audio:audio" --add-data "archivos:archivos" main.py
    ```

3.  **Encuentra tu ejecutable:**
    Una vez que el proceso termine, encontrarás el archivo `main.exe` (o `main` en Linux/macOS) dentro de la nueva carpeta `dist`.

## Estructura del Proyecto

-   `main.py`: El punto de entrada principal del juego. Contiene el bucle del juego.
-   `funciones/`: Contiene la lógica del juego (creación de la baraja, reglas, etc.).
-   `informacion/`: Contiene las constantes y datos del juego (colores, rutas de archivos, etc.).
-   `cartas/`: Contiene las imágenes de las cartas.
-   `audio/`: Contiene los archivos de sonido.
-   `archivos/`: Contiene el `historial.csv` para guardar las puntuaciones.

¡Que te diviertas!
