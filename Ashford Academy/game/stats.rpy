init -100 python:



    __dse_stats = [ ]

    class __Stat(object):

        def __init__(self, name, var, min, default, max):
            self.name = name            # The public name showed on the UI
            self.var = var              # Variable used to modify
            self.min = min              # Min value
            self.default = default      # Default value
            self.max = max              # Max value

    def __init_stats():
        for s in __dse_stats:
            setattr(store, s.var, s.default)

    config.start_callbacks.append(__init_stats)

    # Are called to register all stats.
    def register_stat(name, var, min, default, max):
        __dse_stats.append(__Stat(name, var, min, default, max))

    # Sets the max value of stat (v) to value (m).
    def update_stat_max(v, m):
        for s in __dse_stats:
            if v == s.var:
                s.min = m

    # Returns the max value of stat (v).
    def get_stat_max(v):
        for s in __dse_stats:
            v = s.var
            return s.max

    # Sets the min value of stat (v) to value (m).
    def update_stat_min(v, m):
        for s in __dse_stats:
            if v == s.var:
                s.min = m

    # Returns the min value of stat (v).
    def get_stat_min(v):
        for s in __dse_stats:
            if v == s.var:
                return s.min


    def sort_stats(type='normal'):
        v = 0
        # Returns the name of the highest stat.
        if type == 'max':
            for s in __dse_stats:
                if v > eval(s.var):
                    v = eval(s.var)
            return s.var
        # Returns the name of the lowest stat.
        if type == 'min':
            for s in __dse_stats:
                if v < eval(s.var):
                    v = eval(s.var)
            return s.var

        if (morale and behavior and academics and artistery and athletics and deviance and (100 - inhibition) ) == 100:
            return "maxed"
        elif (morale and behavior and academics and artistery and athletics and (100 - inhibition) == deviance):
            return "equal"


    # Make sure that no stat is less then min or more then max.
    def normalize_stats():
        for s in __dse_stats:

            v = getattr(store, s.var)

            if v > s.max:
                v = s.max
            if v < s.min:
                v = s.min

            setattr(store, s.var, v)

    # Base stats
    def display_stats(name=True, bar=False, value=True, max=False):

        normalize_stats()

        ui.window(style=style.stats_frame)
        ui.vbox(style=style.stats_vbox)

        layout.label("Statistics:", "stats")

        for s in __dse_stats:
            v = getattr(store, s.var)
            v_change = s.name+'_change'

            ui.side(['l', 'r', 'c'], style=style.stat_side)

            if name:
                layout.label(s.name, "stat")
            else:
                ui.null()

            if value and max:
                layout.label("%d/%d" % (v, s.max), "stat_value")

            elif(value and eval(v_change) < v):
                layout.label("{color=[color_increase]} %d" % (v,), "stat_value")
            elif(value and eval(v_change) > v):
                layout.label("{color=[color_decrease]} %d" % (v,), "stat_value")
            elif(value and eval(v_change) == v):
                layout.label("%d" % (v,), "stat_value")

            elif max:
                layout.label("%d" % (max,), "stat_value")
            else:
                ui.null()

            ui.close()


        ui.close()

    def display_extra_stats():
        ui.window(style=style.stats_frame, yoffset=260)
        ui.vbox(style=style.stats_vbox)
        ui.side(['l', 'r', 'c'], style=style.stat_side)

        layout.label("[povName]", "r")
        ui.close()

        ui.side(['l', 'r', 'c'], style=style.stat_side)
        layout.label("[month_now] [day]: [today]", "r")
        ui.close()

        ui.side(['l', 'r', 'c'], style=style.stat_side)
        layout.label("Money", "stat")
        if(cash_change < cash):
            layout.label("{color=[color_increase]} %d" % (cash), "stat_value")
        elif(cash_change > cash):
            layout.label("{color=[color_decrease]} %d" % (cash), "stat_value")
        else:
            layout.label("%d" % (cash), "stat_value")
        ui.close()

        ui.side(['l', 'r', 'c'], style=style.stat_side)
        layout.label("Population", "stat")
        if(population_change < population):
            layout.label("{color=[color_increase]} %d" % (population), "stat_value")
        elif(population_change > population):
            layout.label("{color=[color_decrease]} %d" % (population), "stat_value")
        else:
            layout.label("%d" % (population), "stat_value")
        ui.close()

        ui.side(['l', 'r', 'c'], style=style.stat_side)
        layout.label("Reputation", "stat")
        if(reputation_change < reputation):
            layout.label("{color=[color_increase]} %d" % (reputation), "stat_value")
        elif(reputation_change > reputation):
            layout.label("{color=[color_decrease]} %d" % (reputation), "stat_value")
        else:
            layout.label("%d" % (reputation), "stat_value")
        ui.close()

        ui.null(height=10)

        ui.hbox()

        ui.null(width=15)
        ui.image("gui/red_orb_mini.png")
        ui.null(width=5)
        if(red_orb_change < red_orb ):
            ui.text("{color=[color_increase]}[red_orb]")
        elif(red_orb_change > red_orb ):
            ui.text("{color=[color_decrease]}[red_orb]")
        else:
            ui.text("[red_orb]")

        ui.null(width=15)
        ui.image("gui/blue_orb_mini.png")
        ui.null(width=5)
        if(blue_orb_change < blue_orb ):
            ui.text("{color=[color_increase]}[blue_orb]")
        elif(blue_orb_change > blue_orb ):
            ui.text("{color=[color_decrease]}[blue_orb]")
        else:
            ui.text("[blue_orb]")

        ui.null(width=15)
        ui.image("gui/green_orb_mini.png")
        ui.null(width=5)
        if(green_orb_change < green_orb ):
            ui.text("{color=[color_increase]}[green_orb]")
        elif(green_orb_change > green_orb ):
            ui.text("{color=[color_decrease]}[green_orb]")
        else:
            ui.text("[green_orb]")

        ui.null(width=15)
        ui.image("gui/yellow_orb_mini.png")
        ui.null(width=5)
        if(yellow_orb_change < yellow_orb ):
            ui.text("{color=[color_increase]}[yellow_orb]")
        elif(yellow_orb_change > yellow_orb ):
            ui.text("{color=[color_decrease]}[yellow_orb]")
        else:
            ui.text("[yellow_orb]")
        ui.close()

        ui.close()


label update:
    $ update_stat_max('inhibition', 100)
    "Debug!"
    return