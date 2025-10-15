# Juego de Truco Argentino - Trabajo Práctico

Este proyecto fue desarrollado como parte del trabajo práctico de la materia **Programación I** de la **Tecnicatura Universitaria en Programación** en la **Universidad Tecnológica Nacional (UTN), Facultad Regional Avellaneda**.

El objetivo fue desarrollar una versión del juego de cartas **Truco** para dos jugadores (un jugador contra la máquina), aplicando los conceptos de la programación funcional y la librería Pygame.

## Descripción del Juego

El juego implementa una partida de Truco a 15 o 30 puntos, donde el usuario se enfrenta a un oponente controlado por la computadora. El sistema registra el nombre del jugador y actualiza un historial de puntajes al finalizar cada partida.

### Modos de Oponente

Se puede elegir entre dos tipos de oponentes, cada uno con una lógica de juego distinta:

1.  **Oponente Aleatorio:**
    -   Juega sus cartas de forma completamente aleatoria.
    -   **Envido:** Si tiene envido (dos cartas del mismo palo), siempre lo canta. Si le cantan envido, siempre lo acepta. Si tiene más de 30 puntos de envido, canta "falta envido".

2.  **Oponente Inteligente:**
    -   **Truco:** Si juega primero, siempre juega su carta más alta. Si juega segundo y tiene una carta para empatar o ganar la mano, la juega; de lo contrario, juega su carta más baja.
    -   **Envido:** Solo canta o acepta un envido si su puntaje es superior a 27 puntos.

### Estado Actual del Proyecto

-   [x] Lógica del **Truco** en todas sus variantes (Truco, Retruco, Vale 4).
-   [x] Elección de oponente (Aleatorio o Inteligente).
-   [x] Selección de puntaje máximo (15 o 30 puntos).
-   [x] Sistema de historial de puntajes guardado en `archivos/historial.csv`.
-   [ ] **Funcionalidad del Envido:** La lógica del envido está parcialmente implementada y se encuentra en desarrollo.

## Contenidos y Tecnologías Aplicadas

Para cumplir con las condiciones de aprobación del trabajo práctico, se aplicaron los siguientes conceptos:

-   **Manejo avanzado de TDA:** Uso de listas, diccionarios, sets y tuplas para gestionar la baraja, las manos de los jugadores y el estado del juego.
-   **Manejo de strings:** Para la interacción con el usuario y la presentación de información.
-   **Lectura y escritura de archivos:** Para la persistencia del historial de puntajes en formato `.csv`.
-   **Paradigma funcional:** Se priorizó el uso de funciones puras y la modularización del código.
-   **Pygame:** Para la interfaz gráfica, se implementaron los siguientes elementos:
    -   Ciclo de vida del juego y manejo de eventos.
    -   Configuraciones de pantalla y posicionamiento de elementos.
    -   Carga y manipulación de imágenes y superficies.
    -   Uso de sonidos para mejorar la experiencia de usuario.
    -   Manejo de colisiones para la interacción con botones y cartas.

## ¿Cómo Jugar?

### Ejecutando desde el Código Fuente

1.  **Clona el repositorio:**
    ```bash
    git clone <URL-del-repositorio>
    cd <nombre-del-repositorio>
    ```
2.  **Instala las dependencias:**
    ```bash
    pip install pygame
    ```
3.  **Ejecuta el juego:**
    ```bash
    python main.py
    ```

### Creando un Ejecutable (Windows)

Para compilar un archivo `.exe` que no requiera tener Python instalado:

1.  **Instala PyInstaller:**
    ```bash
    pip install pyinstaller
    ```
2.  **Ejecuta el comando de compilación:**
    ```bash
    pyinstaller --onefile --windowed --add-data "cartas;cartas" --add-data "audio;audio" --add-data "archivos;archivos" main.py
    ```
3.  El archivo `main.exe` estará disponible en la carpeta `dist`.
