def on_button_pressed_a():
    global d
    d = 3
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global d
    d = 9
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global d
    d = 6
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global d
    d = 12
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

scores = 0
d = 0
x = 0
y = 0
rx = randint(0, 4)
rrrrrrrrrrrrrrrrrrrrrrrrrry = randint(0, 4)

def on_forever():
    led.plot(x, y)
basic.forever(on_forever)

def on_forever2():
    global x, y
    basic.pause(1000)
    basic.clear_screen()
    if d == 3:
        x = 1 + x
    if d == 9:
        x = x - 1
    if d == 6:
        y = 1 + y
    if d == 12:
        y = y - 1
    if x > 4:
        x = 0
    if y > 4:
        y = 0
    if x < 0:
        x = 4
    if y < 0:
        y = 4
basic.forever(on_forever2)

def on_forever3():
    led.toggle(rx, rrrrrrrrrrrrrrrrrrrrrrrrrry)
    basic.pause(500)
basic.forever(on_forever3)

def on_forever4():
    global rrrrrrrrrrrrrrrrrrrrrrrrrry, rx, scores
    if rx == x and rrrrrrrrrrrrrrrrrrrrrrrrrry == y:
        rrrrrrrrrrrrrrrrrrrrrrrrrry = randint(0, 4)
        rx = randint(0, 4)
        scores = scores + 1
        basic.show_number(scores)
        basic.pause(100)
basic.forever(on_forever4)
