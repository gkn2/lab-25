let my_sprite = sprites.create(assets.image`mc`, SpriteKind.Player)
my_sprite.setPosition(80, 60)
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_event_down_pressed() {
    animation.runImageAnimation(my_sprite, assets.animation`a`, 100, true)
})
controller.down.onEvent(ControllerButtonEvent.Released, function on_event_down_released() {
    animation.stopAnimation(animation.AnimationTypes.All, my_sprite)
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function on_event_up_pressed() {
    animation.runImageAnimation(my_sprite, assets.animation`b`, 100, true)
})
controller.up.onEvent(ControllerButtonEvent.Released, function on_event_up_released() {
    animation.stopAnimation(animation.AnimationTypes.All, my_sprite)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_event_right_pressed() {
    animation.runImageAnimation(my_sprite, assets.animation`c`, 100, true)
})
controller.right.onEvent(ControllerButtonEvent.Released, function on_event_right_released() {
    animation.stopAnimation(animation.AnimationTypes.All, my_sprite)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_event_left_pressed() {
    animation.runImageAnimation(my_sprite, assets.animation`d`, 100, true)
})
controller.left.onEvent(ControllerButtonEvent.Released, function on_event_left_released() {
    animation.stopAnimation(animation.AnimationTypes.All, my_sprite)
})
