let x = 0
input.onGesture(Gesture.Shake, function () {
    x = randint(0, 2)
    if (x == 0) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (x == 1) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
    music.play(music.stringPlayable("C5 B A G F E D C ", 120), music.PlaybackMode.UntilDone)
})
basic.forever(function () {
	
})
