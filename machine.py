from fsm import TocMachine

def create_machine():
    machine = TocMachine(
    states=[
        'init',
        'gaming',
        'resting',
        'goodend_study', #end
        'arguing',
        'internet_cafe',
        'jay_bread',
        'goodend_turn_down_jay', #end
        'jay_invite',
        'market',
        'goodend_staying_sober', #end
        'jay_house',
        'drink_once',
        'drink_twice',
        'neutralend_drunk', #end
        'jay_tough',
        'jay_fit',
        'jay_youDoNotUnderstand',
        'neutralend_consent',  #end
        'jay_adult',
        'secretend_NCKU', #end
        'jay_porn',
        'jay_blush',
        'jay_letMeSee',
        'jay_ifYouAreNormal',
        'jay_checked_your_body',
        'goodend_too_small', #end
        'jay_get_scared',
        'secretend_reverse', #end
        'jay_listen_letMeSee',
        'jay_punch',
        'jay_took_of_cloth',
        'jay_bed',
        'badend_rape', #end
    ],
    transitions=[
        #source init
        {'trigger': 'advance', 'source': 'init', 'dest': 'gaming', 'conditions': 'is_going_to_gaming'},

        #source gaming
        {'trigger': 'advance', 'source': 'gaming', 'dest': 'arguing', 'conditions': 'is_going_to_arguing'},
        {'trigger': 'advance', 'source': 'gaming', 'dest': 'resting', 'conditions': 'is_going_to_resting'},
        {'trigger': 'advance', 'source': 'gaming', 'dest': 'goodend_study', 'conditions': 'is_going_to_goodend_study'},

        #source resting
        {'trigger': 'advance', 'source': 'resting', 'dest': 'resting', 'conditions': 'is_going_to_resting'},
        {'trigger': 'advance', 'source': 'resting', 'dest': 'goodend_study', 'conditions': 'is_going_to_goodend_study'},
        {'trigger': 'advance', 'source': 'resting', 'dest': 'gaming', 'conditions': 'is_going_to_gaming'},

        #source arguing
        {'trigger': 'advance', 'source': 'arguing', 'dest': 'goodend_study', 'conditions': 'is_going_to_goodend_study'},
        {'trigger': 'advance', 'source': 'arguing', 'dest': 'internet_cafe', 'conditions': 'is_going_to_internet_cafe'},

        #source internet_cafe
        {'trigger': 'advance', 'source': 'internet_cafe', 'dest': 'internet_cafe', 'conditions': 'is_going_to_internet_cafe'},
        {'trigger': 'advance', 'source': 'internet_cafe', 'dest': 'jay_bread', 'conditions': 'is_going_to_jay_bread'},

        #source jay_bread
        {'trigger': 'advance', 'source': 'jay_bread', 'dest': 'jay_invite', 'conditions': 'is_going_to_jay_invite'},
        {'trigger': 'advance', 'source': 'jay_bread', 'dest': 'goodend_turn_down_jay', 'conditions': 'is_going_to_goodend_turn_down_jay'},

        #source jay_invite
        {'trigger': 'advance', 'source': 'jay_invite', 'dest': 'market', 'conditions': 'is_going_to_market'},
        {'trigger': 'advance', 'source': 'jay_invite', 'dest': 'goodend_turn_down_jay', 'conditions': 'is_going_to_goodend_turn_down_jay'},

        #source market
        {'trigger': 'advance', 'source': 'market', 'dest': 'jay_house', 'conditions': 'is_going_to_jay_house'},
        {'trigger': 'advance', 'source': 'market', 'dest': 'goodend_staying_sober', 'conditions': 'is_going_to_goodend_staying_sober'},

        #source jay_house
        {'trigger': 'advance', 'source': 'jay_house', 'dest': 'drink_once', 'conditions': 'is_going_to_drink_once'},
        {'trigger': 'advance', 'source': 'jay_house', 'dest': 'jay_tough', 'conditions': 'is_going_to_jay_tough'},

        #source drink_once
        {'trigger': 'advance', 'source': 'drink_once', 'dest': 'drink_twice', 'conditions': 'is_going_to_drink_twice'},
        {'trigger': 'advance', 'source': 'drink_once', 'dest': 'jay_tough', 'conditions': 'is_going_to_jay_tough'},
        
        #source drink_twice
        {'trigger': 'advance', 'source': 'drink_twice', 'dest': 'jay_tough', 'conditions': 'is_going_to_jay_tough'},
        {'trigger': 'advance', 'source': 'drink_twice', 'dest': 'neutralend_drunk', 'conditions': 'is_going_to_neutralend_drunk'},

        #source jay_tough
        {'trigger': 'advance', 'source': 'jay_tough', 'dest': 'jay_fit', 'conditions': 'is_going_to_jay_fit'},
        
        #source jay_fit
        {'trigger': 'advance', 'source': 'jay_fit', 'dest': 'jay_youDoNotUnderstand', 'conditions': 'is_going_to_jay_youDoNotUnderstand'},

        #source jay_youDoNotUnderstand
        {'trigger': 'advance', 'source': 'jay_youDoNotUnderstand', 'dest': 'jay_adult', 'conditions': 'is_going_to_jay_adult'},
        {'trigger': 'advance', 'source': 'jay_youDoNotUnderstand', 'dest': 'neutralend_consent', 'conditions': 'is_going_to_neutralend_consent'},

        #source jay_adult
        {'trigger': 'advance', 'source': 'jay_adult', 'dest': 'jay_porn', 'conditions': 'is_going_to_jay_porn'},
        {'trigger': 'advance', 'source': 'jay_adult', 'dest': 'secretend_NCKU', 'conditions': 'is_going_to_secretend_NCKU'},

        #source jay_porn
        {'trigger': 'advance', 'source': 'jay_porn', 'dest': 'jay_blush', 'conditions': 'is_going_to_jay_blush'},
        
        #source jay_blush
        {'trigger': 'advance', 'source': 'jay_blush', 'dest': 'jay_letMeSee', 'conditions': 'is_going_to_jay_letMeSee'},
        {'trigger': 'advance', 'source': 'jay_blush', 'dest': 'neutralend_consent', 'conditions': 'is_going_to_neutralend_consent'},

        #source jay_letMeSee
        {'trigger': 'advance', 'source': 'jay_letMeSee', 'dest': 'jay_ifYouAreNormal', 'conditions': 'is_going_to_jay_ifYouAreNormal'},
        {'trigger': 'advance', 'source': 'jay_letMeSee', 'dest': 'neutralend_consent', 'conditions': 'is_going_to_neutralend_consent'},

        #source jay_ifYouAreNormal
        {'trigger': 'advance', 'source': 'jay_ifYouAreNormal', 'dest': 'jay_checked_your_body', 'conditions': 'is_going_to_jay_checked_your_body'},
        {'trigger': 'advance', 'source': 'jay_ifYouAreNormal', 'dest': 'jay_listen_letMeSee', 'conditions': 'is_going_to_jay_listen_letMeSee'},

        #source jay_checked_your_body
        {'trigger': 'advance', 'source': 'jay_checked_your_body', 'dest': 'goodend_too_small', 'conditions': 'is_going_to_goodend_too_small'},
        {'trigger': 'advance', 'source': 'jay_checked_your_body', 'dest': 'jay_bed', 'conditions': 'is_going_to_jay_bed'},
        {'trigger': 'advance', 'source': 'jay_checked_your_body', 'dest': 'jay_get_scared', 'conditions': 'is_going_to_jay_get_scared'},

        #source jay_get_scared
        {'trigger': 'advance', 'source': 'jay_get_scared', 'dest': 'secretend_reverse', 'conditions': 'is_going_to_secretend_reverse'},

        #source jay_listen_letMeSee
        {'trigger': 'advance', 'source': 'jay_listen_letMeSee', 'dest': 'jay_punch', 'conditions': 'is_going_to_jay_punch'},
        {'trigger': 'advance', 'source': 'jay_listen_letMeSee', 'dest': 'jay_bed', 'conditions': 'is_going_to_jay_bed'},

        #source jay_punch
        {'trigger': 'advance', 'source': 'jay_punch', 'dest': 'jay_took_of_cloth', 'conditions': 'is_going_to_jay_took_of_cloth'},

        #source jay_took_of_cloth
        {'trigger': 'advance', 'source': 'jay_took_of_cloth', 'dest': 'jay_bed', 'conditions': 'is_going_to_jay_bed'},

        #source jay_bed
        {'trigger': 'advance', 'source': 'jay_bed', 'dest': 'badend_rape', 'conditions': 'is_going_to_badend_rape'},


        {'trigger': 'go_back',
            'source': [
                'goodend_study', 
                'goodend_turn_down_jay', 
                'goodend_staying_sober', 
                'goodend_staying_sober', 
                'neutralend_consent',  
                'neutralend_drunk', 
                'secretend_NCKU', 
                'goodend_too_small', 
                'secretend_reverse', 
                'badend_rape', 
            ],
            'dest': 'init'
        },
    ],
    initial='init',
    auto_transitions=False,
    show_conditions=True,
    )
    return machine