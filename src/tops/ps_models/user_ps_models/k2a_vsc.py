def load():
    return {
        'base_mva': 900,
        'f': 50,
        'slack_bus': 'B3',

        'buses': [
            ['name',    'V_n'],
            ['B1',      20],
            ['B2',      20],
            ['B3',      20],
            ['B4',      20],
            ['B5',      230],
            ['B6',      230],
            ['B7',      230],
            ['B8',      230],
            ['B9',      230],
            ['B10',     230],
            ['B11',     230],
        ],

        'lines': [
            ['name',    'from_bus', 'to_bus',   'length',   'S_n',  'V_n',  'unit',     'R',    'X',    'B'],
            ['L5-6',    'B5',       'B6',       25,         100,    230,    'p.u.',     1e-4,   1e-3,   1.75e-3],
            ['L6-7',    'B6',       'B7',       10,         100,    230,    'p.u.',     1e-4,   1e-3,   1.75e-3],
            ['L7-8-1',  'B7',       'B8',       110,        100,    230,    'p.u.',     1e-4,   1e-3,   1.75e-3],
            ['L7-8-2',  'B7',       'B8',       110,        100,    230,    'p.u.',     1e-4,   1e-3,   1.75e-3],
            ['L8-9-1',  'B8',       'B9',       110,        100,    230,    'p.u.',     1e-4,   1e-3,   1.75e-3],
            ['L8-9-2',  'B8',       'B9',       110,        100,    230,    'p.u.',     1e-4,   1e-3,   1.75e-3],
            ['L9-10',   'B9',       'B10',      10,         100,    230,    'p.u.',     1e-4,   1e-3,   1.75e-3],
            ['L10-11',  'B10',      'B11',      25,         100,    230,    'p.u.',     1e-4,   1e-3,   1.75e-3],
        ],

        'transformers': [
            ['name',    'from_bus', 'to_bus',   'S_n',  'V_n_from', 'V_n_to',   'R',    'X'],
            ['T1',      'B1',       'B5',       900,    20,         230,        0,      0.15],
            ['T2',      'B2',       'B6',       900,    20,         230,        0,      0.15],
            ['T3',      'B3',       'B11',      900,    20,         230,        0,      0.15],
            ['T4',      'B4',       'B10',      900,    20,         230,        0,      0.15],
        ],

        'loads': [
            ['name',    'bus',  'P',    'Q',    'model'],
            ['L1',      'B7',   967,    100,    'Z'],
            ['L2',      'B9',   1767,   100,    'Z'],
        ],

        'shunts': [
            ['name',    'bus',  'V_n',  'Q',    'model'],
            ['C1',      'B7',   230,    200,    'Z'],
            ['C2',      'B9',   230,    350,    'Z'],
        ],

        # Changing G1 to parameters found on a PMSG generator
        # https://journals.tubitak.gov.tr/cgi/viewcontent.cgi?article=1759&context=elektrik
        'generators': {
            'GEN': [
                ['name',    'bus',  'S_n',  'V_n',  'P',    'V',    'H',    'D',    'X_d',  'X_q',  'X_d_t',    'X_q_t',    'X_d_st',   'X_q_st',   'T_d0_t',   'T_q0_t',   'T_d0_st',  'T_q0_st'],
                ['G1',      'B1',   889,    18.5,     700,    1.03,   6.3,    0,      1.72,    1.69,    0.36,        0.4,       0.25,       0.25,       5.7,        0.4,        0.04,       0.05],
                ['G2',      'B2',   900,    20,     700,    1.01,   6.5,    0,      1.8,    1.7,    0.3,        0.55,       0.25,       0.25,       8.0,        0.4,        0.03,       0.05],
                ['G3',      'B3',   900,    20,     719,    1.03,   6.175,  0,      1.8,    1.7,    0.3,        0.55,       0.25,       0.25,       8.0,        0.4,        0.03,       0.05],
                ['G4',      'B4',   900,    20,     700,    1.01,   6.175,  0,      1.8,    1.7,    0.3,        0.55,       0.25,       0.25,       8.0,        0.4,        0.03,       0.05],
            ]
        },

        'gov': {
            'TGOV1': [
                ['name',    'gen',  'R',    'D_t',  'V_min',    'V_max',    'T_1',  'T_2',  'T_3'],
                ['GOV1',     'G1',   0.05,   0.02,   0,          1,          0.1,    0.09,   0.2],
                ['GOV2',     'G2',   0.05,   0.02,   0,          1,          0.1,    0.09,   0.2],
                ['GOV3',     'G3',   0.05,   0.02,   0,          1,          0.1,    0.09,   0.2],
                ['GOV4',     'G4',   0.05,   0.02,   0,          1,          0.1,    0.09,   0.2],
            ]
        },

        'avr': {
            'SEXS': [
                ['name',   'gen',      'K',    'T_a',  'T_b',  'T_e',  'E_min',    'E_max'],
                ['AVR1',    'G1',       100,    2.0,    10.0,   0.5,    -3,         3],
                ['AVR2',    'G2',       100,    2.0,    10.0,   0.5,    -3,         3],
                ['AVR3',    'G3',       100,    2.0,    10.0,   0.5,    -3,         3],
                ['AVR4',    'G4',       100,    2.0,    10.0,   0.5,    -3,         3],
            ]
        },

        'pss': {
            'STAB1': [
                ['name',    'gen',  'K',    'T',    'T_1',  'T_2',  'T_3',  'T_4',  'H_lim'],
                ['PSS1',    'G1',   50,     10.0,   0.5,    0.5,    0.05,   0.05,   0.03],
                ['PSS2',    'G2',   50,     10.0,   0.5,    0.5,    0.05,   0.05,   0.03],
                ['PSS3',    'G3',   50,     10.0,   0.5,    0.5,    0.05,   0.05,   0.03],
                ['PSS4',    'G4',   50,     10.0,   0.5,    0.5,    0.05,   0.05,   0.03],
            ]
        },

        # 'vsc': {
        #     'VSC': [
        # ['name',    'T_pll',    'T_i',  'bus',  'P_K_p',    'P_K_i',    'Q_K_p',    'Q_K_i',    'P_setp',   'Q_setp',   ],
        # ['VSC1',    0.1,        1,      'B8',   0.1,        0.1,        0.1,        0.1,        100,          100],
        #     ]
    
        # }
        # 'vsc1': {
        #     'VSC_PQ': [
        #         ['name', 'bus', 'S_n', 'p_ref', 'q_ref',  'k_p', 'k_q', 'T_p', 'T_q', 'k_pll','T_pll', 'T_i', 'i_max'],
        #         ['VSC1', 'B1',    50,     1,       0,       3,      3,    0.1,   0.1,     5,      1,      0.03,    1.2],
        #     ],
        # }
        # 'vsc1': {
        #     'VSC_PQ': [
        #         ['name', 'bus', 'S_n', 'p_ref', 'q_ref',  'k_p', 'k_q', 'T_p', 'T_q', 'k_pll','T_pll', 'T_i', 'i_max'],
        #         ['VSC1', 'B1',    100,     0,       0,       5,      5,    0.05,   0.05,     10,      0.5,      0.02,    1.5],
        #     ],
        # },
 
        # 'wt': {
        #     'WT': [
        #         ['name', 'bus', 'S_n', 'p_ref', 'q_ref',  'k_p', 'k_q', 'T_p', 'T_q', 'k_pll','T_pll', 'T_i', 'i_max'],
    }

