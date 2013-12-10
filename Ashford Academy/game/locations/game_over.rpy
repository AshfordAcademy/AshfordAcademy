image bg game_over_shot1 = "locations/splash/game_over_shot1.jpg"
image bg game_over_shot2 = "locations/splash/game_over_shot2.jpg"
image bg game_over_burn = "locations/splash/game_over_burn.jpg"

#Since the game_over function created some weird bugs I made this instead.

label game_over_test:
    if reputation <= 0:
        if evil_points > 2:
            jump game_over_shot
        else:
            jump game_over_fired

    if total_days > 90 and behavior <= 20 and renpy.random.random() > 0.8:
        jump game_over_burn
    else:
        jump day_no_game_over

# If reputation falls to zero at any point of the game, it will end the following day.        
label game_over_fired:
    
    show teacher_susan normal at center
    teacher_susan "[povTitle] [povLastName], I must talk to you."
    pov "Sure, what is it?"
    teacher_susan "We better step into the office."
    pov "Eh, sure."
    scene bg office with fade
    show teacher_susan normal at center
    teacher_susan "..."
    pov "Well?"
    teacher_susan "As you're well aware, the results here at Ashford have been all but acceptable for quite some time now."
    pov "It's been tough, no kidding."
    teacher_susan "Frankly, [povTitle] [povLastName], we counted on you to turn things around. We trusted you with our dearest dream, our academy, our Ashford."
    pov "Wait a sec-"
    teacher_susan "I'm afraid we can wait no longer. The board has instructed me to release you from duty."
    pov "What?"
    teacher_susan "I hereby declare your position vacant. Your services are no longer required."
    pov "Susan, I-"
    teacher_susan "Thank you [povTitle] [povLastName], that will be all. Please have your desk cleared within an hour. Good day."
    "You are an utter failure as a principal. Hopefully, the next couple of decades will be gentle with you, though you'll probably never get a shot at a job this big again."
    info "GAME OVER"
    if persistent.new_game_plus != True:
        $ persistent.new_game_plus = True
        "New Game Plus unlocked."
    if persistent.we_dont_need_no_education_achievement_trigger != True:
        show ach_acquired at screen_center with easeinright
        "We don't need no education Achievement unlocked!"
        $ persistent.we_dont_need_no_education_achievement_trigger = True
    $ renpy.full_restart()


label game_over_shot:
    
    "The door to your office creaks as you open it."
    scene bg game_over_shot1 with fade
    pov "Huh?"
    "You sick bastard! I will punish you for everything you have done and all those you have hurt."
    "You find yourself staring down the barrel of a gun."
    menu:
        "Please, don't do this!":
            pass
        
        "Do it. I'm not afraid.":
            pass

        "Well, I did enjoy every last bit of it." if new_game_plus == True:
            pass

    scene bg game_over_shot2 with vpunch
    "BANG!"
    "In just a shivering second, a life can be taken. One tiny second. The last thing going through your head, except images of young ladies, is the bullet."
    info "GAME OVER"
    if persistent.new_game_plus != True:
        $ persistent.new_game_plus = True
        "New Game Plus unlocked."
    if persistent.my_baby_shot_me_achievement_trigger != True:
        show ach_acquired at screen_center with easeinright
        "Bang bang, My baby shot me down Achievement unlocked!"
        $ persistent.my_baby_shot_me_achievement_trigger = True
    $ renpy.full_restart()


# If behavior drops under 20 after three months of gameplay there is a 20% chance per day that the school will burn down.
label game_over_burn:
    "On your way to Ashford, you see smoke in the vicinity of the school. You get a bit worried since some rascals at school have behaved quite badly for some time now."
    "As you get closer, you hear the sounds of fire engines and feel the distinct smell of burning wood." 
    "When you finally reach the front of Ashford..."
    scene bg game_over_burn
    "...you see everything burning."
    "After a few seconds you understand that the school is beyond saving and repair. This must truly be the end of Ashford Academy."
    info "GAME OVER."
    if persistent.new_game_plus != True:
        $ persistent.new_game_plus = True
        "New Game Plus unlocked."
    if persistent.burning_down_the_school_achievement_trigger != True:
        show ach_acquired at screen_center with easeinright
        "Burning down the school, MY school Achievement unlocked!"
        $ persistent.burning_down_the_school_achievement_trigger = True
    $ renpy.full_restart()
