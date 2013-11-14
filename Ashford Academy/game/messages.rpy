init python:
    import renpy.store as store

    class Mail(store.object):
        def __init__(self, subject, sender, body, attachment, reply_label, view=True, status=True):
            self.subject = subject
            self.sender = sender
            self.body = body
            self.attachment = attachment
            self.reply_label = reply_label
            self.view = view
            self.status = status
            mail.insert(0, self)
            if reply_label:
                self.can_reply = True
            else:
                self.can_reply = False
            global new_messages
            new_messages = new_messages + 1

        def reply(self):
            global reply_screen
            reply_screen = True
            renpy.call_in_new_context(self.reply_label, current_message=self)
            reply_screen = False

        def delete(self):
            self.view = False

        def restore(self):
            self.view = True

        def mark_read(self):
            self.status = False

    def restore_all():
        deleted_messages = [x for x in mail if x.view == False]
        for x in deleted_messages:
            x.restore()
        renpy.restart_interaction()

    def mark_all_read():
        unread_messages = [x for x in mail if x.status]
        for x in unread_messages:
            x.mark_read()

    def add_message(subject, sender, body, attachment="", reply_label=False):
        message = Mail(subject, sender, body, attachment, reply_label)


screen mailbox:
    
    add "gui/phone_bg.jpg" xalign 0.5 yalign 1.0
    tag menu
    modal True
    default current_message = None
    $ visible_messages = [i for i in mail if i.view]
    frame:
        style_group "mailbox"
        vbox:
            label "Inbox"
            if new_messages > 0:
                text ("Messages: " + str(len(visible_messages)) + " ([new_messages] unread)")
            else:
                text ("Messages: " + str(len(visible_messages)))
            side "c r":
                area (5,0,490,110) #Message list
                viewport id "message_list":
                    draggable True mousewheel True
                    vbox:
                        for i in mail:
                            if i.view:
                                if i.status:
                                    textbutton ("*NEW* " + i.sender + " - " + i.subject) action [SetScreenVariable("current_message",i), i.mark_read, SetVariable("new_messages",new_messages-1)] xfill True
                                else:
                                    textbutton (i.sender + " - " + i.subject) action SetScreenVariable("current_message",i) xfill True
                vbar value YScrollValue("message_list")
            hbox:
                null height 10
            side "c r":
                area (5,0,490,455)
                viewport id "view_message":
                    draggable True mousewheel True
                    vbox:
                        if current_message:
                            text ("{b}From:{/b} " + current_message.sender)
                            text ("{b}Subject:{/b} " + current_message.subject +"\n")
                            if current_message.attachment != "":
                                add current_message.attachment
                            text current_message.body
                vbar value YScrollValue("view_message")
            use mailbox_commands
    add "gui/phone.png" xalign 0.5 yalign 1.0
    
screen mailbox_commands:
    hbox:
        if current_message and current_message.can_reply:
            textbutton "Reply" action current_message.reply
        else:
            textbutton "Reply" action None
        if current_message:
            textbutton "Delete" action [current_message.delete, SetScreenVariable("current_message", None)]
        else:
            textbutton "Delete" action None
        if new_messages > 0:
            textbutton "Mark All Read" action [mark_all_read, SetVariable("new_messages",0)]
        else:
            textbutton "Mark All Read" action None
        textbutton "Restore All" action restore_all
        textbutton "Exit" action Return()

init -2 python:
    style.mailbox = Style(style.default)
    style.mailbox_vbox.xalign = 0.5
    style.mailbox_vbox.xfill = False
    style.mailbox_hbox.xalign = 0.5
    style.mailbox_label_text.size = 30
    style.mailbox_label_text.xalign = 0.5
    style.mailbox_label.xfill = False
    style.mailbox_frame.xalign = 0.5
    style.mailbox_frame.yalign = 0.5