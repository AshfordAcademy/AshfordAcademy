init:
    image splash = "gui/splash.jpg"
    image main = "gui/mm_ground.png"

label splashscreen:
    scene black
    show text ""
    with Pause(0.5)
    
    show splash 
    with dissolve
    with Pause(2.0)
    
    scene black
    with dissolve
    with Pause(0.5)

    show main
    with dissolve

    return
