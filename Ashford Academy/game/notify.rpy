image acad_gain = "gui/acad-chibi.png"

screen notify:
    zorder 100
    add message at _notify_transform 

    # This controls how long it takes between when the screen is
    # first shown, and when it begins hiding.
    timer 1.5 action Hide('notify')


transform _notify_transform:
    # These control the position.
    xalign .5 yalign -0.2

    # These control the actions on show and hide.
    on show:
        parallel:
            alpha 0
            linear 0.75 alpha 1.0
        parallel:
            ease 0.75 top
    on hide:
        linear .5 alpha 0.0