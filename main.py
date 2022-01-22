def on_logo_pressed():
    basic.show_icon(IconNames.YES)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

_0 = 0
custom.foo(5, "Hello", MyEnum.TWO)
basic.show_leds("""
    . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
""")
basic.pause(100)
basic.show_leds("""
    . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
""")
music.play_melody("E D G F B A C5 B ", 120)
basic.pause(100)
basic.show_leds("""
    . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
""")
basic.pause(100)
basic.show_leds("""
    . . . . .
        # # # # #
        . . . . .
        # # # # #
        . . . . .
""")

def on_every_interval():
    pass
loops.every_interval(500, on_every_interval)

def on_forever():
    global _0
    if True:
        _0 = 0
        _0 += 7
        led.plot(_0, _0)
        custom.foo(5, "Hello", MyEnum.ONE)
basic.forever(on_forever)
