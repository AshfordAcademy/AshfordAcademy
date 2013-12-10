##########################################################
#
#                       Marceline Ward                      
#
# A teacher at Ashford. Happy and bubble headed that
# always bring positive energy to the table.
# Quite flirtatious ;)
# 
# Several unique sex scenes are available.
#
##########################################################

define marceline_ward_toilet = False

# We load images to be shown and the variations.
image marceline_ward normal = "story/story_screens/marceline_ward/marceline_ward_normal.png"
image marceline_ward normal_blush = "story/story_screens/marceline_ward/marceline_ward_normal_blush.png"
image marceline_ward happy = "story/story_screens/marceline_ward/marceline_ward_happy.png"
image marceline_ward surprised = "story/story_screens/marceline_ward/marceline_ward_surprised.png"
image marceline_ward surprised_blush = "story/story_screens/marceline_ward/marceline_ward_surprised_blush.png"

image marceline_ward 1 = "story/story_screens/marceline_ward/marceline_ward_1.png"
image marceline_ward 2 = "story/story_screens/marceline_ward/marceline_ward_2.png"
image marceline_ward 3 = "story/story_screens/marceline_ward/marceline_ward_3.png"

image marceline_ward 5 = "story/story_screens/marceline_ward/marceline_ward_5.png"

image marceline_ward 7 = "story/story_screens/marceline_ward/marceline_ward_7.png"
image marceline_ward 8 = "story/story_screens/marceline_ward/marceline_ward_8.png"

image marceline_ward_class_happy = "story/story_screens/marceline_ward/events/marceline_ward_class_happy.jpg"
image marceline_ward_class_horny = "story/story_screens/marceline_ward/events/marceline_ward_class_horny.jpg"

# Here we define prefix used for us and what it will show to the player.
# Colors are written in hexadecimal. (FF0000 = Red, 00FF00 = Green, 0000FF = Blue)
define marceline_ward = Character('Marceline Ward', color="#516FA2")


# Here we make a list of all scenes with her. 
init:
    $ event("marceline_ward_hallway", "act == 'class'", event.once(), event.choose_one('class'), event.depends("class_introduction"))
    $ event("marceline_ward_class1", "act == 'class'", event.once(), event.choose_one('class'), event.depends("marceline_ward_hallway"), priority=150)
    $ event("marceline_ward_school_grounds", "act == 'school_grounds'", event.once(), event.choose_one('school_grounds'), event.depends("marceline_ward_class1"), priority=150)
    $ event("marceline_ward_gym", "act == 'gym'", event.once(), event.choose_one('gym'), event.depends("marceline_ward_school_grounds"), priority=150)
    $ event("marceline_ward_class2", "act == 'class'", event.once(), event.choose_one('class'), event.depends("marceline_ward_gym"), priority=150)
    $ event("marceline_ward_class3", "act == 'class'", event.once(), event.choose_one('class'), event.depends("marceline_ward_class2"), priority=150)
    $ event("marceline_ward_school_grounds2", "act == 'school_grounds' and introduce_officer_adaki == True", event.once(), event.choose_one('school_grounds'), event.depends("marceline_ward_school_grounds"), event.only())
    
    #Main story events:
    $ event("marceline_ward_regarding_adaki", "act == 'school_grounds' and introduce_officer_adaki == True", event.once(), event.choose_one('school_grounds'), event.depends("marceline_ward_school_grounds", "adaki_school_grounds"), event.only())


label marceline_ward_hallway:
   
    scene bg hallway with fade
    show marceline_ward happy at center
    marceline_ward "Oh, hello there! I didn't mean to steal your time, but I just wanted to say welcome to us, er, I mean to our school, I mean... Ah shoot, WELCOME!"
    pov "Haha, that's alright, thank you very much Mrs..?"
    marceline_ward "Ah! I don't know what's wrong with me today! I'm Marceline, Marceline Ward, home room teacher for class C."
    pov "Nice to make your acquaintance Marceline, I'm [povName]."
    marceline_ward "Really nice to make your... to meet you to, Principal [povLastName]!"
    pov "Please, just call me [povFirstName]."
    marceline_ward "Right, [povFirstName], and it's not Mrs, it's Miss. Oh!"
    show marceline_ward surprised_blush
    "Why did I mention that? I just... I mean... I gotta go!"
    hide marceline_ward
    pov "Okay, I'll see you later Miss... Wow, she just ran away."
    return


label marceline_ward_class1:

    scene marceline_ward_class_happy with fade
    marceline_ward "Oh, what a nice surprise!"
    pov "Hello again MISS Ward."
    marceline_ward "Oh, hehe... * blush *"
    pov "Well, I just wanted to see how you were doing. I'll see you later."
    marceline_ward "Yes! I mean... hrm... 'til later then."
    return


label marceline_ward_school_grounds:

    scene bg school_grounds with fade
    show marceline_ward normal at center
    pov "Hello there Miss Ward, fancy seeing you here."
    marceline_ward "Please [povTitle] [povLastName], just Marceline."
    pov "Please Marceline, just [povFirstName]."
    show marceline_ward normal_blush
    return


label marceline_ward_gym:

    scene bg gym_locker_room with fade
    show marceline_ward surprised at center
    marceline_ward "Oh!"
    menu:
        "Ah!":
            marceline_ward "You scared me [povFirstName], I was just using the bathroom..."
            pov "I was just passing through, must check everything you know."
            show marceline_ward happy
            marceline_ward "Oh yes, a check up now and then sure feels good!"
            pov "Hmm..."
            show marceline_ward surprised_blush
            marceline_ward "I mean... I... I gotta go!"
            pov "And she's off again."

        "So sorry, didn't mean to scare you.":
            show marceline_ward happy
            marceline_ward "I'm not that easily scared, heheh."
            pov "That's good to know."
            marceline_ward "Hrm, well I was just on my way."
            pov "You have a good day now."
            marceline_ward "You too!"

        "I THOUGHT I heard someone using the toilet!" if new_game_plus == True:
            show marceline_ward surprised_blush
            marceline_ward "..."
            pov "Shish Kebab! Was there a horse in there?!"
            marceline_ward "I- I gotta go!"
            pov "Giddy up!"
            $ marceline_ward_toilet = True
    return


label marceline_ward_class2:

    scene marceline_ward_class_happy with fade
    pov "Knock-knock."
    marceline_ward "Oh, it's you!"
    pov "Expecting somebody else?"
    marceline_ward "Not at all! I mean..."
    menu:
        "Maybe you got a date?":
            marceline_ward "Why, you jealous?"
            pov "What if I am?"
            marceline_ward "Oh, stop it!"
            menu:
                "As always, a pleasure.":
                    "As you leave, you can see that she's smiling."

                "That's ok, I've got a date too.":
                    marceline_ward "Oh! I see..."
                    "As you walk out the door, you can tell that she seems annoyed."

                "I wouldn't take you for someone who'd sleep around." if marceline_ward_toilet == True:
                    pov "Then again, I wouldn't believe what you did to that poor toilet back at the office either."
                    "She keeps her smile but since she's a woman, you know she's crying on the inside."


        "I'm on my way, just thought I'd stop by to say hi.":
            marceline_ward "Stop by anytime you want!"
            menu:
                "Got it!":
                    "As you leave, you feel that the two of you really connected."

                "That goes for you too.":
                    marceline_ward "Oh! Maybe I will..."
                    pov "I'll be looking forward to it."
                    "As you leave, you sense that this flirting is taking a turn for the better."

                "Naah.":
                    marceline_ward "What?"
                    pov "Oh, nothing."
                    marceline_ward "Oh... Ok..."
                    pov "Bye."
                    marceline_ward "Take care!"
                    "As you leave, you're amazed how fucking stupid this bitch really is. Surprised no one smacked her in the face already."
    return


label marceline_ward_class3:

    scene marceline_ward_class_happy with fade
    pov "Good morning Marceline."
    marceline_ward "Oh, good morning!"
    pov "Seems like I caught you early."
    marceline_ward "Well, I have to prepare before today's class. The students are really proving themselves... I just don't want them to think that I'm not, eh, capable."
    pov "You worry about that?"
    marceline_ward "Ha ha, it's silly, I know. But their biology teacher is a regular genius and I don't want to be a lesser teacher."
    menu:
        "You seem capable enough.":
            marceline_ward "Well, a girl's gotta be sure, if you know what I mean."
            pov "I guess so."
            marceline_ward "You're welcome to stay, I just need to scribble a few things on the board."
            pov "I was heading elsewhere, just thought I'd stop by to say hi."
            marceline_ward "Well, hi!"
            pov "Hi."
            "You turn around, ready to leave."
            marceline_ward "Feel free to stop by again!"
            pov "Maybe I will."
            "As you walk away, you see a little smile on her lips."

        "There's nothing \"lesser\" about you.":
            marceline_ward "You really mean that?"
            pov "Cross my heart."
            marceline_ward "You have no idea how happy you've made me!"
            pov "Happy enough to give me some private tutoring?"
            marceline_ward "Oh, I..."
            pov "I bet you give great biology."
            scene marceline_ward_class_horny
            marceline_ward "*gasp* If you only-"
            pov "Looks like the students are coming, perhaps another time then?"
            marceline_ward "Another time, of course! Hrm, I better wipe my..."
            "You leave the room with a smile just as the students start to troop in."

        "Well, we can't all be geniuses.":
            marceline_ward "I just feel so..."
            pov "So?"
            marceline_ward "You know, {i}slow{/i}."
            pov "I can't imagine how that would feel, but I assure you, the kids think you're alright."
            marceline_ward "You think so?"
            pov "I'm almost certain."
            marceline_ward "Maybe I can relax a bit then."
            pov "Well, I gotta go. Good luck with class."
            marceline_ward "Thanks!"
            "As you leave, you think to yourself that the last administration really had an uneven standard when it came to recruiting."
    return


label marceline_ward_school_grounds2:

    scene bg school_grounds2 with fade
    show marceline_ward 7 at center
    "What's this?"
    pov "Hey Marceline, are you alright?"
    show marceline_ward 8 at center
    marceline_ward "[povLastName], I was just..."
    pov "Has something happened?"
    "She's not usually this still."
    marceline_ward "I'm fine, I was just... well... this whole business with your secretary's death..."
    pov "Yes, it was quite a shock, wasn't it?"
    marceline_ward "I never thought, I mean... I didn't know her, but yet..." 
    show marceline_ward 5 at center
    marceline_ward "We bumped into each other a couple of times at school, no heavy conversations but still a few words whenever we met."
    pov "Of course, you were colleagues, it's only natural to be affected."
    marceline_ward "Yes. Yes, I guess so."
    pov "I find myself thinking about it too, makes me sad when I do."
    
    show marceline_ward 1 at center
    marceline_ward "She was your secretary, you must have been affected too, and much worse than me since you worked so closely with her."
    pov "Well, we never got around to getting to know each other that well. It happened so soon after she got here, I..."
    show marceline_ward 2 at center
    marceline_ward "I'm sorry if I drag you down too."
    pov "Don't be silly, we shouldn't be afraid to talk about it. In fact, trying to repress it will only make it worse."
    show marceline_ward normal_blush at center
    marceline_ward "You're right. Hey, I feel better already."
    pov "Glad to hear it."
    marceline_ward "By the way, did the police say anything about it?"
    menu:
        "Don't dig into details.":
            pov "A couple of questions about when she started working here and such. Guess they were just following protocol. "
            marceline_ward "I'm sure you gave them all the help they needed."
            pov "I hope so."
            marceline_ward "But of course you did!"
            show marceline_ward happy at center
            marceline_ward "Say, would you mind walking me to the gate? Maybe I'm silly but right now it would make me feel even better."
            pov "It would be my pleasure."
            "You walk Marceline to the gate and give her a comforting hug. She's better off not knowing all the details, no reason to make her more worried than she already is."

        "Let her in on it.":
            pov "Well, they didn't rule out any possibilities."
            marceline_ward "Meaning what?"
            pov "Meaning we can't rule out that it was no accident."
            show marceline_ward 3 at center
            marceline_ward "What?! No accident? Are you suggesting-"
            pov "That Jennifer got murdered? The police seem to think so, or at least that the circumstances surrounding her death were odd."
            marceline_ward "This is crazy, I mean, who would want poor Jennifer to... to... I don't believe it, do you?"
            pov "I'm not sure what to make of it. The detective in charge said he'd be back with further questions. I'm as puzzled as you."
            marceline_ward "But, does the students know? I mean, what will all the parents say? Imagine sending you kids to school knowing that someone connected to this school got murdered?"
            pov "Let's not jump to conclusions. I had a talk with Susan and we agreed that it would be for the best not to let any details slip out."
            marceline_ward "I... I guess it's for the best, imagine if we had to cancel all the lectures."
            pov "Let's just wait for the investigation to shed some light on things. In the meantime, I'm going to take extra measures to keep everybody at Ashford safe."
            marceline_ward "You mean like alarm systems and such?"
            pov "I'm considering a few options. I don't think anything will happen but rather safe than sorry."
            show marceline_ward happy at center
            marceline_ward "It feels safe to know that you're our principal, I mean... I feel safe with you around."
            pov "Sounds good, I'll do my best, don't you worry."
            "You walk her to the gates and give her a hug. She holds you really tight and let her hand slide down your back before pulling away. You give her a smile and walk away. It feels good to have come clean about the police, although you didn't share every single bit of it."
    return


label marceline_ward_regarding_adaki:                                                   # Always start with a label.
    scene bg school_grounds with fade                                                   # Scene +bg +name
    show marceline_ward normal at center                                                # show +char +state
    pov "Well, hello there Marceline."                                                  # +Name +"text"
    show marceline_ward happy
    marceline_ward "Oh, hello there [povName]!"
    pov "Have you done something with your hair? It sure looks nice."
    show marceline_ward surprised_blush
    marceline_ward "*blushing* T-thanks, I didn't expect anyone to notice..."
    pov "How could you not notice?"
    show marceline_ward surprised
    marceline_ward "W-well, I..."
    pov "Listen, could you tell me something?"
    menu:                                                                               # small caps end with :
        "What's the story on officer Adaki?":                                           # Never a name on menu alternatives, end with :
            show marceline_ward normal
            marceline_ward "Well, I don't know him personally but he's known to be quite a bloodhound."
            pov "How so?"
            show marceline_ward 1
            marceline_ward "You see, there was a case a few years back, I don't recall the details but the newspapers were filled with articles about it."
            pov "Go on."
            marceline_ward "Adaki was on the news every other day talking about how progress was made and that he couldn't give away any details but that he was sure the case would be solved real quick."
            pov "Was it?"
            show marceline_ward surprised
            marceline_ward "Was what?"
            pov "Did he solve the case?"
            marceline_ward "Oh! I... I don't remember! How silly! Here I am making a point out of that he's such a thorough detective, I feel so ignorant."
            pov "Relax, it could have slipped anybody's mind."
            show marceline_ward happy
            marceline_ward "R-really? I mean of course!"
            pov "You've been most helpful Marceline."
            show marceline_ward surprised_blush
            marceline_ward "And you're really cute! I-I mean..."
            "She turns around blushingly and runs away."
            hide marceline_ward
            pov "There she goes again..."

        "Does this symbol mean anything to you?":                                       # Menu alternative 2
            show marceline_ward 1
            marceline_ward "Hmm, it does look somewhat familiar."
            pov "Yes?"
            show marceline_ward normal
            marceline_ward "I wonder... Could it be from some sort of jewellery?"
            pov "I guess it's possible, but have you actually seen it?"
            show marceline_ward 7
            marceline_ward "I'm picking my brain but right now I'm getting nothing."
            pov "That's alright."
            marceline_ward "But it's frustrating!"
            show marceline_ward 2
            pov "You do look cute when you're frustrated."
            marceline_ward "Ah, thank's! But I'm gonna keep trying to come up with where I've might seen it."
            pov "That's great, let me know when you do, right?"
            show marceline_ward 2
            marceline_ward "Right!"
    return                                                                              # All menu options will fall back to this indentation level and will trigger the return.
