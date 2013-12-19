image bg gym1 = "locations/gym/gym1.jpg"
image bg gym2_1 = "locations/gym/gym2-1.jpg"
image bg gym2_2 = "locations/gym/gym2-2.jpg"
image bg gym3 = "locations/gym/gym3.jpg"
image bg gym4 = "locations/gym/gym4.jpg"
image bg gym5_1 = "locations/gym/gym5-1.jpg"
image bg gym5_2 = "locations/gym/gym5-2.jpg"
image bg gym5_3 = "locations/gym/gym5-3.jpg"
image bg gym6 = "locations/gym/gym6.jpg"
image bg gym7 = "locations/gym/gym7.jpg"
image bg gym8_1 = "locations/gym/gym8-1.jpg"
image bg gym8_2 = "locations/gym/gym8-2.jpg"
image bg gym9 = "locations/gym/gym9.jpg"
image bg gym10_1 = "locations/gym/gym10-1.jpg"
image bg gym10_2 = "locations/gym/gym10-2.jpg"
image bg gym10_3 = "locations/gym/gym10-3.jpg"
image bg gym11 = "locations/gym/gym11.jpg"
image bg gym12 = "locations/gym/gym12.jpg"
image bg gym13 = "locations/gym/gym13.jpg"
image bg gym14 = "locations/gym/gym14.jpg"
image bg gym15 = "locations/gym/gym15.jpg"
image bg gym16 = "locations/gym/gym16.jpg"
image bg gym17 = "locations/gym/gym17.jpg"
image bg gym18 = "locations/gym/gym18.jpg"
image bg gym19-1 = "locations/gym/gym19-1.jpg"
image bg gym19-2 = "locations/gym/gym19-2.jpg"
image bg gym19-3 = "locations/gym/gym19-3.jpg"
image bg gym20_1 = "locations/gym/gym20-1.jpg"
image bg gym20_2 = "locations/gym/gym20-2.jpg"
image bg gym21 = "locations/gym/gym21.jpg"
image bg gym22 = "locations/gym/gym22.jpg"
image bg gym23-1 = "locations/gym/gym23-1.jpg"
image bg gym23-2 = "locations/gym/gym23-2.jpg"
image bg gym23-3 = "locations/gym/gym23-3.jpg"
image bg gym23-4 = "locations/gym/gym23-4.jpg"
image bg gym23-5 = "locations/gym/gym23-5.jpg"
image bg gym23-6 = "locations/gym/gym23-6.jpg"
image bg gym24 = "locations/gym/gym24.jpg"
image bg gym25-1 = "locations/gym/gym25-1.jpg"
image bg gym25-2 = "locations/gym/gym25-2.jpg"
image bg gym25-3 = "locations/gym/gym25-3.jpg"
image bg gym26 = "locations/gym/gym26.jpg"
image bg gym27 = "locations/gym/gym27.jpg"
image bg gym28 = "locations/gym/gym28.jpg"

init:
    if persistent.mod_disable_original_events == False:
        $ event("gym1", "act == 'gym' and athletics < 25", event.choose_one('gym'), priority=200)
        $ event("gym2", "act == 'gym' and inhibition > 75", event.choose_one('gym'), priority=200)
        $ event("gym3", "act == 'gym' and inhibition > 85", event.choose_one('gym'), priority=200)
        $ event("gym4", "act == 'gym'", event.choose_one('gym'), priority=200)
        $ event("gym5", "act == 'gym' and inhibition > 75", event.choose_one('gym'), priority=200)
        $ event("gym6", "act == 'gym' and athletics > 25", event.choose_one('gym'), priority=190)
        $ event("gym7", "act == 'gym' and inhibition > 85", event.choose_one('gym'), priority=200)
        $ event("gym8", "act == 'gym' and athletics < 20", event.choose_one('gym'), priority=200)
        $ event("gym9", "act == 'gym' and inhibition < 75", event.choose_one('gym'), priority=190)
        $ event("gym10", "act == 'gym' and inhibition < 90", event.choose_one('gym'), priority=190)
        $ event("gym11", "act == 'gym' and inhibition < 60 and deviance > 40", event.choose_one('gym'), priority=180)
        $ event("gym12", "act == 'gym' and deviance > 5 and behavior < 15", event.choose_one('gym'), priority=190)
        $ event("gym13", "act == 'gym' and inhibition < 80", event.choose_one('gym'), priority=180)
        $ event("gym14", "act == 'gym' and deviance > 30", event.choose_one('gym'), priority=170)
        $ event("gym15", "act == 'gym' and deviance > 10", event.choose_one('gym'), priority=180)
        $ event("gym16", "act == 'gym' and inhibition > 75", event.choose_one('gym'), priority=190)
        $ event("gym17", "act == 'gym' and deviance > 25", event.choose_one('gym'), priority=170)
        $ event("gym18", "act == 'gym' and deviance > 15 and inhibition < 80", event.choose_one('gym'), priority=170)
        $ event("gym19", "act == 'gym' and inhibition < 80", event.choose_one('gym'), priority=170)
        $ event("gym20", "act == 'gym' and deviance > 20", event.choose_one('gym'), priority=150)
        $ event("gym21", "act == 'gym' and athletics < 40", event.choose_one('gym'), priority=150)
        $ event("gym22", "act == 'gym' and inhibition > 70 and inhibition < 95", event.choose_one('gym'), priority=150)
        $ event("gym23", "act == 'gym' and deviance > 15", event.once(), event.depends("class41"), priority=150)
        $ event("gym24", "act == 'gym' and athletics < 50",event.choose_one('gym'), priority=190)
        $ event("gym25", "act == 'gym' and total_days > 50", event.once(), priority=150)
        $ event("gym26", "act == 'gym' and pda_rules == 'pda_bdsm' and behavior < 50", event.once(), priority=150)
        $ event("gym27", "act == 'gym' and inhibition < 5 and deviance > 95", event.choose_one('gym'), priority=100)
        $ event("gym28", "act == 'gym' and inhibition < 85", event.choose_one('gym'), priority=180)
        
label gym1:
    
    scene bg gym1 with fade
    pov "Are you alright? If you've hurt yourself you should see the nurse."
    $ athletics -= 1
    return


label gym2:
    
    $ randImg = renpy.random.choice(["1", "2"])
    $ renpy.show("bg gym2_"+randImg)
    with fade
    "Hmm. It seems like this girl doesn't really care much for your attention."
    $ morale -= 1
    return


label gym3:
    
    scene bg gym3 with fade
    "You see a girl getting ready for P.E."
    $ athletics += 1
    return


label gym4:
    
    scene bg gym4 with fade
    "A girl tripped and fell down. Poor thing, but it did give you quite a nice view."
    $ athletics += 1
    return


label gym5:
    
    $ randImg = renpy.random.choice(["1", "2", "3"])
    $ renpy.show("bg gym5_"+randImg)
    with fade
    "You walked in on a girl changing her clothes after class. After a few seconds she starts screaming and you quickly run away."
    if renpy.random.randint(1,3) == 1:
        $ reputation -= 1
        $ morale -=1
    else:
        $ morale -=1
    return


label gym6:
    
    scene bg gym6 with fade
    info "As you enter the gym you see a friendly match of basket versus another school."
    if renpy.random.randint(0, 75) < athletics:
        "Wow, our school team pushed on and won this great match."
        $ athletics += 1
        $ morale += 1
    else:
        "In the end the other school won."
        $ morale -= 1
    return


label gym7:
    
    scene bg gym7 with fade
    if renpy.random.random() > 0.5:
        "When she notices your stare, she gives you an earnest look of distaste."
    else:
        "As she turns back and notices your interest, she gives you a cheeky look."
    $ athletics -= 1
    $ morale -= 1
    return


label gym8:
    
    $ randImg = renpy.random.choice(["1", "2"])
    $ renpy.show("bg gym8_"+randImg)
    with fade
    pov "Don't forget to stretch those muscles!"
    $ athletics += 1
    return


label gym9:
    
    scene bg gym9 with fade
    pov "If you don't remember to put on a sports bra before class, don't whine over embarrassing moments like this."
    $ athletics -= 1
    $ morale -= 1
    return


label gym10:
    
    $ randImg = renpy.random.choice(["1", "2", "3"])
    $ renpy.show("bg gym10_"+randImg)
    with fade
    "You run into a girl changing her clothes before class."
    girl "..."
    if inhibition > 80:
        menu:
            "I'm sorry, I didn't know this was the girls locker room.":
                girl "Ok..."
                "You leave and get the feeling that she saw right through you."
                if renpy.random.randint(1,3) == 1:
                    $ reputation -= 1
                else:
                    $ inhibition += 1
                    $ morale -= 1
            
            "Oh, pardon me but I'm conducting a walk through of all escape routes in case there's a fire.":
                girl "Oh, I was just..."
                pov "That's ok, how could you know?"
                "You exhale as you leave the room. The girl just stands there dumbfounded."
                $ inhibition -= 1
    else:
        pov "Is something wrong?"
        girl "No, not at all [povTitle] [povLastName]..."
        pov "Good girl."
        $ inhibition -= 1
    return


label gym11:
    
    scene bg gym11 with fade
    pov "Naughty girls gets the naughty treatment. That's the rules of the game."
    $ deviance += 1
    $ morale -= 1
    return
    

label gym12:
    
    scene bg gym12 with fade
    "It seems like some guys are giving the girls a hard time to the extent that they decide to hide during class."
    $ morale -= 1
    return


label gym13:
    
    scene bg gym13 with fade
    girl "Oh, hello there [povTitle] [povLastName]...\n...\nWould you mind some privacy?"
    menu:
        "Of course not.":
            "You turn around and leave quickly."
            
        "Would that include me?" if deviance <= 10:
            girl "Ha ha, you're so funny [povTitle] [povLastName], maybe next time."
            pov "Alright, see you next time."
            $ deviance += 1
        
        "Would that include me?" if deviance > 10 and deviance < 20:
            girl "I would really like that [povFirstName], but I'm in a hurry to class. \nSorry."
            pov "Aww, I hope to catch you again then."
            $ deviance += 1

        "Would that include me?" if deviance >= 20:
            girl "I guess a quickie wouldn't hurt, would you come over here?"
            "As you walk towards her you hear the sound of other students entering, you look into her eyes and swiftly run away before anyone sees you."
            $ deviance += 1
    return


label gym14:

    "As you get closer to the gym you hear a familiar sound."
    "Ahh... Mhmm... Ah!"
    scene bg gym14 with fade
    "You get a good sight of two students having sex on the gym floor."
    menu:
        "Let the young have their fun.":
            "You take a last look at them before you turn around walking away."
            $ inhibition -= 1
            $ deviance += 1
        
        "Give them a warning.":
            "You place your hand on the boy's shoulder and push him back, then order them into the office to lecture them about having sex on school grounds."
            "After lecturing them they seem very embarrassed and promise it will never happen again."
            $ inhibition += 1
            $ deviance -= 1

        "Expel them." if pda_rules == 'pda_expulsion':
            "You quickly step in and interrupt them while telling them to cover up."
            "As soon as they cover up their private parts you drag them to your office and sign the papers for their expulsion."
            $ inhibition += 2
            $ deviance -= 2
    return


label gym15:
    
    "As you get closer to the gym's changing rooms you hear a faint and familiar sound."
    "Mhmm..."
    scene bg gym15 with fade
    "As you enter the changing room you are greeted with a great view."
    girl "Mhmm, AH!"
    menu:
        "Oh, sorry":
            "Before she even said a thing you turn around and leave."
            $ inhibition += 1
            
        "Stop that!":
            girl "Ah!"
            pov "Stop that right now and go and get dressed."
            "With obedient eyes she covers herself as well as she can and walks away to the showers."
            $ deviance -= 1
            $ behavior += 1
            
        "Do you need a hand?" if deviance < 15:
            "When she hears your words she jumps and then tries to cover herself. With a trembling voice she says:"
            girl "Umm, you should leave..."
            "You leave quickly."
            $ deviance -= 1
            $ morale -= 1

        "Do you need a hand?" if deviance >= 15:
            "When she hears your words she looks at you with a smile and says:"
            girl "Umm, maybe I do..."
            "You slowly walk over to her and as you get closer you can see how the girl starts to breathe more heavily for every step you take."
            girl "Is this... really ok?"
            "You look deeply into her eyes and suddenly she says:"
            girl "Sorry, I can't!"
            "She then quickly spurts away."
            $ inhibition -= 1
    return


label gym16:
    
    scene bg gym16 with fade
    "Oops, you just walked into the girls changing room. Sure looks good, but they don't seem too happy about it."
    python:
        morale -= 1
        if renpy.random.randint(0,1) == 1:
            reputation -= 1
    return


label gym17:
    
    "In the locker room, you suddenly hear a squeaking noise. Carefully, you peek around the corner and see a young couple at it."
    scene bg gym17 with fade
    girl "Shh, I thought I heard something!"
    guy "Huh?"
    menu:
        "Stand real still":
            "After a while they carry on their business. You leave real silently."
            $ deviance += 1
            
        "Make some noise":
            "You knock on one of the lockers and hear how they quickly gather their clothes."
            $ deviance -= 1
            
        "Burp" if new_game_plus == True:
            girl "What the hell!?"
            guy "H- hello?"
            pov "* giggle *"
            $ deviance -= 1
    return


label gym18:
    
    scene bg gym18 with fade
    "It's important to wear the right bra for support, right girls?"
    $ morale -= 1
    $ inhibition -= 1
    return


label gym19:
    
    scene bg gym19-1 with fade
    "While at the gym, you decide to have a look at the standards of the locker rooms. While you don't wish to make a great fuss about your presence, a girl turns around just in the wrong moment."
    scene bg gym19-2
    "The standards are... eh... real good."
    scene bg gym19-3
    "She doesn't really know how to respond to this unexpected attention. You wink at her and leave."
    $ behavior -= 1
    $ inhibition -= 1
    return


label gym20:
    $ randImg = renpy.random.choice(["1", "2"])
    $ renpy.show("bg gym20_"+randImg)
    with fade
    "Looks like you arrived just in time to witness how the schools cheerleading actually works."
    if renpy.random.randint(1,2) == 1:
        $ morale += 1
    else:
        $ inhibition -= 1
    return
    

label gym21:
    
    scene bg gym21 with fade
    "The great thing about basketball is that everyone can participate!"
    $ athletics += 1
    return
    

label gym22:
    
    scene bg gym22 with fade
    "Two athletic femmes find your company less appreciated than you would imagine."
    $ morale -= 1
    $ inhibition -= 1
    return


label gym23:
    
    scene bg gym23-1 with fade
    "Just as you're about to enter basketball practice, you hear strange noises from the equipment store room."
    girl "I- I've done exactly as you said, it should be wide enough."
    "monitor" "It better be, for YOUR sake."
    girl "*gulp*"
    "Could this be the very same girl that fingered herself with some kind of toy during class some time ago?"
    "monitor" "Don't hold your breath cutie-pie, just relax."
    scene bg gym23-2
    girl "Aaah, careful!"
    "monitor" "Sure, I'll be really careful to ya, haha."
    scene bg gym23-3
    girl "S- stop, it's not wide enough!"
    "monitor" "Are you kiddin' me? It's wide enough to fit a baseball bat!"
    girl "..."
    scene bg gym23-4
    scene bg gym23-5
    scene bg gym23-6
    return


label gym24:

    scene bg gym24 with fade
    "If you just train hard enough, one day you might be strong enough to beat a boy!"
    $ athletics += 1
    return


label gym25:

    scene bg gym25-1 with fade
    "As you enter the girls locker room, you hear a faint sobbing. You move as quietly as you can and soon discover a girl taking a hot shower after practice."
    girl "I-I'll show them, I swear! One of these days anyway..."
    menu:
        "Better not let her see me.":
            "You sneak out as quietly as you came."
    
        "Stay a bit longer.":
            scene bg gym25-2
            girl "W-wha - Hey!"
            pov "Didn't mean to frighten you. I'll go if you think it's awkward."
            if morale > 40:
                girl "Gee, ya think?! Get out or I'll scream!"
                pov "Ok, ok, just keep it down."
                girl "Get out!"
                "You leave immediately, hoping she won't say anything to anyone."
                $ reputation -= 1
                $ morale -= 1
            else:
                girl "I-I don't... So unusual..."
                pov "Look, I just thought that whoever was in here sounded pretty sad. Is there something wrong?"
                girl "It's... it's stupid. I just..."
                pov "Hey, rainy face, it's ok. You can tell me."
                girl "It's so silly, nothing really..."
                pov "It was obviously making you feel sad, so it must be something."
                girl "*sob*"
                if good_points > 0:
                    scene bg gym25-3
                    "She can't hold back the tears, soon she cries uncontrollably. You decide to remain by her side for a little while, strictly supporting."
                    $ reputation += 1
                else:
                    pov "Was it something the other girls said?"
                    girl "I... I tried to..."
                    pov "Was it something about looks?"
                    girl "They just... they..."
                    pov "Was it about your breasts not being equally sized?"
                    girl "W-what? N-no it... it... are they not..?"
                    menu:
                        "You know, not everybody can be symmetric.":
                            pov "I'm sure the boys will think well of you anyway." 
                            scene bg gym25-3
                            girl "Whaaa! I just want them to like me for who I am!"
                            pov "But of course you do sweetie."
                            "You give her a compassionate smile and then head back to your office. You can hear the poor girl crying as you leave."
                        
                        "Hey, there's always surgery.":
                            pov "You do have wealthy parents, right?"
                            girl "W-what?! No, they... they can hardly afford-"
                            pov "Gee, that's too bad sister. I mean, just a little more filling, nipping and tucking..."
                            girl "A-am I THAT ugly?!"
                            pov "I wouldn't use the term ugly but..."
                            "Suddenly she gets a strange facial expression and sounds like she's got something stuck in her throat. Silent tears flow violently down her cheeks, blend with water and continue down her asymmetrical breasts."
                            pov "I'm sure I have a business card from a descent plastic surgeon somewhere round the office. He's no miracle worker though, so don't get your hopes up too high."
                            "When you leave, you feel like you've reached out and touched that poor girls soul. Such a noble act. Right before you close the door behind you, a sound rings through the otherwise empty locker room. Hmm, sounded almost like a dull, cracking sound. Must have been from the class next door, obviously a medicine ball hitting the wall."
                            $ evil_points += 1
    return


label gym26:
    scene bg gym26:
        pos (0.0, 0.0)
        linear 10.0 pos (0.0, -1.5)
        linear 3.3 pos (0.0, -1.0)
    with fade
    pov "You better behave next time or I will personally have to show you {i}BDSM detention{/i}."
    $ behavior += 1
    return


label gym27:
    scene bg gym27 with fade    
    if renpy.random.randint(1,2) == 1:
        "Everyone is equal when they are nude on the floor with sweat and cum on them."
        $ deviance += 1
    else:
        "Seems like you came just to late to be part of the party."
        $ inhibition -= 1
    return


label gym28:
    scene bg gym28 with fade    
    if renpy.random.randint(1,2) == 1:
        "Some girls gets quite flustered by playing basket."
    else:
        girl "Ah, did he look at me? *blush*"
    return
    
