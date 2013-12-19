image bg bath1 = "locations/bath/bath1.jpg"
image bg bath2_1 = "locations/bath/bath2-1.jpg"
image bg bath2_2 = "locations/bath/bath2-2.jpg"
image bg bath2_3 = "locations/bath/bath2-3.jpg"
image bg bath3_1 = "locations/bath/bath3-1.jpg"
image bg bath3_2 = "locations/bath/bath3-2.jpg"
image bg bath3_3 = "locations/bath/bath3-3.jpg"
image bg bath4 = "locations/bath/bath4.jpg"
image bg bath5_1 = "locations/bath/bath5-1.jpg"
image bg bath5_2 = "locations/bath/bath5-2.jpg"
image bg bath5_3 = "locations/bath/bath5-3.jpg"
image bg bath6-1 = "locations/bath/bath6-1.jpg"
image bg bath6-2 = "locations/bath/bath6-2.jpg"
image bg bath6-3 = "locations/bath/bath6-3.jpg"
image bg bath6-4 = "locations/bath/bath6-4.jpg"
image bg bath7 = "locations/bath/bath7.jpg"
image bg bath8 = "locations/bath/bath8.jpg"
image bg bath9_1 = "locations/bath/bath9-1.jpg"
image bg bath9_2 = "locations/bath/bath9-2.jpg"
image bg bath10 = "locations/bath/bath10.jpg"
image bg bath11-1 = "locations/bath/bath11-1.jpg"
image bg bath11-2 = "locations/bath/bath11-2.jpg"
image bg bath11-3 = "locations/bath/bath11-3.jpg"
image bg bath11-4 = "locations/bath/bath11-4.jpg"
image bg bath12 = "locations/bath/bath12.jpg"
image bg bath13 = "locations/bath/bath13.jpg"
image bg bath14 = "locations/bath/bath14.jpg"
image bg bath15 = "locations/bath/bath15.jpg"
image bg bath16-1 = "locations/bath/bath16-1.jpg"
image bg bath16-2 = "locations/bath/bath16-2.jpg"
image bg bath16-3 = "locations/bath/bath16-3.jpg"
image bg bath17_1 = "locations/bath/bath17-1.jpg"
image bg bath17_2 = "locations/bath/bath17-2.jpg"
image bg bath18 = "locations/bath/bath18.jpg"
image bg bath19-1 = "locations/bath/bath19-1.jpg"
image bg bath19-2 = "locations/bath/bath19-2.jpg"
image bg bath19-3 = "locations/bath/bath19-3.jpg"
image bg bath20-1 = "locations/bath/bath20-1.jpg"
image bg bath20-2 = "locations/bath/bath20-2.jpg"
image bg bath21-1 = "locations/bath/bath21-1.jpg"
image bg bath21-2 = "locations/bath/bath21-2.jpg"
image bg bath22 = "locations/bath/bath22.jpg"
image bg bath23-1 = "locations/bath/bath23-1.jpg"
image bg bath23-2 = "locations/bath/bath23-2.jpg"
image bg bath24_1 = "locations/bath/bath24-1.jpg"
image bg bath24_2 = "locations/bath/bath24-2.jpg"
image bg bath25-1 = "locations/bath/bath25-1.jpg"
image bg bath25-2 = "locations/bath/bath25-2.jpg"
image bg bath26 = "locations/bath/bath26.jpg"
image bg bath27_1 = "locations/bath/bath27-1.jpg"
image bg bath27_2 = "locations/bath/bath27-2.jpg"
image bg bath28 = "locations/bath/bath28.jpg"
image bg bath29 = "locations/bath/bath29.jpg"

image bg bath30-1 = "locations/bath/bath30-1.jpg"
image bg bath30-2 = "locations/bath/bath30-2.jpg"
image bg bath30-3 = "locations/bath/bath30-3.jpg"

init:
    if persistent.mod_disable_original_events == False:
        $ event("bath1", "act == 'bath' and deviance < 5", event.choose_one('bath'), priority=200)
        $ event("bath2", "act == 'bath' and inhibition <= 85", event.choose_one('bath'), priority=190)
        $ event("bath3", "act == 'bath' and deviance > 5", event.choose_one('bath'), priority=200)
        $ event("bath4", "act == 'bath' and deviance < 20", event.choose_one('bath'), priority=200)
        $ event("bath5", "act == 'bath' and inhibition <= 80 and deviance >= 5", event.choose_one('bath'), priority=190)
        $ event("bath6", "act == 'bath' and inhibition <= 80 and deviance >= 10", event.choose_one('bath'), priority=190)
        $ event("bath7", "act == 'bath' and inhibition <= 85", event.choose_one('bath'), priority=190)
        $ event("bath8", "act == 'bath' and inhibition <= 85 and deviance < 15", event.choose_one('bath'), priority=190)
        $ event("bath9", "act == 'bath' and inhibition <= 80", event.choose_one('bath'), priority=200)
        $ event("bath10", "act == 'bath' and inhibition <= 70", event.choose_one('bath'), priority=170)
        $ event("bath11", "act == 'bath' and inhibition <= 85 and deviance < 20", event.choose_one('bath'), priority=180)
        $ event("bath12", "act == 'bath' and deviance > 20", event.choose_one('bath'), priority=180)
        $ event("bath13", "act == 'bath' and inhibition <= 85", event.choose_one('bath'), priority=180)
        $ event("bath14", "act == 'bath' and deviance > 20", event.choose_one('bath'), priority=180)
        $ event("bath15", "act == 'bath' and morale > 50 and deviance > 75 and new_game_plus == True", event.choose_one('bath'), priority=150)
        $ event("bath16", "act == 'bath' and inhibition <= 80", event.choose_one('bath'), priority=170)
        $ event("bath17", "act == 'bath' and inhibition > 90", event.choose_one('bath'), priority=200)
        $ event("bath18", "act == 'bath' and inhibition <= 80 and deviance > 20", event.choose_one('bath'), priority=170)
        $ event("bath19", "act == 'bath' and inhibition <= 70 and deviance > 35", event.choose_one('bath'), priority=160)
        $ event("bath20", "act == 'bath' and inhibition <= 97", event.choose_one('bath'), priority=190)
        $ event("bath21", "act == 'bath'", event.choose_one('bath'), priority=200)
        $ event("bath22", "act == 'bath' and inhibition <= 95", event.choose_one('bath'), priority=200)
        $ event("bath23", "act == 'bath' and deviance > 0", event.choose_one('bath'), priority=180)
        $ event("bath24", "act == 'bath' and inhibition <= 85", event.choose_one('bath'), priority=180)
        $ event("bath25", "act == 'bath' and deviance > 4 and inhibition < 95", event.choose_one('bath'), priority=170)
        $ event("bath26", "act == 'bath' and inhibition > 85", event.choose_one('bath'), priority=200)
        $ event("bath27", "act == 'bath' and inhibition <= 80", event.choose_one('bath'), priority=170)
        $ event("bath28", "act == 'bath' and inhibition <= 80 and deviance > 0", event.choose_one('bath'), priority=170)
        $ event("bath29", "act == 'bath' and inhibition <= 75 and deviance > 5", event.choose_one('bath'), priority=160)
        $ event("bath30", "act == 'bath'", event.choose_one('bath'), priority=170)

label bath1:

    scene bg bath1 with fade
    pov "I'm not really sure I want to know what's going on here."
    return


label bath2:

    $ randImg = renpy.random.choice(["1", "2", "3"])
    $ renpy.show("bg bath2_"+randImg)
    with fade

    "As you sneak into the bath you catch a glimpse of a few girls playing around."
    $ deviance += 1
    return


label bath3:

    $ randImg = renpy.random.choice(["1", "2", "3"])
    $ renpy.show("bg bath3_"+randImg)
    with fade

    'After sneaking in, you get a great view of a girl {i}cleaning{/i} another girl.'
    $ inhibition -= 1
    return


label bath4:

    scene bg bath4 with fade
    'You walk in and see several good looking girls in the bath, what do you do?'
    menu:
        "Walk away":
            "You quickly walk away without being noticed."

        "Join them!":
            if ((inhibition - renpy.random.randint(0,5)) > 75 and povGender == 'male' or (renpy.random.randint(0,10) - inhibition ) > 75 and povGender == 'female'):
                "After the girls notice you, they start to scream and throw stuff at you! You run away as fast as you can."
                $ reputation -= 1
                $ morale -= 1
            else:
                "After the girls notice you, they ask about your day and what business you have in the baths, after chatting for a while, they politely ask you to leave."
                $ inhibition -= 1
                $ morale += 1
    return


label bath5:
    $ randImg = renpy.random.choice(["1", "2", "3"])
    $ renpy.show("bg bath5_"+randImg)
    with fade
    "While wandering around the bathhouse you suddenly bump into two girls."
    pov "Oh, sorry girls, I didn't know anyone was here."
    "The girls barely try to hide themselves and assure you that it's alright as long as you don't stay too long. You take a quick look at them before you walk away."
    $ inhibition -= 1
    return


label bath6:
    "As you sneak into the baths, you suddenly hear a faint voice. You start walking towards it and you hear a girl talking."

    scene bg bath6-1 with fade
    girl "So naughty, sneaking in here, what if someone found out?"
    guy "Don't worry, no one's gonna disturb us. Let's just have some fun."
    girl "* giggle * Are you sure?"
    scene bg bath6-2
    girl "Ahh... Be gentle..."
    "You can see how the guy massages the girls breast and how he enjoy teasing her. The girl doesn't really look as pleased and seems to be worried someone might find out."
    girl "Mhmm, we can't do this here! Ah, no, not there!"
    "The guy pushes her hands away and starts touching her private parts. Even if she says no it's obvious she enjoys it."
    if deviance > 15 or inhibition < 70:
        girl "Ahh, please..."
        "The girl leans over the guy and whispers in his ear, it's a shame you can't hear her words."
        girl "Please?"
        "She seems to have changed her mind and takes a seat on the guy, slowly sliding down on his cock."

        scene bg bath6-3
        girl "Ahh!"
        girl "Yes!"
        "Each time she slides down his cock they both get louder and louder."
        girl "Mhmm, Ahh... Ah!"

        scene bg bath6-4
        "He starts fondling her breast and she is getting really loud and even though you enjoy the show and you decide to walk away before someone hears them and might find you."
        python:
            if renpy.random.randint(1, 2) == 1:
                red_orb += 1
            inhibition -= 1
            deviance += 1
    else:
        girl "I'm sorry, we can't do this here."
        guy "Come on, you can't just tease me like this!"
        girl "Don't worry, I'll repay you after school."
        $ deviance += 1
    return

label bath7:

    scene bg bath7 with fade
    "Hmm, I guess they're only helping each other out with a nice back rub after class..."
    $ inhibition -= 1
    $ morale += 1
    return

label bath8:

    scene bg bath8 with fade
    "You meet the eyes of a lonely girl having a soothing bath. Although you clearly sense the inconvenience of the situation, her beautiful blue eyes won't let you go."
    menu:
        "Leave?":
            "You tell her you're sorry and leave her alone."
            $ morale += 1

        "Just a few more seconds?":
            'As her blushing starts to spread, you clear your throat and mumble something about "the wrong door", then make for the exit.'
            $ inhibition -= 1
    return


label bath9:

    $ randImg = renpy.random.choice(["1", "2"])
    $ renpy.show("bg bath9_"+randImg)
    with fade
    "To some, having a bath can be a very private moment."
    $ morale -= 1
    return


label bath10:

    scene bg bath10 with fade
    girl "Hi [povTitle] [povLastName].\nWhen I have a bath, I always bring my two best friends."
    "You assume she's talking about the rubber ducks..."
    girl "They help me relax, and besides, they are super cute! Don't you think?"
    menu:
        "Compliment her ducks.":
            pov "They sure are cute."
            $ morale += 1
            $ inhibition -= 1

        "Compliment her other two friends.":
            pov "I think I prefer your other two cuties."
            "She giggles and you realize how long you've been standing there."
            $ inhibition -= 1
            $ deviance += 1

        "Make an excuse and leave.":
            pov "Sorry to intrude, gotta go."
            "Some of these girls are a bit childish, to say the least."
            $ inhibition += 1
            $ deviance -= 1
    return


label bath11:

    scene bg bath11-1 with fade
    "You enter one of the smaller rooms only to find it already occupied."
    girl "Eek!"
    menu:
        "You leave as quickly as you can.":
            scene bg bath11-3
            pov "I'm terribly sorry!"
            girl "How awkward!"
            $ morale -= 1

        "Oh, I didn't realize the others left already.":
            girl "The others? ..."
            pov "Yes, I better go find them, bye."
            girl "B - bye."
            $ inhibition -= 1

        "There you are!":
            scene bg bath11-3
            girl "W - what..? You were looking for... for me?"
            pov "But of course, the other girls told me that you've worked really hard lately."
            girl "They... they did?"
            pov "Yeah. I just wanted to say: Keep up the good work!"
            scene bg bath11-2
            girl "T - thanks, I just didn't believe that anybody noticed..."
            menu:
                "You are what this school is all about, remember that.":
                    $ morale += 1
                    girl "Gee [povTitle] [povLastName], you're the greatest!"
                    "As you leave, you feel positive vibes all around."

                "How can anybody NOT notice you? I mean, you really are hot!":
                    scene bg bath11-3
                    girl "Ehm... Thanks [povTitle] [povLastName]."
                    "As you leave, you wonder if that was a bit too heavy."
                    $ inhibition += 1

                "Believe me, I notice.":
                    scene bg bath11-4
                    girl "..."
                    "As you leave, she sighs and drifts away in dreams."
                    $ deviance += 1
                    $ inhibition -= 1
    return


label bath12:

    scene bg bath12 with fade
    "Oops! Is that her guardian angel? I don't even know anymore..."
    $ inhibition -= 1
    $ morale += 1
    return


label bath13:

    scene bg bath13 with fade
    "All bodies look different, that's just how it is. However, girls will never stop comparing."
    $ inhibition -= 1
    $ morale -= 1
    return


label bath14:

    scene bg bath14 with fade
    "It's a dreamy feeling, floating around all naked without as much as a single problem on your mind."
    $ morale += 1
    return


label bath15:

    scene bg bath15:
        pos (0.0, 0.0)
        linear 7.0 pos (-0.5, 0.0)
    with fade
    girls "*giggle* We've been waiting for you principal [povLastName]. The water is perfect, won't you join us?"
    "Ah, those licentious girls! How the hell am I supposed to leave?!"
    menu:
        "Fuck this.":
            "I'm gonna get into so much trouble for even thinking about joining them!"
            girls "Aw, why are you leaving?"
            $ inhibition += 1
            $ deviance -= 1

        "Fuck me.":
            $ deviance += 1
            $ behavior -= 1
            "I really am a horny bastard but can I get away with this?"
            girls "Naw, he's trying to hide it behind his hands."

        "Fuck them.":
            $ deviance += 1
            $ inhibition -= 1
            $ reputation -= 1
            "I'll show the little fuck sluts. They'll get it good and I won't stop until they're all spray-painted."
            girls "*gasp* I - it's... HUGE..!"
            pov "Ah shut up. Open wide - here I come."
    return


label bath16:

    scene bg bath16-1 with fade
    "On your way taking a soothing bath it seems you mixed up the timetable, and mixed it up good! A group of girls bash right into you and you end up on your back with the girls on top."
    menu:
        "Gee this is really embarrassing!":
            scene bg bath16-2
            girl "Oh! [povTitle] [povLastName], did you hurt yourself?"
            pov "I'm fine, hope you girls are alright?"
            girl "There must have been a mix up with the time table!"
            pov "Yeah, that's how it happened!"
            $ inhibition -= 1
            $ deviance -= 1

        "Oh sorry! Lucky you got a soft landing, eh?":
            girls "Ah! [povTitle] [povLastName]! We didn't know you were here..."
            pov "Guess the timetable's pretty mixed up."
            girl "Uh... must be!"
            $ deviance += 1
            $ behavior -= 1

        "Happy boner time!" if new_game_plus == True:
            pov "Uuuh!"
            girl "[povTitle] [povLastName]!"
            pov "Aaah!"
            girl "Are you hurt? I think I fell on your leg!"
            pov "That's not my leg."
            scene bg bath16-3
            girl "WHOA!"
            pov "*giggle*"
            $ deviance += 1
            $ inhibition -= 1
    return


label bath17:

    $ randImg = renpy.random.choice(["1", "2"])
    $ renpy.show("bg bath17_"+randImg)
    with fade

    girl "You really shouldn't be here [povTitle] [povLastName]."
    if renpy.random.randint(1,4) == 1:
        $ reputation -= 1
    $ morale -= 1
    return


label bath18:

    scene bg bath18 with fade
    "Two girls are fooling around in the steam. When you enter, the one on top sees you in the corner of her eye and gives you a little wink."
    menu:
        "Return the wink and leave them alone.":
            "Let them have their fun. Practice makes perfect, eh? "
            $ morale += 1
            $ deviance += 1

        "Clear your throat loud and clear.":
            "They both jump up and look as if they're caught in the act of doing something really naughty. You shake your finger at them and then leave them to their guilt."
            $ inhibition += 1
            $ deviance -= 1

        "Looksie touchy!" if new_game_plus == True:
            "Before you leave, you sneak up behind the girls and softly put your hand on the top girl's butt. She gasps but doesn't reveal your presence."
            $ inhibition -= 1
            $ deviance += 1
    return


label bath19:

    scene bg bath19-1 with fade
    girl "Hello there [povTitle] [povLastName], I thought you'd never show up. Would you like to join me for a nice cup of sake?"
    menu:
        "Be still my heart.":
            pov "As much as I would like to, I'm afraid it's impossible."
            girl "Are you sure? Must be awfully tough to be a principal. All work and no play?"
            pov "Hrm, I - I should go. I'm very flattered though, believe me."
            girl "Oh well. Guess I'll have to wait and see if time is on my side."
            pov "Eh, I guess so."
            "She blows you a kiss just before you leave."

        "What is she doing?":
            pov "Listen here young lady. I understand that it can be confusing sometimes when you are growing from girl to woman. Never the less, I can't accept you taking liberties like this."
            girl "It... You..."
            pov "Look, leave the sake here, get your towel and just walk away."
            girl "It... wasn't supposed to... end like this..."
            pov "Life teaches you stuff and sometimes it hurts. Good side is you always bounce back. Okay kid?"
            girl "I - I'll be on my way."
            pov "Good girl."
            $ behavior += 1

        "Drinking? In school? Hell yeah!" if new_game_plus == True:
            pov "I'd love to, kitty cat."
            girl "Mmm, come sit here with me."
            scene bg bath19-2
            pov "Ah... You can't believe how much I've had to do lately!"
            girl "Poor thing. Need someone to take care of you? Treat you real nice?"
            pov "Damned right. Here's looking at you, kid."
            scene bg bath19-3
            girl "*giggle* I feel so... you know...mature!"
            pov "Fuck mature."
            girl "Oh..!"
            pov "Now then, let's hear you say: Daddy, there's something wrong with my nipples."
            girl "Say... what?"
            pov "No no no, DADDY, there's something wrong with my nipples."
            girl "O...k... D - Daddy... my nipples... there's something wrong with them..."
            pov "*singing* What's up pussy cat? Who-o-o-o-o-ooooo!"
            $ inhibition -= 1
    return


label bath20:

    if  inhibition > 90:
        scene bg bath20-1 with fade
        "You walk in on a student having a nice, calm bath. She doesn't say anything but pulls her towel closer as her face turns red. "
        pov "Nice day for a bath, eh?"
        girl "I- I guess..."
        $ morale -= 1

    elif inhibition > 80:
        scene bg bath20-1 with fade
        "You walk in on a student having a nice, calm bath. She doesn't say anything but pulls her towel closer as her face turns red. "
        menu:
            "Don't worry, you don't need to hide anything from me." if deviance == 0:
                girl "..."
                "Didn't work this time either..."
                $ morale -= 1

            "Don't worry, you don't need to hide anything from me." if deviance > 0:
                girl "... you pervert.."
                pov "Sorry?"
                girl "You just sneak in here to watch us bathe..."
                menu:
                    "Well, I do enjoy beauty as yourself":
                        girl "..."
                        girl "Alright, take a peek... pervert."
                        scene bg bath20-2
                        pov "Yeah, that's a beauty."
                        $ deviance += 1

                    "No no, I'm just doing my job":
                        girl "Stop lying and get out of here!"
                        $ deviance -= 1
                        $ morale -= 1

            "Sorry, wrong room":
                girl "Yeah..."
                pov "Enjoy your bath."
                $ morale -= 1
    else:
        scene bg bath20-2 with fade
        "You walk in on a student having a nice, calm bath."
        pov "Nice day for a bath?"
        girl "Yeah, nice day for peeking?"
        pov "Yeah, a very nice day."
        $ inhibition -=1
    return


label bath21:

    scene bg bath21-1 with fade
    "In the relaxed environment of the baths, girls open up and forget about the outside world for a while."
    scene bg bath21-2
    $ inhibition -= 1
    return


label bath22:

    scene bg bath22 with fade
    "Seems like team spirit does the job!"
    $ inhibition -= 1
    return


label bath23:

    scene bg bath23-1 with fade
    "Sometimes you need a shoulder to lean on."
    scene bg bath23-2
    python:
        if renpy.random.randint(1,3) == 1:
            deviance += 1
        else:
            morale += 1
    return


label bath24:

    $ randImg = renpy.random.choice(["1", "2"])
    $ renpy.show("bg bath24_"+randImg)
    with fade

    pov "Hey there! How's the water?"
    girl "Oh it's nice and warm!"
    pov "Glad to hear it!"
    python:
        if renpy.random.randint(1,3) == 1:
            inhibition += 1
        else:
            inhibition -= 1
    return


label bath25:

    "You stumble upon a cute looking brunette enjoying herself in a soothing bath."
    scene bg bath25-1 with fade
    girl "Hey [povTitle] [povLastName]!"
    pov "Hello... I'm sorry to disturb your privacy."
    girl "Don't be silly, you couldn't possibly know I was here, right?"
    if deviance < 9:
        "She waves as you leave the room, what a nice girl!"
        $ inhibition -= 1
        return
    else:
        pov "Well, that's true."
        girl "But... eeh... were you planning on having a bath?"
        pov "No no, I was just checking that everything's... fine."
        girl "And?"
        pov "I'm sorry?"
        girl "Is it fine? Silly!"
        menu:
            "Better go before you say something you'll regret":
                pov "Have a... nice bath."
                "She gives you a long gaze as you leave the bath."

            "It's been a long day, I deserve a treat." if deviance > 15:
                pov "Well, I can't really see if it's fine. Something is clouding my vision."
                girl "Oh, that's too bad. Better do something 'bout it then."
                scene bg bath25-2
                girl "Is that better?"
                pov "Yeah... everything's much clearer now."
                $ inhibition -= 1
        return


label bath26:

    scene bg bath26 with fade
    girl "Oh!"
    "She quickly covers up and seems to feel really awkward about the situation."
    menu:
        "Leave as smoothly as you can":
            pov "Sorry!"
            girl "Eeh, it's ok."

        "You didn't do anything wrong":
            pov "Huh?"
            girl "Do you mind?"
            pov "Hey, gotta check the perimeter, take it easy will you?"
            girl "..."
            $ morale -= 1
            $ inhibition -= 1

        "Yawn" if evil_points > 0:
            pov "Cunt."
            girl "WHAT?"
            pov "Blunt, really blunt of me to just bash in like this."
            girl "Hmpf."
            $ morale -= 2
    return


label bath27:
    $ randImg = renpy.random.choice(["1", "2"])
    $ renpy.show("bg bath27_"+randImg)
    with fade
    "In water, all big things get weightless."
    $ inhibition -= 1
    return


label bath28:

    scene bg bath28 with fade
    "Anticipation? You betcha!"
    $ inhibition -= 1
    return


label bath29:

    scene bg bath29 with fade
    "What starts out innocent can escalate sooner than you think, young lady!"
    python:
        if renpy.random.randint(1,2) == 1:
            inhibition -= 1
        else:
            deviance += 1
    return


label bath30:

    if inhibition > 80:
        scene bg bath30-1:
            pos (0.0, 0.0)
            linear 1.65 pos (0.0, -0.25)
            linear 0.65 pos (0.0, -0.25)
            linear 1.65 pos (0.0, -0.0)
        with fade
        "Some girls are too shy to bathe naked."
        $ inhibition += 1
    else:
        if renpy.random.randint(1,2) == 1:
            scene bg bath30-2:
                pos (0.0, 0.0)
                linear 6.6 pos (0.0, -1.0)
                linear 0.1 pos (0.0, -1.0)
                linear 6.6 pos (0.0, -0.0)
            with fade
        else:
            scene bg bath30-3:
                pos (0.0, 0.0)
                linear 10.0 pos (0.0, -1.5)
                linear 0.1 pos (0.0, -1.5)
                linear 8.6 pos (0.0, -0.2)
            with fade
        "These baths are sure relaxing for both body and eyes, eh, soul."
        $ inhibition -= 1
    return


