# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    if reply_screen:
        # this is the menu for message replies
        frame:
            style_group "mailbox"

            vbox:
                label "Draft Reply"
                text ("To: " + current_message.sender)
                text ("Subject: Re: " + current_message.subject)
                null  height 30

                for caption, action, chosen in items:

                    if action:
                        button:
                            action action
                            style "menu_choice_button" xalign 0.5

                            text caption text_align 0.5

                    else:
                        text caption style "menu_caption"
    else:
        # this is the default choice menu
        window:
            style "menu_window"
            xalign 0.5
            yalign 0.5

            vbox:
                style "menu"
                spacing 2

                for caption, action, chosen in items:

                    if action:

                        button:
                            action action
                            style "menu_choice_button"

                            text caption style "menu_choice"

                    else:
                        text caption style "menu_caption"


init -2 python:
    config.narrator_menu = True

    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window:
        has vbox

        text prompt
        input id "input"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    imagemap:
            ground persistent.mod_custom_title_screen_ground
            idle "gui/mm_idle.png"
            hover "gui/mm_hover.png"
                
            # This is so that everything transparent is invisible to the cursor.
            alpha False

            if persistent.new_game_plus:
                hotspot (1066, 417, 176, 39) action Start("new_game_plus")
            else:
                hotspot (0, 0, 0, 0) action Start("new_game_plus")

            hotspot (1066, 466, 176, 39) action Start()
            hotspot (1066, 514, 176, 39) action ShowMenu("load")
            hotspot (1066, 561, 176, 39) action ShowMenu("preferences")
            hotspot (1066, 610, 176, 39) action Help()
            hotspot (1066, 657, 176, 39) action Quit(confirm=False)

init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"


##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    imagemap:
            ground "gui/mb_ground.png"
            idle "gui/mb_idle.png"
            hover "gui/mb_hoover.png"
            selected_idle "gui/mb_hoover.png"

            alpha False

            hotspot (1066, 369, 176, 39) action Return()
            hotspot (1066, 417, 176, 39) action ShowMenu("preferences")
            hotspot (1066, 466, 176, 39) action ShowMenu("save")
            hotspot (1066, 514, 176, 39) action ShowMenu("load")
            hotspot (1066, 561, 176, 39) action MainMenu()
            hotspot (1066, 610, 176, 39) action Help()
            hotspot (1066, 657, 176, 39) action Quit(confirm=False)


init -2 python:
    style.gm_nav_button.size_group = "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 6

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    # Format the description, and add it as text.
                    $ description = "% 2s. %s\n%s" % (
                        FileSlotName(i, columns * rows),
                        FileTime(i, empty=_("Empty Slot.")),
                        FileSaveName(i))

                    text description

                    key "save_delete" action FileDelete(i)


screen save:

    # This ensures that any other menu screen is replaced.
    tag menu
    use navigation
    use file_picker


screen load:

    # This ensures that any other menu screen is replaced.
    tag menu
    use navigation
    use file_picker


init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_frame.top_margin = 5
    style.file_picker_frame.left_margin = 5
    style.file_picker_frame.right_margin = 250
    style.file_picker_frame.bottom_margin = 5

    style.file_picker_nav_button.xalign = 0.5

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)



##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox
                label _("{b}Toggle content{/b}")
                grid 1 7:
                    vbox:
                        label _("Googirls")
                        textbutton _("Enabled") action SetDict(persistent.content_list, "googirls", True)
                        textbutton _("Disabled") action SetDict(persistent.content_list, "googirls", False)
                    vbox:
                        label _("Tentacles")
                        textbutton _("Enabled") action SetDict(persistent.content_list, "tentacles", True)
                        textbutton _("Disabled") action SetDict(persistent.content_list, "tentacles", False)
                    vbox:
                        label _("Catgirls")
                        textbutton _("Enabled") action SetDict(persistent.content_list, "catgirls", True)
                        textbutton _("Disabled") action SetDict(persistent.content_list, "catgirls", False)
                    vbox:
                        label _("Loli")
                        textbutton _("Enabled") action SetDict(persistent.content_list, "loli", True)
                        textbutton _("Disabled") action SetDict(persistent.content_list, "loli", False)
                    vbox:
                        label _("Placeholder 1")
                        textbutton _("Enabled") action SetDict(persistent.content_list, "loli", True)
                        textbutton _("Disabled") action SetDict(persistent.content_list, "loli", False)
                    vbox:
                        label _("Placeholder 2")
                        textbutton _("Enabled") action SetDict(persistent.content_list, "loli", True)
                        textbutton _("Disabled") action SetDict(persistent.content_list, "loli", False)
                    vbox:
                        label _("Placeholder 3")
                        textbutton _("Enabled") action SetDict(persistent.content_list, "loli", True)
                        textbutton _("Disabled") action SetDict(persistent.content_list, "loli", False)


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")
            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton "Test":
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            frame:
                style_group "pref"
                has vbox

                label _("Voice Volume")
                bar value Preference("voice volume")

                if config.sample_voice:
                    textbutton "Test":
                        action Play("voice", config.sample_voice)
                        style "soundtest_button"

init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill False
        ypos .1
        xpos .35
        yanchor 0
        ypadding .05
        xpadding .04

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


init -2 python:
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"

    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False

##############################################################################
# Policy Menu
#
# Show policy screen and options.

screen policy_screen:
    imagemap:
        ground "gui/menu_bg.png"

    hbox:
        xfill True
        yfill True
        vbox:
            python:
                ui.imagebutton("gui/student_rules_idle.png", "gui/student_rules_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("policy_screen", "student_rules")])
                ui.imagebutton("gui/learning_materials_idle.png", "gui/learning_materials_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("policy_screen", "learning_materials")])

        vbox:
            xfill True
            xpos 0.008
            ypos 0.008
            if policy_screen == "learning_materials":
                label _("Depiction of the human body")
                if(hyper_anatomic_body > 0 ):
                    textbutton _("Hyper sexualized - Use models based on porn stars.") action SetVariable("anatomic_body", 1.3) xminimum 800
                textbutton _("Normal - Usage of anatomical correct human models.") action SetVariable("anatomic_body", 0.7) xminimum 800
                textbutton _("Non sexual - Non sexualized versions of the human body.") action SetVariable("anatomic_body", 0) xminimum 800
                null height 25

                label _("Learning materials")
                textbutton _("New - Buy new materials for each and every class.") action SetVariable("learning_materials", 1.3) xminimum 800
                textbutton _("Normal - Reuse of materials and buy new when needed.") action SetVariable("learning_materials", 1) xminimum 800
                textbutton _("Old & Cheap - Reuse materials as long as possible.") action SetVariable("learning_materials", 0.7) xminimum 800
                null height 25

                label _("Salary - Here you can adjust the salary of your teachers.")
                textbutton _("High salary - Teachers get a significant salary boost.") action [SetVariable("salary", "salary_high"), SetVariable("salary_skill_multiplier", 1.7)] xminimum 800
                textbutton _("Normal salary - Normal teacher salary used at other schools.") action [SetVariable("salary", "salary_normal"), SetVariable("salary_skill_multiplier", 1.2)] xminimum 800
                textbutton _("Low salary - Teachers get paid a bit less then normal.") action [SetVariable("salary", "salary_low"), SetVariable("salary_skill_multiplier", 0.7)] xminimum 800

            elif policy_screen == "student_rules":
                label _("Entrance requirements - The requirements to be accepted to your school.")
                textbutton _("Perfect record - Perfect behaviour and academics.") action SetVariable("entrance_req", 5) xminimum 800
                textbutton _("Advanced requirements - Need to pass a special exam.") action SetVariable("entrance_req", 4) xminimum 800
                textbutton _("Standard requirements - Need to pass a normal exam.") action SetVariable("entrance_req", 3) xminimum 800
                textbutton _("Age requirements - You only need to be old enough.") action SetVariable("entrance_req", 2) xminimum 800
                textbutton _("No requirements - Everyone is welcome. Even you.") action SetVariable("entrance_req", 1) xminimum 800
                null height 25

                label _("Dress code - What sort of clothing will be required to wear at school. ")
                if nude_uniform > 0:
                    textbutton _("Nude - No clothing allowed during class.") action SetVariable("uniform", "nude_uniform") xminimum 800
                if sexy_uniform > 0:
                    textbutton _("Sexy uniform - A uniform showing more skin. ") action SetVariable("uniform", "sexy_uniform") xminimum 800
                textbutton _("No uniform - Students are allowed to wear anything.") action SetVariable("uniform", "no_uniform") xminimum 800
                textbutton _("Normal uniform - A basic school uniform.") action SetVariable("uniform", "normal_uniform") xminimum 800
                textbutton _("Conservative uniform - A uniform showing less skin.") action SetVariable("uniform", "conservative_uniform") xminimum 800
                null height 25

                label _("PDA Rules - Determines how you will punish public displays of affection.")
                if no_detention > 0:
                    textbutton _("Nothing - Make love, not war, man.") action [SetVariable("pda_rules", "pda_none"), SetVariable("pda_rule_level", 1)] xminimum 800
                textbutton _("Detention - A little lax, but more students will show off this way.") action [SetVariable("pda_rules", "pda_detention"), SetVariable("pda_rule_level", 2)] xminimum 800
                textbutton _("Suspension - Most schools follow this rule.") action [SetVariable("pda_rules", "pda_suspension"), SetVariable("pda_rule_level", 3)] xminimum 800
                textbutton _("Expulsion - Public display are not allowed at all.") action [SetVariable("pda_rules", "pda_expulsion"), SetVariable("pda_rule_level", 4)] xminimum 800
                if bdsm_detention > 0:
                    textbutton _("BDSM Detention - Taste the whip.") action [SetVariable("pda_rules", "pda_bdsm"), SetVariable("pda_rule_level", 5)] xminimum 800
                null height 25

                label _("Behavior - Amount of violence allowed to punish students.")
                textbutton _("Everything goes - Teachers are allowed to do whatever they feel like.") action [SetVariable("behavior_rules", "behavior_no_limit"), SetVariable("behavior_rules_multiplier", 2)] xminimum 800
                textbutton _("Physical abuse - Teachers are allowed to use moderate violence.") action [SetVariable("behavior_rules", "behavior_physical"), SetVariable("behavior_rules_multiplier", 1.5)] xminimum 800
                textbutton _("Verbal abuse - Verbal and non physical abuse are allowed.") action [SetVariable("behavior_rules", "behavior_verbal"), SetVariable("behavior_rules_multiplier", 1)] xminimum 800
                textbutton _("Zero tolerance - No kind of aggression towards students are allowed.") action [SetVariable("behavior_rules", "behavior_zero"), SetVariable("behavior_rules_multiplier", 0.6)] xminimum 800

            else:
                text "Here you choose what rules your students and teachers should follow."
    vbox:
        xalign 0.992
        yalign 0.992
        $ ui.imagebutton("gui/return_button_idle.png", "gui/return_button_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=ui.returns(0))

##############################################################################
# Buildings Menu
#
# Build and upgrade your buildings.

screen buildings_screen:
    imagemap:
        ground "gui/menu_bg.png"

    python:
        building_level = globals()[eval('building_pick')]
        building_cost_array = eval(building_pick + '_price')
        building_cost = building_cost_array[building_level]

        def _buy_building(cost):
            globals()[eval('building_pick')] += 1               # Register the new building.
            globals()['cash'] -= cost                           # Pay the price.

            renpy.restart_interaction()                         # Make sure we update the UI so you get feedback when you buy.
            return

        buy = renpy.curry(_buy_building)                        # Curry is used to make sure buy only gets activated on click. (Think of it as a handler.)

    hbox:
        xfill True
        yfill True
        vbox:
            yfill True
            vbox:
                python:
                    ui.imagebutton("gui/bath_idle.png", "gui/bath_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("building_pick", "building_bath")])
                    ui.imagebutton("gui/classrooms_idle.png", "gui/classrooms_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("building_pick", "building_classrooms")])
                    if persistent.we_dont_need_no_education_achievement_trigger == True:
                        ui.imagebutton("gui/cafeteria_idle.png", "gui/cafeteria_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("building_pick", "building_cafeteria")])
                    if persistent.the_1_achievement_trigger == True:
                        ui.imagebutton("gui/dormitory_idle.png", "gui/dormitory_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("building_pick", "building_dormitory")])
                    ui.imagebutton("gui/grounds_idle.png", "gui/grounds_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("building_pick", "building_grounds")])
                    ui.imagebutton("gui/gym_idle.png", "gui/gym_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("building_pick", "building_gym")])
                    ui.imagebutton("gui/library_idle.png", "gui/library_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("building_pick", "building_library")])
                    ui.imagebutton("gui/pool_idle.png", "gui/pool_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("building_pick", "building_pool")])
                    ui.imagebutton("gui/security_idle.png", "gui/security_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("building_pick", "building_security")])
                    ui.imagebutton("gui/sports_field_idle.png", "gui/sports_field_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("building_pick", "building_sports_field")])
            vbox:
                spacing 10
                xpos 0.1
                ypos 0.31
                text "{size=30}Money : [cash]{/size}"
                $ ui.imagebutton("gui/return_button_idle.png", "gui/return_button_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=ui.returns(0))

        vbox:
            xfill True
            xpos 0.003
            ypos 0.003
            if  building_pick == "building_bath":
                hbox:
                    spacing 5
                    add "buildings/bath.jpg"
                    text "Open hot water baths for students to relax in. Also known as an onsen. \n\nA great way for students to unwind, but can lead to some naughty hijinx. \n\nBuying this will give a tiny increase to {b}morale{/b} every week, and allow you to visit the baths."

            elif building_pick == "building_classrooms":
                hbox:
                    spacing 5
                    add "buildings/classrooms.jpg"
                    text "Quality and state of classrooms, and the value of the educational materials available to teachers. \n\nIncreasing this will randomly add to your academic stats every month. \n\nThe next upgrade will add a tiny amount to all of your {b}academics{/b} each week."

            elif building_pick == "building_dormitory":
                hbox:
                    spacing 5
                    #TODO: Update text and image.
                    add "buildings/classrooms.jpg"
                    text "Build a dormitory to allow students to live on campus. \n\nBuilding this will allow you to visit the dormitory."
            
            elif building_pick == "building_cafeteria":
                hbox:
                    spacing 5
                    #TODO: Update text and image.
                    add "buildings/classrooms.jpg"
                    text "Build a cafeteria to allow students to buy some snacks. \n\nBuilding this will allow you to visit the dormitory and will give you some extra money each month."
                    
            elif building_pick == "building_grounds":
                hbox:
                    spacing 5
                    add "buildings/grounds.jpg"
                    text "This building represents the quality and upkeep of the school. \n\nUpgrading it makes the whole school more beautiful, and students happier. \n\nThe next upgrade will add a small amount of {b}morale{/b} each week."

            elif building_pick == "building_gym":
                hbox:
                    spacing 5
                    add "buildings/gym.jpg"
                    text "Building where students can practice indoor athletic training. \nFirst level allows gym events and gym class, and higher levels give a bonus to {b}athletics{/b}. \n\nBuying this will open up the gym class, and allow you to visit the gym."

            elif building_pick == "building_library":
                hbox:
                    spacing 5
                    add "buildings/library.jpg"
                    text "A library to store the school's collection of books, as well as allow monitored internet access. \n\nBuying this will give a tiny increase to {b}intelligence{/b} every week."

            elif building_pick == "building_pool":
                hbox:
                    spacing 5
                    add "buildings/swimming_pool.jpg"
                    text "This is a swimming pool. \n\nLower levels are crappy, and only allow for some visits.  Higher levels allow for bonuses to {b}athletics{/b}. Buying this will allow you to visit the pool."

            elif building_pick == "building_security":
                hbox:
                    spacing 5
                    add "buildings/security.jpg"
                    text "This is the level of quality of security for the entire school. \n\nWalls, cameras, guards, and all such things that protect from bad behavior. \n\nThe next upgrade will improve {b}school behavior{/b} a small amount each week."

            elif building_pick == "building_sports_field":
                hbox:
                    spacing 5
                    add "buildings/sports_field.jpg"
                    text "Large open fields where students can play, arrange games, practice sports, and generally exercise to their hearts' content. \n\nBuying this will allow fields visits."

            null height 30
            vbox:
                yfill True
                yalign 1.0
                hbox:
                    if building_cost != 0:
                        $ building_next = building_level + 1
                    else:
                        $ building_next = 'Max'
                    spacing 10
                    xpos 0.02
                    ypos 0.37
                    hbox:
                        python:
                            _can_buy = cash >= building_cost                # Can you afford the building?
                            if _can_buy and building_cost > 0:
                                ui.imagebutton("gui/buy_button_idle.png", "gui/buy_button_hover.png", insensitive_image="gui/buy_button_disable.png", clicked=buy(building_cost))
                            elif building_cost > 0:
                                ui.imagebutton("gui/buy_button_idle.png", "gui/buy_button_hover.png", insensitive_image="gui/buy_button_disable.png", clicked=None)
                            else:
                                ui.imagebutton("gui/buy_button_idle.png", "gui/buy_button_hover.png", insensitive_image="gui/buy_button_disable.png", clicked=None)
                    grid 3 1:
                        xfill True
                        xalign 0.5
                        yalign 0.5
                        grid 2 1:
                            hbox:
                                text "{size=30}  Level :   {/size}" # some space padding is used to avoid other grids becoming larger than this and cause a bit of moving around at certain occasions.
                            hbox:
                                if building_level < len(building_cost_array) -2: #checks if next level is the last one, based on the each building costs.
                                    text "{size=30}Max{/size}"
                                else:
                                    text "{size=30}[building_level] -> [building_next]{/size}"
                        grid 2 1:
                            hbox:
                                if building_cost == 0:
                                    text "(Can't upgrade it further)"
                                else:
                                    text "{size=30}Cost : {/size}"
                            hbox:
                                if building_cost == 0:
                                    text ""
                                else:
                                    text "{size=30}[building_cost]{/size}"
                        grid 2 1:
                            if building_cost == 0:
                                hbox:
                                    text ""
                                hbox:
                                    text ""
                            else:
                                hbox:
                                    text "{size=30}Maintenance : {/size}"
                                hbox:
                                    text "{size=30}[building_cost]{/size}"

##############################################################################
# Buyables Menu
#
# Buy extra's with orbs.

screen buyables_screen:
    imagemap:
        ground "gui/menu_bg.png"

    hbox:
        xfill True
        yfill True
        vbox:
            python:
                if sexy_uniform == 0:
                    ui.imagebutton("gui/sexy_uniform_idle.png", "gui/sexy_uniform_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("buyable", "sexy_uniform"), SetVariable("buyable_cost", [3, 0, 0, 0])])
                elif nude_uniform == 0:
                    ui.imagebutton("gui/nude_uniform_idle.png", "gui/nude_uniform_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("buyable", "nude_uniform"), SetVariable("buyable_cost", [8, 0, 0, 0])])
                if bdsm_detention == 0:
                    ui.imagebutton("gui/bdsm_detention_idle.png", "gui/bdsm_detention_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("buyable", "bdsm_detention"), SetVariable("buyable_cost", [5, 0, 0, 0])])
                if magic_accounting == 0:
                    ui.imagebutton("gui/magic_accounting_idle.png", "gui/magic_accounting_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("buyable", "magic_accounting"), SetVariable("buyable_cost", [0, 1, 1, 1])])
                if hyper_anatomic_body == 0:
                    ui.imagebutton("gui/anatomical_models_idle.png", "gui/anatomical_models_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("buyable", "hyper_anatomic_body"), SetVariable("buyable_cost", [4, 0, 0, 0])])
                if lower_inhibition_level < 4:
                    ui.imagebutton("gui/lower_inhibition"+str(lower_inhibition_level)+"_idle.png", "gui/lower_inhibition"+str(lower_inhibition_level)+"_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("buyable", "lower_inhibition_level"), SetVariable("buyable_cost", [2 + lower_inhibition_level, 0, 0, 0])])
                if no_detention == 0 and good_points > 0:
                    ui.imagebutton("gui/no_detention_idle.png", "gui/no_detention_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("buyable", "no_detention"), SetVariable("buyable_cost", [0, 0, 2, 2])])
                #if sexy_uniform == 0:
                #    ui.imagebutton("gui/cheerleader_club_idle.png", "gui/cheerleader_club_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=[SetVariable("buyable", "cheerleader_club"), SetVariable("buyable_cost", [3, 0, 0, 0])])
                    
                def _buy_buyable(buyable_cost):
                    if globals()['buyable'] == 'lower_inhibition_level':
                        update_stat_min('inhibition', get_stat_min('inhibition') - 25)
                    globals()[eval('buyable')] += 1             # Register the new buyable.
                    globals()['red_orb'] -= buyable_cost[0]     # Pay the price.
                    globals()['blue_orb'] -= buyable_cost[1]
                    globals()['green_orb'] -= buyable_cost[2]
                    globals()['yellow_orb'] -= buyable_cost[3]
                    globals()['buyable'] = 'unlocked'

                    renpy.restart_interaction()                 # Make sure we update the UI so you get feedback when you buy.
                    return

                buy = renpy.curry(_buy_buyable)                 # Curry is used to make sure _buy_buyables only gets activated once a click. (Think of it as a handler.)

        vbox:
            xfill True
            xpos 0.008
            ypos 0.008
            if buyable == "sexy_uniform":
                add "buildings/sexy_uniform1.jpg"
                text "All students are forced to wear a more revealing uniform.\nUnlocks sexy uniform dress code."

            elif buyable == "nude_uniform":
                add "buildings/nude_uniform.jpg"
                text "Students are forced to go to school nude or in lingerie.\nUnlocks nude uniform dress code."
                
            elif buyable == "cheerleader_club":
                add "buildings/cheerleader_club.jpg"
                text "Open up a cheerleader club for the students .\nAllows visiting the Cheerleader Club."

            elif buyable == "hyper_anatomic_body":
                add "buildings/classrooms.jpg"
                text "Anatomical models based on pornstarts, since we all know that porn is {i}real{/i}. \nUnlocks hyper sexualized human models."

            elif buyable == "magic_accounting":
                add "buildings/classrooms.jpg"
                text "You don't know how, but it seems you can {i}always{/i} squeeze out some more cash from your budget. \nGives you 10% more money per month and level."

            elif buyable == "bdsm_detention":
                add "buildings/bdsm_detention.jpg"
                text "If they don't listen, spank them. If they don't behave, make them behave.\nUnlocks BDSM detention."

            elif buyable == "no_detention":
                add "buildings/classrooms.jpg"
                text "You know man, love is like the best thing, we should all spread love. \nUnlocks no detention."

            elif buyable == "lower_inhibition_level":
                add "buildings/sexy_uniform2.jpg"
                $ var = get_stat_min('inhibition') - 25
                text "Hep the students become more relaxed in regards to their body. \nLowers minimum inhibition to [var]."

            elif buyable == "unlocked":
                text "Congratulations, you unlocked a new buyable!"

            else:
                null height 20
                text "Here you can buy special upgrades for your school. Most extras will be available directly except for new classes, they will be available the next day."

    hbox:
        xanchor 0
        yanchor 0
        xpos 0.53
        ypos 0.87
        spacing 5
        vbox:
            yalign 0.5
            text "{size=30}Cost:    {/size}"
            text "{size=25}Have:    {/size}"
        grid 8 2:
            xalign 0.5
            yalign 0.5
            spacing 5
            image "gui/red_orb.png"
            text "{size=30}[buyable_cost[0]]{/size}"

            image "gui/blue_orb.png"
            text "{size=30}[buyable_cost[1]]{/size}"

            image "gui/green_orb.png"
            text "{size=30}[buyable_cost[2]]{/size}"

            image "gui/yellow_orb.png"
            text "{size=30}[buyable_cost[3]]{/size}"

            image "gui/red_orb_mini.png"
            text "{size=25}[red_orb]{/size}"

            image "gui/blue_orb_mini.png"
            text "{size=25}[blue_orb]{/size}"

            image "gui/green_orb_mini.png"
            text "{size=25}[green_orb]{/size}"

            image "gui/yellow_orb_mini.png"
            text "{size=25}[yellow_orb]{/size}"
        vbox:
            spacing 5
            python:
                _can_buy = red_orb >= buyable_cost[0] and blue_orb >= buyable_cost[1] and green_orb >= buyable_cost[2] and yellow_orb >= buyable_cost[3] and globals()['buyable'] != 'unlocked'
                if _can_buy:
                    ui.imagebutton("gui/buy_button_idle.png", "gui/buy_button_hover.png", insensitive_image="gui/buy_button_disable.png", clicked=buy(buyable_cost))
                else:
                    ui.imagebutton("gui/buy_button_idle.png", "gui/buy_button_hover.png", insensitive_image="gui/buy_button_disable.png", clicked=None)
            $ ui.imagebutton("gui/return_button_idle.png", "gui/return_button_hover.png", insensitive_image="gui/menubutton_disable.png", clicked=ui.returns(0))


##############################################################################
# Budget Menu
#
# A screen that shows income and expenditure.

screen show_budget_screen:

    # Calculate total sum of cash flow
    python:
        #Income
        student_pay = population * ( 1 + reputation / 10)
        cafeteria_income = int(population * (building_cafeteria / 10 ) )
        cafeteria = cafeteria_income / population
        magic_accounting_boost = int((student_pay * magic_accounting) / 10)
        multiplier = magic_accounting * 10
        each_student_pay = student_pay / population
        total_income = student_pay + cafeteria_income + magic_accounting_boost
        #Expend~
        teacher_salary = int((student_pay / 10 ) * salary_skill_multiplier )
        total_cost_buildings = 0
        total_expend = total_cost_buildings + teacher_salary
        #Total
        sum_total = total_income - total_expend

    frame:
        xpadding 10
        ypadding 10

    grid 3 14: # X columns & Y rows
        ycenter 0.5
        xcenter 0.5
        spacing 3

        text ""
        label "  {b}Ashford Academy budget:{/b}"
        text ""
        
        text ""
        label "{i}All values in thousands of dollars{/i}"
        text ""
        
        text "Income:"
        text ""
        text ""

        text "State funding:"
        text ""
        text "50 $"

        text "Students"
        text "[population] x [each_student_pay] $"
        text "[student_pay] $"

        text "Cafeteria income"
        text "[population] x [cafeteria]"
        text "[cafeteria_income] $"

        text "Magic accounting boost"
        text "[multiplier]%"
        text "[magic_accounting_boost] $"

        text "{b}Total income:{/b}"
        text ""
        text "{b}[total_income] ${/b}"

        text ""
        text ""
        text ""

        text "Expenditures:"
        text ""
        text ""

        text "[povTitle] [povLastName] salary:"
        text ""
        text "50 $"

        text "Teacher salary:"
        text ""
        text "[teacher_salary] $"

        text ""
        text "{b}Total:{/b}"
        text "{b}[sum_total] ${/b}"

        text ""
        text ""

        textbutton _("Return") action Return()


##############################################################################
# Notification Menu
#
# See and answer your notifications!

screen notification_screen:
    frame:
        xpadding 10
        ypadding 10
        has hbox
        xfill True
        yfill True
        vbox:
            spacing 4
            label _("Messages:")

            textbutton _("Hello") action [SetVariable("building_pick", "building_bath")] xminimum 500
        vbox:
            if building_pick == "building_bath":
                #add "buildings/bath.jpg"
                null width 20
                text "Hello and welcome to Ashford. I hope you enjoy your stay."

            hbox:
                textbutton _("Return") action Return() xminimum 170
