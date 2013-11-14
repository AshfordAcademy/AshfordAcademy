image bg sports_field1 = "screens/sports_field/sports_field1.jpg"
image bg sports_field2 = "screens/sports_field/sports_field2.jpg"
image bg sports_field3 = "screens/sports_field/sports_field3.jpg"
image bg sports_field4-1 = "screens/sports_field/sports_field4-1.jpg"
image bg sports_field4-2 = "screens/sports_field/sports_field4-2.jpg"
image bg sports_field4-3 = "screens/sports_field/sports_field4-3.jpg"
image bg sports_field4-4 = "screens/sports_field/sports_field4-4.jpg"
image bg sports_field4-5 = "screens/sports_field/sports_field4-5.jpg"
image bg sports_field5 = "screens/sports_field/sports_field5.jpg"
image bg sports_field6 = "screens/sports_field/sports_field6.jpg"
image bg sports_field7 = "screens/sports_field/sports_field7.jpg"
image bg sports_field8 = "screens/sports_field/sports_field8.jpg"
image bg sports_field9 = "screens/sports_field/sports_field9.jpg"
image bg sports_field10 = "screens/sports_field/sports_field10.jpg"
image bg sports_field11 = "screens/sports_field/sports_field11.jpg"
image bg sports_field12_1 = "screens/sports_field/sports_field12-1.jpg"
image bg sports_field12_2 = "screens/sports_field/sports_field12-2.jpg"
image bg sports_field13-1 = "screens/sports_field/sports_field13-1.jpg"
image bg sports_field13-2 = "screens/sports_field/sports_field13-2.jpg"
image bg sports_field13-3 = "screens/sports_field/sports_field13-3.jpg"
image bg sports_field13-4 = "screens/sports_field/sports_field13-4.jpg"
image bg sports_field13-5 = "screens/sports_field/sports_field13-5.jpg"
image bg sports_field13-6 = "screens/sports_field/sports_field13-6.jpg"
image bg sports_field14_1 = "screens/sports_field/sports_field14-1.jpg"
image bg sports_field14_2 = "screens/sports_field/sports_field14-2.jpg"
image bg sports_field15 = "screens/sports_field/sports_field15.jpg"
image bg sports_field16 = "screens/sports_field/sports_field16.jpg"
image bg sports_field17 = "screens/sports_field/sports_field17.jpg"
image bg sports_field18_1 = "screens/sports_field/sports_field18-1.jpg"
image bg sports_field18_2 = "screens/sports_field/sports_field18-2.jpg"
image bg sports_field19 = "screens/sports_field/sports_field19.jpg"
image bg sports_field20 = "screens/sports_field/sports_field20.jpg"
image bg sports_field21 = "screens/sports_field/sports_field21.jpg"
image bg sports_field22 = "screens/sports_field/sports_field22.jpg"
image bg sports_field23-1 = "screens/sports_field/sports_field23-1.jpg"
image bg sports_field23-2 = "screens/sports_field/sports_field23-2.jpg"
image bg sports_field24 = "screens/sports_field/sports_field24.jpg"
image bg sports_field25-1 = "screens/sports_field/sports_field25-1.jpg"
image bg sports_field25-2 = "screens/sports_field/sports_field25-2.jpg"
image bg sports_field26-1 = "screens/sports_field/sports_field26-1.jpg"
image bg sports_field26-2 = "screens/sports_field/sports_field26-2.jpg"
image bg sports_field27 = "screens/sports_field/sports_field27.jpg"
image bg sports_field28 = "screens/sports_field/sports_field28.jpg"
image bg sports_field29 = "screens/sports_field/sports_field29.jpg"
image bg sports_field30 = "screens/sports_field/sports_field30.jpg"
image bg sports_field31 = "screens/sports_field/sports_field31.jpg"
image bg sports_field32 = "screens/sports_field/sports_field32.jpg"
image bg sports_field33-1 = "screens/sports_field/sports_field33-1.jpg"
image bg sports_field33-2 = "screens/sports_field/sports_field33-2.jpg"
image bg sports_field34 = "screens/sports_field/sports_field34.jpg"

init:
    if persistent.mod_disable_original_events == False:
        $ event("sports_field1", "act == 'sports_field' and deviance < 5", event.choose_one('sports_field'), priority=200)
        $ event("sports_field2", "act == 'sports_field' and deviance < 5 and athletics < 25", event.choose_one('sports_field'), priority=200)
        $ event("sports_field3", "act == 'sports_field' and deviance < 5", event.choose_one('sports_field'), priority=200)
        $ event("sports_field4", "act == 'sports_field' and deviance >= 50 and inhibition <= 80", event.once(), priority=160)
        $ event("sports_field5", "act == 'sports_field' and deviance >= 15 and inhibition <= 80", event.choose_one('sports_field'), priority=180)
        $ event("sports_field6", "act == 'sports_field' and morale >= 10", event.choose_one('sports_field'), priority=190)
        $ event("sports_field7", "act == 'sports_field' and deviance > 5", event.choose_one('sports_field'), priority=180)
        $ event("sports_field8", "act == 'sports_field' and inhibition <= 95", event.choose_one('sports_field'), priority=190)
        $ event("sports_field9", "act == 'sports_field' and deviance > 5", event.choose_one('sports_field'), priority=180)
        $ event("sports_field10", "act == 'sports_field' and deviance > 5", event.choose_one('sports_field'), priority=180)
        $ event("sports_field11", "act == 'sports_field' and inhibition > 95", event.choose_one('sports_field'), priority=200)
        $ event("sports_field12", "act == 'sports_field' and athletics < 50", event.choose_one('sports_field'), priority=200)
        $ event("sports_field13", "act == 'sports_field' and deviance > 55 and behavior < 45", event.choose_one('sports_field'), priority=150)
        $ event("sports_field14", "act == 'sports_field' and athletics > 20", event.choose_one('sports_field'), priority=180)
        $ event("sports_field15", "act == 'sports_field' and behavior > 35", event.choose_one('sports_field'), priority=180)
        $ event("sports_field16", "act == 'sports_field' and (athletics < 45 or behavior < 45)", event.choose_one('sports_field'), priority=180)
        $ event("sports_field17", "act == 'sports_field' and athletics < 50 and behavior < 50 and deviance > 5", event.choose_one('sports_field'), priority=180)
        $ event("sports_field18", "act == 'sports_field' and athletics > 45", event.choose_one('sports_field'), priority=170)
        $ event("sports_field19", "act == 'sports_field' and deviance > 20 and inhibition < 90", event.choose_one('sports_field'), priority=150)
        $ event("sports_field20", "act == 'sports_field' and (inhibition < 50 or uniform == 'nude_uniform')", event.choose_one('sports_field'), priority=150)
        $ event("sports_field21", "act == 'sports_field' and deviance > 5", event.choose_one('sports_field'), priority=160)
        $ event("sports_field22", "act == 'sports_field' and inhibition < 90", event.choose_one('sports_field'), priority=160)
        $ event("sports_field23", "act == 'sports_field' and athletics > 40", event.choose_one('sports_field'), priority=160)
        $ event("sports_field24", "act == 'sports_field' and athletics > 55", event.choose_one('sports_field'), priority=140)
        $ event("sports_field25", "act == 'sports_field' and inhibition < 100", event.choose_one('sports_field'), priority=170)
        $ event("sports_field26", "act == 'sports_field' and inhibition > 70", event.choose_one('sports_field'), priority=170)
        $ event("sports_field27", "act == 'sports_field' and inhibition < 90 and athletics > 50", event.choose_one('sports_field'), priority=170)
        $ event("sports_field28", "act == 'sports_field' and athletics < 50", event.choose_one('sports_field'), priority=170)
        $ event("sports_field29", "act == 'sports_field' and athletics > 50", event.choose_one('sports_field'), priority=150)
        $ event("sports_field30", "act == 'sports_field' and athletics > 40 and inhibition < 95", event.choose_one('sports_field'), priority=180)
        $ event("sports_field31", "act == 'sports_field' and athletics > 45 and inhibition < 100 and inhibition > 75", event.choose_one('sports_field'), priority=180)
        $ event("sports_field32", "act == 'sports_field' and inhibition < 100 and inhibition > 75", event.choose_one('sports_field'), priority=180)
        $ event("sports_field33", "act == 'sports_field' and inhibition > 20", event.choose_one('sports_field'), priority=180)
        $ event("sports_field34", "act == 'sports_field' and morale > 75 and inhibition > 50", event.choose_one('sports_field'), priority=160)
    
label sports_field1:
    
    scene bg sports_field1 with fade
    pov "You see a cute girl running. She's really athletic."
    $ athletics += 1
    return


label sports_field2:
    
    scene bg sports_field2 with fade
    pov "You follow this cute cat until you meet some even cuter girls."
    $ morale += 1
    $ athletics += 1
    return


label sports_field3:
    
    scene bg sports_field3 with fade
    "You see a bunch of students fooling around during class."
    $ morale += 1
    $ behavior += 1
    return


label sports_field4:
    
    scene bg sports_field4-1 with fade
    "In the distance you see someone alone near a tree."
    pov "Hello there, are you okay?"
    "As you walk closer you see a girl tied up to a tree."
    pov "Hey, are you okay? What happened?"
    girl "..."
    girl "Nothing..."
    pov "It's clearly something, you are tied up to a tree young girl."
    girl "Well... I just joined the running team and all the newbies have to do this."
    pov "That's not very nice, is it?"
    "You take a good look at her figure. She's cute."
    girl "..."
    girl "If I leave this tree I will never be able to join the running team!"
    pov "But I just can't leave you like this, what if something would happen?"
    girl "No... Don't worry..."
    girl "They said they would be back at the end of next class."
    "That's at least 45 minutes away. Can I really leave her like this?"
    girl "Please [povTitle] [povLastName], just go."
    "Maybe I could have some fun with her. Her friends won't be back for a while and no one would believe her if she said that I was here."
    menu:
        "Leave her and walk away.":
            jump sports_field4_end
        
        "Well, a bit of fun never hurt anyone.":
            jump sports_field4_rape


label sports_field4_end:
    "You look into her eyes and really hope nothing bad will happen to her."
    pov "Alright, but you make sure to scream as much as you can if anything happens, ok?"
    girl "Yeah, okay, thank you [povTitle] [povLastName]!"
    $ athletics += 1
    $ morale += 1
    $ green_orb += 1
    return


label sports_field4_rape:
    scene bg sports_field4-1
    pov "I'm sorry, I can't leave you like this. But I can keep you company for a while."
    girl "..."
    girl "I guess that's ok..."
    pov "I think so too. So why don't we get to know each other a bit better?"
    "You walk towards her while you inspect her body."
    girl "Umm... Eh?"
    "You can't wait to see more of this young girl. This looks promising."
    pov "Don't worry, I'll be gentle."
    girl "Huh?! [povTitle] [povLastName] what do you mean?!"
    "You can clearly hear the distress in her voice."
    girl "[povTitle] [povLastName], what are you doing?!"
    "She reacted quite strongly when you just put your hand on her."
    girl "Ah!"
    pov "You want no one to know I was here right?"
    pov "Then you have to keep your voice down. You don't want to bring the wrong kind of attention do you?"
    girl "Umm, eh..."
    "You feel it's time to let those breasts breathe a bit."
    
    scene bg sports_field4-2
    girl "Ahh!"
    "You stroke her breast with your hand."
    girl "Ah! You can't touch me like that!"
    pov "Oh but I can."
    "It looks like she is getting close to tears."
    pov "You have a really great body young girl. I like it."
    "As you end your sentence you pinch one of her nipples."
    girl "Ah... Are...you... Mhmm... going to... rape..."
    "It's fantastic that you can get her to let out a small moan while asking that question."
    girl "...me?"
    pov "No, no, you are here alone right?"
    pov "Wait, let me help you get free."
    girl "Huh?!"
    "You loosen the knots but make sure they stay around her. It seems like her hands where also already bound. That's good, then you don't have to."
    girl "Are you releasing me?"
    "She looks very confused."
    pov "Yeah, didn't you want that?"
    girl "Well, yes... but... no... I..."
    pov "Is that a no? Then I'll take you as my pet!"
    "As you still have her bound by the rope you pull her close."
    
    scene bg sports_field4-3
    girl "Ah!"
    pov "Well now, be a good pet and do as I say."
    girl "Eh? Umm... But..."
    pov "Down on you knees."
    girl "Wait! Wait!"
    pov "Down on you knees. Now."
    girl "No, I mean, why, you said..."
    "It's a fun game this, but you know those other girls might be on their way so it's better to get going."
    "You keep fondling her breast until you pull down your pants."
    girl "Oh, no please, please [povTitle] [povLastName]! *sob* Don't do this, don't rape me! Please!"
    "She is about to panic. Oh well, that's not your problem."
    pov "Well, as I said, I'll be gentle."
    "The only thing you do is push a bit of clothing to the side and put a bit of meat inside."
    
    scene bg sports_field4-4
    girl "Ahhhh!"
    "It's a great tight experience. You clearly remember why you love these young girls."
    girl "Ah, mhmm, ah, why... ah, why me..?"
    pov "Well, I was out walking-"
    "You push into her deeper"
    girl "AH!"
    girl "Plea-"
    pov "And then I see this young cute girl all tied up-"
    "Her tight vagina is pulsating around your penis. You pull it out a bit."
    pov "And I wanted to help her, but no, no no, she would rather be tied up in the forest and be raped by a stranger-"
    girl "AHHH!"
    girl "No, you don't... AH! have to... Mhmm... do this!"
    pov "Well, it's better me than some stranger, right?"
    girl "*sob*"
    "Her tight body is really making it really hard not to cum. And still, you wanted to play just a few more minutes with her."
    "You take a good grip of her breast and push in just one last time before you fill her with your cum."
    
    scene bg sports_field4-5
    "You feel how it pours into her, leaving you powerless."
    girl "*sob*"
    pov "You were great. Was it as good for you?"
    girl "..."
    pov "Naww, did your mind wander off? Can't handle a bit of fun?"
    girl "..."
    girl "*sob*"
    "She stares at you. A blank, soulless stare. Even that makes her look cute."
    "You put her back somewhat as you found her before you leave."
    $ evil_points +=1
    $ morale -= 1
    $ red_orb += 1
    $ deviance += 1
    return


label sports_field5:
    
    scene bg sports_field5 with fade
    pov "A girl is taking a breather while teasing both you and the boys in her class."
    $ inhibition -= 1
    return

label sports_field6:
    
    scene bg sports_field6 with fade
    pov "Some people enjoy playing tennis while others enjoy watching."
    $ morale += 1
    $ athletics += 1
    return


label sports_field7:
    
    scene bg sports_field7 with fade
    pov "Anyone up for a double?"
    $ athletics += 1
    return


label sports_field8:
    
    scene bg sports_field8 with fade
    pov "You stop by the tennis court to talk to a girl who seems to be looking for some balls."
    $ deviance += 1
    return


label sports_field9:
    
    scene bg sports_field9 with fade
    "Hard work makes your body produce all kinds of substances."
    $ deviance += 1
    return


label sports_field10:
    
    scene bg sports_field10 with fade
    girl "Oh!"
    menu:
        "Are you alright?":
            girl "... Yes. I just didn't expect anyone to be right behind me."
            return
            
        "I'm sorry, I didn't mean to sneak up on you like that.":
            $ morale += 1
            girl "Ah, It's ok. Haha, I was just so focused that I totally didn't see you!"
            return

        "Close your mouth." if new_game_plus == True:
            $ morale -= 1
            girl "Huh?"
            pov "You look ridiculous when it's wide open like that."
            girl "..."
            return


label sports_field11:
    
    scene bg sports_field11 with fade
    "Tennis is quite popular among the girls. This particular girl wasn't expecting spectators though."
    return


label sports_field12:
    
    $ randImg = renpy.random.choice(["1", '2'])
    $ renpy.show("bg sports_field12_"+randImg)
    with fade
    "It's all about focus."
    $ athletics += 1
    return

    
label sports_field13:
    
    scene bg sports_field13-1 with fade
    girl "Hey, stop fooling around!"
    guy "He he, why? It's only a bit of fun, ain't it?"
    girl "Please, I have to go..."
    guy "Oh sure..."
    scene bg sports_field13-2
    girl "WHA?! Cut it out, I warn you!"
    guy "Ooo, I'm so scared!"
    girl "Stop it right now!"
    scene bg sports_field13-3
    girl "What the fuck!?! S.T.O.P!"
    guy "Relax, whe're only joking with ya."
    "One girl against three boys, it can only end in one way."
    scene bg sports_field13-4
    girl "N- NO! *gasp * I don't want to!"
    guy "Shut it! Or I'll fucking make you regret it."
    girl "* gulp *"
    scene bg sports_field13-5
    guy "Such a filthy whore, give her what she wants."
    girl "... please... don't..."
    scene bg sports_field13-6
    guy "Aaaaah!!"
    girl "* sob * No... no... I... * whimper *"
    "Good old mother nature."
    $ reputation -= 1
    $ morale -= 2
    $ behavior -= 1
    return


label sports_field14:
    $ randImg = renpy.random.choice(["1", '2'])
    $ renpy.show("bg sports_field14_"+randImg)
    with fade

    if renpy.random.randint(1,2) == 1:
        "A fit looking girl is just about to join her P.E. class."
    else:
        "It's always nice to see a girl keeping herself fit."
    $ morale += 1
    return


label sports_field15:

    scene bg sports_field15 with fade
    "Seems like we are trusting our students with deadly weapons these days.\nOh well, I hope no one gets hurt."
    $ athletics += 1
    return


label sports_field16:

    scene bg sports_field16 with fade
    "They must be quite clumsy to succeed with that."
    menu:
        "Give them a hand":
            "They thank you and then try to fix their mess."
        
        "Laugh at them":
            "They get really embarrassed and one of the girls starts to cry.\nStupid students."
            $ morale -= 1
    $ athletics -= 1
    return


label sports_field17:

    scene bg sports_field17 with fade
    "Somehow this poor girl got herself into a mess, and at the same time she shows off almost everything. A good view indeed."
    if renpy.random.randint(1,3) == 1:
        "You decide to give her a hand and help her out."
        if deviance < 15:
            girl "Thanks [povTitle] [povLastName]."
            $ morale += 1
        else:
            girl "Don't you like your girls tied up?"
            "Before you have the time to react she smiles and walks away."
            $ inhibition -= 1
    return


label sports_field18:
    $ randImg = renpy.random.choice(["1", '2'])
    $ renpy.show("bg sports_field18_"+randImg)
    with fade

    if renpy.random.randint(1,3) == 1:
        "Some of our students are really good athletes!"
    elif renpy.random.randint(1,2) == 1:
        pov "That's how you do it!"
    else:
        pov "You go girl!"

    $ athletics += 1
    return


label sports_field19:
    scene bg sports_field19 with fade

    if renpy.random.randint(1,3) == 1:
        "This girl is panting quite heavily for just jogging around."
        $ athletics += 1
    elif renpy.random.randint(1,2) == 1:
        "You hear a faint buzz, maybe someone's phone is ringing?"
        $ inhibition -= 1
    else:
        "That's one way to make P.E. more interesting."
        $ deviance += 1
    return


label sports_field20:
    
    scene bg sports_field20 with fade
    if uniform == "nude_uniform":
        if renpy.random.randint(1,2) == 1:
            "Seems like some girls are still a bit shy about being nude in public."
        else:
            "She seems to have a hard time playing tennis when all eyes are focused on her juggling boobs."
    
    elif renpy.random.randint(1,2) == 1:
        "She would beat me in tennis any day."
    else:
        "Those big beautiful... blue eyes."
    $ athletics -= 1
    return


label sports_field21:

    scene bg sports_field21 with fade
    "She seems to have an itch, maybe she should try a different fabric?"
    $ inhibition -= 1
    return


label sports_field22:

    scene bg sports_field21 with fade
    "While working hard to stay in shape, try to vary your training methods."
    $ athletics += 1
    return


label sports_field23:

    scene bg sports_field23-1 with fade
    "Physical exercise will help keep your mind as well as your body fit."
    scene bg sports_field23-2
    "She pushes herself harder every time, don't you girl?"
    $ athletics += 1
    return


label sports_field24:

    scene bg sports_field24 with fade
    "Sometimes it doesn't matter if you're a boy or a girl, a winner is still a winner."
    $ athletics += 1
    return


label sports_field25:

    scene bg sports_field25-1 with fade
    girl "Oh! Hello there [povTitle] [povLastName], I was just stretching my legs."
    pov "I can see that..."
    if deviance > 5:
        girl "You look like you'd like to see more?"
        pov "Well, I do enjoy a good stretch now and then."
        girl "You brute! If you promise to keep it a secret..."
        pov "Oh I promise..."
        girl "*giggle*"
        scene bg sports_field25-2
        girl "My, it's really hot today, isn't it?"
        pov "If you only knew..."
        girl "So refreshing with a bit of fresh air, don't you think?"
        pov "*swallow*"
        if renpy.random.randint(1,2) == 1:
            $ deviance += 1
        else:
            $ inhibition -= 1
    return


label sports_field26:

    scene bg sports_field26-1 with fade
    pov "Naw, did you fall?"
    girl "I-I just thought that hurdles was my forte..."
    if deviance > 0:
        pov "I see..."
        scene bg sports_field26-2
        girl "Yikes!"
        pov "Oh yes, I see those too..."
        girl "It's the worst day ever!"
        $ inhibition += 1
    return


label sports_field27:

    scene bg sports_field27 with fade
    "If you work hard, only the sky's the limit!"
    $ athletics += 1
    return


label sports_field28:

    scene bg sports_field28 with fade
    if renpy.random.randint(1,2) == 1:
        "Progress is all about focus."
    else:
        "You go girl!" 
    $ athletics += 1
    return


label sports_field29:

    scene bg sports_field29:
        pos (0.0, 0.0)
        linear 7.5 pos (0.0, -1.0)
        linear 7.0 pos (0.0, -0.1)
    with fade
    if povGender == 'male':
        if renpy.random.randint(1,2) == 1:
            "That's a ball girl in my taste."
        else:
            "She sure got her hands on some good balls."
    else:
        "Not every student can be the class ace, but luckily a fine ball girl is always needed."
    $ athletics += 1
    return


label sports_field30:

    scene bg sports_field30 with fade
    if renpy.random.randint(1,2) == 1:
        "Seems like some girls are getting interested in the school's soccer team."
        $ athletics += 1
    else:
        "Not all guys know how to act when I a cute girl hit on you."
        $ inhibition -= 1
    return


label sports_field31:

    scene bg sports_field31 with fade
    if renpy.random.randint(1,2) == 1:
        "Keeping fit is good for both body and mind."
    else:
        if deviance > 5 and povGender == "male":
            "Tight clothes and young bodies, that's how I like it."
        else:
            pov "Don't looks so surprised, I like to take a walk sometimes. "
    $ athletics += 1
    return


label sports_field32:

    scene bg sports_field32 with fade
    if renpy.random.randint(1,2) == 1:
        "It's important to keep hydrated when you train hard."
        $ athletics += 1
    else:
        "Some girls don't mind showing some panties or fail to notice they do."
        $ inhibition -= 1
    return


label sports_field33:

    if athletics > 45:
        scene bg sports_field33-1 with fade
        if renpy.random.randint(1,2) == 1:
            "It's great to see our students pushing it to the max."
        else:
            "Keep on running, you never know whats behind you."
        $ athletics += 1
    else:
        scene bg sports_field33-2 with fade
        "Not all students train enough to call themselves athletes."
    return


label sports_field34:

    scene bg sports_field34 with fade
    if renpy.random.randint(1,2) == 1:
        "Seems like two out of three are having a great time!"
        $ morale += 1
    else:
        "Is that a cry of fear or happiness? Girls can be so confusing."
        $ behavior -= 1

