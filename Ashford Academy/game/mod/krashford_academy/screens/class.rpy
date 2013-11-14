image krashford class1 = "mod/screens/class/class1.jpg"
image krashford class2 = "mod/screens/class/class2.jpg"



init:
    if persistent.mod_disable_original_events == False:
        $ event("class1", "act == 'class' and deviance < 20", event.choose_one('class'), priority=200)
        $ event("class2", "act == 'class' and behavior < 50", event.choose_one('class'), priority=200)
        $ event("class3", "act == 'class' and deviance <= 15", event.choose_one('class'), priority=200)
        $ event("class4", "act == 'class' and deviance >= 50 and pda_rules == 'pda_bdsm'", event.choose_one('class'), priority=160)
        $ event("class36", "act == 'class' and inhibition < 75 and deviance > 20 and good_points > 1 and povGender == 'male'", event.once(), event.only())
        $ event("class37", "act == 'class' and inhibition < 85 and deviance > 10 and tentacles > 0", event.choose_one('class'), priority=80)
        $ event("class38", "act == 'class' and inhibition < 80 and deviance > 5", event.choose_one('class'), priority=80)
        $ event("class39", "act == 'class' and inhibition < 60 and deviance > 25 and povGender == 'male'", event.choose_one('class'), priority=80)
        $ event("class40", "act == 'class' and inhibition < 90 and deviance > 10", event.once(), event.only())


label krashford_class1:
    
    scene krashford class1 with fade
    if renpy.random.randint(1,2) == 1:
        "You better learn to handle that gun, it might give you another day to live."
    else:
        "I'm lucky standing next to her and not in front."
    #TODO: gun training +
    return


label krashford_class2:
    
    scene krashford class2 with fade
    if renpy.random.randint(1,2) == 1:
        "Run, gun and kill those bastards!"
    else:
        "Rage against the "
    #TODO: gun training +
    return

