# Juego Piedra, Papel o Tijeras para Micro:bit (MakeCode)

Un clásico juego de Piedra, Papel o Tijeras implementado para la tarjeta BBC Micro:bit utilizando el editor de bloques MakeCode. El jugador compite contra la Micro:bit, que elige su jugada de forma aleatoria.

## ✨ Características

*   **Elección del Jugador:** Utiliza los botones A, B y A+B para seleccionar Piedra, Papel o Tijeras.
*   **Elección Aleatoria de la Micro:bit:** La Micro:bit selecciona su jugada al azar.
*   **Retroalimentación Visual:** La matriz LED muestra la elección del jugador, la elección de la Micro:bit y el resultado del juego (Ganaste, Perdiste, Empate) mediante iconos.
*   **Retroalimentación Sonora:** Se incluyen efectos de sonido para las elecciones y para los resultados de la partida.
*   **Lógica Completa del Juego:** Implementa las reglas estándar de Piedra, Papel o Tijeras.

## 🎮 Cómo Jugar

1.  Al iniciar, la Micro:bit mostrará un mensaje de bienvenida ("PPT!").
2.  **Elige tu jugada:**
    *   Presiona el **Botón A** para elegir **Piedra** (se mostrará un icono de cuadrado pequeño).
    *   Presiona el **Botón B** para elegir **Papel** (se mostrará un icono de cuadrado grande).
    *   Presiona los **Botones A+B** simultáneamente para elegir **Tijeras** (se mostrará un icono de tijeras).
3.  Después de tu elección, la Micro:bit hará una pausa y luego mostrará su propia elección (Piedra, Papel o Tijeras) en la pantalla LED.
4.  Finalmente, la Micro:bit mostrará el resultado:
    *   **"GANASTE!"** con un icono éxito si ganas.
    *   **"PERDISTE!"** con un icono de fallo si pierdes.
    *   **"EMPATE!"** con un icono neutral si hay empate.
5.  Se reproducirá un sonido correspondiente al resultado.
6.  Después de unos segundos, la pantalla se limpiará, ¡lista para la siguiente ronda!

## 🛠️ Requisitos

### Hardware
*   1 x Tarjeta BBC Micro:bit (v1 o v2)
*   1 x Cable Micro USB
*   (Opcional) Pack de baterías si no se conecta por USB durante el juego.

### Software
*   Acceso a internet y un navegador web para usar [MakeCode para Micro:bit](https://makecode.microbit.org/).

## 🚀 Cómo Cargar el Programa

1.  Abre el editor de [MakeCode para Micro:bit](https://makecode.microbit.org/).
2.  Haz clic en **"Importar"** y luego en **"Importar Archivo"** para cargar el archivo `.hex` de este proyecto (si lo tienes).
3.  Alternativamente, puedes recrear el programa siguiendo la lógica de bloques descrita en clase o en la documentación asociada.
4.  Conecta tu Micro:bit al ordenador mediante el cable USB. Aparecerá como una unidad llamada `MICROBIT`.
5.  Haz clic en el botón **"Descargar"** en MakeCode. Se descargará un archivo `.hex`.
6.  Arrastra y suelta el archivo `.hex` descargado en la unidad `MICROBIT`.
7.  La LED amarilla en la parte posterior de la Micro:bit parpadeará mientras se transfiere el programa. Una vez que deje de parpadear, el programa estará cargado y listo para ejecutarse.

## 🧱 Estructura del Código (Bloques Principales)

El programa se organiza en los siguientes bloques principales:

*   **`al iniciar`**:
    *   Muestra un mensaje de bienvenida ("PPT!").
    *   Inicializa las variables `eleccion_jugador` y `eleccion_microbit` a 0.
*   **`al presionar el botón A`**:
    *   Establece `eleccion_jugador` a `1` (Piedra).
    *   Muestra el icono de Piedra.
    *   Reproduce un sonido de confirmación.
    *   Llama a la función `jugar_partida`.
*   **`al presionar el botón B`**:
    *   Establece `eleccion_jugador` a `2` (Papel).
    *   Muestra el icono de Papel.
    *   Reproduce un sonido de confirmación.
    *   Llama a la función `jugar_partida`.
*   **`al presionar los botones A+B`**:
    *   Establece `eleccion_jugador` a `3` (Tijeras).
    *   Muestra el icono de Tijeras.
    *   Reproduce un sonido de confirmación.
    *   Llama a la función `jugar_partida`.
*   **`función jugar_partida`**:
    *   La Micro:bit elige aleatoriamente un número entre 1 y 3 (`eleccion_microbit`).
    *   Muestra el icono correspondiente a la elección de la Micro:bit.
    *   Compara `eleccion_jugador` con `eleccion_microbit` para determinar el ganador usando lógica condicional (`si...entonces...si no`).
        *   Si son iguales: EMPATE.
        *   Si (jugador=Piedra Y microbit=Tijeras) O (jugador=Papel Y microbit=Piedra) O (jugador=Tijeras Y microbit=Papel): JUGADOR GANA.
        *   En otro caso: MICRO:BIT GANA.
    *   Muestra el resultado (texto e icono) y reproduce el sonido correspondiente (victoria, derrota o empate).
    *   Prepara la pantalla para una nueva partida.

## 💡 Posibles Mejoras y Extensiones

*   **Sistema de Puntuación:** Añadir variables para llevar la cuenta de las victorias del jugador y de la Micro:bit y mostrarlas.
*   **Número de Rondas:** Establecer un número fijo de rondas para determinar un ganador general del juego.
*   **Más Animaciones/Sonidos:** Personalizar aún más los iconos y las melodías para hacer el juego más atractivo.
*   **Diferentes Modos de Entrada:** Experimentar con el acelerómetro (agitar para elegir) u otros sensores si se dispone de ellos.

#### Metadata

* for PXT/microbit
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>
