# Used in Policy screen
define policy_screen = ''

# Buyables
define buyable_cost = [0, 0, 0, 0]
define magic_accounting = 0

# Standard variables for school policy
define uniform = 'normal_uniform'               # nude_uniform, sexy_uniform, no_uniform, normal_uniform, conservative_uniform
define entrance_req = 3                         # 1 easy -- 5 hard
define pda_rules = 'pda_suspension'             # pda_bdsm (5), pda_expulsion (4), pda_suspension (3), pda_normal (2), pda_none (1)
define pda_rule_level = 3

# Unlockables
define nude_uniform = 0
define sexy_uniform = 0
define bdsm_detention = 0
define no_detention = 0
define hyper_anatomic_body = 0
define tentacles = 0

# Variables for Teachers
define salary = 'salary_normal'                 # salary_high, salary_normal, salary_low
define salary_skill_multiplier = 1.2            # 0.7, 1.2, 1.7
define behavior_rules = 'behavior_verbal'       # behavior_no_limit (2), behavior_physical (1.5), behavior_verbal (1), behavior_zero(0.7)
define behavior_rules_multiplier = 1
define anatomic_body = 0                        # anatomic_body_non_sex (0), anatomic_body_normal (1), anatomic_body_sex (2)
define learning_materials = 0.7                 # old (0.7), normal (1.0), new (1.3)

init -100 python:
    
    def policy_bonus():
        globals()['academics'] += (learning_materials * salary_skill_multiplier) * (entrance_req / 3 )
        globals()['artistery'] += (learning_materials * salary_skill_multiplier) * (entrance_req / 3 )
        globals()['athletics'] += (learning_materials * salary_skill_multiplier) * (entrance_req / 3 )
        globals()['behavior'] += (behavior_rules_multiplier * (pda_rule_level / 2) ) - 2
        globals()['morale'] -= (behavior_rules_multiplier * (pda_rule_level / 2) ) - 2
        globals()['deviance'] -= (pda_rule_level / 2 ) - anatomic_body
        globals()['inhibition'] += (pda_rule_level / 2 ) - anatomic_body


        # Behavior data #
        if(behavior_rules == 'behavior_no_limit'):
            globals()['reputation'] -= 1
        
        elif(behavior_rules == 'behavior_zero'):
            globals()['reputation'] += 1

        # Uniform data #
        if(uniform == 'nude_uniform'):
            globals()['morale'] -= 2
            globals()['deviance'] += 3
            globals()['inhibition'] -= 3
            globals()['reputation'] -= 1
        
        elif(uniform == 'sexy_uniform'):
            globals()['morale'] -= 1
            globals()['behavior'] += 1
            globals()['inhibition'] -= 1
            globals()['deviance'] += 1
            
        elif(uniform == 'normal_uniform'):
            globals()['morale'] -= 1
            globals()['behavior'] += 1
            
        elif(uniform == 'no_uniform'):
            globals()['morale'] += 1
            globals()['behavior'] -= 1
            globals()['inhibition'] -= 1
        
        elif(uniform == 'conservative_uniform'):
            globals()['morale'] -= 2
            globals()['behavior'] += 2
            globals()['deviance'] -= 2
            globals()['inhibition'] += 2 