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

### Opción 1: Descargando el Juego (Recomendado)

La forma más sencilla de jugar, sin necesidad de instalar Python ni ninguna dependencia.

1.  **Ve a la sección de [Releases](https://github.com/joacov04/Juego-Truco/releases) de este repositorio.**
2.  Busca la última versión y descarga el ejecutable para tu sistema operativo (Windows o Linux).
3.  Ejecuta el archivo descargado para jugar.

### Opción 2: Ejecutando desde el Código Fuente

Si eres un desarrollador o prefieres ejecutarlo desde el código, sigue estos pasos.

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/joacov04/Juego-Truco.git
    cd Juego-Truco
    ```
2.  **Instala las dependencias:**
    ```bash
    pip install pygame
    ```
3.  **Ejecuta el juego:**
    ```bash
    python main.py
    ```

## Para Desarrolladores: Generar una Nueva Release

Este repositorio utiliza **GitHub Actions** para automatizar la creación de ejecutables para Windows y Linux.

Para generar una nueva release con tus cambios, sigue estos pasos:

1.  **Crea un tag de versión:**
    Usa el formato `vX.Y.Z` (por ejemplo, `v1.0.0`, `v1.1.0`).
    ```bash
    git tag v1.0.0
    ```

2.  **Sube el tag al repositorio:**
    ```bash
    git push origin v1.0.0
    ```

3.  Al subir el tag, una acción se ejecutará automáticamente, compilando los ejecutables y creando una nueva release con ellos.
