##########################################################
#
#                       Kazuna Satoshi                      
#                          by clef
# 
#
##########################################################


# We use this variable to keep track of her feelings towards the player. 
define kazuna_satoshi_points = 0
define kazuna_satoshi_known = 0

init:
    define kazuna_dress = "dressed"  # it can be "dressed" or "nude" 

# Bg to be loaded.
image bg hallway = "screens/places/hallway.jpg"
image bg library = "screens/places/library.jpg"
image bg school_grounds = "screens/places/school_grounds.jpg"

# We load images to be shown and the variations.
image kazuna_satoshi dressed normal = "screens/story_screens/kazuna_satoshi/kazuna_normal.png"
image kazuna_satoshi dressed happy = "screens/story_screens/kazuna_satoshi/kazuna_happy.png"
image kazuna_satoshi dressed blush = "screens/story_screens/kazuna_satoshi/kazuna_blush.png"
image kazuna_satoshi dressed surprised = "screens/story_screens/kazuna_satoshi/kazuna_surprised.png"
image kazuna_satoshi nude normal = "screens/story_screens/kazuna_satoshi/kazuna_nude_normal.png"
image kazuna_satoshi nude happy = "screens/story_screens/kazuna_satoshi/kazuna_nude_happy.png"
image kazuna_satoshi nude blush = "screens/story_screens/kazuna_satoshi/kazuna_nude_blush.png"
image kazuna_satoshi nude surprised = "screens/story_screens/kazuna_satoshi/kazuna_nude_surprised.png"
image kazuna_satoshi dressed yell = "screens/story_screens/kazuna_satoshi/kazuna_yell.png"
image kazuna_satoshi nude yell = "screens/story_screens/kazuna_satoshi/kazuna_nude_yell.png"


# Here we define prefix used for us and what it will show to the player.
# Colors are written in hexadecimal. (FF0000 = Red, 00FF00 = Green, 0000FF = Blue)
define kazuna_satoshi = Character('Kazuna', color="#F8BA87")

# Here we make a list of all scenes with her. 
init:
    $ event("kazuna_satoshi_encounter1", "act == 'class' and total_days > 45 and kazuna_satoshi_points >= 0 and planning_day < 2", event.choose_one('class'), priority=195)
    $ event("kazuna_satoshi_encounter2", "act == 'library' and total_days > 45 and kazuna_satoshi_points >= 0 and planning_day == 3", event.choose_one('library'), priority=195)
    $ event("kazuna_satoshi_encounter3", "act == 'school_grounds' and total_days > 45 and kazuna_satoshi_points >= 0 and planning_day > 4", event.choose_one('school_grounds'), priority=195)
    $ event("kazuna_satoshi_encounter4", "act == 'school_grounds' and total_days > 45 and kazuna_satoshi_points >= 7 and kazuna_satoshi_known == 0", event.once(), event.choose_one('library'))
    # $ event("kazuna_satoshi_encounter5", "act == 'class' and kazuna_satoshi_points >= 3 and behavior > 20",event.once(),event.choose_one('class'))
    # event.once() makes sure it only viewable once.event.depends("kazuna_satoshi_in_class1") - this event must have been seen first.


# Here starts the actual scenes. The name in the list must match the ones below.

label kazuna_satoshi_encounter1:
    # add the encounter point.
    $ kazuna_satoshi_points += 1
    # the right bg is choosen
    if act == 'class':
        scene bg classroom with fade
    if act == 'office':
        scene bg hallway with fade
    
    # here are assembled the possible arguments they will talk about.
    $ kazuna_encounter1_arguments = ["casual"]   
    if academics > 50:
        $ kazuna_encounter1_arguments.append("intelligent")
    if artistery > 50:
        $ kazuna_encounter1_arguments.append("artistic")
    if inhibition < 55:
        $ kazuna_encounter1_arguments.append("talk_of_sex_loudly")
    if inhibition >= 55 and inhibition < 85:
        $ kazuna_encounter1_arguments.append("talk_of_sex")
    if inhibition > 85 and inhibition < 95:
        $ kazuna_encounter1_arguments.append("talk_of_kisses")



    if uniform == 'nude_uniform' and inhibition < 30:
        $ kazuna_dress = "nude"
    else:
        $ kazuna_dress = "dressed"

    if kazuna_satoshi_known == 0:
        $ speaker = girl
        if kazuna_dress == "nude":
            "While walking the beat, you run into some gossiping girls. Some of them are completely nude."
        else:
            "While walking the beat, you run into some gossiping girls."
    else:
        $ speaker = kazuna_satoshi
        if kazuna_dress == "nude":
            "Seems like Kazuna's really enjoying the Nude Uniform policy: you see her talking with some friends while showing off her curvaceous body."
        else:
            "You see Kazuna talking with some friends."     
    if renpy.random.randint(1, 3) == 1: 
        if behavior < 20:
            $ renpy.show("kazuna_satoshi "+kazuna_dress+" normal", at_list=[center]) 
            "As you get closer, a sense of loathing fills the air. \nGuess they don't appreciate your company."
            speaker "Oh... Prying around the girls as usual [povTitle] [povLastName]?"
            pov "Choose your words carefully missy. That's NOT the way to get favours around here."
            speaker "Oh ladida, I'll keep that in mind.\nCome on girls, let's go somewhere else."
            "What the hell!\nThese students really need to be disciplined."
        elif behavior > 60:
            $ renpy.show("kazuna_satoshi "+kazuna_dress+" happy", at_list=[center])
            "When you approach them they shine up."
            speaker "How are you doing [povTitle] [povLastName]?"
            "The girls are really nice and you feel important. "
            "As you leave, they assure you that they'll keep working hard. \nThe students at Ashford are really well educated."
        else:
            $ renpy.show("kazuna_satoshi "+kazuna_dress+" surprised", at_list=[center])
            "You decide to take a minute and give them some attention."
            pov "How's your day girls?"
            $ renpy.show("kazuna_satoshi "+kazuna_dress+" normal", at_list=[center])
            speaker "Hrm..."
            speaker "Good."
            "You try to keep up conversation for a while, but these girls are obviously not comfortable talking to you. \nYou decide to leave and return to your office."
            speaker "... Goodbye [povTitle] [povLastName]."
    else:
        if morale < 25:
            $ renpy.show("kazuna_satoshi "+kazuna_dress+" normal", at_list=[center])
            "You can tell from their faces that they're far from happy with school."
        if morale >= 25 and morale < 60:
            $ renpy.show("kazuna_satoshi "+kazuna_dress+" happy", at_list=[center])
            "They're happy to talk, guess they don't hate Ashford after all."
        if morale > 60:
            $ renpy.show("kazuna_satoshi "+kazuna_dress+" happy", at_list=[center])
            "They're laughing and joking together. These girls really enjoy Ashford."   
        $ kazuna_argument_outcome = renpy.random.choice(kazuna_encounter1_arguments)
        if kazuna_argument_outcome == "casual":
            $ ("Passing near them, you hear that they're talking about "+renpy.random.choice(["flowers and their perfume. ","their favourite type of holiday. "])+"ordinary boring stuff.")
        if kazuna_argument_outcome == "intelligent":
            "Passing near them, you hear that they're talking about their homework, looking for a solution to a tricky math problem."
            "These girls are really dedicated to their studies."
        if kazuna_argument_outcome == "artistic":
            "Passing near them, you hear that they're talking about an exhibition that will open in a few days."
            speaker "If you want, I can accompany you."
            "The students at Ashford really appreciate good art."
        if kazuna_argument_outcome == "talk_of_kisses":
            "Passing near them, you hear that they're talking about kisses."
            speaker "Oh, I thought you didn't like him!"
            "Some of the girls seem to be a bit bothered with the conversation."
        if kazuna_argument_outcome == "talk_of_sex":
            "Passing near them, you can hear that they're talking about sex. Some of them are comming off as really naughty. \nWell, that's just what you were aiming for, so it's good!"
        if kazuna_argument_outcome == "talk_of_sex_loudly":
            "You can hear them talk from afar since they're not even trying to be discrete."
            speaker "Yeah, I did him too. I'm two ahead of you now."
            "God, kids of today really don't have any dignity left!"
    return
        
        
label kazuna_satoshi_encounter2:  
    
    $ kazuna_satoshi_points += 1    
    scene bg library with fade

    if uniform == 'nude_uniform' and inhibition < 30:
        $ kazuna_dress = "nude"
    else:
        $ kazuna_dress = "dressed"

    if kazuna_satoshi_known == 0:
        $ speaker = girl
    else:
        $ speaker = kazuna_satoshi
    if academics < 30:
        "The library is almost empty today. Guess there are cooler places to hang out."
    elif academics > 70:
        "The library is really crowded, the students are working hard."
    else:
        "There's some serious studying going on here."
    "While you look around, a girl bumps into you."
    if behavior < 25:
        $ renpy.show("kazuna_satoshi "+kazuna_dress+" yell", at_list=[center])
        speaker "Pay attention to where you're going! *grumble* Walking around with her eyes closed..."
        hide kazuna_satoshi
        "She leaves without even saying she's sorry."
    else:
        $ renpy.show("kazuna_satoshi "+kazuna_dress+" surprised", at_list=[center])
        speaker "Oh, I'm sorry [povTitle] [povLastName], my mind wandered."
        if kazuna_satoshi_known == 0: 
            "She apologizes to you and then walks away with her books."
            if kazuna_dress == "nude":
                "You take a good look at her ass before returning to your office."
        else:
            pov "Don't worry, it was my fault. So Kazuna, how are things lately?" 
            $ renpy.show("kazuna_satoshi "+kazuna_dress+" happy", at_list=[center])
            "The two of you start to talk about school."
            if kazuna_dress == "nude":
                "It sure is hard to look her in the eyes while she's completely naked."
                "She says good-bye and walks away. You take a good look at her ass before returning to your office."
    return


label kazuna_satoshi_encounter3:
    
    $ kazuna_satoshi_points += 1
    scene bg hallway with fade

    if uniform == 'nude_uniform' and inhibition < 30:
        $ kazuna_dress = "nude"
    else:
        $ kazuna_dress = "dressed"

    if kazuna_satoshi_known == 0:
        $ speaker = girl
    else:
        $ speaker = kazuna_satoshi
    if behavior < 25:
        $ renpy.show("kazuna_satoshi "+kazuna_dress+" normal", at_list=[center])
        if kazuna_satoshi_known == 0:
            "You see a group of students in the hallway. A flock of boys and a single girl."
        else:
            "You see a group of students in the hallway. A flock of boys and that girl Kazuna."
        "The boys are being rude, and she doesn't really care for their manners"
        if inhibition < 20:
            $ renpy.show("kazuna_satoshi "+kazuna_dress+" blush", at_list=[center])
            "She does seem to appreciate all that attention though. They are continuously touching her while talking."
            speaker "Uff, fuck you guys, you're just a bunch of lowly perverts."
            "Boy" "Ahahah! Look who's talking!"
            "All the boys laugh at her while the guy who spoke squeezes her nipple."
            "Boy" "You love being fucked bitch. Just follow us, we're gonna show you just how low we can get"
            "The boys push her down the hallway and she doesn't put up much resistance. She probably wants to be fucked real good."
        elif inhibition < 65:
            $ renpy.show("kazuna_satoshi "+kazuna_dress+" blush", at_list=[center])
            "At the same time, she seems to appreciate all that attention."
            speaker "You could really be nicer when dealing with a girl, you know."
        else:
            $ renpy.show("kazuna_satoshi "+kazuna_dress+" yell", at_list=[center])
            speaker "Fuck off losers. I'm outta here."
            "She pushes them back and walk away."
    else:
        $ renpy.show("kazuna_satoshi "+kazuna_dress+" happy", at_list=[center]) 
        if kazuna_satoshi_known == 0:
            "You see a group of students in the hallway. A flock of boys and a single girl."
        else:
            "You see a group of students in the hallway. A flock of boys and that girl Kazuna."
        "They seem to be enjoying themselves."
        if inhibition < 20:
            speaker "Oh please, just touch them. You know how much I enjoy your sweet attention."
            "Boy" "Touching you? Yeah no problem, but we were thinking about something... more x-rated."
            "They at her with grinning faces."
            speaker "Boys, boys, boys. Do you ever think of anything else? "
            if kazuna_dress == "nude":
                "Boy" "It's your fault! You can't go around here showing off that naked body and then complain if everyone here wants to fuck your brains out!"
                show kazuna_satoshi nude blush at center
                speaker "Oh... Well, you're probably right... It's my responsibility."
                "She smiles and let the boys follow her. You almost hoped that they would have fucked her right here in the hallway."
            else:
                "Boy" "Don't be mean to us, we are men, we have our needs. A body like yours is just too beautiful not to enjoy."
                show kazuna_satoshi dressed blush at center
                speaker "Oh... don't talk about my body as if it was just a piece of meat. \nOk, I will \"help\" you, but try to be nicer, ok?"
                "However it may sound, you know that she wanted it from the beginning. She's such a slut."
                "The gang walks down the hall looking for an empty classroom."
        elif inhibition < 45:
            $ renpy.show("kazuna_satoshi "+kazuna_dress+" surprised", at_list=[center])
            speaker "No, you can't \"just touch\" them. Not even if you ask nicely."
            "Boy" "It's not the first time that we'd be touching you, So why not?"
            speaker "I-it's not something you can do as you please! And not here..."
            "Students... They're always thinking about sex."
        else:
            if kazuna_satoshi_known == 0:
                "You are happy to see that the students are socializing."
            else:
                "You are happy to see that Kazuna is having a good time with her friends."
    return


label kazuna_satoshi_encounter4:   
    
    $ kazuna_satoshi_points += 1    
    scene bg school_grounds with fade
    $ speaker = girl
    $ kazuna_dress = "dressed"
    "You've had a load of paperwork, the evening falls as you set foot on the schoolground. There's only a few people around, most of the students have already gone home."
    show kazuna_satoshi dressed normal at center
    "Your attention is drawn towards a girl just leaving the main building."
    pov "I think I've met her before."
    menu:
        "Make contact.":
            $ kazuna_satoshi_known = 1
            "As she passes, you decide to talk to her."
            show kazuna_satoshi dressed surprised at center            
            pov "Going home late today, huh?"
            "She didn't expect the principal to talk to her."
            girl "N-no... I mean yes... Sorry [povTitle] Principal."
            pov "Haha, no need to apologize. I startled you, didn't I?"
            pov "Now, you obviously know who I am, and you are...?"
            kazuna_satoshi "OH! Sorry again, I'm Kazuna Satoshi."
            show kazuna_satoshi dressed happy at center
            pov "Nice to meet you Kazuna.  \nSo, what were you doing so late at school?"
            show kazuna_satoshi dressed blush at center
            kazuna_satoshi "I forgot one of my books, so I had to go back for it."
            "She is embarrassed from her mistake."
            pov "Girls, girls... Always thinking about boys?"
            "She blushes again."
            kazuna_satoshi "No, not really, I was just really tired today. The teachers were really hard on us."
            show kazuna_satoshi dressed happy at center
            pov "Oh, sorry to hear that."
            "You see a glimpse of hope in her eyes."
            kazuna_satoshi "So... will you tell them to go easier on us? \nPlease?"
            "She looks at you with her puppy beads." 
            show kazuna_satoshi dressed surprised at center
            pov "No."
            pov "Hahaha."
            "Kazuna is so surprised by your fast, sharp answer that you laugh at her expression. \nShe just stares at you, so you feel obligated to spell it out for her."
            show kazuna_satoshi dressed happy at center
            pov "Really, they're not THAT hard on you. As principal, I expect them to push you into giving your all."
            kazuna_satoshi "Oh... Uff..."
            kazuna_satoshi "Well I had to try, don't ya think?"
            "You both laugh."
            hide kazuna_satoshi with fade
            "You continue to chat for a while, but it's late and she has to go.\nYou bid her goodnight."
            show kazuna_satoshi dressed happy at center
            pov "It was nice to meet you. I hope to see you around."
            if behavior < 30:
                kazuna_satoshi "Yes, I was nice to meet you too. See you [povTitle] [povLastName]."
            else:
                kazuna_satoshi "The pleasure was all mine. Good night [povTitle] [povLastName]."
            "You both leave in opposite directions."
             
        "It's late, I just want to go home and get some sleep.":
            "You have no interest in getting acquainted to this student, so you decide to leave."
    return


#Event that will probably never be added.
#when deleting this remember to take out the event $ event(....)
#label kazuna_satoshi_encounter5:

#    $ kazuna_satoshi_points += 1    
#    $ kazuna_dress = "dressed"
#    scene bg classroom with fade
#    if kazuna_satoshi_known == 0:
#        $ speaker = girl
#    else:
#        $ speaker = kazuna_satoshi
#    "........."
#    "You are walking in the hallway visiting the classes on the floor."
#    "N
#            $ renpy.show("kazuna_satoshi "+kazuna_dress+" happy", at_list=[center])
#            "When you walk near them they are all kind and cheerful."
#            speaker "How are you doing Mr [povname]?"
#            pov "I'm good, this is a nice day. \nI should really give you permission to have class outdoors, don't you think?"
#            $ renpy.show("kazuna_satoshi "+kazuna_dress+" surprised", at_list=[center])
#            speaker "R-Really!? It would be awesome! \nCan we really do it?"
#            girl2 "Hahaha, I think the principal was kidding. No way that we can do that for real."
#            $ renpy.show("kazuna_satoshi "+kazuna_dress+" normal", at_list=[center])
#            speaker "Oh... I hoped"
            
#return