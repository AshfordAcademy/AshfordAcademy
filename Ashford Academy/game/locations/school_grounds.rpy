image bg school_grounds1_1 = "locations/school_grounds/school_grounds1-1.jpg"
image bg school_grounds1_2 = "locations/school_grounds/school_grounds1-2.jpg"
image bg school_grounds2_1 = "locations/school_grounds/school_grounds2-1.jpg"
image bg school_grounds2_2 = "locations/school_grounds/school_grounds2-2.jpg"
image bg school_grounds3 = "locations/school_grounds/school_grounds3.jpg"
image bg school_grounds4 = "locations/school_grounds/school_grounds4.jpg"
image bg school_grounds5-1 = "locations/school_grounds/school_grounds5-1.jpg"
image bg school_grounds5-2 = "locations/school_grounds/school_grounds5-2.jpg"
image bg school_grounds6 = "locations/school_grounds/school_grounds6.jpg"
image bg school_grounds7 = "locations/school_grounds/school_grounds7.jpg"
image bg school_grounds8 = "locations/school_grounds/school_grounds8.jpg"
image bg school_grounds9 = "locations/school_grounds/school_grounds9.jpg"
image bg school_grounds10 = "locations/school_grounds/school_grounds10.jpg"
image bg school_grounds11 = "locations/school_grounds/school_grounds11.jpg"
image bg school_grounds12-1 = "locations/school_grounds/school_grounds12-1.jpg"
image bg school_grounds12-2 = "locations/school_grounds/school_grounds12-2.jpg"
image bg school_grounds12-3 = "locations/school_grounds/school_grounds12-3.jpg"
image bg school_grounds13 = "locations/school_grounds/school_grounds13.jpg"
image bg school_grounds14 = "locations/school_grounds/school_grounds14.jpg"
image bg school_grounds15 = "locations/school_grounds/school_grounds15.jpg"
image bg school_grounds16 = "locations/school_grounds/school_grounds16.jpg"
image bg school_grounds17 = "locations/school_grounds/school_grounds17.jpg"
image bg school_grounds18 = "locations/school_grounds/school_grounds18.jpg"
image bg school_grounds19 = "locations/school_grounds/school_grounds19.jpg"
image bg school_grounds20 = "locations/school_grounds/school_grounds20.jpg"
image bg school_grounds21 = "locations/school_grounds/school_grounds21.jpg"
image bg school_grounds22-1 = "locations/school_grounds/school_grounds22-1.jpg"
image bg school_grounds22-2 = "locations/school_grounds/school_grounds22-2.jpg"
image bg school_grounds23-1 = "locations/school_grounds/school_grounds23-1.jpg"
image bg school_grounds23-2 = "locations/school_grounds/school_grounds23-2.jpg"
image bg school_grounds23-3 = "locations/school_grounds/school_grounds23-3.jpg"
image bg school_grounds24 = "locations/school_grounds/school_grounds24.jpg"
image bg school_grounds25_1 = "locations/school_grounds/school_grounds25-1.jpg"
image bg school_grounds25_2 = "locations/school_grounds/school_grounds25-2.jpg"
image bg school_grounds26-1 = "locations/school_grounds/school_grounds26-1.jpg"
image bg school_grounds26-2 = "locations/school_grounds/school_grounds26-2.jpg"
image bg school_grounds27-1 = "locations/school_grounds/school_grounds27-1.jpg"
image bg school_grounds27-2a = "locations/school_grounds/school_grounds27-2a.jpg"
image bg school_grounds27-2b = "locations/school_grounds/school_grounds27-2b.jpg"
image bg school_grounds27-3 = "locations/school_grounds/school_grounds27-3.jpg"
image bg school_grounds27-4 = "locations/school_grounds/school_grounds27-4.jpg"
image bg school_grounds28-1 = "locations/school_grounds/school_grounds28-1.jpg"
image bg school_grounds28-2 = "locations/school_grounds/school_grounds28-2.jpg"
image bg school_grounds29_1 = "locations/school_grounds/school_grounds29-1.jpg"
image bg school_grounds29_2 = "locations/school_grounds/school_grounds29-2.jpg"
image bg school_grounds30 = "locations/school_grounds/school_grounds30.jpg"
image bg school_grounds31 = "locations/school_grounds/school_grounds31.jpg"
image bg school_grounds32 = "locations/school_grounds/school_grounds32.jpg"
image bg school_grounds33 = "locations/school_grounds/school_grounds33.jpg"
image bg school_grounds34 = "locations/school_grounds/school_grounds34.jpg"
image bg school_grounds35 = "locations/school_grounds/school_grounds35.jpg"
image bg school_grounds36 = "locations/school_grounds/school_grounds36.jpg"
image bg school_grounds37 = "locations/school_grounds/school_grounds37.jpg"
image bg school_grounds38-1 = "locations/school_grounds/school_grounds38-1.jpg"
image bg school_grounds38-2 = "locations/school_grounds/school_grounds38-2.jpg"
image bg school_grounds38-3 = "locations/school_grounds/school_grounds38-3.jpg"
image bg school_grounds39 = "locations/school_grounds/school_grounds39.jpg"
image bg school_grounds40_1 = "locations/school_grounds/school_grounds40-1.jpg"
image bg school_grounds40_2 = "locations/school_grounds/school_grounds40-2.jpg"
image bg school_grounds41-1 = "locations/school_grounds/school_grounds41-1.jpg"
image bg school_grounds41-2 = "locations/school_grounds/school_grounds41-2.jpg"
image bg school_grounds42 = "locations/school_grounds/school_grounds42.jpg"

image bg school_grounds43 = "locations/school_grounds/school_grounds43.jpg"
image bg school_grounds44 = "locations/school_grounds/school_grounds44.jpg"
image bg school_grounds45_1 = "locations/school_grounds/school_grounds45-1.jpg"
image bg school_grounds45_2 = "locations/school_grounds/school_grounds45-2.jpg"
image bg school_grounds46 = "locations/school_grounds/school_grounds46.jpg"
image bg school_grounds47 = "locations/school_grounds/school_grounds47.jpg"
image bg school_grounds48-1 = "locations/school_grounds/school_grounds48-1.jpg"
image bg school_grounds48-2 = "locations/school_grounds/school_grounds48-2.jpg"
image bg school_grounds49_1 = "locations/school_grounds/school_grounds49-1.jpg"
image bg school_grounds49_2 = "locations/school_grounds/school_grounds49-2.jpg"

init:
    if persistent.mod_disable_original_events == False:
        $ event("school_grounds1", "act == 'school_grounds' and morale > 25", event.choose_one('school_grounds'), priority=200)
        $ event("school_grounds2", "act == 'school_grounds'", event.choose_one('school_grounds'), priority=200)
        $ event("school_grounds3", "act == 'school_grounds' and deviance > 10", event.choose_one('school_grounds'), priority=190)
        $ event("school_grounds4", "act == 'school_grounds'", event.choose_one('school_grounds'), priority=200)
        $ event("school_grounds5", "act == 'school_grounds' and morale <= 5", event.choose_one('school_grounds'), priority=190)
        $ event("school_grounds6", "act == 'school_grounds' and morale > 25", event.choose_one('school_grounds'), priority=190)
        $ event("school_grounds7", "act == 'school_grounds'", event.choose_one('school_grounds'), priority=200)
        $ event("school_grounds8", "act == 'school_grounds' and inhibition < 90", event.choose_one('school_grounds'), priority=190)
        $ event("school_grounds9", "act == 'school_grounds' and morale > 15", event.choose_one('school_grounds'), priority=190)
        $ event("school_grounds10", "act == 'school_grounds' and inhibition < 85 and deviance > 10", event.choose_one('school_grounds'), priority=190)
        $ event("school_grounds11", "act == 'school_grounds' and morale > 25 and behavior > 25",  event.once(), event.choose_one('school_grounds'), priority=180)
        $ event("school_grounds12", "act == 'school_grounds' and inhibition < 90", event.choose_one('school_grounds'), priority=180)
        $ event("school_grounds13", "act == 'school_grounds' and inhibition < 90", event.choose_one('school_grounds'), priority=180)
        $ event("school_grounds14", "act == 'school_grounds' and behavior < 25 and deviance > 0", event.choose_one('school_grounds'), priority=180)
        $ event("school_grounds15", "act == 'school_grounds' and morale > 25", event.choose_one('school_grounds'), priority=190)
        $ event("school_grounds16", "act == 'school_grounds' and behavior < 15", event.choose_one('school_grounds'), priority=180)
        $ event("school_grounds17", "act == 'school_grounds' and inhibition > 85", event.choose_one('school_grounds'), priority=180)
        $ event("school_grounds18", "act == 'school_grounds' and day > 15", event.choose_one('school_grounds'), priority=190)
        $ event("school_grounds19", "act == 'school_grounds' and inhibition < 100", event.choose_one('school_grounds'), priority=190)
        $ event("school_grounds20", "act == 'school_grounds' and academics < 40", event.choose_one('school_grounds'), priority=200)
        $ event("school_grounds21", "act == 'school_grounds' and morale < 45 and behavior > 22", event.choose_one('school_grounds'), priority=190)
        $ event("school_grounds22", "act == 'school_grounds' and morale < 35", event.choose_one('school_grounds'), priority=190)
        $ event("school_grounds23", "act == 'school_grounds' and deviance > 15 and inhibition > 10", event.choose_one('school_grounds'), priority=170)
        $ event("school_grounds24", "act == 'school_grounds' and morale > 35", event.choose_one('school_grounds'), priority=190)
        $ event("school_grounds25", "act == 'school_grounds' and morale > 40 and inhibition < 95", event.choose_one('school_grounds'), priority=180)
        $ event("school_grounds26", "act == 'school_grounds' and deviance > 25 and inhibition < 75 and new_game_plus == True", event.once(), priority=150)
        $ event("school_grounds27", "act == 'school_grounds' and deviance > 15 and inhibition < 75", event.choose_one('school_grounds'), priority=170)
        $ event("school_grounds28", "act == 'school_grounds' and deviance > 35 and inhibition < 60", event.choose_one('school_grounds'), priority=170)
        $ event("school_grounds29", "act == 'school_grounds' and inhibition > 80", event.choose_one('school_grounds'), priority=70)
        $ event("school_grounds30", "act == 'school_grounds' and deviance > 50 and inhibition < 30", event.choose_one('school_grounds'), priority=170)
        $ event("school_grounds31", "act == 'school_grounds' and inhibition > 85", event.choose_one('school_grounds'), priority=170)
        $ event("school_grounds32", "act == 'school_grounds' and day < 15", event.choose_one('school_grounds'), priority=170)
        $ event("school_grounds33", "act == 'school_grounds' and morale  < 45", event.choose_one('school_grounds'), priority=170)
        $ event("school_grounds34", "act == 'school_grounds' and behavior < 75", event.choose_one('school_grounds'), priority=170)
        $ event("school_grounds35", "act == 'school_grounds' and inhibition < 75", event.choose_one('school_grounds'), priority=170)
        $ event("school_grounds36", "act == 'school_grounds' and morale > 60", event.choose_one('school_grounds'), priority=170)
        $ event("school_grounds37", "act == 'school_grounds' and inhibition > 75 and morale > 40", event.choose_one('school_grounds'), priority=170)
        $ event("school_grounds38", "act == 'school_grounds' and morale > 30", event.choose_one('school_grounds'), priority=180)
        $ event("school_grounds39", "act == 'school_grounds' and pda_rule_level < 3 and inhibition < 100", event.choose_one('school_grounds'), priority=170)
        $ event("school_grounds40", "act == 'school_grounds' and morale > 50", event.choose_one('school_grounds'), priority=160)
        $ event("school_grounds41", "act == 'school_grounds' and behavior > 50", event.choose_one('school_grounds'), priority=170)
        $ event("school_grounds42", "act == 'school_grounds' and morale < 50", event.choose_one('school_grounds'), priority=160)
        $ event("school_grounds43", "act == 'school_grounds' and reputation > 90", event.choose_one('school_grounds'), priority=100)
        $ event("school_grounds44", "act == 'school_grounds' and reputation > 25 and morale > 30", event.choose_one('school_grounds'), priority=100)
        $ event("school_grounds45", "act == 'school_grounds' and morale > 40 and behavior > 40", event.choose_one('school_grounds'), priority=150)
        $ event("school_grounds46", "act == 'school_grounds' and morale > 40", event.choose_one('school_grounds'), priority=160)
        $ event("school_grounds47", "act == 'school_grounds' and inhibition > 75 and inhibition < 95", event.choose_one('school_grounds'), priority=170)
        $ event("school_grounds48", "act == 'school_grounds' and inhibition < 85 and uniform == ('sexy_uniform' or 'nude_uniform')", event.choose_one('school_grounds'), priority=160)
        $ event("school_grounds49", "act == 'school_grounds' and inhibition > 70 and inhibition < 95", event.choose_one('school_grounds'), priority=170)

label school_grounds1:
    $ randImg = renpy.random.choice(["1", '2'])
    $ renpy.show("bg school_grounds1_"+randImg)
    with fade
    "She looks really happy. This school sure is the right place for her."
    $ morale += 1
    return


label school_grounds2:
    $ randImg = renpy.random.choice(["1", '2'])
    $ renpy.show("bg school_grounds2_"+randImg)
    with fade
    "Some girls are having a break after class."
    $ behavior += 1
    return


label school_grounds3:
    
    scene bg school_grounds3 with fade
    "You see two girls kissing. Looks like they didn't expect to be seen by anyone."
    $ deviance += 1
    return


label school_grounds4:
    
    scene bg school_grounds4 with fade
    "You meet some girls talking and giggling about boys and dates."
    $ inhibition -= 1
    return


label school_grounds5:
    
    scene bg school_grounds5-1 with fade
    "You see a sad looking girl sitting against the wall."
    
    menu:
        "Talk to her":
            scene bg school_grounds5-2 with fade
            "You tried to cheer her up, but in the end she just wanted to be alone."
            $ morale += 1
            return
            
        "Ignore her." if evil_points > 0:
            $ morale -= 1
            return


label school_grounds6:
    
    scene bg school_grounds6 with fade
    "Even the best of friends can be caught in the drama of relationships ending. Ah well, that's just life."
    $ behavior += 1
    return


label school_grounds7:
    
    scene bg school_grounds7 with fade
    "One of the girls sure got herself wet!"
    return


label school_grounds8:
    
    scene bg school_grounds8 with fade
    "A girl bent over to adjust her school uniform. A clean-cut and a sharp mind is definitely one way to succeed, 'though there are others."
    $ deviance += 1
    return


label school_grounds9:
    
    scene bg school_grounds9 with fade
    "What in life is greater than having a best friend?"
    $ morale += 1
    return
    

label school_grounds10:
    
    scene bg school_grounds10 with fade
    "As you stroll over the school grounds, you suddenly see a couple of girls just outside the Ashford territory. They take a quick look around and then engage in a sweet kiss."
    menu:
        "Disgusting!":
            "What if someone sees them?"
            $ deviance -= 1
            $ inhibition += 1

        "Aw, that's a nice scene.":
            "Their hearts must beat real hard right now."
            $ inhibition -= 1

        "Just look away.":
            "I'll pretend I didn't see that."

        "Oh la la!" if new_game_plus == True:
            "Two eyes on the girls and one hand in the pants!"
            $ deviance += 1
    return


label school_grounds11:

    scene bg school_grounds11 with fade
    "Taking your pets to school is really a last resort. Most teachers won't allow them in class so students better find someone who can help them watch their animals."
    menu:
        "All pets should be banned, they generate more trouble than good." if new_game_plus != True:
            info "Some students might be upset about this, but rules are rules."
            $ morale -= 3
            return
        
        "All pets should be banned, they generate more trouble than good." if new_game_plus == True:
            "This might be a terrible idea, considering how cute cats are. Maybe I did in some way or another misunderstood the question and made a rash decision."
            "Let's reconsider this."
            menu:
                "Ban all animals":
                    "Could this really be right, considering how much everyone loves cats I would presume there would be an outrage if I did actually ban cats."
                    menu:
                        "Ban all animals including cats":
                            'You can hear the sound of every student crying "OH, GOD WHY!?" while you wonder, did I really choose right...'
                            $ evil_points += 1
                            $ behavior -= 5
                            $ morale -= 5
                            
                        "Ban all animals excluding cats":
                            "Yes, cats are allowed. They have a important function in today's society."
                            $ morale += 1
                            $ artistery += 1
                            
                "Let all animals run wild":
                    "Well... Ashford Zoo here we go."
                    $ behavior -= 5
                    
                "Ban everything except cats":
                    "Ah, I did make a mistake. How could anyone ban cats, only a terrible person would do that. I'm so happy I'm not one of those."
                    $ morale += 1
                    $ artistery += 1
        
        "Taking your pet to school now and then might boost creativity and most certainly bring a smile to fellow students.":
            pov "I love animals, maybe we should invest in a private zoo..?"
            girl "Umm... okay..."
            $ behavior -= 3
            $ morale += 1
            $ artistery += 2
        
        "Perhaps it's for the best that they keep their pets at home. Except for cats!":
            pov "Well, cats are adorable creatures. Make sure you take good care of yours miss!"
            girl "Yes [povTitle] [povLastName]! I promise to take really good care of my cute kitty!"
            $ morale += 1
            $ artistery += 1
    return


label school_grounds12:
    
    scene bg school_grounds12-1 with fade
    "A girl hurt her leg during athletics class and you can see how she's trying real hard not to limp."
    menu:
        "I hope you get better soon.":
            scene bg school_grounds12-2
            girl "Thanks, I hope so too!"
            $ morale += 1
        
        "You're showing your panties.":
            scene bg school_grounds12-3
            girl "Ah! Sorry, sorry [povTitle] [povLastName]!"
            pov "Don't worry about it, I just wanted you to know."
            girl "Oh, thank you! I'll make sure not to flash it around like that!"
            $ inhibition += 1
        
        "Nice panties." if new_game_plus == True:
            scene bg school_grounds12-3
            if (inhibition - deviance ) > 90:
                girl "Ah!"
                "She quickly tries to cover herself and almost falls over due to it."
                girl "Aww..."
                $ inhibition += 1
            else:
                girl "*giggle* You're such a pervert!"
                pov "Someone needs to be one!"
                "She smiles and limps away."
    $ athletics -= 1
    return
    

label school_grounds13:
    
    scene bg school_grounds13 with fade
    "It's good that there are several drinking fountains around the school, many students tend to get hot during the day."
    $ inhibition -= 1
    return
    
    
label school_grounds14:
    
    scene bg school_grounds14 with fade
    "While walking around the school grounds you meet a young happy lady. Something seems off so you decide to chat with her."
    pov "Hey there!"
    girl "Oh, hello there [povTitle] [povLastName]."
    pov "Is everything alright?"
    girl "Yeah..."
    "You can now clearly see that she's drinking beer."
    menu:
        "Confiscate the beer":
            pov "I'm sorry miss, but you know you're not allowed to drink in school."
            girl "Oh yeah... I'm sorry, it won't happen again."
            $ morale -= 1
            $ behavior += 1

        "Let her be":
            pov "You know you're not supposed to drink while in school."
            girl "Oh yeah? Sorry about that..."
            pov "Don't worry about it, but don't do it again!"
            girl "Yes [povTitle] [povLastName]!"
            $ morale +=1

            
        "Ask for a sip" if start_day_with_gin == True:
            pov "So what are you drinking?"
            girl "Oh!"
            pov "Don't you worry about it, I would just like a sip."
            girl "Really? This is just some simple beer, but we can share if you like."
            pov "Thanks girl! I really like you."
            scene black with fade
            "You share the beer and spend a good time with the girl."
            $ morale +=2
            $ behavior -= 2
    return


label school_grounds15:

    scene bg school_grounds15 with fade
    "A smiling girl is humming a tune on her way home from school."
    $ morale +=1
    return
    
    
label school_grounds16:

    scene bg school_grounds16 with fade
    "Some students get so harassed, they don't even want to go inside."
    $ morale -= 1
    return
    
    
label school_grounds17:

    scene bg school_grounds17 with fade
    "Just when you walk out of school you see a girl while a wind gust blows up her skirt."
    menu:
        "Look!" if deviance < 20:
            "You see a hint of white panties while the girl pushes down her skirt and screams pervert at you."
            python:
                if renpy.random.randint(1,3) == 1:
                    reputation -= 1
                    red_orb += 1
                morale -= 1
                deviance += 1
                
        "Look!" if deviance >= 20:
            "You see a hint of white panties while the girl smile and ask if you like what you see."
            if renpy.random.randint(1,3) == 1:
                $ red_orb += 1
            else:
                $ deviance += 1
            
        "Look away":
            "You quickly look away."
    return
            

label school_grounds18:

    scene bg school_grounds18 with fade
    "Whoopsie daisy! She fell in the pond."
    menu:
        "Give her a hand":
            pov "Here, let me help you."
            "She mumbles a thank you and leaves in embarrassment."
            $ morale += 1
            
        "Shake your head":
            "When she sees you, her eyes widen and you can tell she feels stupid."
            $ morale -= 1
            
        "Unzip your pants" if evil_points > 0 and deviance < 15:
            "You give her a wolf grin."
            pov "You must be the wettest girl I've seen so far."
            girl "Heh!"
            "She seems to find your remark amusing."
            $ morale += 1
        
        "Unzip your pants" if evil_points > 0 and deviance > 15 and deviance < 50:
            "You lick your lips."
            "Hey! You perverted old fart!"
            "Damn it! Didn't work this time either..."
            $ morale -= 1
        
        "Unzip your pants" if evil_points > 0 and deviance > 50:
            "You pull it out and decide to take a piss in the pond."
            girl "..."
            pov "When you gotta go, you gotta go. * giggle *"
            $ reputation -= 1
            $ morale -= 3
    return


label school_grounds19:

    scene bg school_grounds19 with fade
    'Some boys are more popular than others, and bring more attention to the girl fortunate enough to be the "flavour of the month".'
    $ inhibition -= 1
    return
    
    
label school_grounds20:

    scene bg school_grounds20 with fade
    girl "Whoa!"
    pov "What is it?"
    girl "Can you see the little froggy?"
    menu:
        "I can see the froggy alright.":
            girl "* giggle *"
            $ morale += 1
        
        "Uhm, I'm not sure, is it... green?":
            girl "It is!"
            pov "Yay..."
            
        "I don't like animals.":
            girl "To bad for you! I'll keep the froggy to myself then!"
            pov "Why would anybody... nevermind."
            $ morale -= 1
    return


label school_grounds21:

    scene bg school_grounds21 with fade
    'Some just want to be left alone, I guess.'
    $ morale -= 1
    return
    
    
label school_grounds22:
    if renpy.random.randint(1,1) == 1: 
        scene bg school_grounds22-1 with fade
    else:
        scene bg school_grounds22-2 with fade
    'Having your lunch outside in the sun surely is great!'
    $ morale += 1
    return


label school_grounds23:

    scene bg school_grounds23-1 with fade
    'In the outskirts of the school grounds, you see two girls standing real close.'
    scene bg school_grounds23-2
    "Suddenly, one leans forward and gives the other a passionate kiss."
    scene bg school_grounds23-3
    "After a short struggle, the other one gives in and lets her tongue answer the invitation."
    python:
        if renpy.random.randint(1,4) == 1:
            red_orb += 1
            inhibition -= 1
        else:
            deviance += 1
    return


label school_grounds24:

    scene bg school_grounds24 with fade
    "A young student shares her lunch break with a beastly cute cat."
    if new_game_plus == True:
        "Maybe you should warn the girl or help the cat..."
        menu:
            "Help the cat!":
                pov "Hey there young lady!"
                girl "Oh, hello [povTitle] [povLastName]!"
                pov "Watch out! The flying elephant is coming for you!!!"
                if renpy.random.randint(1,2) == 1:
                    girl "AHHHH!!!"
                    "She obviously ran for her life giving the cat a full meal."
                    cat "Nyaa~!"
                    pov "No worries, you take care now!"
                    cat "Nyaa~ nyaa~!"
                else:
                    girl "Umm, are you like a crazy person?"
                    if new_game_plus == True:
                        pov "How did you know?! Did the voices tell you that?"
                        girl "Eh, I g-got to go... bye..."
                        pov "Hehehe... Yes... Voices..."
                    else:
                        pov "No no little girl, I just tried to pull your leg."
                        girl "Oh... You better work on your jokes then..."
                        
            "Warn the girl!":
                pov "Careful girl your little friend wants a taste of that!"
                girl "*giggle* I know, isn't he cute? I come here almost everyday just to pet him and give him something to eat."
                "Such a sweet girl."
            "Leave them alone.":
                pass
    $ morale += 1
    return


label school_grounds25:
    $ randImg = renpy.random.choice(["1", '2'])
    $ renpy.show("bg school_grounds25_"+randImg)
    with fade
    "Ah, the young at heart. Not a sorrow in sight!"
    $ behavior -= 1
    $ morale += 1
    return


label school_grounds26:

    scene bg school_grounds26-1 with fade
    "On your walk round the school grounds, you bump into the President of the Students Council. Ever since your first meeting, you've suspected that she has some kind of interest in you."
    girl "Good day Principal [povLastName], how are you sir?"
    pov "Fine, just fine thanks for asking."
    "Her innocence combined with those perky breasts makes for a helluva blood rush to the old ding ding dong."
    pov "Say, that's a nice set of... flowers you got there."
    girl "Oh, thank's for noticing! I don't know who they're from though, they were waiting for me by my locker this morning."
    menu:
        "Seems you've got yourself a secret admirer.":
            girl "*giggles* I guess that comes with being the President."
            pov "Guess it does."
            "You say goodbye and walk away in different directions."

        "Just be careful, you never know who it might be from.":
            girl "Why Principal [povLastName], do i detect a certain jealousy?"
            "That snouty little bitch, who the hell does she think she is?"
            pov "I'm sorry, but I have an important meeting to attend. It's about a recent series of events where several young students have been courted with flowers, and then brutally murdered."
            girl "???"
            pov "Have a good day now."
            "You look suspiciously at her flowers as you strut away."
        
        "I sent you those flowers.":
            pov "I must confess, It was I who bought you the flowers."
            girl "[povTitle] [povLastName]! How romantic!"
            pov "Yup, I'm a regular romance-o-holic."
            girl "Nobody has ever done something like this for me!"
            "Now is your chance of getting a piece of the Presidents perky ones."
            pov "Say, get over here for a second, will you?"
            girl "U- huh?"
            scene bg school_grounds26-2
            "Standing on her lovely bouquet, you pump her ass while twisting her arm so she's forced to bend over against the fence."
            girl "Aiiiih!"
            pov "Happy birthday to you, happy birthday to you, happy birthday Miss. President, happy birthday to youuuuuuaaaaaaaaah!!"
            $ deviance += 1
    return


label school_grounds27:

    scene bg school_grounds27-1 with fade
    "Not all encounters are of the expected kind but this is the kind that are easily enjoyed."
    if deviance > 20 and povGender == 'male':
        menu:
            "Leave her alone.":
                pass
            
            "Spend some time with her.":
                pov "Hey there, nice panties you have there."
                girl "Umm, thanks [povLastName]..."
                if evil_points > 0:
                    scene bg school_grounds27-2b
                    "You walk towards her and and in a swift but forceful motion you pull down her panties."
                    girl "Ah!"
                    pov "Nice pussy too. Now I need you to turn around."
                    "She looks at you nodding slowly."
                else:
                    pov "Do you mind if I take a closer look?"
                    girl "... No... P-please do..."
                    scene bg school_grounds27-2a
                    "With a relaxed motion you slowly pull down her panties as you feel the fresh scent of her young honey pot."
                    pov "I would like to have a taste of that, would you mind?"
                    girl "I... Would like that..."
                    pov "Then just turn around and I'll give you what you want."
                scene bg school_grounds27-3
                "While she slowly turns around you unzip your pants and slowly enter her sweet and tight pussy."
                girl "Mhmm..."
                "You make sure to give her some good treatment playing with her body while you thrust into her."
                girl "Ah! Ahh..."
                scene bg school_grounds27-4
                "As you cum into her soft insides it spills out making a mess."
                girl "Mhmm... T-thank you [povTitle] [povFirstName]..."
                pov "My pleasure."
                
    $ deviance += 1
    $ morale -= 1
    return


label school_grounds28:

    scene bg school_grounds28-1 with fade
    "You see a couple, smoochin' against a rail. The girl notices your glance and decides to make a little provocative stunt. "
    scene bg school_grounds28-2
    "Her boyfriend doesn't realize that he's just a tool, but he doesn't seem like he would care anyway..."
    if renpy.random.randint(1,3) == 1: 
        "I hope not to many saw that, it could damage the school reputation."
        $ red_orb += 1
        $ reputation -= 1
    else:
        $ deviance += 1
    return


label school_grounds29:
    $ randImg = renpy.random.choice(["1", '2'])
    $ renpy.show("bg school_grounds29_"+randImg)
    with fade
    
    if renpy.random.randint(1,2) == 1:
        "School uniforms as far as the eye can see."
    else:
        "Sometimes I wonder if this is a girls only school."
    return


label school_grounds30:

    scene bg school_grounds30 with fade
    'Once a year, the nearby nursery release their patients to come and celebrate "Veterans Day" with the Ashford students. Traditions are important!'
    if renpy.random.randint(1,3) == 1: 
        "This might not be the best place to celebrate, I'm sure it could get some unwanted attention."
        $ red_orb += 1
        $ reputation -= 1
    else:
        $ deviance += 1
    return


label school_grounds31:

    scene bg school_grounds31 with fade
    "As you walk by a young, beautiful student you suddenly trip and grab her skirt to prevent you from falling. That could have been ugly!"
    $ morale -= 1
    return
    
    
label school_grounds32:

    scene bg school_grounds32 with fade
    if renpy.random.randint(1,1) == 1:
        "It's important to drink plenty of liquid during warm and dry afternoons."
    else:
        "Keep looking at me and we might get some wet t-shirt action!"
    return


label school_grounds33:

    scene bg school_grounds33 with fade
    "Enjoy your break, but be sure to go to next class in time!"
    $ behavior += 1
    return


label school_grounds34:

    scene bg school_grounds34 with fade
    "Some students skip the whole backpack thing, and instead don a more fancy case."
    return


label school_grounds35:

    scene bg school_grounds35 with fade
    "You pass right under a girl as she's getting ready to climb over the school fence. You both realize that she's not wearing any panties."
    menu:
        "Leave without a word":
            girl "..."
            
        "Give her a compliment":
            pov "Feels good with a bit of fresh air I presume?"
            girl "Umm, yeah..."
            pov "Keep being a good girl and everyone will be happy."
            girl "..."
            $ inhibition -= 1
            $ morale += 1
            
        "Give her a warning":
            girl "Sorry [povTitle] [povLastName], I promise to wear panties {i}tomorrow{/i}."
            "She leaves with a wry smile."
            $ deviance -= 1
            $ behavior -= 1
            
        "Do I smell fish?" if new_game_plus == True:
            girl "Umm..."
            pov "Do you smell that?"
            girl "..."
            pov "You should consider a shower, it really reeks!"
            girl "*sob*"
            $ morale -= 2
    return


label school_grounds36:

    scene bg school_grounds36 with fade
    "A couple of girls seem to be quite acquainted to each other."
    $ morale += 1
    return


label school_grounds37:

    scene bg school_grounds37 with fade
    if renpy.random.randint(1,2) == 1:
        "No offence, but sometimes you just want to sit by yourself."
    else:
        "Sometimes you just want to play with yourself and no other."
    $ morale += 1
    return


label school_grounds38:

    scene bg school_grounds38-1 with fade
    "A student is having her lunch break on the outskirts of the school ground."
    pov "It sure looks nice."
    girl "The grass is so soft!"
    if inhibition < 90:
        pov "I wasn't talking about the grass."
        scene bg school_grounds38-2
        girl "Oh... I..."
        pov "You make it so much prettier just by sitting here."
        girl "*giggle* You flatter me [povTitle] [povLastName]."
        pov "I speak the truth, the whole truth and nothing but the truth."
        girl "*giggle* So help you God?"
        pov "I bet your legs are as nice as your face."
        girl "B-but you can see my legs..."
        pov "Not the whole nine yards."
        girl "Hmm, I don't know..."
        menu:
            "Hey, it's ok, I'm just as content looking at your beautiful smile.":
                girl "Oh, you're so..."
                "She takes a quick look around and then pulls up her skirt."
                scene bg school_grounds38-3
                pov "A true beauty."
                girl "*sigh* You're so sweet."
                $ inhibition -= 1
                
            "Come on, what's with the hesitation?":
                girl "I-I don't think it's a good idea."
                "What a pity, but at least you made her blush."
                $ inhibition += 1
    return


label school_grounds39:

    scene bg school_grounds39 with fade
    "Now that she's got him in her clutches, she's not going to let him go. At least not for a couple of weeks."
    $ inhibition -= 1
    return


label school_grounds40:

    $ randImg = renpy.random.choice(["1", '2'])
    $ renpy.show("bg school_grounds40_"+randImg)
    with fade
    "It's always nice to hang out with your friends."
    $ morale += 1
    return


label school_grounds41:

    scene bg school_grounds41-1 with fade
    "You walk in on a three part lunch meeting."
    girl "Hello [povTitle] [povLastName], would you care to join us?"
    pov "Perhaps another time girls, but thanks for asking."
    scene bg school_grounds41-2
    girl "Such a gentleman!"
    $ behavior += 1
    return


label school_grounds42:

    scene bg school_grounds42 with fade
    "The company of good comrades is worth it's weight in gold."
    $ morale += 1
    return


label school_grounds43:

    scene bg school_grounds43 with fade
    'To secure Ashfords power needs, the board decided to take part and invest in the local "green energy project" that partly provides the surrounding commercial initiatives. Wind turbines are clean, shiny and imposing. Feel that wind blowing through your hair!'
    return


label school_grounds44:

    scene bg school_grounds44 with fade
    "Looks like she got herself a ride home!"
    $ morale += 1
    return


label school_grounds45:
    $ randImg = renpy.random.choice(["1", '2'])
    $ renpy.show("bg school_grounds45_"+randImg)
    with fade
    
    if renpy.random.randint(1,2) == 1:
        "It's important to refill your energy supply."
    else:
        "A meal with good company always taste great."
    $ behavior += 1
    return


label school_grounds46:

    scene bg school_grounds46 with fade
    "Let life be simple enough, don't worry about tomorrow."
    $ morale += 1
    return


label school_grounds47:

    scene black
    "While relaxing on patch of grass you hear footsteps getting closer."
    scene bg school_grounds47:
        pos (0.0, -1.5)
        linear 10.0 pos (0.0, -0.0)
    with fade
    "The perfect angle sure made my day better. The girl looks a bit surprised though."
    $ morale -= 1
    return


label school_grounds48:
    if uniform == 'sexy_uniform':
        scene bg school_grounds48-1:
            pos (0.0, -0.0)
            linear 7.3 pos (0.0, -1.1)
            linear 0.1 pos (0.0, -1.1)
            linear 7.3 pos (0.0, -0.0)
        with fade
    elif uniform == 'nude_uniform':
        scene bg school_grounds48-2:
            pos (0.0, -0.0)
            linear 3.3 pos (0.0, -0.5)
            linear 0.1 pos (0.0, -0.5)
            linear 3.3 pos (0.0, -0.0)
        with fade
    if renpy.random.randint(1,2) == 1:
        if uniform == 'sexy_uniform':
            "While some girls disapprove of the {i}sexy uniform{/i} others don't care at all."
        elif uniform == 'nude_uniform':
            "While some girls disapprove of the {i}nude uniform{/i} others don't care at all."
        $ inhibition -= 1
    else:
        girl "Bye bye [povTitle] [povLastName]!"
        "Some students really shine like a little sun."
        $ morale += 1
    return


label school_grounds49:
    $ randImg = renpy.random.choice(["1", '2'])
    $ renpy.show("bg school_grounds49_"+randImg)
    with fade
    
    if pda_rule_level > 2:
        if renpy.random.randint(1,2) == 1:
            "Seems like love is the air."
        else:
            "Puppy love sure is sweet."
        $ morale += 1
    else:
        "You tell them to stop clinging to each other or suffer the consequences."
        $ morale -= 1
        $ inhibition -= 1 
    return

