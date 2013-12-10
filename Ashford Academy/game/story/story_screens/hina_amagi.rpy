##########################################################
#
#                       Hina Amagi                      
#
# A student first met in the introduction scene in class.
# Have earlier been part of the swimming team and would 
# like that Ashford Academy rebuilds their swimming pool.
# 
# As female she becomes a friend who opens up about her
# family and dead mother.
#
# As male you become the target of her love.
#
# Three unique sex scenes will be available.
#
##########################################################


# We use this variable to keep track on her feelings towards the player. 
define hina_amagi_points = 0
define hina_amagi_outfit = ''          # This can be '' (nothing), 'short_skirt_', 'cosplay_' or 'sexy_uniform_'.

# We load images to be shown and the variations.
image hina_amagi normal = "story/story_screens/hina_amagi/hina_amagi_normal.png"
image hina_amagi happy = "story/story_screens/hina_amagi/hina_amagi_happy.png"
image hina_amagi blush = "story/story_screens/hina_amagi/hina_amagi_blush.png"
image hina_amagi angry = "story/story_screens/hina_amagi/hina_amagi_angry.png"
image hina_amagi surprised = "story/story_screens/hina_amagi/hina_amagi_surprised.png"
image hina_amagi sad = "story/story_screens/hina_amagi/hina_amagi_sad.png"

image hina_amagi short_skirt_normal = "story/story_screens/hina_amagi/hina_amagi_short_skirt_normal.png"
image hina_amagi short_skirt_happy = "story/story_screens/hina_amagi/hina_amagi_short_skirt_happy.png"
image hina_amagi short_skirt_blush = "story/story_screens/hina_amagi/hina_amagi_short_skirt_blush.png"
image hina_amagi short_skirt_angry = "story/story_screens/hina_amagi/hina_amagi_short_skirt_angry.png"
image hina_amagi short_skirt_surprised = "story/story_screens/hina_amagi/hina_amagi_short_skirt_surprised.png"
image hina_amagi short_skirt_sad = "story/story_screens/hina_amagi/hina_amagi_short_skirt_sad.png"

image hina_amagi sexy_uniform_normal = "story/story_screens/hina_amagi/hina_amagi_sexy_uniform_normal.png"
image hina_amagi sexy_uniform_happy = "story/story_screens/hina_amagi/hina_amagi_sexy_uniform_happy.png"
image hina_amagi sexy_uniform_blush = "story/story_screens/hina_amagi/hina_amagi_sexy_uniform_blush.png"
image hina_amagi sexy_uniform_angry = "story/story_screens/hina_amagi/hina_amagi_sexy_uniform_angry.png"
image hina_amagi sexy_uniform_surprised = "story/story_screens/hina_amagi/hina_amagi_sexy_uniform_surprised.png"
image hina_amagi sexy_uniform_sad = "story/story_screens/hina_amagi/hina_amagi_sexy_uniform_sad.png"

image hina_amagi cosplay_normal = "story/story_screens/hina_amagi/hina_amagi_cosplay_normal.png"
image hina_amagi cosplay_happy = "story/story_screens/hina_amagi/hina_amagi_cosplay_happy.png"
image hina_amagi cosplay_blush = "story/story_screens/hina_amagi/hina_amagi_cosplay_blush.png"
image hina_amagi cosplay_angry = "story/story_screens/hina_amagi/hina_amagi_cosplay_angry.png"
image hina_amagi cosplay_surprised = "story/story_screens/hina_amagi/hina_amagi_cosplay_surprised.png"
image hina_amagi cosplay_sad = "story/story_screens/hina_amagi/hina_amagi_cosplay_sad.png"


# Here we define prefix used for us and what it will show to the player.
# Colors are written in hexadecimal. (FF0000 = Red, 00FF00 = Green, 0000FF = Blue)
define hina_amagi = Character('Hina Amagi', color="#F8BA87")


# Here we make a list of all scenes with her. 
init:
    $ event("hina_amagi_in_class1", "act == 'class' and hina_amagi_points > 0 and hina_amagi_points < 7 and planning_day > 2", event.choose_one('class'), priority=190)
    # "hina_amagi_in_class" is the name/label of this event. "act" defines what type it is, with additional requirement to have planning_day above 5  
    
    $ event("hina_amagi_in_class2", "act == 'class' and hina_amagi_points >= 7 and hina_amagi_points < 17 and planning_day > 2", event.choose_one('class'), event.depends("hina_amagi_in_class1"))
    # event.once() makes sure it only viewable once.event.depends("hina_amagi_in_class1") - this event must have been seen first.

    $ event("hina_amagi_pool_opening", "act == 'pool' and hina_amagi_points > 3", event.once(), event.only())
    #$ event("hina_amagi_about_sexy_uniform", "act == 'office' and hina_amagi_points > 10 and uniform == 'sexy_uniform'", event.once(), event.only())

    $ event("hina_amagi_in_class3", "act == 'class' and hina_amagi_points >= 17 and planning_day > 2", event.choose_one('class'), event.depends("hina_amagi_pool_opening"))
    
    # Endings
    $ event("hina_amagi_transfer_ending", "act == 'office' and hina_amagi_points == -1", event.choose_one('office'), event.depends("hina_amagi_in_class2"))

    # Main story events
    $ event("hina_amagi_regarding_adaki", "act == 'class' and hina_amagi_points > 3", event.choose_one('class'), event.depends("adaki_school_grounds"), event.once(), event.only())
    
    
# Here starts the actual scenes. The name in the list must match the ones below.

label hina_amagi_in_class1:
    
    scene bg classroom with fade
    # We want to load a backdrop named "classroom" with the effect "fade"
    $ renpy.show("hina_amagi "+hina_amagi_outfit+"normal")
    hina_amagi "Hello [povLastName]!"           # [povLastName] is used for printing the users last name in text content.
    menu:                                       # We create a menu where you are given options to respond.
        "Good day.":                            # All menu options must end with a ":" and can include "if" parameters after the option before the ":".
            pov "Good day."                     # pov is the variable for the users name in text boxes.
            
        "Hello there student!":
            $ renpy.show("hina_amagi "+hina_amagi_outfit+"surprised")
            hina_amagi "Don't you remember me?"
            pov "I'm sorry, but I can't remember every student. I hope you understand."
            $ renpy.show("hina_amagi "+hina_amagi_outfit+"sad")
            hina_amagi "I understand [povTitle] [povLastName]..."
            $ hina_amagi_points -= 1
            return
            
        "Hey there Amagi!":
            $ renpy.show("hina_amagi "+hina_amagi_outfit+"happy")
            hina_amagi "You remember me!"
            $ hina_amagi_points += 1
            
    if building_pool == 0:
        hina_amagi "So [povTitle] [povLastName], is there any news regarding the pool?"
        pov "I'm sorry, there's nothing new at the moment."
        hina_amagi "I understand, but please tell me if anything changes!"
        pov "Will do."
    else:
        hina_amagi "I really want to thank you for getting our pool back!"
        pov "Don't worry about it, it's my pleasure to see you students happy."
        hina_amagi "You're the best Principal ever!"
        $ hina_amagi_points += 2
    return


label hina_amagi_in_class2:
    
    scene bg classroom with fade
    $ renpy.show("hina_amagi "+hina_amagi_outfit+"happy")
    hina_amagi "Hello [povLastName]! How are you today?"
    menu:
        "I'm great, thanks for asking":
            $ renpy.show("hina_amagi "+hina_amagi_outfit+"surprised")
            hina_amagi "That makes me happy to hear, anything special?"
            pov "Well, I did run into my favourite student, that always make me happy!"
            $ renpy.show("hina_amagi "+hina_amagi_outfit+"blush")
            hina_amagi "Aww [povLastName], you're so sweet!"
            $ hina_amagi_points += 2
            return
            
        "I'm good, how are you?" if building_pool == 0:
            $ renpy.show("hina_amagi "+hina_amagi_outfit+"normal")
            hina_amagi "Well, I still miss the pool... But I do enjoy chatting with you."
            pov "Oh, yes, sorry about the pool."
            $ renpy.show("hina_amagi "+hina_amagi_outfit+"sad")
            hina_amagi "It's okay... Some things never work out as planned."
            return
            
        "I'm good, how are you?" if building_pool > 0:
            hina_amagi "I'm great, I'm just getting ready for swimming club!"
            pov "You really like swimming, don't you?"
            hina_amagi "Yeah, I really do! And it's all thanks to you we got the new pool, thanks again [povTitle] [povLastName]." 
            pov "Don't mention it."
            $ hina_amagi_points += 1
            return


label hina_amagi_in_class3:

    scene bg classroom with fade
    $ renpy.show("hina_amagi "+hina_amagi_outfit+"happy")
    hina_amagi "Hey there [povTitle] [povLastName]! *giggle*"
    
    if renpy.random.randint(1,2) == 1:
        pov "Hey there Amagi!"
        hina_amagi "Looking for me?"
        menu:
            "Of course!":
                hina_amagi "Did you miss me?"
                pov "Yeah, I did."
                $ renpy.show("hina_amagi "+hina_amagi_outfit+"normal")
                hina_amagi "I bet you say that to all the girls!"
                pov "No no no, only to the ones I like."
                $ renpy.show("hina_amagi "+hina_amagi_outfit+"blush")
                hina_amagi "I..."
                hina_amagi "I think I should go now..."
                pov "Okay, you take care."
                $ hina_amagi_points += 1
            
            "Depends, have you been a bad girl?" if hina_amagi_points < 25:
                $ renpy.show("hina_amagi "+hina_amagi_outfit+"surprised")
                hina_amagi "I... don't think so... Why?"
                pov "Relax, I'm just pulling your leg!"
                hina_amagi "Oh, *giggle* you're funny [povTitle] [povLastName]."
                $ hina_amagi_points += 1
                
            "Depends, have you been a bad girl?" if hina_amagi_points >= 25:
                $ renpy.show("hina_amagi "+hina_amagi_outfit+"blush")
                hina_amagi "..."
                hina_amagi "..."
                pov "Hey, what's wrong, I'm just kidding!"
                "She takes a step closer and look you deeply into the eyes."
                hina_amagi "What would you do if... I'm a bad girl..?"
                pov "You're not a bad girl so don't worry about it."
                $ renpy.show("hina_amagi "+hina_amagi_outfit+"normal")
                hina_amagi "..."
                hina_amagi "How do you know that?"
                pov "Trust me, I just know."
                hina_amagi  "Ok..."
                $ hina_amagi_points += 2
        return
    else:
        menu:
            "Good day Amagi!":
                pov "How are you today?"
                hina_amagi "I'm good, just a bit wet... Ahh! I've just been swimming you know and I haven't really dried, I didn't mean anything else [povLastName] just so you know!"
                $ renpy.show("hina_amagi "+hina_amagi_outfit+"blush")
                pov "Haha, you get {i}wet{/i} when you swim?"
                hina_amagi "Y-y-yeah, you know... All the water and everything..."
                pov "I know {i}exactly{/i}."
                hina_amagi "You... You're pretty special..."
                pov "Thanks... I guess?"
                hina_amagi "Umm... [povTitle] [povLastName] I..."
                $ renpy.show("hina_amagi "+hina_amagi_outfit+"normal")
                hina_amagi "Can I ask... Never mind, I gotta go, see ya!"
                hide hina_amagi
                "There she goes once again."
                $ hina_amagi_points += 1
                
            "Hello Sunshine!" if hina_amagi_points < 25:
                $ renpy.show("hina_amagi "+hina_amagi_outfit+"blush")
                hina_amagi "How cute! I like it when you call me that!"
                pov "I know you do. So where's the light shining today?"
                $ renpy.show("hina_amagi "+hina_amagi_outfit+"happy")
                hina_amagi "*giggle* Today I shine on you!"
                pov "Whaaa, you shine so bright! I might need sunglasses!"
                "You both burst into laughter and continue to play around for a short while."
                $ hina_amagi_points += 1
                
            "Hello Sunshine!" if hina_amagi_points >= 25:
                $ renpy.show("hina_amagi "+hina_amagi_outfit+"blush")
                hina_amagi "[povTitle] [povLastName]..."
                pov "Amagi..?"
                hina_amagi "..."
                pov "?"
                hina_amagi "Did you really like the outfit I had at the pool?"
                pov "Yeah, It was really nice. What about it?"
                hina_amagi "Umm, I was just wondering... I like how you looked at me back then..."
                pov "I'm happy to hear that..?"
                hina_amagi "Well... Umm... Classes are starting soon..."
                pov "I understand."
                hina_amagi "Ok..."
                pov "You take care Sunshine."
                $ hina_amagi_points += 2
        return


label hina_amagi_pool_opening:
    
    scene bg pool with fade
    hina_amagi "Hello there [povLastName]!"
    "You can hear how she quickly runs up behind you."
    show hina_amagi cosplay_normal at center
    "Wow, that outfit..."
    "..."
    "For a second you wonder if this really is appropriate, but you quickly dismiss that thought."
    hina_amagi "Umm... [povLastName], is something wrong?"
    menu:
        "Ah, nothing, I was just stunned by your outfit.":
            hina_amagi "Oh... Does that mean you like it?"
            pov "Yeah, it's really something special."
            show hina_amagi cosplay_happy
            if hina_amagi_points < 10:
                hina_amagi "Thank you! I'm happy you like it"
            else:
                hina_amagi "Thank you! I like you too... WHAA, IT! I like {i}it{/i} too! I like it too!"
                menu:
                    "I like you too.":
                        show hina_amagi cosplay_blush
                        hina_amagi "..."
                        "She just stands there, looking deep into your eyes."
                        "..."
                        "..."
                        hina_amagi "I-I-I... have to go!"
                        hide hina_amagi
                        "And there she runs away..."
                        $ hina_amagi_points += 5

                    "Does that mean that you don't like me?":
                        show hina_amagi cosplay_blush
                        hina_amagi "Eh... Umm... Y-y-you are..."
                        pov "Don't worry Amagi, it was just a joke."
                        hina_amagi "..."
                        show hina_amagi cosplay_sad
                        hina_amagi "Ok..."
                        $ hina_amagi_points -= 2
            
        "Wow, that's sexy!" if hina_amagi_points < 10:
            show hina_amagi cosplay_surprised
            hina_amagi "Whaa, umm, thank you..."
            "She looks equally confused as happy."
            $ hina_amagi_points += 1
        
        "Wow, that's sexy!" if hina_amagi_points >= 10:
            show hina_amagi cosplay_happy
            hina_amagi "*giggle* I knew you would like me... WHAA, IT! I knew you would like {i}it{/i}!"
            pov "Haha, I like {i}it{/i} Amagi and that you're in {i}it{/i} only makes {i}it{/i} better."
            show hina_amagi cosplay_blush
            hina_amagi "Umm..."
            hina_amagi "You're so nice [povLastName]..."
            $ hina_amagi_points += 3
        
        "I can't allow her wandering around like that!":
            pov "What is this?! You can't walk around like that, think of the school reputation!"
            show hina_amagi cosplay_surprised
            hina_amagi "But..."
            pov "What where you thinking when you put THAT thing on?!"
            show hina_amagi cosplay_sad
            hina_amagi "..."
            "You can see that she's close to tears, maybe this was a bit harsh."
            $ hina_amagi_points -= 10
            $ inhibition -= 1
            $ reputation += 1
    return


label hina_amagi_about_sexy_uniform:
    
    scene bg office with fade
    "Someone is knocking on your door."
    pov "It's open, come on in!"
    show hina_amagi normal at center
    hina_amagi "Hello [povLastName]..."
    menu:
        "Good day Amagi.":
            show hina_amagi surprised
            hina_amagi "Wow, you look so serious when you say that here in your office!"
            pov "Haha, well, I am the principal after all."
            hina_amagi "Yeah, that's true, but you really seem like another person in here."
            
        "Hello sunshine, what brings you to my door?":
            hina_amagi "Well... [povLastName]... I have a question..."
            pov "What's bothering you?"
            show hina_amagi sad
            "She looks a bit distressed and takes a deep breath."
            hina_amagi "You know about the new uniform thingy..."
            pov "Yeah, what about it?"
            "She looks at you with sad puppy eyes."
            pov "You don't like it?"
            hina_amagi "Well... It's just that... You know..."
            hina_amagi "It doesn't feel right..."
            pov "What part of it?"
            hina_amagi "Umm... Well... Showing off so much..."
            pov "So what do you want me to do about it?"
            hina_amagi "I don't really know... I know the rules... B-but... You're always so nice to me!"
            menu:
                'Propose a "deal"':
                    pov "Well, maybe I could make an exception..."
                    show hina_amagi happy                    
                    hina_amagi "Oh really! You're the best [povLastName]!"
                    pov "Thanks sunshine, but slow down a bit... If I do this for you, what would you do for me?"
                    if deviance > 50:
                        hina_amagi "Well [povFirstName], I see what you are doing."
                        pov "So what do you say?"
                        hina_amagi "I... I was... I wished you... wanted more than {i}that{/i} from me..."
                        pov "Huh?"
                        hina_amagi "Since... you came here... everyone c-changed..."
                        pov "Don't you approve of my work?"
                        hina_amagi "A-approve..?"
                        pov "Have I done anything wrong?"
                        hina_amagi "I... I don't know... But, I wanted... more..."
                        pov "Wanted more of me? I just gave you the opportunity to have {i}more{/i} of me."
                        if inhibition < 90:
                            # TODO: Should it end this way?
                            hina_amagi "Stupid..."
                        else:
                            hina_amagi "..."
                        pov "..."
                        hina_amagi "Maybe... I'll j-just go..."
                        "She slowly walks away. "
                    
                    elif evil_points > 2:
                        show hina_amagi sad
                        hina_amagi "I've... heard all these rumours..."
                        pov "What are you talking about?"
                        hina_amagi "They say... you have done... b-bad stuff... I didn't..."
                        pov "Who said what?"
                        hina_amagi "I-I... I really... *sob*"
                        "She gives you a look full of sadness."
                        pov "Hey hey, what's wrong? Talk to me."
                        hina_amagi "They say, you have done all... And now..."
                        hina_amagi "Will you do that to me..?"
                        pov "Slow down sunshine!"
                        hina_amagi "*sob* I really, really thought you where different"
                        hina_amagi "I... I... please *sob* let... me go..."
                        pov "You can go when you want..."
                        hina_amagi "I... I thought... I... *sob* might... lov-"
                        "She turns around running away with tears in her eyes. {w}What just happened?"
                        $ hina_amagi_points = -1
                        # Maybe you just meet her and she runs away if you meet her again?
                        
                    else:
                        hina_amagi "I would give you the {b}BIGGEST{/b} hug ever! And maybe even a kiss."
                        hina_amagi "...On the cheek."
                        pov "Haha, you're so cute."
                        menu:
                            "Accept":
                                pov "Okay, come over here little miss sunshine!"
                                show hina_amagi surprised
                                "She stands perfectly still and looks like a frozen beauty."
                                hina_amagi "..."
                                pov "What's wrong?"
                                show hina_amagi blush
                                hina_amagi "Umm, D-do you..."
                                "What now?"
                                hina_amagi "Okay..."
                                "She walks baby steps towards you."
                                hina_amagi "C-ca... Can I..?"
                                "She's standing right in front of you looking terrified."
                                pov "?"
                                hina_amagi "Umm... I..."
                                "She throws herself at you, hugging as hard as her little arms can."
                                pov "What's wrong sunshine?"
                                hina_amagi "N-n... Nothing!"
                                "You smile to yourself, she's such a cute and innocent girl."
                                "It feels like the hug is over but..."
                                
                                if renpy.random.randint(1,2) == 1:
                                    "Suddenly you feel a pair of soft lips against yours, and you see her closed eyes just in front of you."
                                    "She opens her eyes, looking right into yours, and in just a second they turn from blissful to terrified."
                                else:
                                    "Suddenly you feel her soft lips against your cheek while her arm slowly slides down your back."
                                    "You feel her heavy breathing getting closer to your ear and then she whispers:"
                                    hina_amagi "{size=16}...T-thank you [povFirstName].{/size}"
                                
                                hide hina_amagi
                                "She quickly turns around and runs towards the door."
                                "Bye bye sunshine."
                                $ hina_amagi_points += 3
                                
                            "Decline":
                                pov "I'm sorry sunshine, I think I would need something more of you to make this deal worthwhile."
                                show hina_amagi sad
                                hina_amagi "Really? Oh... B-but I have nothing else to give you."
                                pov "Oh, yes you do. Come over here."
                                show hina_amagi normal
                                "She looks a bit confused and then walks slowly towards you."
                                pov "You are a beautiful young girl and if I lock that door over there we could have some private time together. So what do you say?"
                                show hina_amagi blush
                                hina_amagi "A-a-ah! Are you... hitting on m-m-me?"
                                pov "Im just giving a cute girl as yourself options."
                                hina_amagi "W-w-wha... What w-w-would you want me... t-t-o do?"
                                pov "We could start slowly and see where it goes. How does that sound?"
                                show hina_amagi surprised
                                hina_amagi "T-t-t... Then..."
                                pov "Shhh... Just take it easy sunshine, let me guide you."
                                show hina_amagi blush
                                "You take a small and slow step towards her, making sure not to frighten her."
                                hina_amagi "Ah..."
                                "She looks completely terrified and you decide to..."
                                if evil_points > good_points:
                                    "Take what you want."
                                    "With firm hands you grab her wrist and pull her close to you."
                                    show hina_amagi surprised
                                    hina_amagi "Ah!"
                                    "You can feel her breast and speeding heartbeat against your body."
                                    show hina_amagi blush
                                    hina_amagi "U-umm..."
                                    pov "Look at me Hina."
                                    "Her cloudy and confused eyes look deeply into yours."
                                    pov "You didn't want to wear the same uniform as the rest, right?"
                                    hina_amagi "I-I... No..."
                                    pov "Then show me what you want to hide from them so I know if its worth my time."
                                    hina_amagi "W-worth... B-but..."
                                    "You smack her ass."
                                    scene bg office with vpunch
                                    show hina_amagi surprised
                                    hina_amagi "Ah!"
                                    pov "This is the only butt I want to hear about right now."
                                    "You grab her arm and pull her to a seat and push her down into it."
                                    hide hina_amagi
                                    hina_amagi "W-w..."
                                    pov "Shh... You just be quiet."
                                    "Her eyes have a touch of fear in them and she doesn't really seem to like the mess she got herself into."
                                    "For a second you ask yourself, should you really go on with this?"
                                    menu:
                                        "Go on":
                                            pass

                                        "Let her go":
                                            pov "Sorry Hina... You can go now."
                                            hina_amagi "Huh..?"
                                            hina_amagi "... Y-you... Will let me go..?"
                                            pov "Yeah, sorry about this, just forget it leave."
                                            hina_amagi "O-okay..."
                                            "She slowly and clumsy get on her feet before she quickly leave the room."
                                            $ hina_amagi_points -= 3
                                            $ hina_amagi_outfit = 'sexy_uniform_'
                                
                                elif good_points > evil_points:
                                    "Hold her tight and tell her to relax."
                                    hina_amagi "Umm..."
                                    pov "What's on your mind little sunshine?"
                                    show hina_amagi sad
                                    hina_amagi "I-Is... This... Really okay..?"
                                    pov "Don't worry, everything's okay and if they are not, i will make them."
                                    show hina_amagi blush
                                    hina_amagi "*giggle*"
                                    "Her eyes shows both a bit of confusion and bliss."
                                    pov "Are you afraid of what I will do to you?"
                                    hina_amagi "Umm... J-just a bit..."
                                    pov "Don't be. I won't do anything you don't want me to, Okay?"
                                    hina_amagi "..."
                                    pov "Okay?"
                                    hina_amagi "Okay..."
                                    "You look into her beautiful and innocent eyes, every now and then they glimmer like stars."
                                    pov "You have beautiful eyes Hina."
                                    show hina_amagi surprised
                                    hina_amagi "O-oh, th-thank you..."
                                    "Still close to her, you slide your hand down her face and neck."
                                    show hina_amagi blush
                                    pov "It's okay."
                                    hina_amagi "Okay..."
                                    pov "Do you want me to stop?"
                                    hina_amagi "..."
                                    "She looks at you with confusion in her eyes and you continue to slide your hand down her neck to shoulder."
                                    hina_amagi "..."
                                    "You very slowly slide your hands closer and closer to her cleavage and you can see how she gets more and more nervous."
                                    pov "Is this okay?"
                                    hina_amagi "..."
                                    "As you hand touches the top of her breasts she gasps."
                                    # Love goes here
                                else:
                                    pass
                                    # Seems like a pass goes here 

                "Offer a solution.":
                    menu:
                        "Pool opening costume.":
                            pov "Well Sunshine, i got an idea!"
                            hina_amagi "You do!? Yay!"
                            pov "You know that outfit you had at the pool opening?"
                            hina_amagi "Yeah? What about it?"
                            hina_amagi "... Ah, wait!"
                            hina_amagi "I can have that one instead?!"
                            pov "Well, would that make you feel better?"
                            hina_amagi "Well, I guess so! You're the best [povLastName]!"
                            pov "I do what I can."
                            hina_amagi "...Maybe... I... Would you..."
                            pov "Would I?"
                            show hina_amagi blush
                            hina_amagi "Will you... look at me... like you did at the pool opening..."
                            pov "Would you like me too look at you in that way?"
                            hina_amagi "*giggle* S-stop that [povFirstName]!"
                            "She blushes more than you thought was humanly possible."
                            pov "Well, would you like me to look at you in that way?"
                            "She moves a few steps closer to you while keeping her head down."
                            "..."
                            "She's just in front of you and she seems a bit reluctant to whatever she's planning."
                            pov "Are you okay sunshine?"
                            hina_amagi "I..."
                            "She looks up straight into your eyes and you can see a fire burning in there."
                            show hina_amagi surprised
                            hina_amagi "Oh! I-I didn't mean so close!"
                            pov "Don't worry."
                            "She looks down and takes a big breath. {w}Now she's slowly raising her head again."
                            show hina_amagi normal
                            hina_amagi "{cps=*2}Thank you and I hope this Isn't wrong of me or anything I just want to thank you just so you know I really {i}really{/i} like you [povFirstName]!{/cps}"
                            "She gives you one of the worlds quickest kisses and then turns around running for her life. {w}\nThere she goes again."
                            $ hina_amagi_outfit = 'cosplay_'
                    
                        "Shorten her skirt.":
                            pov "Well sunshine... Let's do like this, let's shorten your skirt and that will be all."
                            pov "Does that sound fair to you?"
                            show hina_amagi happy
                            hina_amagi "{cps=*2}Yeah! Thank you thank you thank you!{/cps}"
                            pov "Haha, I'm always happy to help."
                            show hina_amagi normal
                            hina_amagi "Umm, [povLastName] how short should it be?"
                            pov "Come over here and I'll help you!"
                            hina_amagi "Okay, then... Oh..."
                            show hina_amagi blush
                            pov "What's wrong sunshine?"
                            hina_amagi "Umm, n-n-nothing..."
                            "She takes some slow steps towards you, blushing like there's no tomorrow."
                            pov "Come on, I won't bite."
                            show hina_amagi normal
                            hina_amagi "*giggle*"
                            "She's now standing in front of you."
                            pov "Now I need you to turn around."
                            show hina_amagi surprised
                            hina_amagi "..."
                            pov "So I can adjust your skirt sunshine."
                            hina_amagi "Oh, yes... S-skirt..."
                            hina_amagi "Be nice [povFirstName]."
                            pov "Don't worry Hina."
                            hide hina_amagi
                            "She turns around and you put your hand on her waist and unzip her skirt."
                            hina_amagi "Ah... {size=12} P-please, please don't drop it...{/size}"
                            pov "Did you say something?"
                            hina_amagi "Umm... N-no [povLastName]..."
                            "She got such a figure it's a bit hard to keep both your focus and hands at the task."
                            if evil_points > good_points:
                                "You slide one of your hands down and grope her ass."
                                hina_amagi "Ah!"
                                hina_amagi "..."
                                "As you touch her firm ass it obvious that she's an athlete. You decide to give it a slap."
                                hina_amagi "AH!"
                                "She starts to squirm but since you still have one hand on her waist and skirt she can't move to much."
                                hina_amagi "P-p-please [povaLastName]..."
                                pov "Sorry about that, just wanted to confirm that it feels as good as it looks."
                                hina_amagi "Ok..."
                            elif good_points > evil_points:
                                pov "You have a really good figure Hina."
                                hina_amagi "T-t-thanks [povFirstName]..."
                                "In a quick and gentle motion you slide your hand from her waist to her back and then down again."
                                "You seem a bit tense Hina, don't worry about it, I'm here for {i}you{/i}."
                                hina_amagi "S-sorry, I j-just..."
                                "You move closer to her and put your hands back at her waist and then tell her:"
                                pov "Don't worry about it."
                                hina_amagi "T-thanks... [povFirstName] you... M-make me feel... S-safe..."
                            else:
                                "You put your hand on her side and \"by mistake\" touch her side boob."
                                hina_amagi "Ah! P-p-please..."
                                pov "Sorry, sorry..."
                            pov "There, this should be a good length."
                            show hina_amagi short_skirt_normal
                            hina_amagi "Umm... It's kinda short..."
                            pov "Yeah, but if you want the new uniform instead, feel free to change into that one."
                            hina_amagi "N-no, It's alright... I... Can I walk in stairs when..."
                            pov "Are you afraid someone might peek?"
                            hina_amagi "Y-yeah... I know how some guys... act..."
                            pov "If you want I could always go behind you a make sure no one peeks!"
                            hina_amagi "*giggle* I'm sure you would be the one to peek in that case!"
                            hina_amagi "{cps=*2}Oh, sorry [povTitle] [povLastName] I didn't mean that you would act like that it was just a joke please don't be mad at me!{/cps}"
                            pov "Haha, don't worry sunshine. But you better go back to class now."
                            hina_amagi "Oh... Yes, thanks for the help [povLastName]!"
                            $ hina_amagi_outfit = 'short_skirt_'
                        

                "Ignore her plea.":
                    pov "I'm sorry sunshine, but if I make an exception for you everyone would come asking for one."
                    show hina_amagi sad
                    hina_amagi "B-but... Okay, I understand."
                    pov "Think of it like this, you like to swim right?"
                    hina_amagi "Yeah, I love to swim!"
                    pov "So you spend a lot of time in your swimsuit."
                    hina_amagi "Oh, you mean it's like the same?"
                    pov "Yeah, exactly, you catch on quick today!"
                    show hina_amagi happy
                    hina_amagi "Thanks! I'll just have to pretend it's my swimsuit!"
                    pov "Good girl, do you feel better now?"
                    show hina_amagi normal
                    hina_amagi "Not really!"
                    pov "Oh..."
                    hide hina_amagi
                    $ hina_amagi_outfit = 'sexy_uniform_'
    return

#Endings
label hina_amagi_transfer_ending:

    show bg office with fade
    "As you enter your office you can see some new papers on your desk."
    "You walk over and take a seat, quickly looking through the papers."
    "Nothing catches your eye or seems to be of great importance."
    "Except..."
    "You recognize a name on a signed transfer request...{w} Hina Amagi."
    "Well, I guess I won't be seeing her around any more."
    $ population -= 1 # Might react different depending on stats, such as "what a shame..."?
    return


#Main story events
label hina_amagi_regarding_adaki:
    scene bg classroom with fade
    $ renpy.show("hina_amagi "+hina_amagi_outfit+"sad")
    pov "Hey Amagi, how's your day?"
    $ renpy.show("hina_amagi "+hina_amagi_outfit+"happy")
    hina_amagi "Hi [povName], oh it's just great! How's yours?"
    pov "Glad to hear it. Well, it's ok, I have some things to sort out."
    $ renpy.show("hina_amagi "+hina_amagi_outfit+"normal")
    hina_amagi "Oh, just let me know if there's anything I can do."
    pov "That's sweet of you. As a matter of fact, there is something."
    hina_amagi "Oh great!"
    menu:
        "Do you know anything about officer Adaki?":
            $ renpy.show("hina_amagi "+hina_amagi_outfit+"sad")
            hina_amagi "Well, I know he's been hanging around the school grounds for some time now."
            pov "He sure has."
            $ renpy.show("hina_amagi "+hina_amagi_outfit+"surprised")
            hina_amagi "But I haven't really thought about him before, I mean before the accident and all. Hey, I-I didn't mean that I'm thinking about him a whole lot now either!"
            pov "Haha, it's ok, thank's for the help."
            $ renpy.show("hina_amagi "+hina_amagi_outfit+"normal")
            hina_amagi "Glad I could help!"

        "Have you seen this symbol somewhere?":
            $ renpy.show("hina_amagi "+hina_amagi_outfit+"surprised")
            hina_amagi "Is that graffiti?"
            pov "Eh, no, not exactly."
            $ renpy.show("hina_amagi "+hina_amagi_outfit+"sad")
            hina_amagi "I know that some of the boys go around tagging their lockers and sometimes corridor walls, but the janitor always see it and clean it."
            pov "Ok, but have you ever seen this particular symbol?"
            hina_amagi "I don't think so, not that I can think of."
            pov "I see, well thank you anyway."
            $ renpy.show("hina_amagi "+hina_amagi_outfit+"happy")
            hina_amagi "I'll be sure to let you know if I do see it!"
            pov "That's great."
            hina_amagi "Bye!"
    return
    