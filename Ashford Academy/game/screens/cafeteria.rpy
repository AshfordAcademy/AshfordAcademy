image bg cafeteria1 = "screens/cafeteria/cafeteria1.jpg"
image bg cafeteria2-1 = "screens/cafeteria/cafeteria2-1.jpg"
image bg cafeteria2-2 = "screens/cafeteria/cafeteria2-2.jpg"
image bg cafeteria3-1 = "screens/cafeteria/cafeteria3-1.jpg"
image bg cafeteria3-2 = "screens/cafeteria/cafeteria3-2.jpg"
image bg cafeteria3-3 = "screens/cafeteria/cafeteria3-3.jpg"
image bg cafeteria3-4 = "screens/cafeteria/cafeteria3-4.jpg"
image bg cafeteria3-5 = "screens/cafeteria/cafeteria3-5.jpg"
image bg cafeteria4 = "screens/cafeteria/cafeteria4.jpg"
image bg cafeteria5-1 = "screens/cafeteria/cafeteria5-1.jpg"
image bg cafeteria5-2 = "screens/cafeteria/cafeteria5-2.jpg"
image bg cafeteria5-3 = "screens/cafeteria/cafeteria5-3.jpg"
image bg cafeteria5-4 = "screens/cafeteria/cafeteria5-4.jpg"
image bg cafeteria5-5 = "screens/cafeteria/cafeteria5-5.jpg"

init:
    if persistent.mod_disable_original_events == False:
        $ event("cafeteria1", "act == 'cafeteria'", event.choose_one('cafeteria'), priority=200)
        $ event("cafeteria2", "act == 'cafeteria'", event.choose_one('cafeteria'), priority=200)
        $ event("cafeteria3", "act == 'cafeteria'", event.choose_one('cafeteria'), priority=200)
        $ event("cafeteria4", "act == 'cafeteria'", event.choose_one('cafeteria'), priority=200)
        $ event("cafeteria5", "act == 'cafeteria'", event.choose_one('cafeteria'), priority=200)


label cafeteria1:
    
    scene bg cafeteria1 with fade
    "These girls sure enjoy our cafeteria."
    $ behavior -= 1
    return


label cafeteria2:
    
    if morale and behavior < 50:
        scene bg cafeteria2-1 with fade
        "waitress" "I'm so happy that the students seem to enjoy spending time at the cafe!"
        pov "They do get the very best service."
        scene bg cafeteria2-2
        "waitress" "What a nice thing to say!"
        pov "Keep up the good work!"
    else:
        scene bg cafeteria2-2 with fade
        "waitress" "Welcome [povTitle] [povLastName]! Coffee is on the house!"
        pov "Must be my lucky day."
    $ morale += 1
    return


label cafeteria3:
    scene bg cafeteria3-1 with fade
    girl "Oh, I was just about to eat my dessert!"
    pov "Don't mind me, just enjoy your sweets."
    scene bg cafeteria3-2
    girl "Yum yum!"
    pov "That's right, you go girl!"
    scene bg cafeteria3-3
    girl "There's so much of it!"
    pov "You can do it!"
    scene bg cafeteria3-4
    girl "Schluuuuuurp!"
    pov "That's it!"
    scene bg cafeteria3-5
    girl "Oooh, brain freeze..."
    pov "But you did good!"
    scene bg cafeteria3-4
    girl "Mmm, and it was so yummy too!"
    return

    #scene bg cafeteria3-2
    #pov "Looks like she's having another go at it."
    #scene bg cafeteria3-3
    #girl "Oh, it's such a guilty pleasure!"


label cafeteria4:
    scene bg cafeteria4 with fade
    "Feeling a little down? Nothing lifts the spirit like coffee!"
    return


label cafeteria5:

    $ rendEvent = renpy.random.choice(["1", '2', '3'])
    
    if rendEvent == "1":
        scene bg cafeteria5-1 with fade
        waitress "Welcome [povTitle] [povName]! A cup of coffee?"
        pov "You know me too well!"
    
    elif rendEvent == "2":
        scene bg cafeteria5-1 with fade
        waitress "Ah, mr [povName]!"
        pov "Hello, how's business?"
        scene bg cafeteria5-2
        waitress "It's busy busy!"
        pov "Sure looks that way."
    
    elif rendEvent == "3":
        if new_game_plus == True:
            scene bg cafeteria5-3 with fade
            "Is something wrong?"
            waitress "Well... It seems someone didn't pay for their coffee and pie."
            pov "Shine up, I'm sure their thoughts were elsewhere. They'll come back and pay the bill once they've settled down a bit."
            scene bg cafeteria5-2
            waitress "People are honest, I'm sure they will be back!"
            pov "That's the spirit."
            scene bg cafeteria5-5
            waitress "Have you heard the good news?!"
            menu:
                "Yes!":
                    waitress "Isn't it just wonderful?"
                    pov "I guess so!"
                    waitress "It makes the day so shiny and bright!"
                    pov "Covered in rainbows!"
                    waitress "What?"
                    pov "And unicorn pancakes!"
                    waitress "Oh! Unicorns!"
                    $ morale += 1

                "No!":
                    waitress "Two buns at the price of one!"
                    pov "You're pulling my leg!"
                    waitress "Am not!"
                    pov"Are too!"
                    waitress "Bun-Bonanza!"
                    pov "I love this school!"
                    $ morale += 1

                "Cowabunga!":
                    pov "You mean about the café going out of business?"
                    scene bg cafeteria5-3
                    waitress "W-whaat?"
                    pov "That's right, you're fired!"
                    waitress "But my sister's sick and my mother can't afford the medi..."
                    pov "I'm sure you'll grow with this experience."
                    waitress "But..."
                    pov "What-what?"
                    waitress "*sob*"
                    $ morale -= 1
        else:
            scene bg cafeteria5-4 with fade
            "The cafeteria is a warm and cozy place!"
    return


