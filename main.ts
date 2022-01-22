input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    basic.showIcon(IconNames.Yes)
})
let _0 = 0
custom.foo(5, "Hello", MyEnum.Two)
basic.showLeds(`
    . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
`)
basic.pause(100)
basic.showLeds(`
    . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
`)
music.playMelody("E D G F B A C5 B ", 120)
basic.pause(100)
basic.showLeds(`
    . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
`)
basic.pause(100)
basic.showLeds(`
    . . . . .
        # # # # #
        . . . . .
        # # # # #
        . . . . .
`)
loops.everyInterval(500, function on_every_interval() {
    
})
basic.forever(function on_forever() {
    
    if (true) {
        _0 = 0
        _0 += 7
        led.plot(_0, _0)
        custom.foo(5, "Hello", MyEnum.One)
    }
    
})
