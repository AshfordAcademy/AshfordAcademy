image bg cheerleader_club1 = "screens/cheerleader_club/cheerleader_club1.jpg"
image bg cheerleader_club2 = "screens/cheerleader_club/cheerleader_club2.jpg"
image bg cheerleader_club3-1 = "screens/cheerleader_club/cheerleader_club3-1.jpg"
image bg cheerleader_club3-2 = "screens/cheerleader_club/cheerleader_club3-2.jpg"
image bg cheerleader_club4-1 = "screens/cheerleader_club/cheerleader_club4-1.jpg"
image bg cheerleader_club4-2 = "screens/cheerleader_club/cheerleader_club4-2.jpg"
image bg cheerleader_club5 = "screens/cheerleader_club/cheerleader_club5.jpg"
image bg cheerleader_club6 = "screens/cheerleader_club/cheerleader_club6.jpg"

init:
    if persistent.mod_disable_original_events == False:
        $ event("cheerleader_club1", "act == 'cheerleader_club'", event.choose_one('cheerleader_club'), priority=200)
        $ event("cheerleader_club2", "act == 'cheerleader_club'", event.choose_one('cheerleader_club'), priority=200)
        $ event("cheerleader_club3", "act == 'cheerleader_club'", event.choose_one('cheerleader_club'), priority=200)
        
        #TODO: Actually add events!
        $ event("cheerleader_club4", "act == 'cheerleader_club'", event.choose_one('cheerleader_club'), priority=200)
        $ event("cheerleader_club5", "act == 'cheerleader_club'", event.choose_one('cheerleader_club'), priority=200)
        $ event("cheerleader_club6", "act == 'cheerleader_club'", event.choose_one('cheerleader_club'), event.depends("cheerleader_club5"), priority=200)

label cheerleader_club1:
    
    scene bg cheerleader_club1 with fade
    "I'm sure these girls keep the morale high."
    $ morale += 1
    return


label cheerleader_club2:
    
    scene bg cheerleader_club2 with fade
    "These girls really help our team give it all!"
    $ morale += 1
    return


label cheerleader_club3:
    
    if reputation < 40:
        scene bg cheerleader_club3-1 with fade
        "Seems like our cheerleaders are having some problems with their new routine."
        $ morale -= 1
    else:
        scene bg cheerleader_club3-2 with fade
        if povGender == "male":
            "I could observe these girls all day long. Those short skirts and petite breast jumping up and down... Up and down..."
        else:
            "girls" "Go Ashford! *clap* *clap* Go Ashford! *clap* *clap*"
    $ morale += 1
    return

    
label cheerleader_club4:
    
    scene bg cheerleader_club4-1 with fade
    "What's this?"
    girl "N-no! I can explain!"
    pov "Take it easy. Looks like someone left in a hurry?"
    girl "B-but it's not what it looks like!"
    pov "The school policy is pretty strict when it comes to immoral behaviour, but you know that."
    girl "I-I'm so... SORRY!"
    pov "This is a serious matter young lady."
    menu:
        "It takes two to tango.":
            "Tell me who the boy was, I will talk with him myself while you head to the nurse and have a long overdue lecture about birds and bees."
            girl "I-I feel so... cheap!"
            pov "Now now, don't think to much in the wrong direction. Head to the nurse right away, understood? I'll give her a call so she'll be expecting you."
            girl "Ok..."
            "She's going to be okay and there will be a while before she tries something like this again." 
            $ deviance -= 2
    
        "That boy...":
            "Now, give me the boy's name and I'll let you run along."
            girl "But p-promise that you won't expel him!"
            pov "You are not in the position to demand anything young lady. Give me his name and go have a shower."
            girl "A-alright..."
            "I know they're young and all, but someone's gotta teach them some basic behaviour and manners!!"
            $ deviance -= 1
            
        "So girls just want to have fun, eh?" if povGender == "Male":
            pov "Relax, I'm not gonna make a big fuzz about this."
            girl "Y-you're not?"
            pov "Everybody makes mistakes from time to time."
            girl "I-I guess so."
            pov "What's important here is to accept, forgive and forget, right?"
            girl "Uh, right!"
            pov "Good girl. So I accept what you've done, it's pretty obvious that I can't do anything about what happened."
            girl "I-I guess not."
            pov "I mean, it's not like I can alter time and space."
            girl "No, heh."
            pov "And there's no reason for me to hold a grudge against you since, well, life is too short and all."
            girl "Oh, you're so kind!"
            pov "And since life is so short, we gotta do everything we can to forget our worries so that we can make room in our lives for more positive experiences. We have to move on."
            girl "[povTitle] [povName], you're a very smart principal!"
            pov "Thank you. But I can't solve everything on my own, you understand that right? Though I'm kind and smart and everything, I still need your help."
            girl "You need my help? But, how can I help?"
            pov "See, that's the part I was hoping I could show you."
            "At first, she was concerned that you where going to hurt her..."
            "But after explaining it all in a very convincing manner, she realized that she'd be better off if she just gave you what you wanted."
            scene bg cheerleader_club4-2
            pov "That's right, you just push back against me. Such a good girl, mmh, sweet girl."
            girl "Ah, go easy! I'm not that wet and -"
            pov "Aah you make me so horny, you have such delicate skin and you smell so good!"
            girl "Oh, ah, it... it hurts a little but it's ok."
            "Hearing her moan and knowing that you probably enjoy this a hell of a lot more than she can even pretend... Well it's just so fucking great!"
            $ deviance += 1
    return


label cheerleader_club5:
    
    scene bg cheerleader_club5 with fade
    girl "Oh [povTitle] [povName]! Have you come to watch us practise?"
    pov "Hello girls, how's it going?"
    girl "Just swell! Since we won the regional cup, coach said that we should try building our routine from a more trademark point of view."
    pov "Sounds interesting."
    girl "It is! We've come up with an idea that everybody will love."
    pov "Tell me!"
    girl "We're gonna be the ASHFORD KITTENS!"
    menu:
        "Everybody loves cats!":
            pov "Sounds really great!"
            girl "I know!"
            "What a bunch of productive, cute students! "
            $ morale += 1

        "Are you kitten-ing me?":
            pov "Wow, sounds pretty lame."
            girl "How could you actually say such a thing? We're talking about cats!"
            pov "Hmm, on second thought, everybody loves cats."
            girl "That's the spirit! I knew you had it in you!"
            "You steered away from cat-astrophy."
            $ morale -= 1

        "What about ducks?" if new_game_plus == True:
            pov "I got it!"
            girl "What is it?"
            pov "I know how you can strengthen your appearance as a squad!"
            girl "OMG tell me tell me tell me!"
            pov "It's so frickin' cool, I nearly burst out in tears!"
            girl "This is such an YOLO-moment!! Tell me already!"
            pov "Hold on to your mittens! Hear me out!"
            girl "SPIT IT OUT!"
            pov "DUCK!"
            girl "Look out!"
            pov "NO! I mean like QUACK!"
            girl "Beware! Doctors without license!"
            pov "NOOO! I mean like in the water!"
            girl "It came from the sea! Run for your lives!"
            pov "This is going nowhere!"
            girl "Oh no! We can't move!"
            pov "Forget I said anything!"
            girl "Total amnesia!"
            pov "Keep practising girls!!"
            girl "Who are you?"
            "A lame duck..."
    return


label cheerleader_club6:

    scene bg cheerleader_club6 with fade
    "Cheerleading can sure boost the spirit of any team that... Wait a minute."
    pov "What happened to the kitten concept?"
    girl "Kittens are sooo yesterday!"
    pov "Literally speaking..."
    girl "Now we're the Ashford BATS 'N' ANGELS!"
    pov "Ok..."
    girl "We had this two great alternatives, so we simply decided to smack them together!"
    pov "I'm not sure it makes it twice as good though."
    girl "TWO TIMES THE POW!"
    pov "Well, as long as it works for you."
    girl "Thanks! Go Bats 'n' Angels!"
    return

