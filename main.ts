radio.onReceivedValue(function (name, value) {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Entertainer), music.PlaybackMode.InBackground)
    music.rest(music.beat(BeatFraction.Whole))
    basic.showArrow(ArrowNames.North)
})
input.onSound(DetectedSound.Quiet, function () {
    if (true) {
        radio.sendNumber(0)
    }
})
basic.showLeds(`
    . . . . .
    . # . # .
    . # # # .
    . . # . .
    . . . . .
    `)
