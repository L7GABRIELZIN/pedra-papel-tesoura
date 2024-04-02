x = 0

def on_gesture_shake():
    global x
    x = randint(0, 2)
    if x == 0:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif x == 1:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
    music.play(music.string_playable("C5 B A G F E D C ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
