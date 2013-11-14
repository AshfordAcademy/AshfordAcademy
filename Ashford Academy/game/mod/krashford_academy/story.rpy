########################################################
#
#  KRAshford Academy
#  GET TO THE CHOPPA!
#
########################################################

label krashford_start:
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

    'Standing at the gates, you brush off some dust from your jacket. The school area towers up before you as you peek through the bars. "Ashford" - the wide, cold letters make an old fashioned scenery pop up in your head and you feel a proud history whisper to you: "Welcome stranger, to our university".'
    "Proud as it may be, Ashford of today is far from it's prime. Things have been going downhill for quite some time and the last administration gave up and made a run for it. At least that's what you've heard. The situation called for serious action to be taken and that's when they called you."
    'The gates bid you welcome. \nYou take a deep breath and push them open.'

    # Show the Ashford backgrounds with Susan.
    scene bg Ashford_Academy with fade
    show ka_kiri_kora normal at center

    
    ka_kiri_kora "Hey! What the fuck are you doing? Get down!"
    pov "But-"
    ka_kiri_kora "No butts for you [povTitle], come with me if you want to live."
    pov "What's going on?!"
    ka_kiri_kora "I'll tell you what's going on, we're being invaded, that's what goes!"
    pov "Invaded? Huh? Who are you? Where's Susan?"
    ka_kiri_kora "Susan's dead."
    pov "W-what? NOOOOOOO!"
    ka_kiri_kora "Yup. Dead as a door nail."
    pov "NOOOOOOO!"
    ka_kiri_kora "Sleeping with the fishes."
    pov "NOOOOOOO!"
    ka_kiri_kora "Putting away the newspaper."
    pov "NOOOO- What?"
    ka_kiri_kora "Never mind. She's gone and you're under my jurisdiction now."
    pov "I'm confused, invaded by whom?"
    ka_kiri_kora "Not by whom, by what. Ashford is infested with the undead."
    pov "LOL! You had me going there for a second. Susan dead, Ashford infested with zombies, me being under your jurisdiction. ROFL!"
    ka_kiri_kora "Look fucktard, you can ROFLYAO for all that I care. The truth is, all Hell's broken loose and we're not only talking about zombies. Imagine germ warfare gone awry leaving us little gifts, only these gifts explode in your face when you try to open them. Basically, your worst nightmare."
    pov "No, waking up without my penis is my worst nightmare."
    ka_kiri_kora "Oh, alright, ok, it might not be your WORST nightmare but it's quite up there!"
    pov "Who did you say you were again?"
    ka_kiri_kora "I didn't."
    pov "Ah. Look missy, I appreciate women's liberation and all, but please. If shit has really hit the fan, step back and let a man handle this."
    ka_kiri_kora "How many teeth do you have?"
    pov "What?"
    ka_kiri_kora "How many teeth?"
    pov "I don't see what my teeth has got to do..."
    ka_kiri_kora "*BAM*"
    pov "*crying* For the love of God! Please don't hurt me, baaaaaaaaaaw!"
    ka_kiri_kora "Zip it bitch, I control this party. You just be a good little principal and do as I say, capiche?"
    pov "Boohoo, just d-don't *sniffle* h-hit *sob* m-me no more!"
    ka_kiri_kora "Jesus H Christ."
    pov "Mommy!"
