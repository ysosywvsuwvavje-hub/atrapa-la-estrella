def on_received_value(name, value):
    music._play_default_background(music.built_in_playable_melody(Melodies.ENTERTAINER),
        music.PlaybackMode.IN_BACKGROUND)
    music.rest(music.beat(BeatFraction.WHOLE))
    basic.show_arrow(ArrowNames.NORTH)
radio.on_received_value(on_received_value)

def on_sound_quiet():
    if True:
        radio.send_number(0)
input.on_sound(DetectedSound.QUIET, on_sound_quiet)

basic.show_leds("""
    . . . . .
    . # . # .
    . # # # .
    . . # . .
    . . . . .
    """)