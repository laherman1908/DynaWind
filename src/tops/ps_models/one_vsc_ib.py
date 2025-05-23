def load():
    return {
        'base_mva': 50,
        'f': 50,
        'slack_bus': 'B3',

        'buses': [
            ['name',    'V_n'],
            ['B1',         10],
            ['B2',        245],
            ['B3',        245],
        ],

        'lines': [
            ['name',  'from_bus', 'to_bus',     'length',   'S_n',  'V_n',  'unit', 'R',    'X',   'B'],
            ['L2-3',        'B2',     'B3',        250,      50,     245,    'PF',   0,    0.4,     0],
        ],

        'transformers': [
            ['name', 'from_bus', 'to_bus', 'S_n', 'V_n_from', 'V_n_to', 'R', 'X'],
            ['T1',         'B1',     'B2',    50,         10,      245,   0, 0.1],
        ],

        'loads': [
            ['name', 'bus', 'P', 'Q', 'model'],
            ['L1',    'B2',  25,   0,     'Z'],
        ],

        'generators': {
            'GEN': [
                ['name',   'bus',  'S_n',  'V_n',    'P',    'V',      'H',    'D',    'X_d',  'X_q',  'X_d_t',    'X_q_t',    'X_d_st',   'X_q_st',   'T_d0_t',   'T_q0_t',   'T_d0_st',  'T_q0_st'],
                ['IB',      'B3',    1e6,    245,    -10,  0.898,      1e5,      0,     1.05,   0.66,    0.328,      0.66,       1e-5,      1e-5,         1e5,      10000,          1e5,        1e5],
            ],
        },

        # 'vsc': {
        #     'VSC_PV': [
        #         ['name', 'bus', 'S_n', 'p_ref', 'V', 'k_p', 'k_v', 'T_p', 'T_v', 'k_pll', 'T_pll', 'T_i', 'i_max'],
        #         ['VSC1', 'B1',    50,   0.8,    0.93,    1,      1,   0.1,   0.1,     5,      1,      0.01,    1.2],
        #     ],
        #     #'VSC_PQ': [
        #     #    ['name', 'bus', 'S_n', 'p_ref', 'q_ref',  'k_p', 'k_q', 'T_p', 'T_q', 'k_pll','T_pll', 'T_i', 'i_max'],
        #     #    ['VSC1', 'B1',    50,     1,       0,       1,      1,    0.1,   0.1,     5,      1,      0.01,    1.2],
        #     #],
        # }

        'vsc': {
            'GridSideConverter': [ 
                ['name',   'bus',    'S_n',      "p_ref_grid",      "q_ref_grid",   'k_p',      'k_q',    'T_p',     'T_q',     'k_pll',   'T_pll',    'T_i',      "i_max"],
                ['WT1',    'B3',      20,         0.5,               0.0,           5,          1,        0.1,        0.1,        5,        1,         0.01,      1.2],
            ]
        }
    }