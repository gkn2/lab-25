my_sprite = sprites.create(assets.image("""mc"""), SpriteKind.player)

my_sprite.set_position(80, 60)




def on_event_down_pressed():
    animation.run_image_animation(
        my_sprite,
        assets.animation("a"),
        100,
        True 
    )

def on_event_down_released():
    animation.stop_animation(animation.AnimationTypes.All, my_sprite)

controller.down.on_event(ControllerButtonEvent.PRESSED, on_event_down_pressed)
controller.down.on_event(ControllerButtonEvent.RELEASED, on_event_down_released)





def on_event_up_pressed():
    animation.run_image_animation(
        my_sprite,
        assets.animation("b"),
        100,
        True
    )

def on_event_up_released():
    animation.stop_animation(animation.AnimationTypes.All, my_sprite)

controller.up.on_event(ControllerButtonEvent.PRESSED, on_event_up_pressed)
controller.up.on_event(ControllerButtonEvent.RELEASED, on_event_up_released)





def on_event_right_pressed():
    animation.run_image_animation(
        my_sprite,
        assets.animation("c"),
        100,
        True
    )

def on_event_right_released():
    animation.stop_animation(animation.AnimationTypes.All, my_sprite)

controller.right.on_event(ControllerButtonEvent.PRESSED, on_event_right_pressed)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_event_right_released)





def on_event_left_pressed():
    animation.run_image_animation(
        my_sprite,
        assets.animation("d"),
        100,
        True
    )

def on_event_left_released():
    animation.stop_animation(animation.AnimationTypes.All, my_sprite)

controller.left.on_event(ControllerButtonEvent.PRESSED, on_event_left_pressed)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_event_left_released)