init -100 python:
    import collections # this library is used for enumerating list items to find quantity of each item in the list

############################
    persistent.mod_disable_monthly_planning = False
    persistent.mod_disable_weekly_planning = False
    
    persistent.mod_disable_original_stats = False
    persistent.mod_disable_original_events = False
    persistent.mod_disable_original_story_events = False
    persistent.mod_disable_original_locations = False
    
    persistent.mod_custom_new_game = ""
    persistent.mod_custom_new_game_plus = ""
    
    #persistent.mod_custom_title_screen = False
    
    persistent.mod_custom_title_screen_ground = "gui/mm_ground.png"
    persistent.mod_custom_title_screen_ild = "gui/mm_idle.png"
    persistent.mod_custom_title_screen_hover = "gui/mm_hover.png"


    trigger_object = "" # these are for internal code use and should be left blank for init purposes.
    trigger_name = ""   # what they do is actually split the mod trigger into an object part, namely persistent, and the actual trigger name.
    mod_trigger1 = True
    # here we define the starting mod list.
    mod_list = [('test','events','0.1','0.4050','stable','mod_trigger1')] # this is the initial mods list, most likely empty.
    mod_list.insert(0,('test2','gui','1.0','0.4','unstable','persistent.mod_trigger2')) # this is how mod info is added to the list.
                                                                           # 0 specifies the position in the list -at the start- and the rest is following the format (Mod Name,Mod Type,Mod Version,Game Version,Mod State,Mod Trigger)

# mods list screen
screen mod_list_screen:
    python:
        mod_list_enumeration = collections.Counter(mod_list) # when the modification screen is opened, we check for items in the mod list.
        mod_names_keys = mod_list_enumeration.keys()  # assign items in a new temporary list. counter.keys index can't be called for some reason.
        mod_names_values = mod_list_enumeration.values() # assign amount of each items in a new temporary list. same as above for counter.values index.

    vbox:
        xpos 20
        ypos 20
        xmaximum 1240
        ymaximum 660
        viewport:
            vbox:
                spacing 20
                frame:
                    hbox:
                        grid 6 1:
                            xfill True
                            hbox:
                                xalign 0.5
                                text "Mod Name"
                            hbox:
                                xalign 0.5
                                text "Mod Type"
                            hbox:
                                xalign 0.5
                                text "Mod Version"
                            hbox:
                                xalign 0.5
                                text "Game Version"
                            hbox:
                                xalign 0.5
                                text "Mod State"
                            hbox:
                                xalign 0.5
                                text "Mod Status"
                vbox:
                    xfill True
                    spacing 20
                    vbox:
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            frame:
                                vbox:
                                    spacing 20
                                    for i in range(0, len(mod_list_enumeration.keys())): # show each item in inventory until all items are shown ( duplicates count as one item )
                                        grid 6 1:
                                            xfill True
                                            spacing 20
                                            python:
                                                if "." in str(mod_list[i][5]):#checks if trigger is persistent or not.
                                                    trigger_object,trigger_name = mod_list[i][5].split(".")
                                            hbox:
                                                xalign 0.5
                                                yalign 0.5
                                                text(str(mod_list[i][0])) # show item name after converting the the index to a string for concatenation with actual text.
                                            hbox:
                                                xalign 0.5
                                                yalign 0.5
                                                text(str(mod_list[i][1])) # show item name after converting the the index to a string for concatenation with actual text.
                                            hbox:
                                                xalign 0.5
                                                yalign 0.5
                                                text(str(mod_list[i][2])) # show item name after converting the the index to a string for concatenation with actual text.
                                            hbox:
                                                xalign 0.5
                                                yalign 0.5
                                                text(str(mod_list[i][3])) # show item name after converting the the index to a string for concatenation with actual text.
                                            hbox:
                                                xalign 0.5
                                                yalign 0.5
                                                text(str(mod_list[i][4])) # show item name after converting the the index to a string for concatenation with actual text.
                                            hbox:
                                                xalign 0.5
                                                yalign 0.5
                                                if "." in str(mod_list[i][5]):#checks if trigger is persistent or not.
                                                    if eval(mod_list[i][5]) == True: # show item name after converting the the index to a string for concatenation with actual text.
                                                        textbutton _("Enabled") action SetField(persistent,trigger_name,False)
                                                    elif eval(mod_list[i][5]) == False:
                                                        textbutton _("Disabled") action SetField(persistent,trigger_name,True)
                                                    else
                                                        hbox:
                                                            textbutton _("Disable") action SetField(persistent,trigger_name,False) # since persistent values are not (and shouldn't be) declared in init, both buttons are shown initially
                                                            textbutton _("Enable") action SetField(persistent,trigger_name,True)
                                                else
                                                     if eval(mod_list[i][5]) == True: # show item name after converting the the index to a string for concatenation with actual text.
                                                         textbutton _("Enabled") action SetVariable(str(mod_list[i][5]),False)
                                                     elif eval(mod_list[i][5]) == False:
                                                         textbutton _("Disabled") action SetVariable(str(mod_list[i][5]),True)
                                                     else
                                                         text"No Trigger"
    hbox:
            xalign 0.985
            yalign 0.99
            textbutton _("Return") action Return()