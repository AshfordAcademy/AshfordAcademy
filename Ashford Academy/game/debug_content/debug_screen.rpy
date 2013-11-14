init:
    $ dbg_lbl_jump = ""

screen debug_screen:
    
    imagemap:
        ground "gui/menu_bg.png"
    vbox:    
        null height 20
        hbox:
            null width 20
            vbox:
                spacing 3
                text "{b}Morale{/b}"
                text "{b}Behavior{/b}"
                text "{b}Academics{/b}"
                text "{b}Artistery{/b}"
                text "{b}Athletics{/b}"
                text "{b}Inhibition{/b}"
                text "{b}Deviance{/b}"
                text "{b}Reputation{/b}"
                null height 20
                text "{b}Good points{/b}"
                text "{b}Evil points{/b}"
            null width 20
            grid 11 1:
                spacing 20
                vbox:
                    textbutton "0" action SetVariable("morale", 0)
                    textbutton "0" action SetVariable("behavior", 0)
                    textbutton "0" action SetVariable("academics", 0)
                    textbutton "0" action SetVariable("artistery", 0)
                    textbutton "0" action SetVariable("athletics", 0)
                    textbutton "0" action SetVariable("inhibition", 0)
                    textbutton "0" action SetVariable("deviance", 0)
                    textbutton "0" action SetVariable("reputation", 0)
                    null height 20
                    textbutton "0" action SetVariable("good_points", 0)
                    textbutton "0" action SetVariable("evil_points", 0)                    

                vbox:
                    textbutton "10" action SetVariable("morale", 10)
                    textbutton "10" action SetVariable("behavior", 10)
                    textbutton "10" action SetVariable("academics", 10)
                    textbutton "10" action SetVariable("artistery", 10)
                    textbutton "10" action SetVariable("athletics", 10)
                    textbutton "10" action SetVariable("inhibition", 10)
                    textbutton "10" action SetVariable("deviance", 10)
                    textbutton "10" action SetVariable("reputation", 10)
                    null height 20
                    textbutton "1" action SetVariable("good_points", 1)
                    textbutton "1" action SetVariable("evil_points", 1)

                vbox:
                    textbutton "20" action SetVariable("morale", 20)
                    textbutton "20" action SetVariable("behavior", 20)
                    textbutton "20" action SetVariable("academics", 20)
                    textbutton "20" action SetVariable("artistery", 20)
                    textbutton "20" action SetVariable("athletics", 20)
                    textbutton "20" action SetVariable("inhibition", 20)
                    textbutton "20" action SetVariable("deviance", 20)
                    textbutton "20" action SetVariable("reputation", 20)
                    null height 20
                    textbutton "2" action SetVariable("good_points", 2)
                    textbutton "2" action SetVariable("evil_points", 2)

                vbox:
                    textbutton "30" action SetVariable("morale", 30)
                    textbutton "30" action SetVariable("behavior", 30)
                    textbutton "30" action SetVariable("academics", 30)
                    textbutton "30" action SetVariable("artistery", 30)
                    textbutton "30" action SetVariable("athletics", 30)
                    textbutton "30" action SetVariable("inhibition", 30)
                    textbutton "30" action SetVariable("deviance", 30)
                    textbutton "30" action SetVariable("reputation", 30)
                    null height 20
                    textbutton "3" action SetVariable("good_points", 3)
                    textbutton "3" action SetVariable("evil_points", 3)

                vbox:
                    textbutton "40" action SetVariable("morale", 40)
                    textbutton "40" action SetVariable("behavior", 40)
                    textbutton "40" action SetVariable("academics", 40)
                    textbutton "40" action SetVariable("artistery", 40)
                    textbutton "40" action SetVariable("athletics", 40)
                    textbutton "40" action SetVariable("inhibition", 40)
                    textbutton "40" action SetVariable("deviance", 40)
                    textbutton "40" action SetVariable("reputation", 40)
                    null height 20
                    textbutton "4" action SetVariable("good_points", 4)
                    textbutton "4" action SetVariable("evil_points", 4)

                vbox:
                    textbutton "50" action SetVariable("morale", 50)
                    textbutton "50" action SetVariable("behavior", 50)
                    textbutton "50" action SetVariable("academics", 50)
                    textbutton "50" action SetVariable("artistery", 50)
                    textbutton "50" action SetVariable("athletics", 50)
                    textbutton "50" action SetVariable("inhibition", 50)
                    textbutton "50" action SetVariable("deviance", 50)
                    textbutton "50" action SetVariable("reputation", 50)
                    null height 20
                    textbutton "5" action SetVariable("good_points", 5)
                    textbutton "5" action SetVariable("evil_points", 5)

                vbox:
                    textbutton "60" action SetVariable("morale", 60)
                    textbutton "60" action SetVariable("behavior", 60)
                    textbutton "60" action SetVariable("academics", 60)
                    textbutton "60" action SetVariable("artistery", 60)
                    textbutton "60" action SetVariable("athletics", 60)
                    textbutton "60" action SetVariable("inhibition", 60)
                    textbutton "60" action SetVariable("deviance", 60)
                    textbutton "60" action SetVariable("reputation", 60)
                    null height 20
                    textbutton "6" action SetVariable("good_points", 6)
                    textbutton "6" action SetVariable("evil_points", 6)

                vbox:
                    textbutton "70" action SetVariable("morale", 70)
                    textbutton "70" action SetVariable("behavior", 70)
                    textbutton "70" action SetVariable("academics", 70)
                    textbutton "70" action SetVariable("artistery", 70)
                    textbutton "70" action SetVariable("athletics", 70)
                    textbutton "70" action SetVariable("inhibition", 70)
                    textbutton "70" action SetVariable("deviance", 70)
                    textbutton "70" action SetVariable("reputation", 70)
                    null height 20
                    textbutton "7" action SetVariable("good_points", 7)
                    textbutton "7" action SetVariable("evil_points", 7)

                vbox:
                    textbutton "80" action SetVariable("morale", 80)
                    textbutton "80" action SetVariable("behavior", 80)
                    textbutton "80" action SetVariable("academics", 80)
                    textbutton "80" action SetVariable("artistery", 80)
                    textbutton "80" action SetVariable("athletics", 80)
                    textbutton "80" action SetVariable("inhibition", 80)
                    textbutton "80" action SetVariable("deviance", 80)
                    textbutton "80" action SetVariable("reputation", 80)
                    null height 20
                    textbutton "8" action SetVariable("good_points", 8)
                    textbutton "8" action SetVariable("evil_points", 8)

                vbox:
                    textbutton "90" action SetVariable("morale", 90)
                    textbutton "90" action SetVariable("behavior", 90)
                    textbutton "90" action SetVariable("academics", 90)
                    textbutton "90" action SetVariable("artistery", 90)
                    textbutton "90" action SetVariable("athletics", 90)
                    textbutton "90" action SetVariable("inhibition", 90)
                    textbutton "90" action SetVariable("deviance", 90)
                    textbutton "90" action SetVariable("reputation", 90)
                    null height 20
                    textbutton "9" action SetVariable("good_points", 9)
                    textbutton "9" action SetVariable("evil_points", 9)

                vbox:
                    textbutton "100" action SetVariable("morale", 100)
                    textbutton "100" action SetVariable("behavior", 100)
                    textbutton "100" action SetVariable("academics", 100)
                    textbutton "100" action SetVariable("artistery", 100)
                    textbutton "100" action SetVariable("athletics", 100)
                    textbutton "100" action SetVariable("inhibition", 100)
                    textbutton "100" action SetVariable("deviance", 100)
                    textbutton "100" action SetVariable("reputation", 100)
                    null height 20
                    textbutton "10" action SetVariable("good_points", 10)
                    textbutton "10" action SetVariable("evil_points", 10)

        null height 70
        vbox:
            spacing 20
            textbutton "Jump to label" action Jump("dbg_lbl_input")
            textbutton "Repeat last jump" action Jump("dbg_lbl_jmp")
    hbox:
            xalign 0.95
            yalign 0.95
            $ ui.imagebutton("gui/return_button_idle.png", "gui/return_button_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=ui.returns(0))
        
label dbg_lbl_jmp:
    if renpy.has_label(dbg_lbl_jump):
        hide screen debug_screen
        jump expression dbg_lbl_jump
    else:
        "Sorry no such label was found. Try again."
        $ update_stat("Deviance", "deviance", 0, 20, 100)
        return
        
label dbg_lbl_input:
    $ dbg_lbl_jump = renpy.input("Write the label name","")
    call dbg_lbl_jmp

