init python:
    import collections # this library is used for enumerating list items to find quantity of each item in the list
    # here we define starting inventories for the principal and/or story characters 
    principal_inventory = ["spycam","spycam2","spycam2"]
    hina_inventory = ["sexy_swimsuit"]  # we can also set items already contained in inventory at the beginning
    baths_equipment = ["peepholes"]  # same goes for buildings

############################ Usage of inventory system in events ############################ 

# $ principal_inventory.append("spycam")  <-- this one pushes the item "spycam" at the end of the inventory list, essentially "giving" the character that item
# $ principal_inventory.remove("spycam")  <-- this one deletes the first item named "spycam" from the list. If the player has multiple spycams, it will only delete the first occurence in list, like decreasing the amount by 1

# if hina_inventory.has_item(sexy_swimsuit):  <-- this checks for appropriate items in inventory before following an event chain. Same applies for building equipment lists
    # do stuff

############################ 

# inventory screen
screen inventory_screen:
    python:
        principal_inventory_counter = collections.Counter(principal_inventory) # when the inventory screen is opened, we check for items in the inventory and the amount of each of them
        principal_inventory_items = principal_inventory_counter.keys()  # assign items in a new temporary list. counter.keys index can't be called for some reason.
        principal_inventory_amount = principal_inventory_counter.values() # assign amount of each items in a new temporary list. same as above for counter.values index.

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
                        grid 3 1:
                            xfill True
                            hbox:
                                text "{b}Inventory{/b}"
                            hbox:
                                xalign 0.5
                                text "Item Name"
                            hbox:
                                xalign 0.5
                                text "Item Quantity"
                vbox:
                    xfill True
                    spacing 20
                    vbox:
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            vbox:
                                spacing 20
                                for i in range(0, len(principal_inventory_counter.keys())): # show each item in inventory until all items are shown ( duplicates count as one item )
                                    frame:
                                        grid 3 1:
                                            xfill True
                                            spacing 20
                                            vbox:
                                                xalign 0.5
                                                if renpy.exists("gui/"+str(principal_inventory_items[i])+".png"):
                                                    image("gui/"+str(principal_inventory_items[i])+".png") # show item image. Image has to be in the Gui folder, have the same name as the item and a .png extension.
                                                else
                                                    text("No Image")
                                            hbox:
                                                xalign 0.5
                                                yalign 0.5
                                                text (principal_inventory_items[i]) # show item name after converting the the index to a string for concatenation with actual text.
                                            hbox:
                                                xalign 0.5
                                                yalign 0.5
                                                text (str(principal_inventory_amount[i])) # show item quantity after converting the number to a string.

    hbox:
            xalign 0.985
            yalign 0.99
            textbutton _("Return") action Return()