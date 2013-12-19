image bg library1 = "locations/library/library1.jpg"
image bg library2 = "locations/library/library2.jpg"
image bg library3-1 = "locations/library/library3-1.jpg"
image bg library3-2 = "locations/library/library3-2.jpg"
image bg library4 = "locations/library/library4.jpg"
image bg library5 = "locations/library/library5.jpg"
image bg library6 = "locations/library/library6.jpg"
image bg library7 = "locations/library/library7.jpg"
image bg library8 = "locations/library/library8.jpg"
image bg library9 = "locations/library/library9.jpg"
image bg library10 = "locations/library/library10.jpg"
image bg library11 = "locations/library/library11.jpg"
image bg library12 = "locations/library/library12.jpg"
image bg library13 = "locations/library/library13.jpg"
image bg library14 = "locations/library/library14.jpg"
image bg library15 = "locations/library/library15.jpg"
image bg library16 = "locations/library/library16.jpg"
image bg library17-1 = "locations/library/library17-1.jpg"
image bg library17-2 = "locations/library/library17-2.jpg"
image bg library18 = "locations/library/library18.jpg"
image bg library19-1 = "locations/library/library19-1.jpg"
image bg library19-2 = "locations/library/library19-2.jpg"
image bg library19-3 = "locations/library/library19-3.jpg"
image bg library20-1 = "locations/library/library20-1.jpg"
image bg library20-2 = "locations/library/library20-2.jpg"
image bg library20-3 = "locations/library/library20-3.jpg"
image bg library21-1 = "locations/library/library21-1.jpg"
image bg library21-2 = "locations/library/library21-2.jpg"
image bg library22 = "locations/library/library22.jpg"
image bg library23 = "locations/library/library23.jpg"
image bg library24 = "locations/library/library24.jpg"
image bg library25 = "locations/library/library25.jpg"
image bg library26-1 = "locations/library/library26-1.jpg"
image bg library26-2 = "locations/library/library26-2.jpg"
image bg library27 = "locations/library/library27.jpg"
image bg library28 = "locations/library/library28.jpg"
image bg library29-1 = "locations/library/library29-1.jpg"
image bg library29-2 = "locations/library/library29-2.jpg"
image bg library30-1 = "locations/library/library30-1.jpg"
image bg library30-2 = "locations/library/library30-2.jpg"
image bg library31 = "locations/library/library31.jpg"

init:
    if persistent.mod_disable_original_events == False:
        $ event("library1", "act == 'library'", event.choose_one('library'), priority=200)
        $ event("library2", "act == 'library' and academics > 20", event.choose_one('library'), priority=200)
        $ event("library3", "act == 'library' and academics < 20", event.choose_one('library'), priority=200)
        $ event("library4", "act == 'library' and inhibition < 95 and behavior > 20", event.choose_one('library'), priority=190)
        $ event("library5", "act == 'library' and inhibition < 90", event.choose_one('library'), priority=190)
        $ event("library6", "act == 'library'", event.choose_one('library'), priority=200)
        $ event("library7", "act == 'library' and morale < 50", event.choose_one('library'), priority=200)
        $ event("library8", "act == 'library'", event.choose_one('library'), priority=200)
        $ event("library9", "act == 'library' and behavior > 10", event.choose_one('library'), priority=190)
        $ event("library10", "act == 'library' and inhibition < 80 and deviance > 20", event.choose_one('library'), priority=180)
        $ event("library11", "act == 'library' and inhibition < 85", event.choose_one('library'), priority=180)
        $ event("library12", "act == 'library' and behavior > 25", event.choose_one('library'), priority=190)
        $ event("library13", "act == 'library' and inhibition < 90", event.choose_one('library'), priority=190)
        $ event("library14", "act == 'library' and deviance < 20", event.choose_one('library'), priority=180)
        $ event("library15", "act == 'library' and deviance < 20", event.choose_one('library'), priority=200)
        $ event("library16", "act == 'library' and behavior > 25", event.choose_one('library'), priority=180)
        $ event("library17", "act == 'library' and academics > 45", event.choose_one('library'), priority=180)
        $ event("library18", "act == 'library' and uniform == 'no_uniform'", event.choose_one('library'), priority=190)
        $ event("library19", "act == 'library' and inhibition < 80 and deviance > 10", event.choose_one('library'), priority=150)
        $ event("library20", "act == 'library' and academics > 30", event.choose_one('library'), priority=170)
        $ event("library21", "act == 'library' and inhibition < 90", event.choose_one('library'), priority=170)
        $ event("library22", "act == 'library' and inhibition < 25 and deviance > 75", event.choose_one('library'), priority=100)
        $ event("library23", "act == 'library' and morale < 50", event.choose_one('library'), priority=170)
        $ event("library24", "act == 'library' and inhibition < 75", event.choose_one('library'), priority=150)
        $ event("library25", "act == 'library' and inhibition < 50 and deviance > 50", event.choose_one('library'), priority=120)
        $ event("library26", "act == 'library' and inhibition < 50 and deviance > 50", event.choose_one('library'), priority=120)
        $ event("library27", "act == 'library' and inhibition < 90 and deviance > 0 and deviance < 50", event.choose_one('library'), priority=180)
        $ event("library28", "act == 'library' and inhibition < 90 and inhibition > 60", event.choose_one('library'), priority=160)
        $ event("library29", "act == 'library' and inhibition < 90", event.choose_one('library'), priority=160)
        $ event("library30", "act == 'library' and academics > 30 and uniform == 'no_uniform' and building_library > 2", event.choose_one('library'), priority=160)
        $ event("library31", "act == 'library' and academics > 30 and building_library > 2", event.choose_one('library'), priority=150)
        
label library1:
    
    scene bg library1 with fade
    "You meet two girls who blushingly give you compliments for your good work."
    $ morale += 1
    return


label library2:
    
    scene bg library2 with fade
    "While walking around in the library you meet two students working on a project. When you walk up to them they ask you to help them with a difficult task."
    "Before you even know it, you have spent an hour helping them. They are very grateful and thank you for helping them."
    python:
        if renpy.random.random() > 0.5:
            academics += 1
        else:
            blue_orb += 1
    return


label library3:
    
    "As you walk around in the library you suddenly hear a faint snore."
    scene bg library3-1 with fade
    "You see a student who fell asleep in the middle of study and decide to wake her up."
    girl "Mhmm? Oh!"
    scene bg library3-2
    girl "[povTitle] [povLastName]! I'm sorry, I just have this important test coming up and I must have fallen asleep..."
    "She looks really worried so you decide to tell her:"
    menu:
        "Don't worry, just keep up your studies.":
            $ academics += 1

        "This time it's ok, but from now on make sure to get enough sleep at home.":
            $ behavior += 1

        "It's alright, but don't forget to take some time to just relax.":
            $ morale += 1
            
    girl "Yes [povTitle] [povLastName]!"
    return


label library4:
    
    scene bg library4 with fade
    "In the library you see a pair of students absorbed in their books."
    $ academics += 1
    return


label library5:
    
    scene bg library5 with fade
    "You see an embarrassed girl dressed up in some weird clothes."
    menu:
        "(Just ignore her, she seems embarrassed enough.)":
            $ inhibition -= 1

        "Compliment the outfit.":
            $ morale += 1
            girl "Umm... Thanks [povTitle] [povLastName]."

        "Tell her to change back into her school uniform.":
            $ morale -= 1
            $ inhibition += 1
            $ behavior += 2
            "After you told her, she starts crying and quickly runs away."
    return


label library6:
    
    scene bg library6 with fade
    "As you enter the library you see a girl who just borrowed a huge stack of books. It makes you happy that the students take their studying seriously."
    $ academics += 1
    return


label library7:
    
    scene bg library7 with fade
    "Some students study in the library. They don't seem to enjoy it very much though."
    $ academics += 1
    $ morale -= 1
    return
    
label library8:
    
    scene bg library8 with fade
    "You meet a student in the library studying for a test. You try to help as much as possible, but in the end you're not sure that it really was helpful."
    python:
        if renpy.random.random() > 0.5:
            academics += 1
        else:
            academics -= 1
    return


label library9:
    
    scene bg library9 with fade
    girl "Hello Principal! Can I ask you a question?"
    pov "Hello there, sure, ask away."
    girl "What subjects are your strongest?"
    menu:
        "Science is the logical choice." if academics > 30:
            "After explaining your train of thought you share some bits of information."
            $ academics += 1
        
        "Sports and keeping fit." if athletics > 30:
            "You tell her stories about your old training regime and how important it is to stay fit."
            $ athletics += 1

        "Creative work and art." if artistery > 30:
            "While sketching up a quick portrait of her, you talk about how a creative flow can benefit other subjects."
            $ artistery += 1
        
        "It's all about fun!" if morale > 30:
            "You two talk and joke with each other while you explain the importance of having fun."
            $ morale += 1

        "Human anatomy and biology." if inhibition < 80:
            "You spend some time describing and discussing human reproduction."
            $ deviance += 1
            
        "Quickly turn around and walk away.":
            "You can see the girl looking confused as you glance back at her."
    return


label library10:
    
    "While walking in the library you hear a slurping sound, you decide to find out where it comes from."
    scene bg library10 with fade
    "Suddenly you see the source. It seems like they haven't noticed you yet."
    menu:
        "Leave them":
            "You decide not to spoil the fun and quickly walk away."
            python:
                inhibition -= 1
                deviance += 1
                if renpy.random.random() > 0.5:
                    red_orb += 1
            
        "Give them a warning":
            $ inhibition += 1
            $ deviance -= 1
            $ behavior += 1
            "You give them both a very strict warning and they both promise that it will never happen again."
        
        "Expel them." if pda_rules == 'pda_expulsion':
            $ inhibition += 3
            $ deviance -= 3
            $ behavior += 4
            "You bring them to your you office and you quickly sign the paperwork. You tell them to clean up and get their stuff before leaving the school."
    return


label library11:
    
    scene bg library11 with fade
    "You see a girl reaching for an algebra book. Luckily for you it was on the top shelf."
    $ inhibition -= 1
    return


label library12:
    
    scene bg library12 with fade
    "Some students really put extra effort in taking care of their books."
    $ behavior += 1
    return


label library13:
    
    scene bg library13 with fade
    "While passing through the library, you suddenly come across a young girl who apparently fell asleep in the middle of studying."
    menu:
        "She must be exhausted.":
            pov "I don't have the heart to wake her up."
            $ morale += 1
            $ academics -= 1
        
        "This is no place for napping!":
            pov "What's this?"
            girl "Uh... oh... I must have dozed off."
            pov "As long as you are on school premises, you follow our code young lady."
            girl "I - I'm sorry [povTitle]... I was just so tired."
            pov "From now on I expect you to go to bed early on weekdays. Less fooling around after school is the right medicine."
            girl "Y - yes sir."
            $ deviance -= 1
            $ behavior += 1
        
        "Hey, sleepy head, it's time to wake up." if evil_points < 1:
            girl "U...uhm..."
            pov "Wow, you were really out of it."
            girl "Oh [povTitle]... I'm so sorry. I had the strangest dream."
            pov "Now now, that's alright. We all get tired, don't we?"
            girl "I - I guess... But, you're so kind. I really shouldn't be sleeping while in school."
            pov "Nothing to worry about. What kind of dream was it?"
            girl "Oh... Umm..."
            pov "Ha - ha, I think I can guess..."
            girl "*giggle*"
            $ morale += 1
            $ inhibition -= 1
    return
            
            
label library14:
    
    scene bg library14 with fade
    "Some of the books on human anatomy has got quite a few graphic pages in it."
    $ deviance += 1
    return
    
    
label library15:
    
    scene bg library15 with fade
    "The relaxed environment makes the library a perfect place to wind down after class."
    $ morale += 1
    return
    

label library16:
    
    scene bg library16 with fade
    "It makes you happy to see that so many of the students found a sanctuary in the library."
    $ academics += 1
    return
    
    
label library17:
    
    scene bg library17-1 with fade
    "You meet a girl in the library, and suddenly realize that you've helped her out with her assignment earlier."
    girl "[povTitle] [povLastName]! Thank you so much for spending all that time with my assignment. If I hadn't been able to ask you all of those questions, I would've never passed the test!"
    pov "Hey, when a student is so dedicated to her assignment, I'm only glad to help."
    
    if deviance < 15:
        girl "Once again, thanks!"
        "You leave the library with a smile on your face."
        $ morale += 1

    else:
        girl "Oh how I wish I could return the favour!"
        pov "Well, as a matter of fact, there is one thing."
        girl "Great, just say it and I'll do my best!"
        pov "I'm sure you will."
        scene bg library17-2
        "Funny, she doesn't look at all glad about helping."
        $ inhibition -= 1
        $ morale -= 1
    return


label library18:
    
    scene bg library18 with fade
    if renpy.random.randint(1,2) > 1:
        "Not every student enjoys the company of the principal."
    else:
        $ "You meet a student in the library and decide to help her find a good book. You end up giving her a book by "+renpy.random.choice(["Carl Gustav Jung.", "Stephen Hawking", "Michio Kaku", "Lawrence Maxwell Krauss", "Paul Ekman"])+"."
    $ academics += 1
    return


label library19:
    
    scene bg library19-1 with fade
    "As you walk through the library, out of nowhere, a pink haired student rushes right into you and causes you both to fall to the floor."
    girl "Oh! [povTitle] [povLastName]!"
    pov "Mhmff!"
    girl "Are you okay?"
    pov "Mmmfffffftt!"
    girl "I can't hear a word of what you're saying!"
    pov "Blblllfff!"
    girl "Here, I'll just roll off your face so I can hear what you're trying to say."
    pov "*gasp*"
    scene bg library19-2
    girl "Oh, you're strong! Hey! I- I don't have any panties on!"
    pov "Here, let me just help you up."
    girl "But- but, I'm already up!"
    menu:
        "Of course you are, I'm just trying to prevent us both from falling again.":
            girl "Oh, b- but... ahh, be careful not to..."
            pov "Let me just retain my balance. There, much better."
            girl "This was not..."
            "You leave quickly but will probably never forget that sweet, sweet sight."

        'You "accidentally" give her a little push...':
            scene bg library19-3
            girl "Ouch!"
            pov "How clumsy of me, I'm truly sorry."
            "No panties indeed..."
            $ deviance += 1

        "That's what you think. I myself live by alternate rules of physics!:" if new_game_plus == True:
            "Let me tell you this much: you're still lying on the floor."
            girl "That's so weird!"
            pov "I KNOW!"
            girl "What should we do?!"
            pov "Quickly, down on all fours!"
            girl "But... WHY?"
            pov "To prevent us from getting sucked into space, there's really not much time sister!"
            girl "Yikes! I'll get down as quickly as I can!"
            pov "Space-e-e-e-e-e-e-e-e..."
            scene bg library19-3
            girl "Help! Won't anybody help us?"
            pov "Sucke-e-e-e-e-e-e-e-d..."
            girl "Are there any Astronauts in the building?!"
            pov "Stupid hoe-e-e-e-e-e-e..."
    return


label library20:
    
    scene bg library20-1 with fade
    if behavior < 25:
        girl "Schh! You have to keep quiet."
        pov "Sorry, didn't mean to disturb."
        scene bg library20-2
        girl "SCHH!"
        if evil_points > 0:
            pov "SCHH!"
            scene bg library20-1
            girl "..."
            $ morale -= 1
        else:
            pov "..."
            
    elif behavior < 50:
        girl "Keep it down, will you? We're preparing for the test."
        pov "Please, don't let me intrude."
        "She glares at you and you decide to sneak away as quietly as you can."
    else:
        girl "Oh, would you mind keeping it down?"
        pov "Certainly, I just wanted to say that you're the embodiment of the Ashford spirit."
        scene bg library20-3
        girl "Gee [povTitle] [povLastName], that sure means a lot!"
        if evil_points > 0:
            pov "SCHH!"
            scene bg library20-1
            girl "..."
            $ morale -= 1
        else:
            pov "You're welcome kid."
            $ morale += 1
    $ academics += 1
    return


label library21:
    
    scene bg library21-1 with fade
    "The library can be a good place for a secret rendezvous."
    scene bg library21-2
    "See, I told you, books get people closer."
    $ inhibition -= 1
    return


label library22:
    
    scene bg library22 with fade
    "It's nice to see the students study hard before their sex-ed class."
    $ deviance += 1
    return


label library23:
    
    scene bg library23 with fade
    "Oh I'm sorry, am I disturbing you?"
    $ academics -= 1
    return


label library24:
    
    scene bg library24:
        pos (0.0, 0.0)
        linear 10.0 pos (0.0, -1.5)
        linear 8.6 pos (0.0, -0.2)
    with fade
    "The library can be a true sanctuary in an otherwise stressful environment."
    $ morale += 1
    return


label library25:
    
    scene bg library25 with fade
    "It's important to keep your voice down unless you want to disturb the other students."
    guy "Keep. Your. Voice. Down."
    girl "*sob*"
    $ deviance += 1
    $ morale -= 1
    return


label library26:
    
    scene bg library26-1 with fade
    "A couple of students have gotten themselves really comfortable between the aisles."
    menu:
        "I don't want to see this.":
            "You decide to let them go on without disturbances."
        
        "This is kind of hot!":
            "You decide to stay for a few more seconds to see if it escalates."
            scene bg library26-2
            "They try to keep as quiet as possible but soon get caught up by their swelling emotions. The girl mounts her friend and gives him both a sexy ride and a nice view. "
            boy "I-I think I'm gonna..."
            girl "No! Not inside me!"
            "You decide to leave before the mess is a fact."
            $ deviance += 1
            $ behavior -= 1
    return


label library27:
    
    scene bg library27 with fade
    if renpy.random.randint(1,2) == 1:
        "A few uncertain steps towards your secret crush can sometimes end with a lovely scene."
        $ morale += 1
    else:
        "Sometimes the privacy and silence of the library is exactly what a student need."
        $ inhibition -= 1
    return


label library28:
    
    scene bg library28 with fade
    if renpy.random.randint(1,2) == 1:
        "Seems like the latest trend is for students have to take some risque photos of themselves."
        $ inhibition -= 1
    else:
        "Showing a little skin might be a bit near the knuckle, but I will leave her alone for now."
        $ morale += 1
    return
    
    
label library29:
    
    scene bg library29-1 with fade
    girl "Hello there [povTitle] [povLastName], would you like to give me a hand?"
    menu:
        "Ignore her and walk away.":
            "You can see her pout while you slowly walk away."
            $ morale -= 1
        
        "Sure, what can I do for you?":
            if deviance < 80:
                $ topic = random_topic("academics")
                girl "Well do you know anything about [topic]?"
                "You decide to help out the girl as good as you can."
                $ academics += 1
            
            else:
                girl "Well... Maybe you could take a look at this?"
                scene bg library29-2
                menu:
                    "Hey hey, stop it!":
                        girl "..."
                        pov "You can't go showing yourself like that."
                        girl "Ok..."
                        $ deviance -= 1

                    "That certainly looks good.":
                        girl "*giggle* It does?"
                        pov "...Indeed."
                        girl "You want a taste?"
                        pov "Sorry little miss, I am the principal after all."
                        girl "Aww, okay..."
                        $ inhibition -= 1

                    "I know what you want!":
                        girl "*giggle* I know you do!"
                        pov "Here goes!"
                        girl "Ah!"
                        scene black with fade
                        if deviance > 50:
                            "You give both her ass and pussy a massive pounding before you cum all over her."
                            girl "Ahhh!"
                        else:
                            "You quickly penetrate her tight young pussy and fill her up, hopefully before anyone saw you."
                        girl "Mhmm...."
                        $ deviance += 1
    return


label library30:
    
    scene bg library30-1 with fade
    $ topic = random_topic("academics")
    "This student seems really captivated by her book, it seems like the money spent on the library was a good idea."
    $ inhibition -= 1

    girl "Well do you know anything about [topic]?"
    return


label library31:
    
    scene bg library31 with fade
    $ topic = random_topic("academics")
    "Installing computers in the library seems to have been a great idea. Now students spend even more time studying [topic]!"
    return

