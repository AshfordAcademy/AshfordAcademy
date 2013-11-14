# define achievement notification image and reset all achievement triggers
image ach_acquired = "gui/achievement_acquired.png"
image ach_not_acquired = "gui/achievement_not_acquired.png"


python:
    example_achievement_trigger = False

    ## Stat related vars
    persistent.perfect_students_achievement_trigger = False
    persistent.behave_and_be_happy_achievement_trigger = False
    persistent.ein_zwei_einstein_achievement_trigger = False
    persistent.monet_madness_achievement_trigger = False
    persistent.pumping_iron_achievement_trigger = False
    persistent.the_1_achievement_trigger = False
    persistent.hentai_highschool_achievement_trigger = False
    persistent.take_that_mit_achievement_trigger = False

    ## Ending related vars - Note that they are called directly from game_over.rpy
    persistent.my_baby_shot_me_achievement_trigger = False
    persistent.burning_down_the_school_achievement_trigger = False
    persistent.we_dont_need_no_education_achievement_trigger = False

init:
    # define achievement notification position
    $ screen_center = Position(xpos=0.5, ypos=0.5)
    # define achievements criteria

    ## Let's keep example for study reasons.
    # $ event("example_achievement", "morale >= 0 and example_achievement_trigger == False", event.solo())

    ## Stat related
    $ event("perfect_students_achievement", "behavior == 100 and academics == 100 and artistery == 100 and athletics == 100 and persistent.perfect_students_achievement_trigger != True", event.solo())
    $ event("behave_and_be_happy_achievement", "behavior == 100 and morale == 100 and persistent.behave_and_be_happy_achievement_trigger != True", event.solo())
    $ event("ein_zwei_einstein_achievement", "academics == 100 and persistent.ein_zwei_einstein_achievement_trigger  != True", event.solo())
    $ event("monet_madness_achievement", "artistery == 100 and persistent.monet_madness_achievement_trigger != True", event.solo())
    $ event("pumping_iron_achievement", "athletics == 100 and persistent.pumping_iron_achievement_trigger != True", event.solo())
    $ event("the_1_achievement", "cash >= 25000 and persistent.the_1_achievement_trigger != True", event.solo())
    $ event("hentai_highschool_achievement", "deviance == 100 and inhibition == 0 and persistent.hentai_highschool_achievement_trigger != True", event.solo())
    $ event("take_that_mit_achievement", "reputation >= 100 and persistent.take_that_mit_achievement_trigger != True", event.solo())


# example achievement
label example_achievement:
    # floats the achievement image on screen until player interacts
    show ach_acquired at screen_center with easeinright
    # message to be presented to the player
    "Example Achievement unlocked!"
    # possible unlock triggers. buildings, policies, etc.
    # flag for achievement set to true
    $ example_achievement_trigger = True
    return


label perfect_students_achievement:
    show ach_acquired at screen_center with easeinright
    "Perfect Students Achievement unlocked!"
    $ persistent.perfect_students_achievement_trigger = True
    return


label behave_and_be_happy_achievement:
    show ach_acquired at screen_center with easeinright
    "Behave and be happy Achievement unlocked!"
    $ persistent.behave_and_be_happy_achievement_trigger = True
    return


label ein_zwei_einstein_achievement:
    show ach_acquired at screen_center with easeinright
    "Ein, Zwei, Einstein Achievement unlocked!"
    $ persistent.ein_zwei_einstein_achievement_trigger = True
    return


label monet_madness_achievement:
    show ach_acquired at screen_center with easeinright
    "Monet Madness Achievement unlocked!"
    $ persistent.monet_madness_achievement_trigger = True
    return


label pumping_iron_achievement:
    show ach_acquired at screen_center with easeinright
    "Pumping Iron Achievement unlocked!"
    $ persistent.pumping_iron_achievement_trigger = True
    return


label the_1_achievement:
    show ach_acquired at screen_center with easeinright
    "The 1\% Achievement unlocked!"
    $ persistent.the_1_achievement_trigger = True
    return


label hentai_highschool_achievement:
    show ach_acquired at screen_center with easeinright
    "Hentai Highschool Achievement unlocked!"
    $ persistent.hentai_highschool_achievement_trigger = True
    return


label take_that_mit_achievement:
    show ach_acquired at screen_center with easeinright
    "Take that M.I.T. Achievement unlocked!"
    $ persistent.take_that_mit_achievement_trigger = True
    return


# achievements summary screen
screen achievement_summary_screen:
    frame:
        xpos 20
        ypos 20
        xmaximum 1240
        ymaximum 660
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            hbox:
                xfill True
                grid 3 11:
                    xfill True
                    spacing 20
                    vbox:
                        if persistent.perfect_students_achievement_trigger == True:
                            image("gui/achievement_acquired.png")
                        else:
                            image("gui/achievement_not_acquired.png")
                    vbox:
                        ypos 20
                        text("{b}Perfect Students{/b}")
                        text("All study related stats maxed.")
                    vbox:
                        ypos 20
                        text("Achievement unlockables")

                    vbox:
                        if persistent.behave_and_be_happy_achievement_trigger == True:
                            image("gui/achievement_acquired.png")
                        else:
                            image("gui/achievement_not_acquired.png")
                    vbox:
                        ypos 20
                        text("{b}Kindergarten cop - Behave and be happy{/b}")
                        text("Behavior and Morale at max.")
                    vbox:
                        ypos 20
                        text("Achievement unlockables:\n{i}Cheerleading Club{/i}")

                    vbox:
                        if persistent.ein_zwei_einstein_achievement_trigger == True:
                            image("gui/achievement_acquired.png")
                        else:
                            image("gui/achievement_not_acquired.png")
                    vbox:
                        ypos 20
                        text("{b}Ein, Zwei, Einstein{/b}")
                        text("Academics at max.")
                    vbox:
                        ypos 20
                        text("Achievement unlockables")

                    vbox:
                        if persistent.monet_madness_achievement_trigger == True:
                            image("gui/achievement_acquired.png")
                        else:
                            image("gui/achievement_not_acquired.png")
                    vbox:
                        ypos 20
                        text("{b}Monet Madness{/b}")
                        text("Art at max.")
                    vbox:
                        ypos 20
                        text("Achievement unlockables")

                    vbox:
                        if persistent.pumping_iron_achievement_trigger == True:
                            image("gui/achievement_acquired.png")
                        else:
                            image("gui/achievement_not_acquired.png")
                    vbox:
                        ypos 20
                        text("{b}Pumping Iron{/b}")
                        text("Athletics at max.")
                    vbox:
                        ypos 20
                        text("Achievement unlockables")

                    vbox:
                        if persistent.hentai_highschool_achievement_trigger == True:
                            image("gui/achievement_acquired.png")
                        else:
                            image("gui/achievement_not_acquired.png")
                    vbox:
                        ypos 20
                        text("{b}Hentai Highschool{/b}")
                        text("Max deviance with zero inhibition.")
                    vbox:
                        ypos 20
                        text("Achievement unlockables")

                    vbox:
                        if persistent.the_1_achievement_trigger == True:
                            image("gui/achievement_acquired.png")
                        else:
                            image("gui/achievement_not_acquired.png")
                    vbox:
                        ypos 20
                        text("{b}The 1%{/b}")
                        text("Amass more then 25 000 $.")
                    vbox:
                        ypos 20
                        text("Achievement unlockables: \n{i}Dormitory{/i}")

                    vbox:
                        if persistent.take_that_mit_achievement_trigger == True:
                            image("gui/achievement_acquired.png")
                        else:
                            image("gui/achievement_not_acquired.png")
                    vbox:
                        ypos 20
                        text("{b}Take that M.I.T.{/b}")
                        text("Achieve maximum reputation.")
                    vbox:
                        ypos 20
                        text("Achievement unlockables")

                    vbox:
                        if persistent.my_baby_shot_me_achievement_trigger == True:
                            image("gui/achievement_acquired.png")
                        else:
                            image("gui/achievement_not_acquired.png")
                    vbox:
                        ypos 20
                        text("{b}Bang Bang, My baby shot me down.{/b}")
                        text("???")
                    vbox:
                        ypos 20
                        text("Achievement unlockables")

                    vbox:
                        if persistent.we_dont_need_no_education_achievement_trigger == True:
                            image("gui/achievement_acquired.png")
                        else:
                            image("gui/achievement_not_acquired.png")
                    vbox:
                        ypos 20
                        text("{b}We don't need no education.{/b}")
                        text("???")
                    vbox:
                        ypos 20
                        text("Achievement unlockables: \n{i}Cafeteria{/i}")

                    vbox:
                        if persistent.burning_down_the_school_achievement_trigger == True:
                            image("gui/achievement_acquired.png")
                        else:
                            image("gui/achievement_not_acquired.png")
                    vbox:
                        ypos 20
                        text("{b}Burning down the school, MY school.{/b}")
                        text("???")
                    vbox:
                        ypos 20
                        text("Achievement unlockables")

    hbox:
            xalign 0.985
            yalign 0.99
            textbutton _("Return") action Return()