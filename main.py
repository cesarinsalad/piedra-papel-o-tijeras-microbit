def jugar_partida():
    global eleccion_microbit
    basic.pause(500)
    eleccion_microbit = randint(1, 3)
    if eleccion_microbit == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif eleccion_microbit == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
    music.play(music.tone_playable(440, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(100)
    if eleccion_jugador == eleccion_microbit:
        basic.show_leds("""
            . # # # .
            # . . . #
            # . . . #
            # . . . #
            . # # # .
            """)
        music.play_melody("C E C E - - - - ", 700)
        basic.pause(200)
        basic.show_string("EMPATE!")
    elif eleccion_jugador == 1 and eleccion_microbit == 3:
        basic.show_icon(IconNames.YES)
        basic.show_string("GANASTE!")
        music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
            music.PlaybackMode.IN_BACKGROUND)
    elif eleccion_jugador == 2 and eleccion_microbit == 1:
        basic.show_icon(IconNames.YES)
        basic.show_string("GANASTE!")
        music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
            music.PlaybackMode.IN_BACKGROUND)
    elif eleccion_jugador == 3 and eleccion_microbit == 2:
        basic.show_icon(IconNames.YES)
        basic.show_string("GANASTE!")
        music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
            music.PlaybackMode.IN_BACKGROUND)
    else:
        basic.show_icon(IconNames.NO)
        basic.show_string("PERDISTE!")
        music._play_default_background(music.built_in_playable_melody(Melodies.POWER_DOWN),
            music.PlaybackMode.IN_BACKGROUND)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
        . . . . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # . . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # # .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        """)
    basic.clear_screen()

def on_button_pressed_a():
    global eleccion_jugador
    eleccion_jugador = 1
    basic.show_icon(IconNames.SMALL_SQUARE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    jugar_partida()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global eleccion_jugador
    eleccion_jugador = 3
    basic.show_icon(IconNames.SCISSORS)
    music.play(music.tone_playable(392, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    jugar_partida()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global eleccion_jugador
    eleccion_jugador = 2
    basic.show_icon(IconNames.SQUARE)
    music.play(music.tone_playable(330, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    jugar_partida()
input.on_button_pressed(Button.B, on_button_pressed_b)

eleccion_jugador = 0
eleccion_microbit = 0
eleccion_microbit = 0
eleccion_jugador = 0
basic.show_string("PPT!")
basic.pause(500)
basic.show_icon(IconNames.HAPPY)
basic.pause(1000)
basic.clear_screen()