##########################################################
#
#                       Jack Drake
#
# A somewhat weird teacher (?) that the player meets on
# his/her first visit in the office.
#
# No sex scenes are available.
#
##########################################################

init python:
    hit_the_road_jack = False
    jack_drake_pov_nickname = ''
    jack_drake_nickname = ''
    jack_drake_points = 0

define jack_drake = Character('Jack Drake', color="#878083")

# Sprites
image jack_drake smile = "chars/jack_drake_smile.png"
image jack_drake normal = "chars/jack_drake_normal.png"
image jack_drake normal_blink = "chars/jack_drake_normal_blink.png"
image jack_drake surprised = "chars/jack_drake_surprised.png"
image jack_drake surprised_blink = "chars/jack_drake_surprised_blink.png"
image jack_drake sweat = "chars/jack_drake_sweat.png"
image jack_drake facepalm = "chars/jack_drake_facepalm.png"
image jack_drake facepalm_sad = "chars/jack_drake_facepalm_sad.png"


init:
    #First we have all the povGender == 'male' interactions:
    $ event("office_introduction_male", "act == 'office' and povGender == 'male'", event.once(), event.only())
    $ event("jack_drake_office", "act == 'office' and planning_day > 2 and hit_the_road_jack == False", event.choose_one('office'), event.depends("office_introduction_male"), priority=180)

    #The povGender == 'female' ones:
    $ event("office_introduction_female", "act == 'office' and povGender == 'female'", event.once(), event.only())

    # And lastly, the non gender related.
    $ event("office_where_is_jack", "act == 'office' and hit_the_road_jack == True", event.once(), event.only())


label office_introduction_male:
    scene bg office with fade
    "As you enter your new office, you see some guy walking around aimlessly."
    show jack_drake normal at center
    pov "Hello, can I help you?"
    show jack_drake smile
    "???" "Oh, hey man! You must be the new head honcho!"
    pov "I guess you could call me that. Who are you and what are you doing in my office?"
    show jack_drake normal
    jack_drake "Oh, yeah... I'm Jack, nice to meet ya. I was just a tad interested in who the new guy could be."
    pov "Alright Jack, here I am."
    jack_drake "Mhmm..."
    pov "..."
    jack_drake "Oh yes, I should probably tell you how stuff works right?"
    menu:
        "Yeah, that sounds like a plan.":
            show jack_drake normal_blink
            jack_drake "Well, every now and then you'll get back to your office for stuff like weekly and monthly planning. But I'm sure Susan will help you with that."
            show jack_drake normal
            jack_drake "When you decide to take a peek into your office during school days, you most likely will be interrupted on your way here since teachers and staff rooms are next to your place."
            jack_drake "And, yeah I guess that's it..."
            pov "Well, that sure was a lot of information."
            jack_drake "Yeah, I know, it's such a hassle. Oh well, I better get back to my turf. See ya."

        "Don't worry about it.":
            show jack_drake smile
            jack_drake "That's the spirit! You made me worry there for a second, it's a tad to early to get to work, right?"
            pov "Eh, yeah..."
            jack_drake "Well, I guess I have classes or something to take care of."
            pov "Right, good luck with that."
            jack_drake "Thanks man."

        "You got any strong stuff?" if start_day_with_gin == True:
            show jack_drake surprised
            jack_drake "Fuck yeah!"
            show jack_drake smile
            jack_drake "What do you need? Or should I say, what do you need it for?"
            pov "Well, a Gin and tonic would hit the spot!"
            show jack_drake normal_blink
            jack_drake "Oh, yeah... THAT strong stuff, well give me a sec."
            hide jack_drake
            "Jack quickly runs away just to return soon again with a bottle."
            show jack_drake smile
            "He quickly opens one of your cabinets and pulls out two glasses and mixes a drink."
            jack_drake "Here ya go man, cheers!"
            pov "Cheers!"
            scene black with fade
            "You spend a tender moment with a bottle of Gin and a weird but nice guy."

        "Hit the road Jack." if new_game_plus == True:
            show jack_drake surprised
            jack_drake "Did you just fire me?"
            show jack_drake facepalm
            pov "Sure seems so. And don't you come back no more."
            jack_drake "No more?"
            pov "No more."
            jack_drake "No more..."
            show jack_drake facepalm_sad
            jack_drake "Oh well, I guess my slacking days are over."
            $ hit_the_road_jack = True
            $ evil_points += 1
    return


label office_introduction_female:
    scene bg office with fade
    "As you enter your new office, you see some guy walking around aimlessly."
    show jack_drake normal at center
    pov "Hello, can I help you?"
    show jack_drake smile
    "???" "Oh, OH! *cough*{w} Well, hello there! Miss principal I presume?"
    pov "Yes, I am the new principal. Who are you and what are you doing in my office?"
    jack_drake "Oh, yes, sorry... I'm Jack, Jack Drake. When I heard about you I decided to greet you in person."
    pov "I see. Good day Mr. Drake, I'm [povFirstName] [povLastName]."
    show jack_drake normal_blink
    jack_drake "Miss [povFirstName], please, no need for formalities."
    menu:
        "I agree Jack":
            $ jack_drake_pov_nickname = "Miss "+povFirstName
            $ jack_drake_nickname = "Jack"
            $ jack_drake_points += 1
            show jack_drake smile
            jack_drake "I'm happy to hear that [jack_drake_pov_nickname]."

        "I would actually prefer to keep it formal.":
            $ jack_drake_pov_nickname = povTitle+" "+povLastName
            $ jack_drake_nickname = "Mr. Drake"
            show jack_drake normal
            jack_drake "Hmph... If you say so {i}[jack_drake_pov_nickname]{/i}."
            pov "Much better {i}[jack_drake_nickname]{/i}."

    jack_drake "Mhmm..."
    "You see how [jack_drake_nickname]'s eyes are slowly inspecting your body..."
    pov "..."
    jack_drake "Sorry [jack_drake_pov_nickname], I should probably tell you how stuff works here, right?"
    menu:
        "That sounds like a plan.":
            show jack_drake normal_blink
            jack_drake "You see, every now and then you'll get back to your office for meetings about weekly and monthly planning. But I'm sure Susan will help you with that."
            show jack_drake normal
            jack_drake "If you decide to come back to your office during school days, you most likely will be interrupted on your way here since teachers and staff rooms are next to your place."
            jack_drake "And, yeah I guess that's it..."
            pov "Well, that sure was a lot of information."
            jack_drake "If there's anything I can do for you [jack_drake_pov_nickname], don't hesitate to come to me."
            pov "Thank you [jack_drake_nickname], I'll keep it in mind."

        "Don't worry about it.":
            show jack_drake smile
            jack_drake "I see, maybe you have a more hands on approach."
            pov "Well-"
            show jack_drake normal
            jack_drake "Haha, I'm just kidding with you [jack_drake_pov_nickname]."
            pov "Sorry [jack_drake_nickname], but I need to get to work now."
            jack_drake "I understand [jack_drake_pov_nickname]. Good luck with that and if you need me, I'll be here for you."

        "You got anything to drink?" if start_day_with_gin == True:
            show jack_drake surprised
            jack_drake "Of course! What do you prefer, a glass of wine or maybe a whiskey?"
            pov "Some wine would do fine."
            show jack_drake smile
            jack_drake "Anything for you miss!"
            hide jack_drake
            "Jack quickly runs away just to return soon again with a bottle."
            show jack_drake normal at center
            "He quickly opens one of your cabinets and pulls out two glasses and pours up wine."
            show jack_drake smile
            jack_drake "For the wonderful new miss principal!"
            pov "For me!"
            scene black with fade
            "You spend a tender moment with a bottle of wine and a nice but weird guy."
            $ jack_drake_points += 1

        "Hit the road Jack." if new_game_plus == True:
            show jack_drake surprised
            jack_drake "Did you just fire me?"
            show jack_drake facepalm
            pov "Sure seems so. And don't you come back no more."
            jack_drake "No more?"
            pov "No more."
            jack_drake "No more..."
            show jack_drake facepalm_sad
            jack_drake "Oh well, I guess my slacking days are over."
            $ hit_the_road_jack = True
            $ evil_points += 1
    return


label jack_drake_office:

    scene bg office with fade

    if renpy.random.randint(1,2) == 1:
        "While doing some mundane paperwork your office doors suddenly open."
    else:
        "As you enter your office you see..."

    show jack_drake normal at center
    jack_drake "Hey man!"

    if new_game_plus == True:
        pov "Oh, Hai Drake!"
    elif jack_drake_pov_nickname:
        pov "Hey there Drake."

    if jack_drake_pov_nickname == '':
        jack_drake "So what's up [povFirstName]?"
    else:
        jack_drake "So... What's up [jack_drake_pov_nickname]?"
    pov "Some old, how about you?"
    jack_drake "Naah, I'm just taking a break from all the teachin' stuff. It's a tad tiring you know."
    if deviance > 95 and inhibition < 5 and academics > 95 and behavior > 95:
        show jack_drake smile
        jack_drake "Sure, they do {i}exactly{/i} what they are told and ace every test... But still, if you don't fuck their brains out before class they sure as hell will make you fuck them senseless during class."
    elif deviance > 90 and inhibition < 10:
        show jack_drake smile
        jack_drake "Giving all these girls {i}private{/i} lessons sure makes me sore. Fuckin' love it tho. A fresh young snitch a day keeps the nurse in play."
    elif deviance > 50 and inhibition < 50:
        show jack_drake smile
        jack_drake "I can barely walk over to your office these days without a bunch of sexy young girls asking for me. But... Good work man, we can all enjoy ourselves here."
    elif deviance > 25 and inhibition < 75 and (uniform == sexy_uniform or uniform == nude_uniform):
        show jack_drake normal_blink
        jack_drake "You know, keepin' your eyes on class when you got some young bodies showing off in front of ya, it ain't easy."
    elif deviance > 25 and inhibition < 75:
        jack_drake "Just the other day one of the girls {i}slid a pen in{/i} during class, how the fuck am I supposed keep focus seeing that man?"
    elif academics > 90:
        show jack_drake normal_blink
        jack_drake "Teachin' these young geniuses forces me to keep up and research every fuckin' field. Just the other they I had to explain {i}string theory's{/i} relation with {i}Everett's many worlds theory{/i}."
    elif academics > 60:
        jack_drake "Some kids actually have some brains and asks a shit load of stupid questions. Of-{i}fuckin'{/i}-course was the majority of Carl Jung's later work influenced by his experience of cocaine."
    elif academics > 35:
        show jack_drake facepalm
        jack_drake "Have you ever woken up in some random place hungover as hell and then walked to work to teach some stupid ass kids?"
        pov "..."
        jack_drake "No..? Eh, me neither."
    else:
        jack_drake "They might be stupid as hell but they are still makin' me work like a horse. "
    pov "Sure sounds like it could be worse, Jack."
    show jack_drake normal
    jack_drake "Yeah, you're right mate, but still..."

    return


label office_where_is_jack:

    scene bg office with fade
    show susan_marina normal at center
    susan_marina "Oh, there you are!\nI was just looking for you."
    menu:
        "What's it about?":
            pass

        "Can't stop thinking of me?" if povGender == 'male':
            show susan_marina angry
            susan_marina "Very funny [povTitle] [povLastName]."

        "Can't stop thinking of me?" if povGender == 'female':
            susan_marina "Sorry? {w}Oh... This is not the time for jokes [povTitle] [povLastName]."

    show susan_marina normal
    susan_marina "It's about one of our teachers, Jack Drake. For a few days now, he hasn't shown up for work and I haven't been able to get in touch with him."
    susan_marina "So I wonder if you have seen him around or if he have contacted you?"
    menu:
        "Yeah, I told him to hit the road.":
            show susan_marina surprised
            susan_marina "YOU WHAT?!"
            susan_marina "Did you fire Jack Drake?!"
            pov "Yeah..."
            show susan_marina angry
            susan_marina "Why would you do that?! Do you even know what he does around here?"
            menu:
                "Actually...":
                    pass

                "Well...":
                    pass

                "This is...":
                    pass

            show susan_marina sad
            susan_marina "..."
            show susan_marina angry
            susan_marina "He's one of the schools most prominent professors, boasting a Ph.D in cognitive neuropsychology, Ph.D in bioinformatics and Sc.D in informatics!"
            susan_marina "This school already has a bad reputation and the first thing you do is to fire the highest educated teacher we have..."
            susan_marina "Do you know how important it is to have highly educated teachers these days? How are we supposed to attract new students now?"
            pov "Well, we could alway-"
            susan_marina "Always what? \nHire him again? Yeah, good luck with that!"
            pov "..."

        "Jack? Nope, doesn't ring a bell.":
            susan_marina "Alright, It was worth a shot. Anyway, if you hear anything please tell me."
            pov "Will do."
    return
