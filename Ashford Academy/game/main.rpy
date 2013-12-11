###############################################
#               Ashford Academy
#               Revision 0.4036
#FIXME
#
###############################################

# For transition effect
image bg circleiris = "transitions/id_circleiris.png"

# The variable we store for the entered name of the main char and a DynamicCharacter that has the same stored in povName.
define povFirstName = ""
define povLastName = ""
define povName = ""             # povName = povFirstName + povLastName
define povGender = "male"       # Female/Male - As in social gender, You will be able to be perceived as male AND Futa or female AND Futa.
define povFuta = False          # True/False
define povTitle = "Mr."         # Mr./Ms.
define povBdsmTitle = "Master"  # Master/Mistress
define pov = DynamicCharacter("povName", color=(150, 0, 32, 255))


init python:
    # Load/Import library "Math", it's used in some calcs such as "pay_day".
    import math

    # Variables for unlockable scenes
    new_game_plus = False
    start_day_with_gin = False

    inhibition_min = 75
    lower_inhibition_level = 1

    # Stuff for notification system
    new_messages = 0
    mail = []
    reply_screen = False

    if persistent.mod_disable_original_stats == False:
        # Stats that will be shown on the "main" GUI
        register_stat("Morale", "morale", 0, 5, 100)
        register_stat("Behavior", "behavior", 5, 0, 100)
        register_stat("Academics", "academics", 10, 0, 100)
        register_stat("Artistery", "artistery", 10, 0, 100)
        register_stat("Athletics", "athletics", 10, 0, 100)
        register_stat("Deviance", "deviance", 0, 0, 100)
        register_stat("Inhibition", "inhibition", 75, 100, 100)

    # Stats - Orbs
    red_orb = 0
    blue_orb = 0
    green_orb = 0
    yellow_orb = 0



########################################################
#   This will most likely be moved at some point in time

    # Image dissolve Transitions.
    circleirisout = ImageDissolve("transitions/id_circleiris.png", 1.0, 8)
    circleirisin = ImageDissolve("transitions/id_circleiris.png", 1.0, 8, reverse=True)

    # Content options - can be changed in the options screen. Will be used mostly for third-party content.
    persistent.content_list = dict(googirls=False, tentacles=False, catgirls=False, loli=False)

    #Disable the rollback function - No cheating!
    config.rollback_enabled = False

########################################################
#   Sets the choices of the daily planner.
#   @returns nothing
    def setDayPlannerChoices():
        dp_period("Morning", "morning_act")
        dp_choice("Office", "office")
        if (building_sports_field > 0):
            dp_choice("Sports field", "sports_field")
        if (building_gym > 0):
            dp_choice("Gym", "gym")

        dp_period("Afternoon", "afternoon_act")
        dp_choice("Class", "class",)
        if (building_pool > 0):
            dp_choice("Pool", "pool")
        if (building_cafeteria > 0):
            dp_choice("Cafeteria", "cafeteria")

        dp_period("Evening", "evening_act")
        dp_choice("School grounds", "school_grounds")
        if (building_dormitory > 0):
            dp_choice("Dormitory", "dormitory")
        if (building_library > 0):
            dp_choice("Library", "library")
        if (building_bath > 0):
            dp_choice("Bath", "bath")
        return


########################################################
#
#  Game start
#  The script here is run as soon as you press new game.
#
########################################################

label new_game_plus:
    if renpy.has_label(persistent.mod_custom_new_game_plus):
        $ renpy.jump(persistent.mod_custom_new_game_plus)
    else:
        scene black
        "New content unlocked."
        $ new_game_plus = True
        "Please choose your gender:"
        menu:
            "Male":
                $ povGender = 'male'
                $ povTitle = "Mr."
            "Female":
                $ povGender = 'female'
                $ povTitle = "Mrs."

# This is the entry point into the game. Find more info in story.rpy.
label start:
    if renpy.has_label(persistent.mod_custom_new_game):
        $ renpy.jump(persistent.mod_custom_new_game)
    else:
        jump new_game

# This is the label that is jumped to at the start of a day. Also, check available classes.
label day:

    # Increment the day and add any new buildings to the list.
    $ new_day()

##############################################################################
# Here's some story triggers and game over stuff
#
# See game_over.py in /screens for more information.

    # Default school background.
    scene bg Ashford_Academy with circleirisout

    jump game_over_test

label day_no_game_over:

    if first_week == False and introduce_jennifer_adriano == False:
        "You remember what Susan said so you decide to go and meet you new secretary."
        call jennifer_adriano_introduction

#
# Here ends the story and game over stuff.
#
##############################################################################

    # See what classes we have and what needs to be done to access them. Every 7th day is planning day with weekly bonus.
    # The 1st of every month we have monthly extra planning.
    # Remember, at least one class in each period is req. to actually "play/plan" each day.

    $ planning_day += 1

    if (day == 1 and persistent.mod_disable_monthly_planning == False):
        "Today is the monthly planning day. Better get on with it!"
        $ pay_day(population,reputation)
        jump monthly_planning

    elif (planning_day >= 7):
        $ planning_day = 0
        $ building_bonus()
        $ policy_bonus()
           
        if persistent.mod_disable_weekly_planning == False:
            "Weekly planning day is today!"
            jump weekly_planning

    else:
        python:
            setDayPlannerChoices()

    $ today = weekday_name[planning_day]


    # Here we set up the default values for the day planner.

    $ morning_act = None
    $ afternoon_act = None
    $ evening_act = None

    # Now, we call the day planner, which may set the act variables
    # to new values. We call it with a list of periods that we want
    # to compute the values for.
    call day_planner(["Morning", "Afternoon", "Evening"])


    # We process each of the three periods of the day, in turn.
label morning:

    # We set the "change" value so we can visualize the change as in red/green numbers on the UI.
    python:
        Morale_change = morale
        Behavior_change = behavior
        Academics_change = academics
        Artistery_change = artistery
        Athletics_change = athletics
        Deviance_change = deviance
        Inhibition_change = inhibition

        cash_change = cash
        reputation_change = reputation
        population_change = population

        red_orb_change = red_orb
        blue_orb_change = blue_orb
        green_orb_change = green_orb
        yellow_orb_change = yellow_orb


    # Tell the user what period it is.
    scene black with fade
    if(year > 1):
        centered "Year: %(year)d [month_now] %(day)d: [today] morning"
    else:
        centered "[month_now] %(day)d: [today] morning"

    # Set these variables to appropriate values, so they can be
    # picked up by the expression in the various events defined below.
    $ period = "morning"
    $ act = morning_act

    # Ensure that the stats are in the proper range. (0-var.max)
    $ normalize_stats()

    # Execute the events for the morning.
    call events_run_period

    # That's it for the morning, so we fall through to the afternoon.

label afternoon:

    # It's possible that we will be skipping the afternoon, if one
    # of the events in the morning jumped to skip_next_period. If
    # so, we should skip the afternoon.
    if check_skip_period():
        jump evening

    # The rest of this is the same as for the morning.
    scene black with fade
    if(year > 1):
        centered "Year: %(year)d [month_now] %(day)d: [today] afternoon"
    else:
        centered "[month_now] %(day)d: [today] afternoon"

    $ period = "afternoon"
    $ act = afternoon_act

    $ normalize_stats()

    call events_run_period


label evening:

    # The evening is the same as the afternoon.
    if check_skip_period():
        jump night

    scene black with fade
    if(year > 1):
        centered "Year: %(year)d [month_now] %(day)d: [today] evening"
    else:
        centered "[month_now] %(day)d: [today] evening"

    $ period = "evening"
    $ act = evening_act

    $ normalize_stats()

    call events_run_period


label night:

    # This is now the end of the day, and not a period in which normal events
    # can be run. We put some boilerplate end-of-day text in here.

    scene bg home with circleirisin
    centered "Night"

    if introduce_jennifer_adriano == True and extroduce_jennifer_adriano == False and planning_day == 6:
        jump jennifer_adriano_extroduction

    if extroduce_jennifer_adriano == True and introduce_officer_adaki == False and planning_day == 5:
        jump interrogation


    if planning_day == 0:
        python:
            if povGender == "male":
                drink = renpy.random.choice(["Jack Daniels", 'Glenfiddich', 'Bagpiper', 'Captain Morgan', 'Red label', 'Ole Smoky', 'Laphroaig', 'Yamazaki', 'Black Label', 'Teerenpeli'])
            elif povGender == "female":
                drink = renpy.random.choice(["Chateau d'Yquem", 'Musella', 'Bourgogne Chardonnay', 'Abraxas', 'Hidden Rock'])
            else:
                drink = "Error"
        "After a long day of planning you decide to pour yourself a glass of [drink]."

    elif planning_day == 8:
        "You don't remember why, but this day feels special. You decide a glass of Bombay Sapphire on the rocks would be appropriate."

    if renpy.random.randint(1,20) == 1:
        if povGender == "female":
            "You decide to take a shower and {i}comfort yourself{/i} before going to bed."
        else:
            "You decide to shower and shave before going to bed."
    else:
        "It's getting late, so you decide to go to sleep."

    # We call events_end_day to let it know that the day is done.
    call events_end_day

    # And we jump back to day to start the next day. This goes
    # on forever, until an event ends the game.
    jump day


# This is a callback that is called by the day planner. One of the
# uses of this is to show the statistics to the user.
label dp_callback:

    $ display_stats()
    $ display_extra_stats()
    return


label after_load:
    # TODO: Make sure mail get loaded here as well.
    python:
        update_stat_min('inhibition', 100 - (lower_inhibition_level * 25))
    $ setDayPlannerChoices()
    return

