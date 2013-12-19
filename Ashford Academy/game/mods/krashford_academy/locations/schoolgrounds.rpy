image krashford school_grounds1 = "mods/krashford_academy/locations/school_grounds/school_grounds1.jpg"
image krashford school_grounds2 = "mods/krashford_academy/locations/school_grounds/school_grounds2.jpg"
image krashford school_grounds3-2 = "mods/krashford_academy/locations/school_grounds/school_grounds3-1.jpg"
image krashford school_grounds3-2 = "mods/krashford_academy/locations/school_grounds/school_grounds3-2.jpg"
image krashford school_grounds4_1 = "mods/krashford_academy/locations/school_grounds/school_grounds4-1.jpg"
image krashford school_grounds4_2 = "mods/krashford_academy/locations/school_grounds/school_grounds4-2.jpg"

init:
    if mod_trigger_krashford == True:
        $ event("krashford_school_grounds1", "act == 'class'", event.choose_one('class'), priority=200)
        $ event("krashford_school_grounds2", "act == 'class'", event.choose_one('class'), priority=200)
        $ event("krashford_school_grounds3", "act == 'class'", event.choose_one('class'), priority=200)
        $ event("krashford_school_grounds4", "act == 'class'", event.choose_one('class'), priority=200)

label krashford_school_grounds1:
    
    scene krashford school_grounds1 with fade
    if renpy.random.randint(1,2) == 1:
        "SHOOT THEM! SHOOT THEM ALL!"
    else:
        "*click* *BANG* *BANG* *BANG*"
    return


label krashford_school_grounds2:
    
    scene krashford school_grounds2 with fade
    if renpy.random.randint(1,2) == 1:
        pov "Oh hey, keeping the grounds safe, eh?"
        girl "Shhh...."
        "Never mind I'll just leave then..."
    else:
        "Target in sight..."
        with flash
        "*BANG*"
        "Target down."
    #TODO: gun training +
    return


label krashford_school_grounds3:
    
    scene krashford school_grounds3-1 with fade
    "..."
    scene krashford school_grounds3-2
    "*Rata-ta-ta-ta*"
    return


label krashford_school_grounds4:
    
    $ randImg = renpy.random.choice(["1", "2"])
    $ renpy.show("krashford_school_grounds4_"+randImg)
    with fade
    "Another one bites the dust..."
    $ population -= 1
    return


