######################################################################
# Here we store and manage all information regarding notifications
#
# How does it work?
# $ add_message("Topic", "Sender", "Text content", "attached image", "reply screen")
# 
# Some examples:
#
# $ add_message("Miss u <3", "Jen", "", "jen_sexy.jpg")
# This would only include "Subject", "Sender" and a "Image".
#
#
# $ add_message("When are you coming home?", "Jen", "Hey bb,\nAre you working late to night? \nMiss u <3", "", "jen_reply")
# This would include "Subject", "Sender", "Text" and a reply options, see beneath.
#
#
#label jen_reply(current_message):
#    menu:
#        "Don't worry Jen, I'll see you in a hour. ":
#            $ add_message("Yay!", "Jen", "I'll wait for you in bed! <3")
#            $ current_message.can_reply = False
#
#        "Sorry Jen I'll be late, you go to bed w/o me.":
#            $ add_message("Aww...", "Jen", "Ok... I hope you're not sleeping around again... </3")
#            $ current_message.can_reply = False
#
#        "Don't reply yet.":
#            pass
#    return 
#

init:
    $ disable_NPA = False

    $ event("NPA_mail1", "total_days > 0", event.once())
    $ event("NPA_mail2", "disable_NPA == False", event.once(), event.depends("NPA_mail1"))
    $ event("NPA_mail3", "disable_NPA == False", event.once(), event.depends("NPA_mail2"))
    $ event("NPA_mail4", "disable_NPA == False", event.once(), event.depends("NPA_mail3"))
    $ event("NPA_mail5", "disable_NPA == False", event.once(), event.depends("NPA_mail4"))
    $ event("NPA_mail6", "disable_NPA == False", event.once(), event.depends("NPA_mail5"))
    
    #$ event("jack_drake_mail1", "disable_NPA == False", event.once())


# The game starts here.

label NPA_mail1:
    $ add_message("Back to school!", "N.A.P.", "{b}Good day [povTitle] [povLastName]!{/b} \nLet us first congratulate you regarding your new position as principal.\nCongratulations. \n\nSince you are still considered a {i}junior{/i} member we will occasionally send some information. If you do not want this, please respond and we will remove you from our mailing list. \n\n{i}Good luck turning Ashford Academy back into its former glory.{/i}\n-National Association of Principals", "", "NPA_mail1_reply")
    return

label NPA_mail1_reply(current_message):
    menu:
        "Please don't send any more information.":
            $ add_message("Confirmation mail.", "N.A.P.", "We received your mail and have removed you from our mailing list.\n\n-National Association of Principals")
            $ current_message.can_reply = False
            $ disable_NPA = True
        "Don't reply yet.":
            pass
    return


label NPA_mail2:
    $ add_message("Morale", "N.A.P.", "{b}Morale.{/b} \nThis is the general happiness of the school.\n{i}Are they in high spirits or more doom and gloom.{/i} \n\nAs principals we have great power to influence the daily activity of our students. We can play nice and have lax policies and open up a pool or bath.\nPlease remember, focusing to much on morale will most likely lower their behavior. \n\n-National Association of Principals", "", "NPA_mail1_reply")
    return


label NPA_mail3:
    $ add_message("Behavior", "N.A.P.", "{b}Behavior.{/b} \nThis is how obedient your students are.\n{i}Do they act as told or do they terrorize the others?{/i} \n\nAs principals we have great power to influence the daily activity of our students. We can force them do do our bidding and follow our every whim, raise the security and expel those who disobey. \nThat {i}would obviously be immoral{/i} and lower the morale of our students. \n\n-National Association of Principals", "", "NPA_mail1_reply")
    return


label NPA_mail4:
    $ add_message("Academics, Artistery & Athletics", "N.A.P.", "{b}Academics, Artistery & Athletics.{/b} \nThese are how good your school is in reference to the national average.\n{i}Does your school have the students of the future?{/i}\n\nTo motivate and better our students we can upgrade and build new buildings as well as give our teachers better salary and equipment by changing the school policy. \n\n-National Association of Principals", "", "NPA_mail1_reply")
    return


label NPA_mail5:
    $ add_message("Deviance & Inhibition", "N.A.P.", "{b}Deviance & Inhibition.{/b} \nAs responsible for the students future we have to make sure that our students {i}don't{/i} act deviantly and involve themselves in immoral and sexual behavior. \n\nA good way to keep the students in place is to make sure they act modest and stay away from places like public baths and make sure they dress properly.  \n\n-National Association of Principals", "", "NPA_mail1_reply")
    return


label NPA_mail6:
    $ add_message("Warning about orbs", "N.A.P.", "{b}Orbs.{/b} \nThere seems to be a rumour going that there could exist some kind of {i}magical orbs{/i} that would make it possible to influence teachers and students alike.\n\nThis is {i}obviously{/i} a ruse and should be avoided at all cost. \nAny sane person would stay away from this and the person(s) claiming involved with this.\n\n-National Association of Principals", "", "NPA_mail1_reply")
    return


label script:

    $ add_message("Thanks", "Hina Amagi", "Hi [povLastName], sorry to msg u... I just wanna thank you for helping me out the other day! Thx!", "", "hina_amagi_reply")
    $ add_message("Miss u <3", "Jen", "Miss u <3", "test.jpg")
    
    return


label hina_amagi_reply(current_message):
    menu:
        "No problem sunshine, I hope everything worked out well for you :)":
            $ add_message("You're so nice!", "Hina Amagi", "Thanks again :)")
            $ current_message.can_reply = False
        "Miss Amagi please don't send messages to my private phone.":
            $ add_message("Sorry...", "Hina Amagi", "Ok, I won't do it again... Sorry :(")
            $ current_message.can_reply = False
        "Don't reply yet.":
            pass
    return





