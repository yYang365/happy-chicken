class ActionKind {
    static Walking = 0
    static Idle = 1
    static Jumping = 2
}

controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    animation.setAction(chicken, ActionKind.Walking)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    animation.setAction(chicken, ActionKind.Walking)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    chicken.setImage(img`
        ................................
                ................................
                ................................
                ............eeeeeeee............
                ...........eeee22e2e............
                ...........ee2e2222e............
                ...........ee222222e............
                ............eeeeeeee............
                ..........eee555555eee..........
                .........ee5555555555ee.........
                ...eeeeeee555555555555ee........
                ...eebdbe55555555555555e........
                ....eebe555ee45555555557e.......
                ......ee555ee55555555555e.......
                ......ee5555555555555555e.......
                ......ee5555555555555555e.......
                ......ee5555555555555555eeeee...
                .....eee5555555555555555e755e...
                ....eeee5555555555555555e554e...
                ....ee.e7555555555555554e55ee...
                .......ee55555555555555e7554e...
                ........ee5555555555557e55ee....
                .........ee55555555557eee55e....
                ..........eee5555555ee...ee.....
                .........ee.eeeeeeeeee..........
                .....eeeee...........eeeee......
                .......eee...........eee........
                .......eee...........e.e........
                .........e...........e..........
                ................................
                ................................
                ................................
    `)
    chicken.z = 1
    //  enum SpriteKind {
    //  Player,
    //  Enemy
    //  }
    egg = sprites.create(img`
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . c c c . . . . . . . 
                    . . . . . c b d d e . . . . . . 
                    . . . . c d d d d d e . . . . . 
                    . . . . b d d d d d d c . . . . 
                    . . . c d d d d d d d e . . . . 
                    . . . c d d d d d d d b . . . . 
                    . . . c d d d d d d d b . . . . 
                    . . . c d d d d d d d b . . . . 
                    . . . c d d d d d d d e . . . . 
                    . . . . c d d d d d d c . . . . 
                    . . . . c b d d d b c . . . . . 
                    . . . . . . c c c c . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        `, SpriteKind.Projectile)
    egg.z = 0
    egg.setPosition(chicken.x, chicken.y)
    egg.y += 5
    chicken.y += -16
    music.playTone(880, music.beat(BeatFraction.Whole))
    pause(200)
    for (let index = 0; index < 4; index++) {
        chicken.x += 5
        pause(50)
        chicken.y += 4
    }
    chicken.setImage(assets.image`
        chicken1
    `)
    info.changeScoreBy(1)
    if (info.score() == 10) {
        game.over(true)
    }
    
})
controller.right.onEvent(ControllerButtonEvent.Released, function on_right_released() {
    animation.setAction(chicken, ActionKind.Idle)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    animation.setAction(chicken, ActionKind.Walking)
})
controller.up.onEvent(ControllerButtonEvent.Released, function on_up_released() {
    animation.setAction(chicken, ActionKind.Idle)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    animation.setAction(chicken, ActionKind.Walking)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    animation.setAction(chicken, ActionKind.Walking)
})
controller.left.onEvent(ControllerButtonEvent.Released, function on_left_released() {
    animation.setAction(chicken, ActionKind.Idle)
})
controller.menu.onEvent(ControllerButtonEvent.Pressed, function on_menu_pressed() {
    game.reset()
})
controller.down.onEvent(ControllerButtonEvent.Released, function on_down_released() {
    animation.setAction(chicken, ActionKind.Idle)
})
let egg : Sprite = null
let chicken : Sprite = null
info.setScore(0)
let chicken32_2 = img`
    ................................
        ................................
        ................................
        ............eeeeeeee............
        ...........eeee22e2e............
        ...........ee2e2222e............
        ...........ee222222e............
        ............eeeeeeee............
        ..........eee555555eee..........
        .........ee5555555555ee.........
        ...eeeeeee555555555555ee........
        ...eebdbe55555555555555e........
        ....eebe555ee45555555557e.......
        ......ee555ee55555555555e.......
        ......ee5555555555555555e.......
        ......ee5555555555555555e.......
        ......ee5555555555555555eeeee...
        .....eee5555555555555555e755e...
        ....eeee5555555555555555e554e...
        ....ee.e7555555555555554e55ee...
        .......ee55555555555555e7554e...
        ........ee5555555555557e55ee....
        .........ee55555555557eee55e....
        ..........eee5555555ee...ee.....
        .........ee.eeeeeeeeee..........
        .....eeeee...........eeeee......
        .......eee...........eee........
        .......eee...........e.e........
        .........e...........e..........
        ................................
        ................................
        ................................
`
let egg16 = img`
    . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . c c c . . . . . . . 
        . . . . . c b d d e . . . . . . 
        . . . . c d d d d d e . . . . . 
        . . . . b d d d d d d c . . . . 
        . . . c d d d d d d d e . . . . 
        . . . c d d d d d d d b . . . . 
        . . . c d d d d d d d b . . . . 
        . . . c d d d d d d d b . . . . 
        . . . c d d d d d d d e . . . . 
        . . . . c d d d d d d c . . . . 
        . . . . c b d d d b c . . . . . 
        . . . . . . c c c c . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . .
`
scene.setBackgroundColor(9)
//  enum SpriteKind {
//  Player,
//  Enemy
//  }
chicken = sprites.create(assets.image`
    chicken1
`, SpriteKind.Player)
let walking_chicken = animation.createAnimation(ActionKind.Walking, 100)
walking_chicken.addAnimationFrame(img`
    ................................
        ................................
        ................................
        .............ccceeeec...........
        ............ceee2eeec...........
        ............ceee2e2ec...........
        ............ce22222ec...........
        ............ceeeeeeec...........
        ...........cee55555eec..........
        ..........ce555555555ec.........
        ........cee555555555554c........
        ......ceee5555555555555ec.......
        ....ce7de455ee5555555555e.......
        ...ce7dde555ee5555555555ec......
        ...ceeeee555555555555555ec......
        ....e7d7e5555555555555554c......
        .....c77e5555555555555554cccc...
        ......cee5555555555555557e55ec..
        .......ce555555555555555e555ec..
        ........e555555555555555e554c...
        ........ce55555555555555e555e...
        .........ce555555555555ee55fc...
        ..........ce5555555555ecc45e....
        ...........cee555555eec..ccc....
        ............cccceecccc..........
        ............cc......cc..........
        ...........cffc....cfc..........
        ..........cccccc..cccccc........
        ..........c.cc.c..c.cc.c........
        ................................
        ................................
        ................................
`)
walking_chicken.addAnimationFrame(img`
    ................................
        ................................
        ................................
        .............ccceeeec...........
        ............ceee2eeec...........
        ............ceee2e2ec...........
        ............ce22222ec...........
        ............ceeeeeeec...........
        ...........cee55555eec..........
        ..........ce555555555ec.........
        ........cee555555555554c........
        ......ceee5555555555555ec.......
        ....ce7de455ee5555555555e.......
        ...ce7dde555ee5555555555ec......
        ...ceeeee555555555555555ec......
        ....e7d7e5555555555555554c......
        .....c77e5555555555555554cccc...
        ......cee5555555555555557e55ec..
        .......ce555555555555555e555ec..
        ........e555555555555555e554c...
        ........ce55555555555555e555e...
        .........ce555555555555ee55fc...
        ..........ce5555555555ecc45e....
        ...........cee555555eec..ccc....
        ............cccceecccc..........
        ............cc.....cfc..........
        ............cc....cccccc........
        ...........cffc...c.cc.c........
        ..........cccccc................
        ..........c.cc.c................
        ................................
        ................................
`)
walking_chicken.addAnimationFrame(img`
    ................................
        ................................
        ................................
        .............ccceeeec...........
        ............ceee2eeec...........
        ............ceee2e2ec...........
        ............ce22222ec...........
        ............ceeeeeeec...........
        ...........cee55555eec..........
        ..........ce555555555ec.........
        ........cee555555555554c........
        ......ceee5555555555555ec.......
        ....ce7de455ee5555555555e.......
        ...ce7dde555ee5555555555ec......
        ...ceeeee555555555555555ec......
        ....e7d7e5555555555555554c......
        .....c77e5555555555555554cccc...
        ......cee5555555555555557e55ec..
        .......ce555555555555555e555ec..
        ........e555555555555555e554c...
        ........ce55555555555555e555e...
        .........ce555555555555ee55fc...
        ..........ce5555555555ecc45e....
        ...........cee555555eec..ccc....
        ............cccceecccc..........
        ...........cffc.....cc..........
        ..........cccccc....cc..........
        ..........c.cc.c...cfc..........
        ..................cccccc........
        ..................c.cc.c........
        ................................
        ................................
`)
animation.attachAnimation(chicken, walking_chicken)
controller.moveSprite(chicken)
chicken.setStayInScreen(true)
