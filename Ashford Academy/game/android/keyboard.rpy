########################################################
#   Android keyboard input stuff, adapted from: http://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=14985
python:
    text_list1=["Q","W","E","R","T","Y","U","I","O","P","0",
                      "A","S","D","F","G","H","J","K","L","0",
                      "Z","X","C","V","B","N","M","0"]
    text_list2=["q","w","e","r","t","y","u","i","o","p","0",
                      "a","s","d","f","g","h","j","k","l","0",
                      "z","x","c","v","b","n","m","0"]
    input_text = ''
    input_header = 'NAME:'
    text_limit = 16
    text_list=text_list1
    text_group=1
    
########################################################
#   More android keyboard input stuff, adapted from: http://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=14985

label inputter:
    if text_group==1:
        $text_list=text_list1
    elif text_group==2:
        $text_list=text_list2
         
    $ ui.frame(xpos=0.5, ypos=0.1, xanchor=0.5, yanchor=0, xminimum=450)
    $ ui.vbox()
    $ ui.text(input_header+" "+input_text)
    $ ui.null(height=30)

    $ ui.hbox()
    $ ui.textbutton("Done", clicked=ui.returns("Done"))
    $ui.textbutton("Backspace", clicked=ui.returns("Backspace"))
    $ui.textbutton("Delete all", clicked=ui.returns("Deleteall"))
    if text_group==1:
        $ ui.textbutton("Caps (ON)", clicked=ui.returns("locase"))
    elif text_group==2:
        $ ui.textbutton("Caps (off)", clicked=ui.returns("upcase"))
    $ ui.close()

    $ ui.null(height=10)

    $ ui.hbox(xalign= 0.5)
    python:
        for text_code in text_list:
            if text_code=="0":
                ui.close()
                ui.hbox(xalign= 0.5)
            elif  len(input_text)<=text_limit-1:
                ui.textbutton(text_code, clicked=ui.returns(text_code))
    $ ui.close()
    $ ui.close()
    $ button_selection=ui.interact()
               
    if button_selection=="Backspace":
        $ input_text=input_text[:-1]
        jump inputter
    elif button_selection=="Deleteall":
        $ input_text=''
        jump inputter
    elif button_selection=="upcase":
        $text_group=1
        jump inputter
    elif button_selection=="locase":
        $text_group=2
        jump inputter
    elif button_selection=="Done":
        return
    $ select_text=button_selection

    python:
        for text_code in text_list:
            if select_text==text_code:
                input_text += text_code
    jump inputter