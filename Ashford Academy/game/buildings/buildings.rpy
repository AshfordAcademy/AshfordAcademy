# Buildings and starting level. 0 equals to not built.
define building_bath = 0
define building_classrooms = 1
define building_grounds = 1
define building_gym = 1
define building_library = 0
define building_pool = 0
define building_security = 0
define building_sports_field = 0

define building_dormitory = 0
define building_cafeteria = 0

#define building_club_house = 0
define building_cheerleader_club = 0


define balancer = 1    # This variable is used (ATM) to balance out the buildings

# Buildings and prices for each level, we put prices in an array and let the level indicate the index for the price. All buildings are upgradeable until the price reaches "0".

define building_bath_price = [325, 400, 475, 550, 700, 0]
define building_classrooms_price = [275, 350, 425, 550, 675, 0]
define building_grounds_price = [510, 620, 730, 840, 950, 0]
define building_gym_price = [250, 400, 550, 700, 875, 0]
define building_library_price = [250, 300, 375, 450, 575, 0]
define building_pool_price = [350, 450, 550, 675, 800, 0]
define building_security_price = [275, 325, 400, 525, 700, 0]
define building_sports_field_price = [225, 350, 475, 625, 750, 0]


define building_cafeteria_price = [725, 880, 1000, 1200, 0]
define building_cheerleader_club_price = [350, 500, 750, 0]
define building_dormitory_price = [650, 775, 900, 1125, 1300, 0]


define building_pick = 'building_bath'
define building_level = eval(building_pick)
define building_cost_array = eval(building_pick + '_price')
define building_cost = building_cost_array[building_level]


init -100 python:
    
    # NOTE: New buildings might need rebalance.
    # TODO: Add "building_dormitory".
    def building_bonus():
        globals()['morale'] += (building_bath + building_grounds + building_pool + building_cheerleader_club) / 3 - (building_security / 2 ) - balancer
        globals()['behavior'] += building_security - balancer
        globals()['academics'] += (building_library + building_classrooms) / 2 - balancer
        globals()['artistery'] += (building_library + building_classrooms ) / 2 - balancer
        globals()['athletics'] += (building_pool + building_gym + building_sports_field - building_cafeteria) / 3 - balancer
        globals()['deviance'] += (building_bath / 2 ) - balancer
        globals()['inhibition'] -= (building_bath / 2 ) + (building_pool / 4 ) - balancer
        globals()['reputation'] += good_points - evil_points
