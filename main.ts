input.onButtonPressed(Button.A, function () {
    d = 3
})
input.onButtonPressed(Button.AB, function () {
    d = 9
})
input.onButtonPressed(Button.B, function () {
    d = 6
})
input.onGesture(Gesture.Shake, function () {
    d = 12
})
let scores = 0
let d = 0
let x = 0
let y = 0
let rx = randint(0, 4)
let rrrrrrrrrrrrrrrrrrrrrrrrrry = randint(0, 4)
basic.forever(function () {
    led.plot(x, y)
})
basic.forever(function () {
    basic.pause(1000)
    basic.clearScreen()
    if (d == 3) {
        x = 1 + x
    }
    if (d == 9) {
        x = x - 1
    }
    if (d == 6) {
        y = 1 + y
    }
    if (d == 12) {
        y = y - 1
    }
    if (x > 4) {
        x = 0
    }
    if (y > 4) {
        y = 0
    }
    if (x < 0) {
        x = 4
    }
    if (y < 0) {
        y = 4
    }
})
basic.forever(function () {
    led.toggle(rx, rrrrrrrrrrrrrrrrrrrrrrrrrry)
    basic.pause(500)
})
basic.forever(function () {
    if (rx == x && rrrrrrrrrrrrrrrrrrrrrrrrrry == y) {
        rrrrrrrrrrrrrrrrrrrrrrrrrry = randint(0, 4)
        rx = randint(0, 4)
        scores = scores + 1
        basic.showNumber(scores)
        basic.pause(100)
    }
})
