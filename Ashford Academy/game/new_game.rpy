# TODO: Relocate and sort variables and functions.

# Initialize the default values of some of the variables used in the game.
define cash = 0
define cash_change = 0
define population = 0
define population_change = 0
define reputation = 0
define reputation_change = 0

# "Hidden" variables for planning
define beh_focus = 0
define academics_focus = 0
define art_focus = 0
define ath_focus = 0
define sex_focus = 0

define evil_points = 0
define good_points = 0

define buyable = ''
define buyable_cost = [ ]

# Is "new game +" available?
$ persistent.new_game_plus = False


# Define game_mode = 'normal' -- TODO: Remove and replace.
init python:

    def new_game(game_mode):

        # Starting stats:
        if(game_mode=='normal'):
            globals()['cash'] = 500
            globals()['population'] = 100
            globals()['reputation'] = 10

        globals()['Morale_change'] = globals()['morale']
        globals()['Behavior_change'] = globals()['behavior']
        globals()['Academics_change'] = globals()['academics']
        globals()['Artistery_change'] = globals()['artistery']
        globals()['Athletics_change'] = globals()['athletics']
        globals()['Deviance_change'] = globals()['deviance']
        globals()['Inhibition_change'] = globals()['inhibition']

        globals()['cash_change'] = globals()['cash']
        globals()['population_change'] = globals()['population']
        globals()['reputation_change'] = globals()['reputation']

        # Send the first tutorial message
