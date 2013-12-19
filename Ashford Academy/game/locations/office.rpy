image bg office1-1 = "locations/office/office1-1.jpg"
image bg office1-2 = "locations/office/office1-2.jpg"
image bg office2 = "locations/office/office2.jpg"
image bg office3-1 = "locations/office/office3-1.jpg"
image bg office3-2 = "locations/office/office3-2.jpg"
image bg office4 = "locations/office/office4.jpg"
image bg office5 = "locations/office/office5.jpg"
image bg office6 = "locations/office/office6.jpg"
image bg office7 = "locations/office/office7.jpg"
image bg office8 = "locations/office/office8.jpg"
image bg office9 = "locations/office/office9.jpg"
image bg office10 = "locations/office/office10.jpg"
image bg office11-1 = "locations/office/office11-1.jpg"
image bg office11-2 = "locations/office/office11-2.jpg"
image bg office12 = "locations/office/office12.jpg"
image bg office13 = "locations/office/office13.jpg"
image bg office14 = "locations/office/office14.jpg"
image bg office15 = "locations/office/office15.jpg"
image bg office16 = "locations/office/office16.jpg"
image bg office17 = "locations/office/office17.jpg"
image bg office18 = "locations/office/office18.jpg"
image bg office19-1 = "locations/office/office19-1.jpg"
image bg office19-2 = "locations/office/office19-2.jpg"
image bg office20 = "locations/office/office20.jpg"
image bg office21 = "locations/office/office21.jpg"
image bg office22 = "locations/office/office22.jpg"

init:
    if persistent.mod_disable_original_events == False:
        $ event("office1", "act == 'office' and morale > 30", event.choose_one('office'), priority=190)
        $ event("office2", "act == 'office' and morale < 35", event.choose_one('office'), priority=200)
        $ event("office3", "act == 'office' and deviance >= 45 and pda_rules == 'pda_expulsion'", event.once(), priority=100)
        $ event("office4", "act == 'office'", event.choose_one('office'), priority=200)
        $ event("office5", "act == 'office'", event.choose_one('office'), priority=200)
        $ event("office6", "act == 'office'", event.choose_one('office'), priority=200)
        $ event("office7", "act == 'office'", event.choose_one('office'), priority=200)
        $ event("office8", "act == 'office' and morale > 30", event.choose_one('office'), priority=190)
        $ event("office9", "act == 'office' and pda_rule_level > 2", event.choose_one('office'), priority=190)
        $ event("office10", "act == 'office' and morale > 30", event.choose_one('office'), priority=190)
        $ event("office11", "act == 'office' and deviance > 20 and inhibition < 90", event.choose_one('office'), priority=180)
        $ event("office12", "act == 'office' and behavior < 30", event.choose_one('office'), priority=180)
        $ event("office13", "act == 'office' and deviance > 45 and behavior < 30", event.choose_one('office'), priority=160)
        $ event("office14", "act == 'office' and behavior < 30", event.choose_one('office'), priority=180)
        $ event("office15", "act == 'office' and deviance > 30 and inhibition < 70", event.choose_one('office'), priority=170)
        $ event("office16", "act == 'office' and morale > 30", event.choose_one('office'), priority=180)
        $ event("office17", "act == 'office' and deviance < 5 ", event.choose_one('office'), priority=180)
        $ event("office18", "act == 'office' and deviance > 40 and inhibition < 85", event.choose_one('office'), priority=170)
        $ event("office19", "act == 'office' and deviance > 50 and inhibition < 60", event.choose_one('office'), priority=150)
        $ event("office20", "act == 'office' and deviance > 75 and inhibition < 50", event.choose_one('office'), priority=100)
        $ event("office21", "act == 'office' and deviance > 50 and inhibition < 50 and evil_points > 0", event.choose_one('office'), priority=110)
        $ event("office22", "act == 'office' and morale > 50", event.choose_one('office'), priority=170)
        $ event("office23", "act == 'office' and deviance > 20 and class15_sex == True", event.choose_one('office'), event.depends("class15"), priority=120)

label office1:
    
    if deviance > 0:
        scene bg office1-2 with fade
        "Working with her {i}always{/i} puts a smile on my face."
    else:
        scene bg office1-1 with fade
        pov "I'm very happy to have such dedicated teachers."
        $ morale += 1
    return


label office2:
    
    scene bg office2 with fade
    pov "Well, even teachers need a break sometimes."
    return


label office3:
    
    scene bg office with fade
    "I just got these two girls sent to my office. I've been told that they have been involved in immoral behavior."
    pov "So tell me girls, how come you are here?"
    girl1 "..."
    girl2 "Well... *Looks at the other girl*"
    girl1 "We were just fooling around in the showers..."
    girl1 "And when one of the teachers found out she got all crazy, saying we are both bad girls and stuff."
    pov "And that's why you where sent here? Just a bit of fun in the showers?"
    girl2 "Umm, we... kinda... did it..."
    girl1 "*stare*"
    pov '{i}It?{/i} Would you like to explain further?'
    girl1 "We were just having some fun! Nothing more, please don't expel us!"
    girl2 "I just... Can you please... Don't tell my parents about this... Please?"    
    menu:
        "I'm sorry, but in this school we have rules to follow.":
            girl1 "But we did nothing wrong!"
            pov "I'm very sorry girls, but you did this to yourselves."
            girl2 "But... Will you tell our parents?"
            pov "If you prefer, I can expel you for something else?"
            girl1 "*stare*"
            girl2 "Would you..?"
            pov "Sure, I will work something out. Go meet Susan at the end of the day and she will have the papers."
            girl2 "Oh, thank you! Thank you so much!"
            girl1 "*stare*"
            $ population -= 2
            $ behavior += 3
            $ morale -= 1

        "Well, we might be able to work something out...":
            girl2 "Really?"
            pov "Yeah, I doesn't sound to me like you did {i}anything{/i} wrong or bad."
            girl1 "Yeah, I've said so all the time, but no one listens! We didn't do anything at all!"
            girl2 "*stare*"
            pov "Is that so? Hmm, and you just got me interested."
            "Both girls are looking at each other confused."
            girl2 "Umm, [povTitle] [povLastName], what do you mean?"
            pov "Well, to be honest, I was interested in what you girls did and maybe you could let me be a judge first hand."
            girl1 "{b}WHAT?!{/b} You pervert! Why would we ever do something like that with you!"
            girl2 "*stare*"
            girl2 "Umm..."
            pov "So you did do something? Then you need to be expelled."
            girl2 "No... please..."
            girl1 "But we can't!"
            girl2 "What... would you like us to do...?"
            girl1 "You can't be serious?!"
            pov "I would like you to get down on your knees and ask for forgiveness."
            "One of the girls quickly gets up from the chair and sits down on the floor."
            girl2 "Please forgive me, I don't know why I did it. I'm very sorry."
            girl1 "Heh, I don't think that's what he meant..."
            pov "Smart girl there. Let's ask this one for forgiveness."
            "Both girls follow you with their eyes as you stand up."
            girl2 "Do... you want us... to..."
            "You slowly unzip your pants while you look them in their eyes."
            pov "Unless, of course, you prefer to be expelled."
            "While you where talking both girls have moved in front of you."

            scene bg office3-1 with fade
            pov "Here, give me a reason to let you stay in this school and not to tell your parents."
            girl1 "Are we really doing this..?"
            girl2 "*slurp*"
            girl2 "I've never done this before, but *slurp* I hope..."
            pov "Don't worry, just start with doing your best."
            "It looks like one of the girls are about to cry."
            pov "Don't worry, just take turns... Ahh..."
            girl1 "Is this... *slurp* ok?"
            "You enjoy the girls sucking your dick, watching how their pretty little mouths are playing around."
            girl2 "I... *slurp* Really... Do my best..."
            girl1 "..."
            girl1 "Me... too... *sob*"
            "Watching them so close to tears only makes it better."

            scene bg office3-2
            pov "Ahhh..."
            "The girls gasp as your cum comes flying over them."
            girl2 "Ahh!"
            girl1 "..."
            girl2 "So, no telling, right?"
            pov "Ah, good girls. I {i}knew{/i} you did nothing wrong."
            girl1 "*stare*"
            girl2 "Yeah...But no telling our parents... Right?!"
            pov "Yeah, yeah, just clean yourself and leave. We are done for today."
            girl1 "*sob*"
            "You watch them clean off your cum and silently leave."
            $ deviance += 2
            $ red_orb += 1
    return


label office4:
    
    scene bg office4 with fade
    "A teachers assistant is preparing study materials for class."
    $ academics += 1
    return


label office5:
    
    scene bg office5 with fade
    "On your way to office you meet one of the teachers. She seems to be picking up a pen and while doing that, giving you a nice view."
    "She see your eyes wander and immediately starts to blush. You tell her:"
    menu:
        "Nice view!":
            if inhibition < 70:
                teacher "You like them, don't you?"
                pov "Of course, it's one of your bigger assets"
                teacher "*giggle*"
                $ deviance += 1
            elif inhibition < 90:
                teacher "Oh... Thank you [povTitle] [povLastName]."
                $ inhibition -= 1
            else:
                teacher "Umm... I have to go." 
                $ morale -= 1

        "Sorry, It wasn't my intention to stare." if inhibition > 70:
            teacher "Don't worry [povTitle] [povLastName], I understand."
            "She smiles and walk away."
            $ morale += 1
            
        "Sorry, It wasn't my intention to stare." if inhibition <= 70:
            teacher "Oh... you don't like them?"
            "She smirks and walk away."
            $ morale -= 1
    return
            
            
label office6:
    
    scene bg office6 with fade
    if deviance < 25:
        "You bump into a girl waiting for counseling. Just because you're bright and beautiful doesn't mean you sleep well at night."
    else:
        "You know you're supposed to help and guide them, but sometimes you just want to see what they taste like."
    return


label office7:
    
    scene bg office7 with fade
    if deviance < 5:
        'Workdays can be long and students can be quite demanding. Some "mew time" sure hits the spot.'
    else:
        "When you've got a few minutes to yourself, playing with your pussy can be really soothing."
    return
    

label office8:
    
    scene bg office8 with fade
    "The spirit among the teachers is good. You can tell that they put pride into their work."
    $ morale += 1
    return
    

label office9: 
    
    scene bg office9 with fade
    "As you enter the teachers office you see two students waiting to meet a teacher."
    menu:
        "Ignore them":
            pass
        "Ask why they are here":
            girl "Umm, one of the teachers wanted to see us."
            guy "Yeah, seems like they don't like that we're a pair..."
            menu:
                "Tell them about the school policy":
                    pov "You should know that you're not allowed to show off any public display of affection."
                    guy "Yeah, but that makes no sense! I can have a girlfriend if I want!"
                    pov "Indeed, but don't go around showing her off, you two can do whatever you want as long as you're not in school. We have rules for a reason and in time you will understand this."
                    guy "..."
                    $ morale -= 1
                    $ inhibition += 1
                
                "Take care of it for them":
                    "Oh, young love should not be punished! I'll take care of this for you, but next time don't show off in public."
                    girl "Okay, thank you [povTitle] [povLastName]!"
                    guy "Yeah, thanks [povLastName]!"
                    $ morale += 1
                    $ inhibition -= 1
                
                "Have some fun and blame the guy" if new_game_plus == True:
                    pov "So you young man have been taking advantage of this young, innocent girl?"
                    guy "What? No!"
                    pov "Are you telling me that this cute face has taken advantage of you?"
                    guy "No, no! No one has taken advantage of anyone!"
                    girl "Umm, we actually like each other..."
                    pov "That's cute young girl, but you understand, this kid just wants you for your body and can't comprehend your needs."
                    guy "HEY! What do you know about that!?"
                    pov "Don't talk back to me."
                    guy "Don't talk shit about me then!"
                    pov "That's nice, you just got yourself half a ticket to expulsion, do you want the other half as well?"
                    guy "..."
                    pov "That's more like it.\nNow Miss, young girls like you need an older man who actually understands what you need. This is why we have this policy."
                    "You can feel the intense stare of the guy."
                    girl "But... Um... We're in love..."
                    pov "I understand that you feel that way, but unfortunately most young men are unable to feel what you call love. Most of them feel lust and confuse the two."
                    guy "That's not-"
                    "You cut him of with just a stare."
                    pov "Love is when you see a person and the world stops. You want to give everything and just stay close to that special one. Is that what you feel Miss?"
                    girl "I guess..."
                    pov "That's unfortunate since what this young man feels is lust. Lust is a deviant feeling, wanting to rip your clothes off and do unmentionable things to your body."
                    "You can clearly see her embarrassed face so you go on."
                    pov "Has he not asked you to do such things?"
                    girl "Well... Ummm..."
                    guy "I... Uh..."
                    pov "Now now young man, no need to explain yourself."
                    "The girl turns to the guy, looking at him with pleading eyes."
                    girl "Don't you love me?"
                    guy "Of course I do!"
                    girl "But... But... You can't feel that and at the same time ask me to do... things..."
                    "You see the confusion you have created and decide to stop at that."
    return

label office10:
    
    scene bg office10 with fade
    "One of your teachers is about to eat her lunch."
    pov "Bon apetit!"
    $ morale += 1
    return


label office11:
    
    scene bg office11-1 with fade
    "Some teachers seem to have been inspired by the students thoughts of sexiness."
    if new_game_plus == True:
        menu:
            "Compliment the outfit.":
                pov "That's a sexy outfit."
                if povGender == "female":
                    teacher "Thank you [povFirstName], it's a bit risque but I wanted to give it a try."
                    pov "It suits you and your great body perfectly."
                    teacher "*giggle*"
                else:
                    teacher "Oh [povTitle] [povLastName], are you hitting on me?"
                    pov "Maybe I am."
                
            "Smack her ass.":
                scene bg office11-2 with hpunch
                teacher "Ah!"
                if deviance < 50:
                    teacher "What do you think you are doing?!"
                    pov "Well, how do you think you dress?"
                    scene bg office11-1
                    teacher "What does that have to do with anything?!"
                    pov "Everything. If you dress like a whore I treat you like one."
                    scene bg office11-2
                    teacher "WHAT?!"
                    pov "You heard me."
                    $ morale -= 1
                else:
                    teacher "Ah!"
                    teacher "*giggle* Can't keep your hand in place eh?"
                    scene bg office11-1
                    pov "Not when you're in that outfit."
                    teacher "I might use it more often then."
                    
            "Grope her.":
                scene bg office11-2
                if deviance < 50:
                    "You walk around her and push yourself against her while taking a good grab of her breast."
                    teacher "[povTitle] [povLastName] what on earth are you doing?!"
                    pov "Don't you feel what I'm doing?"
                    teacher "Of course I do, but... You can't!"
                    pov "I can."
                    teacher "Stop it!"
                    pov "Nah."
                    teacher "STOP IT!"
                    scene black with hpunch
                    "She smacked you and left. That was uncalled for."
                    $ morale -= 2
                else:
                    "You walk around her and push yourself against her while taking a good grab of her breast."
                    teacher "Mhmm..."
                    pov "You like that don't you?"
                    scene bg office11-1
                    teacher "Yeah... Just like that..."
                    "You push the fabric down from her breast and starts playing and pinching her nipples."
                    teacher "Ah... Mhmm..."
                    "You decide to stop and invite her into your office."
                    teacher "Aww... I can't [povTitle] [povLastName], I have a class to attend."
                    $ deviance += 1
    $ inhibition -= 1
    return


label office12:
    
    scene bg office12 with fade
    "Not all students are comfortable with having to see the principal."
    $ morale -= 1
    return


label office13:
    
    scene bg office13 with fade
    girl "Oooh [povTitle] [povLastName], I promise I'll behave from now on!"
    $ deviance += 1
    return


label office14:
    
    scene bg office14 with fade
    "A couple of role-playing geeky girls have been called to the principals office. An incident involving cutting off the hair of a cheerleader calls for a few strict words. The girls stayed in character through out the meeting."
    $ behavior += 1
    return


label office15:
    
    scene bg office15 with fade
    "One of your teachers seems to get some moral support from one of his students."
    $ morale += 1
    return


label office16:
    
    scene bg office16 with fade
    "It doesn't happen all the time, but occasionally students express their relief of passing an important test in a somewhat physical manner. There's surely hope for humankind!"
    $ morale += 1
    return


label office17:
    
    scene bg office17 with fade
    "There come ungrateful days when you're a teacher, days you wish you'd never left bed."
    $ morale -= 1
    return


label office18:

    scene bg office18 with fade
    if pda_rules == 'pda_bdsm' or behavior_rules == 'behavior_no_limit':
        girl "Sorry teacher! I-AH!-won't- AH!- do it-AH!-ah-Ahgain..."
        "Seems like one of the male teachers are punishing a girl for her disobedience."
        $ behavior += 1
    else:
        girl "You promise-Ah! Mhmm... Give me be-Ahhh... grades."
        "Might this cute girl whore herself to get better grades?"
        menu:
            "Unacceptable - Grades are not earned this way.":
                "You interrupt them and just as you thought they traded sex for grades. You gave them a scolding and left them to their shame."
                $ academics += 1
                $ deviance -= 1
                
            "Unacceptable - Teachers should not fuck students.":
                "You interrupt them and explain how this is against the moral code of Ashford. They promise not to let it happened again."
                $ deviance -= 2
                
            "Acceptable - I don't give a fuck.":
                $ deviance += 1
                $ behavior -= 1
    return


label office19:

    scene black 
    "As you walk the corridors outside the teachers office you hear the familiar sound of something vibrating. I believe to have found the source and open the door."
    scene bg office19-1 with fade
    teacher "Ahhh...."
    "She looks at you with desire."
    menu:
        "Join her." if povGender == "male":
            "You walk towards her and let her perky tits fill you hands while you play with them."
            teacher "Ah... Mhmm..."
            pov "Do you like that?"
            teacher "Yeah... Pinch them."
            "You do as you're told and start pinching her nipples while you let another hand slide towards her ass."
            teacher "Mhmm... Ahh, Yes... Harder."
            "At the same time as you play with her ass, you put some strength into your pinches and you can hear how her moans reach new levels. "
            teacher "Ahhh, yes, use me...{w}\nMore... Harder!"
            "She pushes her toy hard against her pussy while you can both see and smell her juices."
            teacher "Ahh.. Ah! Ahhh!"
            "You notice how close she's to climax and you pinch and pull her nipples harder in a matching tempo to her heavier and heavier moaning."
            teacher "Ahhhhh..."
            "You can feel the surge going through her body while she cramps with one arm around you and the other one still pushing her vibrator against her pussy."
            teacher "Mhmm..."
            pov "Did you enjoy that?"
            teacher "Y-yeah... Mhmm..."
            "You decide it's time for you to enjoy yourself as well and help her down on all fours."
            pov "Don't fall asleep now, I still want my fun."
            teacher "*giggle* Don't worry... Please, I want you."
            "Her wet and juicy pussy sure looks delicious but you decide to choose something tighter."
            pov "Open your mouth, I will need a little lube."
            "She obediently follows your order and soaks your fingers in saliva. You then start playing with her anus and slowly sliding a finger inside."
            teacher "May I?"
            "You notice her eyes focusing on your cock and you nod. She quickly drowns it fluids while gently playing with her tongue. You decide foreplay is over and pull it out just to be able to put it in again."
            scene bg office19-2
            teacher "Ah!"
            "The few minutes you got to play with her anus was enough to soften it up for you to put in the top."
            teacher "Oh... You're.. Ah.. So big!"
            pov "Don't worry, I will try not to break you."
            "She smiles at your last remark while her tight anus enclose the top of your cock while you slowly pull it out and push it in and every time you get in a little bit deeper."
            teacher "Ah, come here with it..."
            "She wants more saliva and without hesitation takes you cock in her mouth again. Before you can put it back in her ass you need to remove her hand that covered it in your absence."
            teacher "Ahh! Just... Mhmm.. Push it!{w}\nOh god!"
            "You follow her orders and slide it in, over and over, for every push her moans get louder and you get one step closer to cum."
            teacher "Yes! Mhmm... Fuck me.... Fuck my ass!"
            "You keep pushing your cock inside of her and you notice how she puts a vibrator inside her pussy."
            pov "Is that how you like it?"
            teacher "Mhmm... Ah, ahhh!"
            "Obviously unable to answer you decide to fuck her harder and you put your hand on the vibrator pushing both it and your cock in at the same time."
            teacher "Ahhh! AH! Mhmm... AH! Ahhh..."
            "You make sure both her holes are getting a good fuck before you fill her tight anus up with as much cum as humanly possible."
            pov "Ahh!"
            teacher "Mhmmmm..."
            scene black with fade
            "Before you leave she cleans your cock with her mouth and {i}thank you for today{/i}."
            $ deviance += 1
            $ behavior -= 1
            
        "Leave her.":
            "You smile to yourself while you leave. You can clearly hear her moan as she's getting closer to climax."
             
        "Stop her." if povGender == "male":
            "You slowly approach her and you can clearly see how exited she becomes. You stop right in front of her and put you hand on her vibrator and remove it from her cunt."
            pov "Bad teacher. Very bad teacher."
            teacher "Ah... Mhmm... Please? {w}Fuck me... Please!"
            pov "You have been a very bad teacher..."
            "She looks deep into your eyes and with swift hands she have taken a hold on your bulging pants."
            teacher "Please, just give it to me... {w}Just fuck me!"
            menu:
                "No, you must stop this.":
                    "You remove her hands from your pants and help her up."
                    pov "Listen to me, you can't do this while you work. We have a reputation to take care of."
                    teacher "Please... Just this time..."
                    "After spending some time with her you get her back to senses and with great embarrassment she promises it will not happened again."
                    $ behavior += 2
                    $ deviance -= 1
                    
                "Grant her desire.":
                    "You can feel how she's playing with your cock and how much she craves it."
                    pov "Ok, I will fuck you."
                    teacher "Ah! Yes... Please!"
                    "You can see happiness in her sex-crazed eyes while her hands unzip your pants."
                    teacher "Please... Use me as your toy..."
                    "She has a solid and experienced grip around your penis while her other hand finds its way back to her vibrator and pussy."
                    teacher "Oh... It's bigger then im used to!"
                    "You give her a wry smile while you start touching her fine body."
                    pov "Open wide."
                    "She obeys and you put your cock in her mouth while she plays with her pussy. She's doing a great job taking care of you while you hear her muffled moans."
                    teacher "Mhuhghmm... Ahh...*slurp*"
                    "Whatever she's saying can't be too important so you ignore it while making good use of her fit body. Touching, pinching, and playing with every last part of it."
                    teacher "Mhmm... *slurp* Aghhhh..."
                    pov "Don't speak with meat in you mouth, it's impolite."
                    "She's getting silenced with the exception of her moans and dripping wet pussy. In the corner of you eye you see another vibrator."
                    pov "Oh, another toy?"
                    teacher "Mhmmm... *slurp*"
                    "You pick it up and slide it around the outside of her wet pussy. You can clearly see that she wants it."
                    pov "Is my cock not enough?"
                    teacher "Nhmm *slurp* ishhmm  *slurp*"
                    "She still doesn't make much sense, but she did shake her head. You slowly slide it into her pussy and you can see how all her body reacts to it."
                    pov "It that what you want?"
                    teacher "*slurp* Mhmm..."
                    "You pull it out starts playing with her anus, slowly putting it in and out. Preparing it for your cock."
                    teacher "Mhm.. Mhmmm.. *slurp*"
                    pov "Now now, lets put this cock to good use."
                    teacher "Yes [povLastName], please fuck my ass.{w}\nPlease use me."
                    "She doesn't need to beg for that, but you do enjoy her pleading eyes. You quickly walk around her and easily push you cock into her ass."
                    scene bg office19-2
                    teacher "Ah! Yes!!!"
                    pov "Is this how you like it huh?"
                    teacher "Yes! Ah, pl-AH!-ease, fuck my ass-Mhmm..."
                    "While the vibrator sure made it easier to get into her she's still quite tight. You decide to switch holes and bring the vibrator back into business."
                    teacher "Mhmm... Ah! Ah!"
                    "To her great pleasure you switch back and forth between her ass and pussy and preoccupy the empty hole with her vibrator."
                    teacher "Ah, ah, yes, Harder! Mhmm! Mhmmm!"
                    "She moans louder and louder while her she's pushing against you with all her might, you can feel how close you both are getting to climax."
                    teacher "Please, AH! Fu-Ah-fuck me... Mhmm, ah... Oh god! Mhmm..."
                    "You decide to finish it off and make a few hard and last pushes before you both cum."
                    teacher "Ahhhh!"
                    pov "Ahh!"
                    scene black with fade
                    if new_game_plus == True:
                        "She passed out cold when you both came so you decide to use her skirt to dry off the body fluids from your penis before you leave."
                    else:
                        "She passed out cold when you both came so you decide to pull up her panties and move her to the side to make it a bit less obvious what happened to her."
                    $ deviance += 1
    return



label office20:
    
    scene bg office20 with fade
    "Whats the difference between counseling and cuddling? Let's find out!"
    if renpy.random.randint(1,3) == 1:
        $ red_orb += 1
    else:
        $ deviance += 1
    return


label office21:
    
    scene bg office21:
        pos (0.0, 0.0)
        linear 3.3 pos (0.0, -0.5)
        linear 3.0 pos (0.0, -0.2)
    with fade
    "The substitutes all learn the school policy soon enough."
    "substitute" "T-this can't be legal!"
    pov "Schh."
    "substitute" "I-I want to be transferred to another school!"
    pov "Sure, along with a letter saying that you stole from the locker rooms."
    "substitute" "W-WHAT?!"
    pov "Hush now little puppy or your ass will be next."
    "substitute" "B-but, I-I'm not clean there!"
    pov "Alright, you asked for it."
    "substitute" "!!!"
    if renpy.random.randint(1,3) == 1:
        $ red_orb += 1
    else:
        $ deviance += 1
    return


label office22:
    
    scene bg office22 with fade
    "Seems like all workplaces have their rebels and bohemian wannabes."
    $ behavior -= 1
    return


label office23:
    
    scene bg class15-2 with fade
    "May returns for her counseling session."
    pov "Say it again."
    "She speaks in between slurping thrusts between her breasts into her mouth."
    teacher_may "I'm sorry for assaulting a student. I will not assault students. I won't... I won't stop boys from having their fun."
    scene bg class15-3
    "She's learning her lessons very well."
    $ deviance += 1
    $ behavior += 1
    return


