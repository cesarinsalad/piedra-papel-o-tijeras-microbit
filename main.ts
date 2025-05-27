function jugar_partida () {
    basic.pause(500)
    eleccion_microbit = randint(1, 3)
    if (eleccion_microbit == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (eleccion_microbit == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
    music.play(music.tonePlayable(440, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    basic.pause(100)
    if (eleccion_jugador == eleccion_microbit) {
        basic.showLeds(`
            . # # # .
            # . . . #
            # . . . #
            # . . . #
            . # # # .
            `)
        music.playMelody("C E C E - - - - ", 700)
        basic.pause(200)
        basic.showString("EMPATE!")
    } else if (eleccion_jugador == 1 && eleccion_microbit == 3) {
        basic.showIcon(IconNames.Yes)
        basic.showString("GANASTE!")
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerUp), music.PlaybackMode.InBackground)
    } else if (eleccion_jugador == 2 && eleccion_microbit == 1) {
        basic.showIcon(IconNames.Yes)
        basic.showString("GANASTE!")
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerUp), music.PlaybackMode.InBackground)
    } else if (eleccion_jugador == 3 && eleccion_microbit == 2) {
        basic.showIcon(IconNames.Yes)
        basic.showString("GANASTE!")
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerUp), music.PlaybackMode.InBackground)
    } else {
        basic.showIcon(IconNames.No)
        basic.showString("PERDISTE!")
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerDown), music.PlaybackMode.InBackground)
    }
    basic.pause(1000)
    basic.showLeds(`
        . . . . .
        . . . . .
        # . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . . . . .
        # # . . .
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . . . . .
        # # # . .
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . . . . .
        # # # # .
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        `)
    basic.clearScreen()
}
input.onButtonPressed(Button.A, function () {
    eleccion_jugador = 1
    basic.showIcon(IconNames.SmallSquare)
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    jugar_partida()
})
input.onButtonPressed(Button.AB, function () {
    eleccion_jugador = 3
    basic.showIcon(IconNames.Scissors)
    music.play(music.tonePlayable(392, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    jugar_partida()
})
input.onButtonPressed(Button.B, function () {
    eleccion_jugador = 2
    basic.showIcon(IconNames.Square)
    music.play(music.tonePlayable(330, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    jugar_partida()
})
let eleccion_jugador = 0
let eleccion_microbit = 0
eleccion_microbit = 0
eleccion_jugador = 0
basic.showString("PPT!")
basic.pause(500)
basic.showIcon(IconNames.Happy)
basic.pause(1000)
basic.clearScreen()
