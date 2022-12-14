class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2

def on_up_pressed():
    animation.set_action(chicken, ActionKind.Walking)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_down_pressed():
    animation.set_action(chicken, ActionKind.Walking)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_a_pressed():
    global egg
    chicken.set_image(img("""
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
    """))
    chicken.z = 1
    # enum SpriteKind {
    # Player,
    # Enemy
    # }
    egg = sprites.create(img("""
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
        """),
        SpriteKind.projectile)
    egg.z = 0
    egg.set_position(chicken.x, chicken.y)
    egg.y += 5
    chicken.y += -16
    music.play_tone(880, music.beat(BeatFraction.WHOLE))
    pause(200)
    for index in range(4):
        chicken.x += 5
        pause(50)
        chicken.y += 4
    chicken.set_image(assets.image("""
        chicken1
    """))
    info.change_score_by(1)
    if info.score() == 10:
        game.over(True)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_right_released():
    animation.set_action(chicken, ActionKind.Idle)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_right_pressed():
    animation.set_action(chicken, ActionKind.Walking)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_up_released():
    animation.set_action(chicken, ActionKind.Idle)
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_b_pressed():
    animation.set_action(chicken, ActionKind.Walking)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_left_pressed():
    animation.set_action(chicken, ActionKind.Walking)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_left_released():
    animation.set_action(chicken, ActionKind.Idle)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_menu_pressed():
    game.reset()
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def on_down_released():
    animation.set_action(chicken, ActionKind.Idle)
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

egg: Sprite = None
chicken: Sprite = None
info.set_score(0)
chicken32_2 = img("""
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
""")
egg16 = img("""
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
""")
scene.set_background_color(9)
# enum SpriteKind {
# Player,
# Enemy
# }
chicken = sprites.create(assets.image("""
    chicken1
"""), SpriteKind.player)
walking_chicken = animation.create_animation(ActionKind.Walking, 100)
walking_chicken.add_animation_frame(img("""
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
"""))
walking_chicken.add_animation_frame(img("""
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
"""))
walking_chicken.add_animation_frame(img("""
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
"""))
animation.attach_animation(chicken, walking_chicken)
controller.move_sprite(chicken)
chicken.set_stay_in_screen(True)