image bg phone1 = "screens/splash/phone1.jpg"
image bg phone2 = "screens/splash/phone2.jpg"

init python:

    # Story Variables
    first_week = True
    introduce_jennifer_adriano = False
    extroduce_jennifer_adriano = False
    susan_returns = False
    introduce_officer_adaki = False

init:
    if persistent.mod_disable_original_events == False:
        $ event("susan_marina_regarding_adaki", "act == 'office'", event.once(), event.choose_one('office'), event.depends("adaki_school_grounds"), event.only())

label t:
    $ v = sort_stats('max')
    "[v]"
    return

label new_game:
    scene black

    if povName == '':
        info "Please enter your name."
        if not renpy.variant('touch'):
            $ povFirstName = renpy.input("What is your first name?", length=16) or "Principal"
            $ povLastName = renpy.input("What is your last name?", length=16) or "Shinryu"
            $ povName = povFirstName +" "+povLastName

        elif renpy.variant('touch'):
            info "What is your first name? (leave blank for 'Principal')"
            $ input_header = 'First name:'
            call inputter
            $ povFirstName = input_text or "Principal"
            info "What is your last name? (leave blank for 'Shinryu')"
            $ input_header = 'Last name:'
            $ text_group = 1
            $ input_text = ''
            call inputter
            $ povLastName = input_text or "Shinryu"
            $ povName = povFirstName +" "+povLastName

        else:
            $ povFirstName = "Principal"
            $ povLastName = "Shinryu"
            $ povName = povFirstName +" "+povLastName

        $ new_game('normal')

    'Standing at the gates, you brush off some dust from your jacket. The school area towers up before you as you peek through the bars. "Ashford" - the wide, cold letters make an old fashioned scenery pop up in your head and you feel a proud history whisper to you: "Welcome stranger, to our academy".'
    "Proud as it may be, Ashford of today is far from it's prime. Things have been going downhill for quite some time and the last administration gave up and made a run for it. At least that's what you've heard. The situation called for serious action to be taken and that's when they called you."
    'The gates bid you welcome. \nYou take a deep breath and push them open.'

    # Show the Ashford backgrounds with Susan.
    scene bg Ashford_Academy with fade
    show susan_marina normal at center

    susan_marina "Welcome [povTitle] [povLastName]. \nI'm the permanent under-secretary of the administrative department. I'm very happy to hear that you are our new principal here at the Ashford Academy."
    susan_marina "Your predecessor left on a rather short notice and things are a bit muddled around here when it comes to policy and management, I'm afraid."
    susan_marina "I understand you have a lot of questions. I have to hold an introduction to the students in a few minutes so please start with a brief tour around the school on your own. We'll take the rest as it moves along, shall we?"

    menu:
        "Sounds fine to me.":
            pov "No need to panic, I'm sure it's going to work out just fine."
            susan_marina "Glad that you see it that way, things have been quite busy here lately."
            pov "I can imagine."
            susan_marina "Well, I'm on my way. Be sure to drop by and perhaps introduce yourself to the students."
            pov "I'll see you shortly."

        "I'd appreciate if you gave me a memo.":
            pov "Surely you will have all the information I require ready by the end of the day."
            susan_marina "Of course, I'll leave it at your desk as soon as possible."
            pov "That's good."
            susan_marina "Good bye for now."

        "Never mind 'bout the bureaucracy, I could use a steady drink!" if new_game_plus == True:
            susan_marina "Need I remind you that your work starts immediately as from this minute?"
            pov "You say potato, I say Gin and Tonic."
            susan_marina "..."
            pov "Cheerio!"
            $ start_day_with_gin = True

    # We jump to "day" to start the first day.
    jump day


label jennifer_adriano_introduction:

    scene bg office with fade
    show jennifer_adriano normal at center
    jennifer_adriano "Hi, I'm Jennifer Adriano from the Agency."
    pov "Hello Jennifer, I'm [povName]. Nice to meet you."
    jennifer_adriano "Nice to meet you to! Susan gave me the quick version on how things run around here. I'm sure I'll get the hang of it in a couple of days."
    pov "I'm sure you will. Just take your time and get acquainted with the principles."
    jennifer_adriano "Yes sir!"
    $ introduce_jennifer_adriano = True
    jump day


label jennifer_adriano_extroduction:

    scene bg phone1
    "Your phone's ringing."
    scene bg phone2
    pov "Hello?"
    dr_kent "[povTitle] [povLastName]? I'm doctor Kent from the County Hospital. Sorry to disturb you at this hour but there has been an accident."
    pov "An accident?"
    dr_kent "Yes, I'm sorry but the girl doesn't seem to have any relatives in town so I was hoping that perhaps you could come here and -"
    pov "I'm sorry doctor but which girl are we talking about?"
    dr_kent "Oh, how clumsy of me. I'm terribly sorry, I should have... She had a briefcase with documents that carried Ashford's header and an ID that -"
    pov "Which girl doctor?!"
    dr_kent "Her name is Jennifer. The Id says: Jennifer Adriano, but it doesn't say if she's -"
    pov "My god..."
    dr_kent "Obviously you must know her and -"
    pov "She was my secretary."
    dr_kent "Oh, I... I'm truly sorry [povTitle] [povLastName]."
    pov "I'm on my way."

    scene bg hospital_night with fade
    show dr_kent normal at center
    pov "What happened?"
    dr_kent "Looks like a hit and run. I'm sorry, but the injuries were far too severe for us to be able to save her. She was in a real mess when she came in."
    pov "..."
    dr_kent "I understand she was your secretary?"
    pov "Yes, she started working for me just a few days ago."
    dr_kent "Once again, you have my condolences."
    pov "Thank you."
    $ extroduce_jennifer_adriano = True
    jump night


label interrogation:

    scene bg phone1
    "Your phone's ringing."
    "What is it this time..."
    scene bg phone2
    pov "Hello?"
    "???" "Is this [povTitle] [povLastName]?"
    pov "Yes, who am I talking to?"
    officer_adaki "This is officer Adaki from the Metro Crime Unit. We would like you to come down to the station."
    pov "Okay... What is it about?"
    officer_adaki "We have some formalities regarding Ms. Adrianos death. Seems her family is not in the country right now, and since you're her latest employer we'd appreciate if you could fill in some of the blanks."
    pov "Sure, I mean, I was her boss but she was employed through The Agency."
    officer_adaki "Yeah, we're aware of that but you're the closest link to the questions we have."
    pov "I see, when would you like me to-"
    officer_adaki "Right now. Would that be a problem?"
    pov "Well- No, no problem officer."
    officer_adaki "Good. I'll expect you shortly then."
    pov "Right..."

    scene black with fade
    "You call a cab and get down to the station."
    "As soon as you enter the station you are escorted into a small room."

    scene bg police_station_interrogation with fade
    show officer_adaki normal
    "As soon as you enter the room, a man shoves a piece of paper in your face. It seems to have some strange symbol on it."
    officer_adaki "What do ya make of this?"
    pov "I've never seen it before, why do you ask?"
    officer_adaki "That girl had it on her when she got hit by the car."
    pov "Ok, but why would I know what it means?"
    officer_adaki "It came in this."

    "Adaki shows you a letter with [povName] written on it."

    officer_adaki "I was hoping you could shed some light on this."
    pov "I have no idea why she would have a letter with my name on it."
    officer_adaki "Really?"
    pov "Look, officer Adaki is it? Am I accused of anything? In that case I would like a lawyer to be present."
    show officer_adaki smile
    officer_adaki "Take it easy mister, I'm just askin'. You gotta admit it's kinda strange that she'd be carrying a letter for you with a weird symbol and all."
    pov "I barely knew the girl!"
    officer_adaki "She was your secretary, wasn't she?"
    pov "Yes but only for a few days! Jesus, she had barely settled in."
    officer_adaki "Yeah? Perhaps you two were more than just co-workers, ya know what I'm sayin'?"
    pov "What?"
    officer_adaki "And maybe the little missy found out about it?"
    pov "Look, what the hell are you implying?!"
    show officer_adaki normal
    officer_adaki "Relax, we're gonna need your fingerprints and then you can go home. Wouldn't leave town though."
    pov "Are you quite done?"
    officer_adaki "As soon as you've given your prints to my assistant, you're free as a bird."
    scene black with fade
    "They take your fingerprints and have you sign some papers before you take a cab home again."
    $ introduce_officer_adaki = True
    jump night


label adaki_school_grounds:

    scene bg school_grounds
    show officer_adaki normal
    "Is that officer Adaki?"

    officer_adaki "Hey, can I have a word?"
    menu:
        "Sure, what's on your mind?":
            officer_adaki "I'll tell you what's on my mind, the safety of your students."
            pov "What do you mean?"
            officer_adaki "What do I mean? I mean that somebody just got murdered, somebody connected to this school."

            menu:
                "By the sound of it, you completely rule out that it might have been an accident?":
                    officer_adaki "This was no accident alright. Things just doesn't add up."
                    pov "Meaning?"
                    officer_adaki "Meaning that I wouldn't be surprised if my investigation rattled the snakes."
                    pov "Eh, yeah..."
                    officer_adaki "Somebody's oughta be nervous about new evidence turning up, that's for sure."

                    menu:
                        "So there's new evidence?":
                            officer_adaki "Might be, but I ain't telling you about that."
                            pov "Still convinced that I had something to do with it?"
                            officer_adaki "I ain't ruling out nothing at this time."
                            pov "I understand, you got to follow protocol, right?"
                            officer_adaki "You can't sweet-talk yourself out of the investigation, capiche?"
                            pov "I wasn't trying to, I just..."
                            officer_adaki "Save it, I need to talk to your students. We need to take some precautions you know."

                        "Whe're all lucky to have you on the job then.":
                            officer_adaki "Trying to be a smartass, eh? Remember that you're on my list, pal."
                            pov "..."
                            officer_adaki "I want to talk to your students about some basic safety, ask them a couple of questions to."

                "Go on.":
                    officer_adaki "It's important that the students are well aware of the situation, just in case somebody might see something suspicious, you follow?"
                    pov "I follow."
                    officer_adaki "Hey! Don't expect me to let you off the hook just because you're such a glad-hand."
                    pov "But I wasn't..."
                    officer_adaki "You're still a suspect pal, don't think otherwise."
                    pov "But..."
                    officer_adaki "I would like to talk to your students, give them a security introduction class just to play it safe."
                    menu:
                        "I understand, I'll see if I can squeeze it in.":
                            officer_adaki "I wasn't askin'. Squeeze it, and squeeze it good."
                            pov "I..."
                            officer_adaki "Call the station and leave the info once you've fixed it. I'll see you around."
                            pov "Guess I'll get to it then..."

                        "Sounds like a good idea.":
                            officer_adaki "Yeah."
                            pov "So... What do you need?"
                            officer_adaki "Their ears 'n' time, preferably on a morning class so they stay sharp during the day."
                            pov "Right, morning class, anything else?"
                            officer_adaki "Look, this is gonna be simple as a walk in the park. Just leave the info bit to me."
                            pov "Of course, just let me know when."
                            officer_adaki "Yeah yeah, I'll let you know."

        "Is this connected to the investigation or are you just lost?":
            officer_adaki "Wiseguy eh? You don't wanna be on my shit list, so watch it."
            pov "Playing bad cop must be your favourite part, am I right?"
            officer_adaki "You're diggin' a hole pal, just sayin'."
            menu:
                "Ok, I'm sorry.":
                    officer_adaki "You'll be sorry alright if you try to mess with me."
                    pov "I don't want to cause any trouble, I can assure you."
                    officer_adaki "Not so cocky anymore, eh?"
                    menu:
                        "Can I assist you with anything?":
                            officer_adaki "Damn right you can. You can arrange for a safety class so the students know what to expect when shit hits the fan."

                        "...":
                            officer_adaki "Cat got your tongue, eh? Listen up pal, I request that you set aside a class for the students to get some safety information."
                            pov "Safety information?"
                            officer_adaki "What's with the echo? You heard me, and I'ts gonna be me who run the show."
                    menu:
                        "Of course, just tell me what you need.":
                            officer_adaki "I'm gonna need an hour or so to talk to them, explain a couple of good-to-knows, ask a few questions."
                            pov "I'll set it up."
                            officer_adaki "U-hu, I'll get you posted on when."

                        "I'm not completely comfortable with this arrangement.":
                            officer_adaki "But you're comfortable with crisis and murder?"
                            pov "I'm afraid my answer is no."
                            officer_adaki "Well then, suit yourself. You're gonna be seeing a whole lot of me from now on."

                "Look, are you going to say something useful or simply continue to waste my time?":
                    officer_adaki "So I'm wasting your time, eh? Precious time kept from trying to cover your tracks?"
                    pov "Take me in, or take a hike. As long as you actually do SOMETHING."
                    officer_adaki "Oh I'm gonna do something alright, I'm gonna see to it that your students know what to expect from you in this situation."
                    pov "Stay away from my students."
                    officer_adaki "We'll see 'bout that, and I'll see you again."
                    pov "Oh I can't wait."
    return
    
label susan_marina_regarding_adaki:
    scene bg office with fade
    show susan_marina normal at center
    pov "Hello Susan. The days rush by, don't they?"
    show susan_marina happy
    susan_marina "Hello [povTitle] [povLastName], *giggle* they sure do."
    pov "I've been meaning to ask you something."
    show susan_marina normal
    susan_marina "Yes?"
    menu:
        "What's with this Adaki character?":
            show susan_marina normal_hand
            susan_marina "Oh, I've tried to figure him out myself. He's been skulking around here from time to time during his cases. Even if you're helpful and kind, he always seem to have a grumpy attitude."
            show susan_marina closed_eyes_hand
            pov "So he's been hanging around here before?"
            show susan_marina normal_hand
            susan_marina "Well, I wouldn't call it hanging around, but I remember one particular occasion when he insisted that every single teacher and student accounted for their whereabouts in detail."
            pov "What occasion was that?"
            show susan_marina normal
            susan_marina "He didn't give away much when it came to details himself, but it was a missing persons case a few years ago."
            pov "Who was the missing person?"
            susan_marina "That particular detail wasn't shared I'm afraid."
            pov "I see."
            susan_marina "What's on your mind?"
            pov "I'm not sure, but there's something about Adaki that makes my gut react."
            susan_marina "I wouldn't dwell upon it to much. But let me know if he bothers you."
            pov "Thank's, I will."

        "What do you make of this symbol?":
            show susan_marina normal_hand
            susan_marina "A peculiar pattern, where did you find it?"
            pov "No where particular, it just came to my attention."
            show susan_marina normal
            susan_marina "I'm no expert on symbols, ancient or otherwise. Could it be religious?"
            pov "What makes you think that?"
            susan_marina "Nothing really, just a guess as good as any."
            pov "Hmm, well thanks for your input."
            susan_marina "Not sure if I contributed, but you're welcome."
    return
