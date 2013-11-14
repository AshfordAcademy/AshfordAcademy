image bg sports_tourney1 = "screens/special_events/sports_tourney1.jpg"         # Win
image bg sports_tourney2 = "screens/special_events/sports_tourney2.jpg"         # Loss
image bg sports_tourney3 = "screens/special_events/sports_tourney3.jpg"         # Win 
image bg sports_tourney4 = "screens/special_events/sports_tourney4.jpg"         # Great victory
image bg sports_tourney5 = "screens/special_events/sports_tourney5.jpg"         # Bad loss

image bg fitness_training1 = "screens/special_events/fitness_training1.jpg"
#image bg fitness_training2 = "screens/special_events/fitness_training2.jpg"
#image bg fitness_training3 = "screens/special_events/fitness_training3.jpg"
#image bg fitness_training4 = "screens/special_events/fitness_training4.jpg"
#image bg fitness_training5 = "screens/special_events/fitness_training5.jpg"

image bg standard_test1 = "screens/special_events/standard_test1.jpg"

image bg art_exhibit1 = "screens/special_events/art_exhibit1.jpg"

image bg school_trip1 = "screens/special_events/school_trip1.jpg"
image bg school_trip2 = "screens/special_events/school_trip2.jpg"
image bg school_trip3 = "screens/special_events/school_trip3.jpg"
image bg school_trip4 = "screens/special_events/school_trip4.jpg"
image bg school_trip5 = "screens/special_events/school_trip5.jpg"
image bg school_trip6 = "screens/special_events/school_trip6.jpg"

# Raise money options
image raise_money clean_the_streets = "screens/special_events/raise_money_clean_the_streets.jpg"

init python:

    weekly_planning_focus_bonus = 0.6                # Additive for every time you focus the same.
    weekly_planning_focus = 2                        # The base bonus you always get per focus.
    monthy_event_bonus = 1
    first_sexual_weekly = False
    first_monthly_goal = False

    monthly_goal = ""
    monthly_goal_value = ""
    monthly_goal_type = ""
    monthly_goal_difficulty = ""
    
    def monthly_goal_check():
        if globals()['monthly_goal_type'] == "building":
            if globals()[eval('goal_building')] > globals()['monthly_goal_value']:
                return True
            
        elif globals()['monthly_goal_type'] == "stat":
            if globals()[eval('monthly_goal')] >= globals()['monthly_goal_value']:
                return True
        else:
            return True
        return

    def monthly_goal_menu():
        # Buidlings
        goal_list_buildings = []
        buildings = ['building_bath', 'building_classrooms', 'building_grounds', 'building_gym', 'building_library', 'building_pool', 'building_security', 'building_sports_field']
        for building in buildings:
            building_level = eval(building)
            building_cost_array = eval(building + '_price')
            building_cost = building_cost_array[building_level]
            if building_cost > 0:
                goal_list_buildings.append (building)
        
        if not goal_list_buildings:
            skip_building_goal = True
        
        globals()['goal_building'] = renpy.random.choice(goal_list_buildings)
        goal_building_name = goal_building.replace("building_", "")
        globals()['goal_building_name'] = goal_building_name.replace("_", " ")
        
        # Stats
        
        goal_list_stats = []
        normal_stats = ['Morale', 'Behavior', 'Academics', 'Artistery', 'Athletics']
        extra_stats = ['Inhibition', 'Deviance', 'Money']
        extras = ['reputation', 'orbs']
        for stat in normal_stats:
            stat = stat.lower()
            stat_num = eval(stat)
            if stat_num < 85:
                goal_list_stats.append (stat)
        
        if not goal_list_stats:
            goal_list_stats.append ("reputation")
        
        globals()['goal_stat'] = renpy.random.choice(goal_list_stats)
        globals()['goal_stat_num'] = globals()[eval('goal_stat')]
        
        # NOTE: Will be removed and replaced with "policy combinations", but need a system to keep track of daily policies first.
        globals()['goal_stat2'] = renpy.random.choice(goal_list_stats)

        goal = renpy.display_menu([
            (goal_building_name, "goal_building"),
            (goal_stat, "goal_stat"),
            (goal_stat2, "goal_stat2")
            ])

        if goal == "goal_building":
            globals()['monthly_goal'] = goal_building
            globals()['monthly_goal_value'] = building_level
            globals()['monthly_goal_type'] = "building"

        elif goal == "goal_stat":
            globals()['monthly_goal'] = goal_stat
            globals()['monthly_goal_type'] = "stat"

            globals()['goal_difficulty3'] = eval(goal_stat) + 10 + (5 * 3)
            globals()['goal_difficulty2'] = eval(goal_stat) + 10 + (5 * 2)
            globals()['goal_difficulty1'] = eval(goal_stat) + 10 + (5 * 1)

            globals()['monthly_goal_value'] = renpy.display_menu([
                ("[goal_stat]: [goal_difficulty3]" , goal_difficulty3),
                ("[goal_stat]: [goal_difficulty2]" , goal_difficulty2),
                ("[goal_stat]: [goal_difficulty1]" , goal_difficulty1)
                ])

        elif goal == "goal_stat2":
            globals()['monthly_goal'] = goal_stat2
            globals()['monthly_goal_value'] = eval(goal_stat2) + 20
            globals()['monthly_goal_type'] = "stat"
            
        else:
            "Error: No goal selected."

        return

# Weekly planning - Part 1
label weekly_planning:
    
    scene bg office with fade
    if extroduce_jennifer_adriano == True and susan_returns == False:
        show teacher_susan sad at center
        pov "I'm glad you stayed around. I really have no idea what I would have done if you hadn't."
        teacher_susan "I - I don't know what to say. That poor girl..."
        pov "I know, feels surreal."
        teacher_susan "Well, I'll be staying for as long as you need me."
        pov "That's good to know, thank you."
        teacher_susan "..."
        pov "Well, as the song says, the show must go on. We must focus on the work at hand."
        teacher_susan "I guess so."
        pov "Thank you Susan."
        teacher_susan "Well Ashford, here we go again."
        $ susan_returns = True
    else:
        show teacher_susan normal at center
        teacher_susan "Today we need to plan what to focus on for the next week. Remember, every week you can change your plan."
    menu:
        "Make them behave.":
            python:
                behavior += weekly_planning_focus + beh_focus
                beh_focus += weekly_planning_focus_bonus
                if renpy.random.random() > 0.5:
                    reputation += 1

        "We should create the next generation of great minds!":
            python:
                academics += weekly_planning_focus + academics_focus
                academics_focus += weekly_planning_focus_bonus
                if renpy.random.random() > 0.5:
                    blue_orb += 1

        "Let's create the art and culture of tomorrow!":
            python:
                artistery += weekly_planning_focus + art_focus
                art_focus += weekly_planning_focus_bonus
                if renpy.random.random() > 0.5:
                    yellow_orb += 1

        "Our students shall become the next Olympic champions!":
            python:
                athletics += weekly_planning_focus + ath_focus
                ath_focus += weekly_planning_focus_bonus
                if renpy.random.random() > 0.5:
                    green_orb += 1

        "We should encourage them to... Explore their bodies." if deviance > 5:
            if first_sexual_weekly == False and inhibition > 50:
                $ first_sexual_weekly = True
                teacher_susan "Sorry?"
                show teacher_susan surprised
                teacher_susan "Did you say... Explore their bodies?"
                menu:
                    "Indeed, they need to be more comfortable with their bodies.":
                        teacher_susan "I... see..."
                        teacher_susan "But [povTitle] [povLastName] do you really think this is appropriate?"
                        pov "You see Susan there is only one way for students to learn about this and since we are responsible for their future we have to do this."
                        teacher_susan "I understand [povTitle] [povLastName]."
                    
                    "It's important for psychosexual development.":
                        teacher_susan "I'm not sure I follow [povTitle] [povLastName]."
                        pov "Don't you know your psychology?"
                        show teacher_susan sad
                        teacher_susan "Well it's not my field, Jack Drake usually covers that part."
                        pov "The point is that humans are born polymorphously perverse and if you deny the sexual development, such as getting to know your own body, your mental health will suffer."
                        show teacher_susan closed_eyes
                        teacher_susan "I'm not really sure about this [povTitle] [povLastName], but its up to you."
                        pov "It is and this is how we will do it."
                        
                    "Hell yeah! Why do you think I work here?" if new_game_plus == True:
                        show teacher_susan angry
                        teacher_susan "..."
                        teacher_susan "You are a very, very disturbing person."
                        pov "Susan?"
                        teacher_susan "[povTitle] [povLastName]?"
                        pov "Maybe we should explore your body as well?"
                        teacher_susan "..."
                        
            python:
                deviance += weekly_planning_focus + sex_focus
                sex_focus += weekly_planning_focus_bonus
                if renpy.random.random() > 0.5:
                    red_orb += 1

    show teacher_susan normal at center
    if first_week == False:
        teacher_susan "Very well, I will inform the rest of the teachers."
    else:
        teacher_susan "Well [povTitle] [povLastName], I just talked to the board. They said that the Agency sends their best wishes, and they wanted me to tell you that the new secretary will arrive on monday morning."
        pov "The new secretary?"
        teacher_susan "Oh, it must have slipped my mind. Since I was assigned by the old administration, the board thought it would be better for you to mold your own team."
        menu:
            "What about you?":
                pov "Sounds a bit unfair, don't you think?"
                teacher_susan "Oh, don't worry about me, I'll have enough to do as it is. Sweet of you to care though."

            "Sounds fair.":
                pov "If that's what they want, I guess I'll move along accordingly."
                teacher_susan "I really think it's for the best. With all the recent events still fresh in mind, the board wants to make a clean slate."

            "But- but, I thought I was gonna score!" if new_game_plus == True:
                teacher_susan "..."
                pov "Ahaha, sometimes I just kill myself!"
                teacher_susan "If only..."
    
    
    # Weekly planning - Part 2
    scene bg office with fade
    show nurse_normal at center
    nurse  "Hello [povTitle] [povLastName]."
    
    $ called_in_sick = renpy.random.randint(0, population/20)
    
    nurse "This week [called_in_sick] students have called in sick."
    pov "Thank you nurse. Keep up the good work."
    nurse  "My pleasure [povTitle] [povLastName]."
    

    # Weekly planning - Part 3
    scene bg office with fade
    if first_week == True:
        show teacher_susan normal at center
        pov "Thank you for getting me up to speed with school administration and all. It sure is a long road ahead, but at least now I know a little about which direction to take."
        teacher_susan "Glad to be of assistance. Hope your new secretary settles in smoothly."
        pov "I'm sure she will."
        teacher_susan "Well, goodbye [povTitle] [povLastName]. And good luck to you."
        pov "Thank you."
        $ first_week = False
    else:
        info "You think to yourself..."
        python:       
            if academics and artistery and athletics < 20 + month:
                pov("Maybe we should focus a bit more on the basic education.")
            elif behavior < 20 + month:
                pov("It would be good if we could get the students to behave better.")
            elif morale < 20 + month:
                pov("I wonder what we could do to make the students happier?")
            elif inhibition > 85 - month:
                pov("I think it would be good for all of us if the students would be a bit more relaxed.")
            else:
                pov("A job well done.")
    jump night


# Monthly planning - Part 1
label monthly_planning:
    
    scene bg office with fade
    show teacher_susan normal at center
    teacher_susan "The first of every month we organize something special for the students. What would you like us to do?"
    menu:
        "Science fair":
            teacher_susan "I will organize this [povLastName]."
            
            $ academics += monthy_event_bonus
        
        "Standard tests" if academics > 45:
            python:
                renpy.transition(fade, None, False)
                if renpy.random.randint(1, 101) < academics:
                    renpy.scene()
                    standard_test_win = renpy.random.choice(["standard_test1"])
                    renpy.show("bg "+standard_test_win)
                    teacher_susan("Our score was so high that Ashford Academy is rated one of the best in the nation.")
                    academics += 1
                    reputation += 1
                
                elif renpy.random.randint(1, 101) > academics:
                    renpy.scene()
                    renpy.show("bg standard_test1")
                    teacher_susan("Our students got some of the worst grades in the country.")
                    academics += 1
                    reputation -= 1
                
                else:
                    renpy.scene()
                    renpy.show("bg standard_test1")
                    
                    teacher_susan("School results where in the midrange with most other schools.")
                    academics += 1

        "Fitness training":
            scene bg fitness_training1 with fade
            teacher_susan "We made great progress with the Ashford Volleyball Team."
            
            $ athletics += monthy_event_bonus
        
        "Sports Tourney" if athletics > 45:
            python:
                renpy.transition(fade, None, False)
                if renpy.random.randint(1, 101) < athletics:
                    renpy.scene()
                    sports_tourney_win = renpy.random.choice(["sports_tourney1", 'sports_tourney3', 'sports_tourney4' ])
                    renpy.show("bg "+sports_tourney_win)
                    teacher_susan("The Ashford Volleyball Team did great and won every match including the finals!")
                    athletics += 1
                    reputation += 1
                
                elif renpy.random.randint(1, 101) > athletics:
                    renpy.scene()
                    renpy.show("bg sports_tourney5")
                    teacher_susan("Our team was utterly destroyed and had nothing against the other teams.")
                    athletics += 1
                    reputation -= 1
                
                else:
                    renpy.scene()
                    renpy.show("bg sports_tourney2")
                    
                    teacher_susan("Our Volleyball Team had a good start but lost against some of the best national teams.")
                    athletics += 1

        "Visit museum":
            teacher_susan "I will organize this [povLastName]."
            
            $ artistery += monthy_event_bonus
        
        "Art Exhibit" if artistery > 45:
            python:
                renpy.transition(fade, None, False)
                if renpy.random.randint(1, 101) < artistery:
                    renpy.scene()
                    renpy.show("bg art_exhibit1")
                    teacher_susan("Our exhibit got a lot of attention and some students even sold some of their art!")
                    artistery += 1
                    reputation += 1
                
                elif renpy.random.randint(1, 101) > artistery:
                    renpy.scene()
                    renpy.show("bg art_exhibit1")
                    teacher_susan("We didn't get much attention and the few who came thought it was a joke.")
                    artistery += 1
                    reputation -= 1
                
                else:
                    renpy.scene()
                    renpy.show("bg art_exhibit1")
                    teacher_susan("We got some attention although mostly from parents and family.")
                    artistery += 1

        "Raise money":
            teacher_susan "This is what we can do to raise money."
            menu:
                "Clean the streets":
                    python:
                        renpy.scene()
                        renpy.show("raise_money clean_the_streets")
                        raise_money = int(renpy.random.randint(1, 2) * population )
                        cash += raise_money
                        morale -= 2
                        teacher_susan("Our students raised [raise_money]$ but didn't enjoy the task.")
                "Cancel":
                    jump monthly_planning
                    
        "School trip" if cash >= population:
            teacher_susan "This is usually a good boost to morale and will cost [population] $.\nIs this ok?"
            menu:
                "Yes":
                    python:
                        cash -= population
                        renpy.transition(fade, None, False)
                        if renpy.random.randint(1, 3) == 1:
                            renpy.scene()
                            school_trip = renpy.random.choice(["school_trip1", "school_trip2","school_trip3", "school_trip4", "school_trip5"])
                            renpy.show("bg "+school_trip)
                            teacher_susan("Everyone had a great time with lots of fun.")
                            morale += 2
                            reputation += 1
                        
                        elif renpy.random.randint(1, 5) == 1:
                            renpy.scene()
                            renpy.show("bg school_trip6")
                            teacher_susan("The school trip went ok, not everyone enjoyed it.")
                            morale += 1
                            reputation -= 1
                        
                        else:
                            renpy.scene()
                            renpy.show("bg school_trip1")
                            
                            teacher_susan("They had a good time.")
                            morale += 1

                "No":
                    jump monthly_planning

    # Monthly planning - Part 2
    scene bg office with fade
    pov "A job well done."
    
    # Monthly planning - Part 3 - Set up a goal for the next month.
    scene bg office with fade
    show teacher_susan normal at center
    if first_monthly_goal == False:
        susan_marina "[povTitle] [povLastName] every month we receive feedback from students, teachers and parents organizations. We use this feedback to set up a list of goals for our academy to strive for."
        susan_marina "I try to order all the feedback and create a list where we choose one goal to focus on every month. Failing to achieve the set goal will result in negative publicity and hurt the schools reputation."
        susan_marina "Please also keep in mind that you can influence how high we set each and every goal."
        $ first_monthly_goal = True
    else:
        if monthly_goal_check() == True:
            show teacher_susan happy
            susan_marina "Good work with last months goal I am sure this will boost Ashfords reputation."
            $ reputation += 3
        else:
            show teacher_susan sad
            susan_marina "Your failure resulted in negative publicity and hurt the schools reputation."
            $ reputation -= 5
    
    show teacher_susan normal
    susan_marina "So [povTitle] [povLastName], what goal will we have for this month?"
    $ monthly_goal_menu()

    if monthly_goal_type == "building":
        if monthly_goal_value == 0:
            susan_marina "Our goal for the next month is to build a [goal_building_name]."
        else:
            susan_marina "Our goal for the next month is to upgrade our [goal_building_name] above level [monthly_goal_value]."
            
    elif monthly_goal_type == "stat":
        susan_marina "Our goal for the next month is for [monthly_goal] to reach [monthly_goal_value]."
        
    else:    
        susan_marina "You obviously have no goal in life. So sad..."
    
    jump night
