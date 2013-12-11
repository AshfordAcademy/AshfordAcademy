image bg class1 = "locations/class/class1.jpg"
image bg class2 = "locations/class/class2.jpg"
image bg class3 = "locations/class/class3.jpg"
image bg class4 = "locations/class/class4.jpg"
image bg class5 = "locations/class/class5.jpg"
image bg class6 = "locations/class/class6.jpg"
image bg class7_1 = "locations/class/class7-1.jpg"
image bg class7_2 = "locations/class/class7-2.jpg"
image bg class7-3-1 = "locations/class/class7-3-1.jpg"
image bg class7-3-2 = "locations/class/class7-3-2.jpg"
image bg class7-3-3 = "locations/class/class7-3-3.jpg"
image bg class7-3-4 = "locations/class/class7-3-4.jpg"
image bg class7-3-5 = "locations/class/class7-3-5.jpg"
image bg class8 = "locations/class/class8.jpg"
image bg class9-1 = "locations/class/class9-1.jpg"
image bg class9-2 = "locations/class/class9-2.jpg"
image bg class9-3 = "locations/class/class9-3.jpg"
image bg class10 = "locations/class/class10.jpg"
image bg class11 = "locations/class/class11.jpg"
image bg class12 = "locations/class/class12.jpg"
image bg class13 = "locations/class/class13.jpg"
image bg class14 = "locations/class/class14.jpg"
image bg class15-1 = "locations/class/class15-1.jpg"
image bg class15-2 = "locations/class/class15-2.jpg"
image bg class15-3 = "locations/class/class15-3.jpg"
image bg class16-1 = "locations/class/class16-1.jpg"
image bg class16-2 = "locations/class/class16-2.jpg"
image bg class17 = "locations/class/class17.jpg"
image bg class18-1 = "locations/class/class18-1.jpg"
image bg class18-2 = "locations/class/class18-2.jpg"
image bg class19 = "locations/class/class19.jpg"
image bg class20 = "locations/class/class20.jpg"
image bg class21 = "locations/class/class21.jpg"
image bg class22 = "locations/class/class22.jpg"
image bg class23 = "locations/class/class23.jpg"
image bg class24 = "locations/class/class24.jpg"
image bg class25 = "locations/class/class25.jpg"
image bg class26 = "locations/class/class26.jpg"
image bg class27 = "locations/class/class27.jpg"
image bg class28 = "locations/class/class28.jpg"
image bg class29 = "locations/class/class29.jpg"
image bg class30 = "locations/class/class30.jpg"
image bg class31 = "locations/class/class31.jpg"
image bg class32 = "locations/class/class32.jpg"
image bg class33 = "locations/class/class33.jpg"
image bg class34 = "locations/class/class34.jpg"
image bg class35 = "locations/class/class35.jpg"
image bg class36-1 = "locations/class/class36-1.jpg"
image bg class36-2 = "locations/class/class36-2.jpg"
image bg class37 = "locations/class/class37.jpg"
image bg class38 = "locations/class/class38.jpg"
image bg class39 = "locations/class/class39.jpg"
image bg class40-1 = "locations/class/class40-1.jpg"
image bg class40-2 = "locations/class/class40-2.jpg"
image bg class41-1 = "locations/class/class41-1.jpg"
image bg class41-2 = "locations/class/class41-2.jpg"
image bg class41-3 = "locations/class/class41-3.jpg"
image bg class41-4 = "locations/class/class41-4.jpg"
image bg class41-5 = "locations/class/class41-5.jpg"
image bg class41-6 = "locations/class/class41-6.jpg"
image bg class42 = "locations/class/class42.jpg"
image bg class43 = "locations/class/class43.jpg"
image bg class44-1 = "locations/class/class44-1.jpg"
image bg class44-2 = "locations/class/class44-2.jpg"
image bg class44-3 = "locations/class/class44-3.jpg"
image bg class44-4 = "locations/class/class44-4.jpg"
image bg class44-5 = "locations/class/class44-5.jpg"
image bg class45 = "locations/class/class45.jpg"
image bg class46 = "locations/class/class46.jpg"
image bg class47 = "locations/class/class47.jpg"
image bg class48 = "locations/class/class48.jpg"
image bg class49 = "locations/class/class49.jpg"
image bg class50 = "locations/class/class50.jpg"
image bg class51 = "locations/class/class51.jpg"
image bg class52 = "locations/class/class52.jpg"
## image bg class99 = "locations/class/class99.jpg"

define class15_sex = False

init:
    # Intro class, needed to initiate Hina Amagi storyline
    $ event("class_introduction", "act == 'class'", event.once(), event.only())
    
    if persistent.mod_disable_original_events == False:
        $ event("class1", "act == 'class' and deviance < 20", event.choose_one('class'), priority=200)
        $ event("class2", "act == 'class' and behavior < 50", event.choose_one('class'), priority=200)
        $ event("class3", "act == 'class' and deviance <= 15", event.choose_one('class'), priority=200)
        $ event("class4", "act == 'class' and deviance >= 50 and pda_rules == 'pda_bdsm'", event.choose_one('class'), priority=160)
        $ event("class5", "act == 'class' and behavior <= 10", event.choose_one('class'), priority=190)
        $ event("class6", "act == 'class' and inhibition > 40", event.choose_one('class'), priority=200)
        $ event("class7", "act == 'class' and inhibition <= 85 and deviance >= 10", event.choose_one('class'), priority=180)
        $ event("class8", "act == 'class' and inhibition <= 70 and deviance >= 65 and behavior < 75", event.once(), event.only())
        $ event("class9", "act == 'class' and inhibition <= 95 and deviance >= 10 and inhibition > 50", event.choose_one('class'), priority=190)
        $ event("class10", "act == 'class' and inhibition < 90 and inhibition > 60", event.choose_one('class'), priority=190)
        $ event("class11", "act == 'class' and inhibition > 50 and pda_rule_level <= 2", event.choose_one('class'), priority=190)
        $ event("class12", "act == 'class' and academics > 35", event.choose_one('class'), priority=190)
        $ event("class13", "act == 'class' and inhibition <= 85 and deviance >= 10", event.choose_one('class'), priority=190)
        $ event("class14", "act == 'class' and inhibition < 65 and deviance > 50", event.choose_one('class'), priority=180)
        $ event("class15", "act == 'class' and day > 25 and deviance > 15 and inhibition > 40", event.choose_one('class'), priority=180)
        $ event("class16", "act == 'class' and inhibition <= 80 and deviance >= 15", event.choose_one('class'), priority=180)
        $ event("class17", "act == 'class' and inhibition <= 85 and morale >= 25", event.choose_one('class'), priority=190)
        $ event("class18", "act == 'class' and behavior >= 25", event.choose_one('class'), priority=190)
        $ event("class19", "act == 'class' and inhibition <= 85 and behavior <= 20", event.choose_one('class'), priority=180)
        $ event("class20", "act == 'class' and inhibition <= 85 and academics <= 40", event.choose_one('class'), priority=180)
        $ event("class21", "act == 'class' and deviance > 5 and behavior < 35", event.choose_one('class'), priority=170)
        $ event("class22", "act == 'class' and deviance > 0 and inhibition < 100", event.choose_one('class'), priority=180)
        $ event("class23", "act == 'class' and deviance > 50 and inhibition < 50", event.choose_one('class'), priority=150)
        $ event("class24", "act == 'class' and inhibition < 100 and deviance > 5", event.choose_one('class'), priority=180)
        $ event("class25", "act == 'class' and inhibition < 85 and deviance > 10", event.choose_one('class'), priority=160)
        $ event("class26", "act == 'class' and inhibition < 75 and deviance > 25 and behavior < 45", event.choose_one('class'), priority=140)
        $ event("class27", "act == 'class' and learning_materials == 0.7 and inhibition < 90 and academics > 45", event.once(), event.only())
        $ event("class28", "act == 'class' and inhibition < 90 and deviance > 10", event.choose_one('class'), priority=160)
        $ event("class29", "act == 'class' and inhibition < 85 and deviance > 10", event.choose_one('class'), priority=160)
        $ event("class30", "act == 'class' and behavior < 45 and morale < 45 and month > 1", event.once(), event.only())
        $ event("class31", "act == 'class' and morale > 50 and behavior > 35", event.choose_one('class'), priority=170)
        $ event("class32", "act == 'class' and morale > 50 and behavior > 35", event.choose_one('class'), priority=160)
        $ event("class33", "act == 'class' and inhibition < 85 and deviance > 10", event.choose_one('class'), priority=170)
        $ event("class34", "act == 'class' and inhibition < 75 and deviance > 20 and pda_rules == 'pda_bdsm'", event.choose_one('class'), priority=150)
        
        ## Here be Class35
        
        $ event("class36", "act == 'class' and inhibition < 75 and deviance > 20 and good_points > 1 and povGender == 'male'", event.once(), event.only())
        $ event("class37", "act == 'class' and inhibition < 85 and deviance > 10 and tentacles > 0", event.choose_one('class'), priority=80)
        $ event("class38", "act == 'class' and inhibition < 80 and deviance > 5", event.choose_one('class'), priority=80)
        $ event("class39", "act == 'class' and inhibition < 60 and deviance > 25 and povGender == 'male'", event.choose_one('class'), priority=80)
        $ event("class40", "act == 'class' and inhibition < 90 and deviance > 10", event.once(), event.only())
        $ event("class41", "act == 'class' and inhibition < 90 and deviance > 10", event.once(), event.depends("class40"), event.only())
        $ event("class42", "act == 'class' and deviance <= 15 and morale >= 25", event.choose_one('class'), priority=190)
        $ event("class43", "act == 'class' and deviance <= 40 and inhibition < 95", event.choose_one('class'), priority=180)
        $ event("class44", "act == 'class' and academics > 35", event.choose_one('class'), priority=180)
        $ event("class45", "act == 'class' and academics < 50", event.choose_one('class'), priority=200)
        $ event("class46", "act == 'class' and morale > 35 and academics > 35", event.choose_one('class'), priority=180)
        $ event("class47", "act == 'class' and morale > 40 and reputation < 15", event.choose_one('class'), priority=180)
        $ event("class48", "act == 'class' and morale > 35 and academics > 35", event.choose_one('class'), priority=180)
        $ event("class49", "act == 'class' and inhibition > 75", event.choose_one('class'), priority=180)
        $ event("class50", "act == 'class' and reputation > 15", event.choose_one('class'), priority=180)
        $ event("class51", "act == 'class' and inhibition < 85", event.choose_one('class'), priority=160)
        $ event("class52", "act == 'class' and building_cafeteria > 0", event.choose_one('class'), priority=160)
        
        #$ event("class99", "act == 'class' and inhibition < 70 and deviance > 25 and good_points > 0", event.once(), priority=50)
        
label class_introduction:
    
    scene bg classroom with fade
    "You enter the classroom and Susan swiftly switches from lecturing to introducing you."

    show teacher_susan normal at center
    teacher_susan "Listen up class!"
    teacher_susan "This is [povTitle] [povLastName], our new principal. Would you like to introduce yourself?"
    menu:
        "Make a serious introduction.":
            pov "Hello students, as Susan told you, my name is [povTitle] [povLastName]. I will make sure that our school reaches new heights and that we all work towards this goal."
            teacher_susan "Thank you [povTitle] [povLastName], do we have any questions?"
            teacher_susan "..."
            teacher_susan "No questions? Well then, thank you for joining us today principal."
            "As you leave the room you hear students mumbling about you. Mostly that you seem strict."
            $ behavior += 3
            
        "Make a relaxed introduction.":
            pov "Hello class, my name is [povFirstName] [povLastName]!"
            "Class: Hello principal [povLastName]!"
            pov "I'm happy to meet you all and to work here at Ashford Academy. I will do my best for both students and teachers alike. If you have any problems, don't hesitate to talk to me."
            teacher_susan "Thank you [povTitle] [povLastName], do we have any questions?"
            teacher_susan "Yes, Hina, please introduce yourself to [povTitle] [povLastName] and state your question."
            show teacher_susan normal at left with move
            show hina_amagi normal at center
            hina_amagi "Hello principal, my name is Hina Amagi, it's nice to meet you."
            hina_amagi "I wonder, do you know if there are any plans on building a new pool?"
            menu:
                "Yes, as a matter of fact it's one of my first priorities to build a new pool.":
                    show hina_amagi happy at center
                    hina_amagi "That's wonderful news! We will be able to train and compete again!"
                    hide hina_amagi
                    show teacher_susan normal at center with move
                    teacher_susan "Any other questions for [povTitle] [povLastName]?"
                    teacher_susan "..."
                    teacher_susan "No questions? Well then, thank you for joining us today principal."
                    pov "My pleasure."
                    "As you leave the room you hear students talking about you and the new pool. They seem to think that you're a really nice guy."
                    $ hina_amagi_points += 2
                    $ morale += 2
            
                "I can't answer that right now.":
                    pov "I will look it up and hopefully be able to tell you next time we meet."
                    show hina_amagi normal
                    hina_amagi "I understand [povTitle] [povLastName]..."
                    hide hina_amagi
                    show teacher_susan normal at center with move
                    teacher_susan "Any other questions for [povTitle] [povLastName]?"
                    teacher_susan "..."
                    teacher_susan "No more questions? Well then, thank you for joining us today principal."
                    pov "My pleasure."
                    "As you leave the room you hear students talking about you. They seem to think that you're a nice guy."
                    $ hina_amagi_points += 1
                    $ morale += 1
                
                "Not at the moment, sorry.":
                    show hina_amagi sad
                    hina_amagi "But... Why?"
                    pov "Well, right now we have more pressing matters that needs to be taken care of."
                    hina_amagi "Ok..."
                    hide hina_amagi
                    show teacher_susan normal at center with move
                    teacher_susan "Well, please take your seat Amagi. Thank you for joining us today [povLastName], we all hope to see more of you soon."
                    "As you leave the room you hear students talking about you. They seem to think that you're okay."
                    $ hina_amagi_points += 1
                    $ morale -= 1
            
        "Decline.":
            pov "I am sorry, but I have important business to attend to."
            teacher_susan "I understand, but I'm sure that we all look forward to be working with you."
            "As you leave the room you hear students wondering about you."
            $ academics += 1
            $ artistery += 1
            $ athletics += 1
            
        "Ask for a drink." if start_day_with_gin == True:
            pov "Hello, my name is [povName] and I'm a... Oh, wait... Do any of you kids have a drink?"
            class "..."
            teacher_susan "Oh my..."
            if povGender == 'male':
                pov "I do prefer gin or whiskey but anything would be fine."
            elif povGender == 'female':
                pov "I do prefer wine or whiskey but anything would be fine."
            class "..?"
            pov "Come on kids, I'm sure some of you have a lil' bottle with you in school!"
            teacher_susan "I'm sorry class, I'm sure [povTitle] [povLastName] is making a joke. Ha ha ha, [povTitle] [povLastName], very funny."
            class "..."
            teacher_susan "Well, that's all for now since I presume [povTitle] [povLastName] have {i}important business{/i} to attend to."
            "As you leave the room you can see a class full of severely confused students."
            $ deviance += 1
    return


label class1:
    
    scene bg class1 with fade
    "Seems like the last student is leaving."
    return


label class2:
    
    scene bg class2 with fade
    pov "You should be more focused on class!"
    $ academics += 1
    return


label class3:
    
    scene bg class3 with fade
    pov "That could raise some questions from the teachers council, what should I do?"
    menu:
        "Stop fooling around like that!":
            $ behavior += 1
            "They both look embarrassed and go back to class."
            return

        "Just smile and let it pass." if inhibition > 90:
            python:
                deviance += 1
                behavior -= 1
                if renpy.random.random() > 0.75:
                    red_orb += 1
            "When they see your smile they suddenly stop."
            return
        
        "Just smile and let it pass." if inhibition < 90:
            python:
                deviance += 1
                behavior -= 1
                if renpy.random.random() > 0.55:
                    red_orb += 1
            "When they see your smile their eyes start to glimmer."
            return


label class4:
    scene bg class4 with fade
    pov "Seems like someone's been a bad girl."
    $ deviance += 2
    $ behavior += 1
    $ morale -= 1
    return


label class5:
    scene bg class5 with fade
    "The students are completely out of control. This doesn't look good for you. Will you try to intervene?"
    menu:
        "Yes":
            if renpy.random.random() > (reputation / 20 ):
                "They listen somewhat and the class calms down a bit."
                $ behavior += 1
            else:
                "They won't listen and you can't do anything about it..."
                $ behavior -= 1
                $ academics -= 2
            return
        
        "No":
            info "You quickly turn around and leave."
            python:
                behavior -= 1
                academics -= 1
                artistery -= 1
                athletics -= 1
            return


label class6:
    scene bg class6 with fade
    pov "Aww, are you alright? You should be more careful!"
    $ morale += 1
    return


label class7:
    if renpy.random.randint(1,2) == 1:
        $ randImg = renpy.random.choice(["1", "2"])
        $ renpy.show("bg class7_"+randImg)
        with fade
        "As you walk into a classroom you see a girl pleasuring herself by rubbing her pussy against a table."
        menu:
            "What are you doing?":
                girl "Uh, ah, umm.."
                pov "You need to behave while in school. Stuff like that should be done at home."
                girl "Y... yeah... Sorry [povTitle] [povLastName]."
                pov "It's alright this time."
                "You watch the girl as she leaves embarrassed."
                $ behavior += 1
                $ inhibition += 1
                $ morale -= 1

            "Turn around and leave her alone.":
                "As you leave the room, you can hear her moan loudly."
                $ inhibition -=1
                if renpy.random.random() > 0.6:
                    $ red_orb += 1
    else:
        scene bg class7-3-1 with fade
        "As you walk into a classroom you see a girl pleasuring herself by rubbing her pussy against a table."
        menu:
            "What are you doing?":
                girl "Uh, ah, umm.."
                pov "You need to behave while in school. Stuff like that should be done at home."
                girl "Y... yeah... Sorry [povTitle] [povLastName]."
                pov "It's alright this time."
                "You watch the girl as she leaves embarrassed."
                $ behavior += 1
                $ inhibition += 1
                $ morale -= 1

            "Turn around and leave her alone.":
                "As you leave the room, you can hear her moan loudly."
                $ inhibition -= 1
                if renpy.random.random() > 0.8:
                    $ red_orb += 1
                    
            "Stay and watch":
                "You can clearly both hear and see how horny she is, slowly rubbing herself against the table and occasionally releasing a soft and weak moan."
                scene bg class7-3-2
                girl "Ah..."
                "Just as she moan her eyes refocus and she sees you."
                if inhibition - deviance > (80 + renpy.random.randint(0,10) ):
                    girl "Ahh!"
                    "She quickly tries to pull down her skirt and hide herself from you before she runs away. You really hope that she's too embarrassed to tell anyone what actually happened."
                    $ inhibition += 1
                    if renpy.random.random() > 0.5:
                        $ reputation -= 1
                else:
                    girl "*giggle* Do you, Ah... Like what you see?"
                    "Lucky for you she only seems to get more excited by you watching her."
                    scene bg class7-3-3
                    pov "I do, but please don't mind me Miss."
                    scene bg class7-3-2
                    girl "Ah... Mhmm... As you say [povTitle] Mhmm... [povLastName]..."
                    scene bg class7-3-3
                    "Her soft moan is for every rub growing in strength."
                    girl "Mhmm... Ah! It's getting awfully hot in here... Mhmm... Isn't it [povTitle] [povLastName]?"
                    scene bg class7-3-4
                    "Wow, she's really putting up a show."
                    girl "Ah! Mhmm... ah... Seeing you here... Mhmm... Really turns me on..."
                    if povGender == 'male':
                        "You can see how her pussy is dripping down to both her legs and the table while her eyes are focused on the growing bulge in your pants."
                    else:
                        "You can see how her pussy is dripping down to both her legs and the table while her eyes are slide up and down your body."
                    scene bg class7-3-4
                    girl "AH! I'm happy... Mhmm... That you enjoy this-Ah.... as well. Mhmm..."
                    "You see how her tempo rises and you suspect she's about to cum."
                    girl "Ah! AH! Mhmm.... Mhm! Ahhh..."
                    girl "*pant* Hah *giggle*"
                    scene black with fade
                    "She smiles and winks your way before she fixes her uniform and run away."
                    $ deviance += 1
                    if renpy.random.random() > 0.75:
                        $ red_orb += 1
    return


label class8:
    scene bg class8 with fade
    "As you walk into a classroom you see what looks like a gang rape. It's obvious that the girl is crying and struggling to get free."
    menu:
        "Stop that! What the hell are you doing?":
            pov "Get away from her right away!"
            guy "Hey, don't worry, she likes it."
            pov " Get. The. Fuck. away from her."
            girl "*sob*"
            pov "Hey there, don't worry, I'll help you, it's over now."
            girl "*sob* *sob* Th... *sob* ks..."
            guy "Hush stupid. We where just messing around-"
            pov "Stay back. Shut up. And don't you leave this room."
            girl "*sob* Thank... *sob* you... mr [povLastName] *sob*"
            pov "It's alright. This wasn't your fault."
            "You help the girl to the nurse and hand the guys over to the police."
            $ behavior += 2
            $ inhibition += 2
            $ morale -= 3
            
        "Join them." if povGender == 'male':
            "As you see her tearful eyes you can't stop yourself."
            "You walk over and push away the guy holding her head."
            guy "Hey! What the fuck man?"
            "You ignore him while you put you hand around her throat and pull out your dick."
            "She looks into your eyes pleading."
            "You tighten you grip around her throat."
            pov "Suck it."
            "Then you forcefully shove it into her mouth. She tries to resist but since she is already being pounded in the ass she can't do much."
            "You force your dick in and out. So hard she can barely breathe. You can hear her cry between the gasps of air."
            pov "You deserve this. Dirty slut."
            "How cute. It looks like she tries to say something. You remove your dick and put your head closer."
            girl "*sob* Please... *sob* no... no more... *sob* I... *sob can't *sob* take it... *sob*"
            pov "Huh? You want more? Did i hear you right? You are a slut and want more? Well then, I won't keep you waiting."
            "You put your hand over her mouth and look into her eyes. Despair. Fear."
            "You enjoy it."
            "As you walk around her you touch her body."
            pov "What a slutty body, you really are a whore."
            guy "Hey, don't overdo it man."
            "You look at him. He looks away. Fucking trash."
            "While you try to get eye contact with her you start touching her pussy, it looks like she lost all power. Weak."
            "One finger slides into her overused pussy. You guess that two or three others already fucked her today."
            pov "Oh, I wonder how much more your pussy can take. You're lucky. If you wouldn't be such a slut you would have gotten hurt long ago."
            girl "*sob* *sob*"
            "You're starting to lose interest in this cum-whore. You decide to end it quickly."
            "As you force your dick in, you can hear her trying to scream. You can feel her tremble as she really starts to cry."
            pov "Don't cry, you're so ugly when you cry. And come on, a cum-whore like you doesn't want to be ugly. Right?"
            "The only answer you get is a few weak sobs."
            "You slam your dick into her, over and over again. You try to get a reaction. But she is too weak."
            "As a last resort, you grab her breast a pull her up."
            girl "Ahhhh! Sss-... Stop!! Ah, pl...ea...se... *sob*"
            "You get harder and pull her closer as you pound her."
            pov "I will fill you up. You dirty slut."
            "When you are about to reach your climax you put your hand around her throat."
            pov "I won't let you breathe 'til you tighten up your slutty pussy so I can fill you up."
            "You slam your cock harder and harder into her. It feels like you massacre her. It feels good."
            "Suddenly you feel how she's getting heavier, and that very same second you fill her to the brim."
            "It feels so good you smile. This is life."
            pov "Hey, she passed out. Clean this shit up. And don't forget to remove that blood. No stains on the school floor."
            $ inhibition -= 2
            $ morale -= 4
            $ deviance += 2
            $ red_orb += 2
            $ reputation -= 3
            $ evil_points += 2
            
        "Watch them." if povGender == 'female':
            "You can clearly see the tearful eyes of the once pretty little thing as she gets fucked and degraded by her classmates. Over and over again."
            girl "*sob* Please... *sob* no... no more... *sob* I... *sob can't *sob* take it... *sob*"
            "The guys take turns fucking both her mouth and pussy until some guy gets the idea to try her ass. You can see the fear and pain in her eyes while they do their best to shove a large dick into her tight anus."
            girl "Ahhhh! Sss-... Stop!! Ah, pl...ea...se... *sob*"
            "Ah, the first time is always special..."
            pov "*giggle*"
            $ inhibition -= 2
            $ morale -= 5
            $ deviance += 2
            $ red_orb += 1
            $ reputation -= 3
            $ evil_points += 1
    return


label class9:
    scene bg class9-1 with fade
    "Just as you walk into the room a girl runs up and takes a solid grab of a classmates boobs."
    girl "Ahhhhhhhhhhhh!"
    
    scene bg class9-2
    pov "It's okay! Don't scream!"
    girl "But, but..."
    "At first you where certain she was about to cry."
    
    scene bg class9-3
    girl "YOU!"
    "It seems like she understood it was just a joke from her friend. As you see the anger building up you decide to walk away."
    "As you leave the room you can hear the girls screaming at each other. Kids these days."
    $ behavior -= 1
    $ inhibition -= 1
    $ morale += 1
    return


label class10:
    scene bg class10 with fade
    "On your way into a classroom you suddenly see several half naked girls."
    girl "Ahhhhhhhhhhhh!"
    girl "Get out!"
    pov "Sorry, sorry!"
    "You leave the room as soon as possible and try not to look back at them."
    $ behavior -= 1
    $ morale -= 1
    return


label class11:
    
    scene bg class11 with fade
    pov "Young love is cute, but it might be bad for the schools reputation to let them act this way so publicly."
    menu:
        "Stop that! You have to behave when at school!":
            $ behavior += 2
            $ morale -= 1
            girl "Oh, sorry [povTitle] [povLastName], we won't do it again."

        "Leave and let them have their innocent fun.":
            $ deviance += 1
            $ behavior -= 1
            "You leave the classroom without looking back."
    return


label class12:

    scene bg class12 with fade
    "They seem to be very concentrated, you get the feeling that you're disturbing them."
    $ academics += 1
    return


label class13:

    scene bg class13 with fade
    "You enter the room just as a student examines her breasts. An awkward silence but a beautiful moment."
    $ deviance += 1
    return


label class14:
    
    scene bg class14 with fade
    "You stumble into a supposedly empty room and find a young girl in an interesting position. Clearly she was expecting someone else."
    girl "..."
    menu:
        "Give her a reprimand.":
            $ behavior += 1
            $ deviance -= 1
            pov "I want you to go home right now and think about your behaviour. You don't want the other students to think that you're a bad girl, right?"
            "She shakes her head and her eyes start to water."

        "Degrade her.":
            pov "Pull up your panties and wash your hands."
            "She looks both surprised and ashamed. You leave the room with a grin."
            python:
                morale -= 1
                behavior += 1
                if renpy.random.random() > 0.75:
                    red_orb += 1
        
        "Turn around and leave her alone.":
            "You turn around as quickly as you can. As you leave the room you hear her hurry to adjust her clothes."
            python:
                deviance += 1
                behavior -= 1
                if renpy.random.random() > 0.6:
                    red_orb += 1
    return


label class15:
    
    scene bg class15-1 with fade
    "As you walk down the corridor, you see one of the teachers give one of the boys a really harsh treatment. A frightened girl stands beside them with her gaze in the other direction."
    menu:
        "Go right up to them and ask what's going on.":
            "You straighten your posture and walk up right beside them."
            pov "What is going on here?"
            teacher_may "This boy has been harassing that poor girl all day. Just now, I caught him in the act trying to grope her butt."
            if behavior_rules != "behavior_no_limit" and deviance > 20 and evil_points > 0:
                menu:
                    "Side with the boy":
                        pov "And you thought that was a good reason to physically assault him? You should be ashamed. He's just a young boy doing what young boys do. I see a dozen more risque events around this school every day!"
                        teacher_may "Yes, but-"
                        pov " I'm sorry that our teacher set a bad example. I'll see HER in my office. You two can carry on like before."
                        "The teacher seems very unhappy and worried and rushes out of the room. The girl seems extremely unhappy and tries to rush out of the elevator, but you grab her and hand her back to the boy who still has a startled expression on his face. Slowly realizing you're encouraging him, he happily pushes the unhappy girl against the wall and begins to fondle her butt."
                        guy "The teachers aren't going to save you now. You're all mine..."
                        "You leave the extremely happy boy and the very unhappy girl to their activities. You're sure at least one of them will enjoy themselves."
                        jump class15_2
                    
                    "Side with the teacher":
                        pov "I understand. We'd better continue this in my office."
                        "Both the teacher and the girl look on you with respect. The boy follows you to your office where you give him a sharp warning."
                        $ behavior += 1
                        $ deviance -= 1
            else:
                pov "I understand. We'd better continue this in my office."
                "Both the teacher and the girl look on you with respect. The boy follows you to your office where you give him a sharp warning."
                $ behavior += 1
                $ deviance -= 1
            
        "Let's see what happens.":
            "You stand back and make sure they don't see you."
            "The teacher is very upset and pushes the boy to the wall. After a streak of intense talking, she lets go of him and turns to the girl."
            "As the boy droops along, the teacher suddenly turns and sees you standing down the corridor. You feel uneasy and walk back to the office."
            $ behavior -= 1
            $ morale -= 1
            
        "Nice to see that the teachers are following school policy." if behavior_rules == 'behavior_no_limit':
            "You wait until the situation is resolved, and then approach the teacher."
            pov "Good job, hope he learned his lesson."
            teacher_may "Thank you principal, I just had to set him straight."
            "You give her a smile and she immediately starts to fiddle with her hair."
            python:
                behavior += 2
                morale -= 1
                if renpy.random.random() > 0.8:
                    reputation -= 1
            
        "Violence is NEVER the solution!" if behavior_rules == 'behavior_zero':
            "You rush up to them and literally pull them apart. The boy looks shattered."
            pov "Go back to class." 
            "The students hurry to get away from the scene. You face the teacher and struggle not to use foul language."
            pov "This is NOT how we handle things here at Ashford! Not while I'm around."
            teacher_may "But principle [povLastName], I just..."
            pov "Matters are not up for discussion, have I made myself clear?"
            teacher_may "I - I'm sorry, it won't happen again."
            pov "Damned right it won't!"
            menu:
                "Let her go":
                    teacher_may "..."
                    python:
                        behavior -= 1
                        morale += 2
                        reputation += 1

                "Teach her a lesson":
                    jump class15_2
    return

label class15_2:
    scene bg hallway with fade
    scene bg office with fade
    show teacher_may normal
    "You escort the unhappy and worried teacher back to your office."
    teacher_may "I wasn't being that unreasonable-"
    pov "You were assaulting a student. That's not just a firing offence, that's jail time."
    "The teacher suddenly seems very worried."
    pov "If I report it, that is. If you don't want me to report you, I'll need you to do something for me."
    "She looks at you with confusion until you wheel your chair out from behind your desk and unzip your pants."
    pov "pull your top down, and sit."
    hide teacher_may
    scene bg class15-2
    "She wavers for a moment, unsure. But you motion to pick up the phone on your desk, looking her straight in the eyes, and she takes a seat. With a deep breath, she pulls down her top and does her best to look stoic. You waste no time in taking advantage."
    scene bg class15-3
    "After you're satisfied you tell her:"
    pov "A very productive counselling session. We'll have to repeat this regularly to ensure you get the message. No more assaulting students, and no more interfering with the boys. Understood?"
    teacher_susan "... Yes sir."
    "The teacher unhappily leaves the room."
    $ class15_sex = True
    $ deviance += 1
    $ behavior += 1
    $ morale -= 1
    return



label class16:

    scene bg class16-1 with fade
    "As you enter the classroom you see a girl leaning over a table. It sure looks good, but if someone sees you it might put you in a tight spot."
    girl "Hello there [povTitle] [povLastName], guess what, I have something to show you."
    menu:
        "I know what you want." if deviance > 25:
            menu:
                "Slap that ass":
                    "You pull up her skirt and spank her."
                    scene bg class16-2
                    pov "Who's been a bad girl?"
                    girl "Ah, yes, I've been a bad girl.\nI've been a very bad girl.\nAh!"
                    "You spank and touch her some before leaving the room."
                    python:
                        if renpy.random.randint(1,2) == 1 and inhibition > 70:
                            info("The loud sound of you spanking her seems to draw attention and a few students catch you in the act.")
                            reputation -= 1
                            deviance += 1
                            inhibition -=1
                            morale -= 1
                        else:
                            info("As you leave the room you walk past a few students. That was a close call.")
                            deviance += 1
                            inhibition -=1
                            behvaiour += 1
                    
                "Degrade her in front of her class." if pda_rules == 'pda_bdsm' or behavior_rules == 'behavior_no_limit':
                    "You assemble the class while leaving the girl leaning over the table."
                    pov "Hello students, as you know we have a few rules here at Ashford."
                    class "..."
                    pov "I do enjoy putting my eyes on you students but that does NOT mean it's acceptable to act like a slut in public."
                    pov "Right here we have one of those, she tried to tempt me with her tight little ass and now I will show what happens if you do like her."
                    "You pull up her skirt and give her a hard spank. It echoes loudly in the quiet classroom."
                    scene bg class16-2
                    girl "Ahh!"
                    "You look at her and can't really figure out her reaction. So you decide to spank her again. And again."
                    girl "Ahh! AH!"
                    class "..."
                    pov "Do you understand class? This is what happens to bad girls."
                    class "Yes [povTitle] [povLastName]."
                    "As you leave the room you are unsure if you motivated or discouraged the behaviour."
                    $ morale -= 1
                    $ deviance += 2
                    $ inhibition +=3
            return

        "Oh, let me see.":
            scene bg class16-2
            girl "Do you like what you see?"
            pov "Yeah, that's a good girl."
            python:
                if renpy.random.randint(1,5) > 4:
                    info("Just as you said your last words a few students enter the room. This can't be good.")
                    reputation -= 1
                    deviance += 1
                    inhibition -=1
                else:
                    deviance += 1
                    inhibition -=1
            
        "Stop that and get back to class.":
            girl "You're so boring [povLastName]."
            $ deviance -= 1
    return


label class17:

    scene bg class17 with fade
    "Some of the older students give the younger ones challenges and assignments to carry out. You are not sure if this particular girl is involved in such activities. Her blushing suggests something is going on, but her confident look stops you from asking."
    $ morale += 1
    return


label class18:

    scene bg class18-1 with fade
    "While helping with handing out the graded assignments, one of the girls just didn't watch where she was going."
    menu:
        "Give her a hand":
            girl "Thank you [povTitle] [povLastName]."
            $ morale += 1
            
        "Leave her alone":
            scene bg class18-2
            "She looks embarrassed while you stand there looking at her."
            
        "Make fun of her" if evil_points > 0:
            pov "Little girl, don't you know how to walk properly?"
            girl "Umm, sorry..."
            pov "Don't tell me you're sorry, clean up this mess and go back to your seat."
            scene bg class18-2
            girl "Yes [povLastName]."
            pov "It's [povTitle] [povLastName]."
            girl "..."
            girl "Yes [povTitle] [povLastName]."
            $ morale -= 2
    return


label class19:

    scene bg class19 with fade
    "You witness a moment of girl-power. Apparently their teacher made a sexist remark or perhaps even tried to grope one of them? Either way, those who lie down with dogs get fleas."
    $ morale -= 1
    $ behavior -= 1
    return


label class20:

    scene bg class20 with fade
    "Working too hard can literally bring you to your knees. Make sure you get enough sleep!"
    $ morale -= 1
    return


label class21:

    scene bg class21 with fade
    "As you enter the room, you see a student sleeping in an awkward position against a table. One of her friends must have pulled a prank on her and tucked up her skirt."
    girl "..."
    "She twitches and suddenly becomes aware of your presence."
    menu:
        "Hrm, time to wake up?":
            "She's to embarrassed to speak but quickly straightens her skirt and runs out."
            $ behavior += 1
            $ morale -= 1

        "Cheeks of joy!":
            "You don't say anything, you just stand there and look."
            girl "I- I must have dozed off!"
            pov "Forget about it."
            girl "* gulp *"
            pov "* smile *"
            $ deviance += 1
            
        "What the..?":
            pov "Really, this is highly inappropriate."
            girl "I don't know how I got like this, I- I promise!"
            pov "Move along, just do it."
            "She leaves in a hurry and you can see that she is feeling really bad about the situation."
            $ inhibition += 1
            $ deviance -= 1
            $ behavior += 1
    return


label class22:

    scene bg class22 with fade
    if povGender == 'male':
        "As the students work in pairs, you see an obvious player with a cute girl in his clutches. Lucky guy."
    elif povGender == 'female':
        "As the students work in pairs, you see an obvious player with a cute girl in his clutches."
    $ morale += 1
    return


label class23:

    scene bg class23 with fade
    "Immoral behaviour! I love it!"
    python:
        if renpy.random.randint(1,4) == 1:
            reputation -= 1
            deviance += 1
        else:
            red_orb += 1
            deviance += 1
    return


label class24:

    scene bg class24 with fade
    "While fooling around, one of the girls worked up quite a sweat chasing her classmate around the room."
    $ morale += 1
    return


label class25:

    scene bg class25 with fade
    "Good girls go to heaven, I wonder where this little girl will go?"
    $ inhibition -= 1
    return


label class26:

    scene bg class26 with fade
    "When temptation comes around, having a girlfriend really isn't that big a deal. Unless she catches you, that is..."
    python:
        if renpy.random.randint(1,2):
            deviance += 1
            behavior -= 1
        else:
            red_orb += 1
            behavior -= 1
    return


label class27:

    scene bg class27 with fade
    "You walk right into the middle of a rather loud discussion."
    girl "[povTitle] [povLastName]!"
    pov "What's all the hubbub about?"
    girl "It says in our biology books that the woman is inferior to the man!"
    menu:
        "That is clearly a bad print":
            pov "What? Show me."
            girl "Right here! See? It says that genetically, the man is the one who takes the lead through evolution. It makes me so mad!"
            pov "Calm down, I'll take this to the school board. Don't you worry, this is NOT what Ashford stands for."
            "As you leave the room, the discussion calms and the girls nod to each other. You just earned yourself a great deal of respect."
            $ reputation += 1
            $ blue_orb += 1

        "Take it easy":
            pov "Material tends to age, and doesn't always keep up with history."
            girl "So what are you gonna do about it?"
            pov "Since changing all books is a rather hefty cost, you'll just have to be patient for now."
            girl "How long?"
            pov "I'll make sure to bring it up in the next budget talks. Meanwhile, take the rest of the lesson to rip out that particular page from all the books."
            "They seem somewhat content to the solution, but you can still hear them mumble about the sexist society as you leave."
            $ morale += 1
            $ behavior -= 1
            
        "So?" if povGender == 'male':
            pov "Damn right! Evolution is a wonderful thing, don't ya think?"
            girl "WHAT?!"
            pov "And the best part is, once a woman gets old and her tits get saggy, you just throw her out and get a younger one!"
            girl "ARE YOU FUCKIN' KIDDIN' ME?!"
            pov "Young lady, you assume that I have a bad sense of hearing since I'm older than you. Rest assured, I'm a supreme biological being. I hear you fine sweetie."
            girl "!!!???!!!"
            pov "What? Did someone rip a fart?"
            girl "I THINK I'M GONNA-"
            pov "I think I'm gonna go to my office now and surf some loli."
            girl "* gasps *"
            pov "You DID rip a stinker, I knew it!"
            "Before the poor little inferior thing gets to her senses, you take a bow and leave the room. Like a boss."
            $ evil_points += 1
    return


label class28:

    scene bg class28 with fade
    "You enter class only to find the students gone. Before your eyes, a teacher bends over and seems to drift away in graphic dreaming."
    $ inhibition -= 1
    return


label class29:

    scene bg class29 with fade
    "Sometimes when fooling around, students tend to forget that anyone can walk in on them. Or they don't care... Hello girls!"
    python:
        if renpy.random.randint(1,2) == 1:
            inhibition -= 1
        else:
            morale += 1
    return


label class30:

    "A faint sobbing catches your attention."
    scene bg class30 with fade
    girl "* sniffle *"
    pov "Hey, has something happened?"
    girl "It's nothing, I'm... nothing."
    menu:
        "What is going on?":
            pov "Nothing huh?"
            girl "I... just... I'd like to be alone."
            pov "Did someone do something to you?"
            girl "Please... I..."
            menu:
                "Leave her alone, poor thing":
                    "You hesitate, but if she wants to be alone..."
                    pov "You know my door's always open, right?"
                    "She gives an empty smile, you walk away with a lump in your throat."
                    $ morale -= 1
                
                "Get to the bottom of it":
                    "You sit down beside her in silence. After a while you turn to her."
                    pov "You don't have to tell me anything, not about anyone or any matter."
                    girl "..."
                    pov "Just hear me out, ok?"
                    girl "... Ok..."
                    pov "Whatever happened to you, if someone did anything or said anything, if you're having trouble at home..."
                    "She starts to cry, at first silent and soft, but it soon intensifies."
                    pov "Let's go to my office, shall we? It's more private, no one will see you and you can decide then if you want to share with me, ok?"
                    girl "I- I... yes... thank-"
                    "She buries her head in her arms and shake heavily. You support her back to your office and get her something warm to drink."
                    $ good_points += 1
                    $ morale += 1
            return
                    
        "If it's nothing, don't you have classes to attend?":
            pov "You better get back to class."
            girl "But... I..."
            pov "Yes?"
            girl "I- I feel so..."
            menu:
                "Poor thing":
                    pov "Look, maybe you should take the rest of the day off."
                    girl "Yes... that might be..."
                    "She gets to her feet and you walk her to her locker."
                    $ morale += 1
                
                "Chin up":
                    pov "Now, now, it can't be that bad. I'm sure whatever caused those tears will soon be forgotten."
                    girl "..."
                    pov "Run along now, and tell your teacher that you just needed a breath of air, ok?"
                    girl "Ok..."
                    "Geese, all the drama surrounding these girls!"
                    $ morale -= 1
            return
                
        "Great, another emo...":
            pov "What's your name?"
            girl "M- my name?"
            pov "Ye-es, your name. What is it?"
            girl "I'm-"
            pov "Oh for fuck's sake spit it out."
            girl "... * sob * ... "
            pov "How many of you little dramaqueens must I endure?"
            girl "H- how do you-"
            pov "I mean, since I got here, I don't know just how many of your kind I've encountered."
            girl "My... my kind?"
            pov "Sure, weak minded little cunts like yourself."
            "She just stares at you with eyes full of tears."
            girl "W- what have I done?"
            pov "You tell me, what have you been up to?"
            girl "I don't know what-"
            pov "Ah gee, you don't know your name and you don't know why you're sobbing like a baby, is that it? Have I read the situation correctly?"
            girl "NO! I- I... I mean..."
            pov "DON'T YOU RAISE YOUR VOICE AT ME, UNDERSTOOD?"
            girl "* gasp *"
            pov "Just shut. the fuck. up."
            girl "Ah, aah..."
            pov "Jesus! Shut your fuckin' trap and listen the fuck up, you hear what I'm sayin'? DO YOU?"
            girl "Pleeease! I- I'm..."
            pov "Ugly and stupid whore!"
            girl "... ! ..."
            pov "Boo-hoo, is your boyfriend having a go at the other girls? Is that it?"
            girl "NO!"
            pov "Aaw, your parents are disgusted that they have such a fucking waste for a daughter, is that it?"
            girl "Stop it..."
            pov "Or is your step daddy tired of fucking your over-used and smelly cunt?"
            girl "STOP IT!!!"
            pov "You stop it."
            girl "What?"
            pov "You heard me. You stop it."
            "She gets up and starts to move away. You grab her shoulders and push her against the wall."
            girl "Ouch!"
            "You lean in on her, and as you keep a firm grip of her shoulders, you whisper in her ear:"
            pov "You are fat. You should kill yourself."
            "You let her go and look at her. She looks like she's gonna throw up. You give her your most constrained smile, turn around and start to whistle as you walk  down the corridor. You don't look back, not even once."
            $ evil_points += 1
            $ morale -= 3
    return


label class31:

    scene bg class31 with fade
    "Friends will be friends, no matter what!"
    $ morale += 1
    return
    
    
label class32:

    scene bg class32 with fade
    "Two girls decided to take a rest between classes. Isn't that adorable!"
    $ morale += 1
    return
    
    
label class33:

    scene bg class33 with fade
    "In the best of worlds, a little sneak peek can turn into something more..."
    $ deviance += 1
    return
    
    
label class34:

    scene bg class34 with fade
    "After getting caught masturbating during class, a young girl is forced to call her parents to tell them why she will get detention."
    girl "Yes dad, something came up... far up..."
    if renpy.random.randint(1,3) == 1:
        $ red_orb += 1
    else:
        $ deviance += 1
    return


## Class 35


label class36:

    scene bg class36-1 with fade
    "Upon entering a classroom, two girls rush towards you and throw themselves around your neck."
    girl1 "[povTitle] [povLastName]! Thank you so much for all your effort!"
    girl2 "Yeah, it's amazing to know that you are so dedicated!"
    scene bg class36-2
    $ reputation += 1
    menu:
        "Girls, girls, I'm only doing my job here.":
            girl1 "But we are truly privileged to have you as our principal!"
            girl2 "Truly, madly, deeply!"
            "Their affection is touching."
            $ behavior += 1
            $ morale += 1
            
        "Ah what the heck, I am pretty awesome!":
            girl1 "It's always so special when you visit!"
            girl2 "It's a shame you're not here more often!"
            "It wouldn't hurt to come to this class more often, that's for sure!"
            $ inhibition -= 1
            
        "It's a me, Principal!" if new_game_plus == True:
            girl1 "Let me be your princess!"
            girl2 "And I can be in another castle!"
            "Looks like there will be some plumbing tonight..."
            $ deviance += 1
    return
    
    
label class37:

    scene bg class37 with fade
    if renpy.random.randint(1,2) == 1:
        "During class, some weary girls drift away to dream land. Unfortunately, dreams are not always that pleasant. Wait a minute, this is not a dream... "
    else:
        "Squidle-dee, squidle-daa, she's got something slimy in her braa."
    $ deviance += 1
    return


label class38:

    scene bg class38 with fade
    if renpy.random.randint(1,2) == 1:
        "Since you just use one hand writing, there's plenty of fun to be done with the other one."
    else:
        "Some girls just wanna have fun."
    $ deviance += 1
    return


label class39:

    scene bg class39 with fade
    "You arrive early to meet up with a girl who's been skipping class on a regular basis. Since she didn't want to get expelled, she said she'd do practically anything to avoid it."
    "Such a beautiful morning!"
    $ deviance += 1
    return


label class40:

    scene bg class40-1 with fade
    "On your way to class, you see one of the hall way monitors getting pretty ugly with one of the girls."
    "monitor" "I thought I told you, if you're late to class more than five times a week we're gonna have to do something about it."
    girl "Gulp!"
    "monitor" "I'm sure we can find some quiet little space where no one will disturb us, eh?"
    girl "B- but..."
    "monitor" "Oh I see, you need some time to warm up..."
    girl "WHAT?"
    "monitor" "Gee, that's very thoughtful of you missy. Wanting me to feel comfortable and all."
    girl "No, I- I don't want you to feel ANYTHING!"
    "monitor" "You just be a good girl and pump that cute pussy wide enough for me, you hear? I'll be looking for you once you're ready."
    girl "Pump?! W- what are you saying?"
    "monitor" "I'm saying that you better put that cute little device of yours into good use. That's right, I know you got one of them gadgets in your bag."
    scene bg class40-2
    girl "How can you... I mean, I've never..."
    "monitor" "It's Ashford baby, no secret stays hidden in this place."
    "You're not sure about what you just witnessed. Was it an innocent moment between two young ones with a teasing edge, or was it something altogether different?"
    return
    
    
label class41:

    scene bg class41-1 with fade
    "As you visit class, you see that young girl from earlier in the hall. Seems like she's trying to do what her friend requested."
    scene bg class41-2
    girl "Oh, eh..."
    "You move in front of her row, carefully examining the action going on under the desk."
    pov "Is everything alright young lady?"
    scene bg class41-3
    girl "Mhm..."
    pov "You seem very concentrated."
    girl "I- I just... ehm..."
    pov "Just carry on with your assignment, don't let me slow you down."
    girl "T- thanks... oh..."
    "You leave her alone and let her finish her work."
    scene bg class41-4
    scene bg class41-5
    scene bg class41-6
    girl "H- how embarrassing!"
    $ red_orb += 1
    return


label class42:

    scene bg class42 with fade
    "Are you alright? Mind your step next time."
    if renpy.random.randint(1,2) == 1:
        $ morale -= 1
    else:
        $ inhibition -= 1
    return
    
    
label class43:

    scene bg class43 with fade
    if renpy.random.randint(1,2) == 1:
        "They are either going to go out on a date, or stand there frozen solid for the remainder of the break."
    else:
        "Puppy love. How cute."
    $ inhibition -= 1
    return


label class44:

    scene bg class44-3 with fade
    teacher "And so you see, Marco Polo really didn't know how to use a spoon with his left hand." 
    girl "..."
    teacher "I'll give you some time before lunch to write down the essentials and sort your notes. Don't forget that the assignment is due next Tuesday."
    scene bg class44-4
    girl "Oh great, the assignment..."
    pov "Hey there, you seem a bit off."
    scene bg class44-1
    girl "I'm sorry [povTitle] Principal, I just don't know if I'll manage to get all this work done in time."
    menu:
        "Reminds me of the old days.":
            pov "I know the feeling, when I was your age I'd find myself sitting with my homework wondering if I'd ever graduate."
            scene bg class44-2
            girl "Really? Wow, and now you're principal and all!"
            pov "So you see, it's quite natural to feel as if there's not time enough. You'll pull through, I'm sure of it."
            girl "I'll do my very best, thank you sir!"
            pov "Don't mention it, I take personal interest in seeing my students increase their knowledge and ability."
            scene bg class44-5
            "She blushingly turns her attention towards the board, you can almost see her confidence rising."
            $ academics += 1
            
        "Kids of today...":
            pov "Perhaps you should try mind mapping?"
            girl "..."
            pov "It's easy once you get the hang of it. I'm sure your teacher could tell you all about it."
            girl "More to think about, great..."
            pov "What's that?"
            girl "Nothing, thank you [povTitle] Principal..."
            pov "Please, it's what I'm here for."
            girl "Right..."
            scene bg class44-4
            "She turns to the board and seems to be thinking real hard. At least it's a start."
            $ morale -= 1
            $ behavior -= 1
    return


label class45:

    scene bg class45 with fade
    pov "And how are we doing?"
    girl "Oh, it's a bit frustrating right now but I'm sure I'll get the hang of it."
    pov "That's the spirit."
    if renpy.random.randint(1,2) == 1:
        $ academics += 1
    else:
        $ academics -= 1
    return


label class46:

    scene bg class46 with fade
    "Daydreaming, an essential part of school."
    $ morale += 1
    $ academics -= 1
    return


label class47:

    scene bg class47 with vpunch
    girl "W-whaa!"
    pov "Did you hurt yourself?"
    girl "N-no, I'm alright."
    pov "That's good to hear."
    $ behavior += 1
    return


label class48:

    scene bg class48 with fade
    "Sometimes, drifting away helps you get right back on track."
    $ morale += 1
    return


label class49:

    scene bg class49 with fade
    "Some girls sport a more conservative outfit."
    $ inhibition -= 1
    return


label class50:

    scene bg class50 with fade
    "Who knows what the future will bring? The only thing we can be sure of is that busy bees need a rest too."
    $ morale += 1
    return


label class51:

    scene bg class51:
        pos (0.0, 0.0)
        linear 10.0 pos (0.0, -1.5)
        linear 8.6 pos (0.0, -0.2)
    with fade
    
    if renpy.random.randint(1,2) == 1:
        "I would love to have {i}her{/i} as my biology teacher."
    else:
        "Suddenly the idea of {i}private lessons{/i} feel very compelling."
    $ deviance += 1
    return


label class52:
    scene bg class52:
    girl "Principal povName! Thank you very much for getting us our very own café!"
    pov "Whoa, you're welcome!"
    girl "I really am a cake and cookie kind'a girl! I better be careful or I'm bound to look like a sumo-wrestler in just a couple of weeks!"
    pov "What, that's... You be careful then..."
    girl "I will <3"
return
