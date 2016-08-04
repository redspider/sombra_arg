import base64
import binascii
import json

data = dict()

data['cipher_base64'] = """U2FsdGVkX1+vupppZksvRf5pq5g5XjFRlipRkwB0K1Y96Qsv2Lm+31cmzaAILwytX/z66ZVWEQM/ccf1g+9m5Ubu1+sit
+A9cenDxxqklaxbm4cMeh2oKhqlHhdaBKOi6XX2XDWpa6+P5o9MQw=="""
decoded = base64.b64decode(data['cipher_base64'])
data['cipher_salt_hex'] = str(binascii.hexlify(decoded[8:16]))
data['cipher_text_hex'] = str(binascii.hexlify(decoded[16:]))

data['alphabet'] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

data['maps'] = {
    'anubis': {
        'name': 'Anubis',
        'location': 'Egypt'
    },
    'nepal': {
        'name': 'Nepal',
        'location': 'Nepal'
    },
    'hanamura': {
        'name': 'Hanamura'
    },
    'hollywood': {
        'name': 'Hollywood'
    },
    'gibraltar': {
        'name': 'Gibraltar'
    },
    'volskaya': {
        'name': 'Volskaya'
    },
    'kings_row': {
        'name': 'Kings Row'
    }
}

data['usernames'] = [
    'WNSTN',
    'SMBRA'
]

data['characters'] = {
    'mercy': {
        'name': 'Mercy',
        'real_name': 'Angela Ziegler'
    },
    'd.va': {
        'name': 'D.va',
        'real_name': 'Hana Song'
    },
    'torb': {
        'name': 'Torbjorn',
    },
    'genji': {
        'name': 'Genji'
    },
    'mccree': {
        'name': 'McCree'
    },
    'symmetra': {
        'name': 'Symmetra'
    },
    'bastion': {
        'name': 'Bastion'
    },
    'winston': {
        'name': 'Winston'
    },
    'tracer': {
        'name': 'Tracer'
    }
}

data['directions'] = {
    'c': {
        'character': 'd.va',
        'map': 'anubis',
        'time': 19
    },
    'e': {
        'character': 'mercy',
        'map': 'route66',
        'time': 17
    },
    'n': {
        'character': 'torb',
        'map': 'nepal',
        'time': 21
    },
    's': {
        'character': 'genji',
        'map': 'hanamura',
        'time': 22
    },
    'se': {
        'character': 'mccree',
        'map': 'hollywood',
        'time': 24
    },
    'w': {
        'character': 'symmetra',
        'map': 'gibraltar',
        'time': 30
    },
    'sw': {
        'character': 'bastion',
        'map': 'hollywood',
        'time': 34
    },
    'ne': {
        'character': 'winston',
        'map': 'volskaya',
        'time': 46
    },
    'nw': {
        'character': 'tracer',
        'map': 'kings_row',
        'time': 47
    }
}

data['airline_boards_original'] = [
    {'time': '20:00', 'origin': 'seoul',        'flight': 'HG 0614', 'status': 'on_time', 'side': 'left'},
    {'time': '21:30', 'origin': 'moscow',       'flight': 'ES 4R41', 'status': 'delayed', 'side': 'left'},
    {'time': '22:15', 'origin': 'cork',         'flight': 'BF 3264', 'status': 'on_time', 'side': 'left'},
    {'time': '22:55', 'origin': 'hong kong',    'flight': 'HA 3252', 'status': 'on_time', 'side': 'left'},
    {'time': '24:00', 'origin': 'buenos aires', 'flight': 'OL 7215', 'status': 'on_time', 'side': 'left'},
    {'time': '1:05',  'origin': 'rome',         'flight': 'VW A353', 'status': 'on_time', 'side': 'left'},
    {'time': '1:20',  'origin': 'madrid',       'flight': 'CQ 4142', 'status': 'canceled', 'side': 'left'},
    {'time': '2:25',  'origin': 'paris',        'flight': 'SJ 5863', 'status': 'delayed', 'side': 'left'},
    {'time': '2:35',  'origin': 'tokyo',        'flight': 'KU 4352', 'status': 'delayed', 'side': 'left'},
    {'time': '2:55',  'origin': 'delhi',        'flight': 'PO 2567', 'status': 'on_time', 'side': 'left'},
    {'time': '3:30',  'origin': 'shanghai',     'flight': 'RG 2554', 'status': 'on_time', 'side': 'left'},
    {'time': '3:55',  'origin': 'frankfurt',    'flight': 'JG 2564', 'status': 'canceled', 'side': 'left'},

    {'time': '4:00',  'origin': 'london',       'flight': 'GR 0254', 'status': 'on_time', 'side': 'right'},
    {'time': '4:20',  'origin': 'austin',       'flight': 'TE 1331', 'status': 'canceled', 'side': 'right'},
    {'time': '4:10',  'origin': 'mexico city',  'flight': 'SX 0126', 'status': 'on_time', 'side': 'right'},
    {'time': '4:45',  'origin': 'new york',     'flight': 'EE 2342', 'status': 'delayed', 'side': 'right'},
    {'time': '5:00',  'origin': 'san francisco','flight': 'UT 2543', 'status': 'on_time', 'side': 'right'},
    {'time': '5:20',  'origin': 'cairo',        'flight': 'KE 7145', 'status': 'on_time', 'side': 'right'},
    {'time': '5:35',  'origin': 'johannesburg', 'flight': 'DQ 1276', 'status': 'on_time', 'side': 'right'},
    {'time': '5:55',  'origin': 'los angeles',  'flight': 'AH 8343', 'status': 'on_time', 'side': 'right'},
    {'time': '6:30',  'origin': 'london',       'flight': 'GT 4212', 'status': 'delayed', 'side': 'right'},
    {'time': '6:40',  'origin': 'versailles',   'flight': 'GR 3337', 'status': 'on_time', 'side': 'right'},
    {'time': '6:55',  'origin': 'los angeles',  'flight': 'AT 3245', 'status': 'on_time', 'side': 'right'},
    {'time': '7:20',  'origin': 'irvine',       'flight': 'BJ 3567', 'status': 'delayed', 'side': 'right'},
]

data['airline_boards_new'] = [
    {'time': '20:00', 'origin': 'seoul',        'flight': 'HG 0614', 'status': 'on_time', 'side': 'left'},
    {'time': '21:30', 'origin': 'moscow',       'flight': 'ES 4R41', 'status': 'canceled', 'side': 'left'},
    {'time': '22:15', 'origin': 'cork',         'flight': 'BF 3264', 'status': 'on_time', 'side': 'left'},
    {'time': '22:55', 'origin': 'hong kong',    'flight': 'HA 3252', 'status': 'on_time', 'side': 'left'},
    {'time': '24:00', 'origin': 'buenos aires', 'flight': 'OL 7215', 'status': 'on_time', 'side': 'left'},
    {'time': '1:05',  'origin': 'rome',         'flight': 'VW A353', 'status': 'on_time', 'side': 'left'},
    {'time': '1:20',  'origin': 'madrid',       'flight': 'CQ 4142', 'status': 'canceled', 'side': 'left'},
    {'time': '2:25',  'origin': 'paris',        'flight': 'SJ 5863', 'status': 'on_time', 'side': 'left'},
    {'time': '2:35',  'origin': 'hanamura',     'flight': 'KU 4352', 'status': 'on_time', 'side': 'left'},
    {'time': '2:55',  'origin': 'delhi',        'flight': 'PO 2567', 'status': 'on_time', 'side': 'left'},
    {'time': '3:30',  'origin': 'shanghai',     'flight': 'RG 2554', 'status': 'on_time', 'side': 'left'},
    {'time': '3:55',  'origin': 'frankfurt',    'flight': 'JG 2564', 'status': 'canceled', 'side': 'left'},

    {'time': '4:00',  'origin': 'singapore',    'flight': 'GR 0254', 'status': 'on_time', 'side': 'right'},
    {'time': '4:20',  'origin': 'austin',       'flight': 'TE 1331', 'status': 'canceled', 'side': 'right'},
    {'time': '4:10',  'origin': 'dorado',       'flight': 'SX 0126', 'status': 'on_time', 'side': 'right'},
    {'time': '4:45',  'origin': 'new york',     'flight': 'EE 2342', 'status': 'on_time', 'side': 'right'},
    {'time': '5:00',  'origin': 'san francisco','flight': 'UT 2543', 'status': 'on_time', 'side': 'right'},
    {'time': '5:20',  'origin': 'taipei',       'flight': 'KE 7145', 'status': 'on_time', 'side': 'right'},
    {'time': '5:35',  'origin': 'johannesburg', 'flight': 'DQ 1276', 'status': 'on_time', 'side': 'right'},
    {'time': '5:55',  'origin': 'sydney',       'flight': 'AH 8343', 'status': 'on_time', 'side': 'right'},
    {'time': '6:30',  'origin': 'kings row',    'flight': 'CK 1117', 'status': 'on_time', 'side': 'right'},
    {'time': '6:40',  'origin': 'versailles',   'flight': 'GR 3337', 'status': 'on_time', 'side': 'right'},
    {'time': '6:55',  'origin': 'los angeles',  'flight': 'AT 3245', 'status': 'on_time', 'side': 'right'},
    {'time': '7:20',  'origin': 'irvine',       'flight': 'BJ 3567', 'status': 'delayed', 'side': 'right'},
]

data['keypad_1'] = {
    'nw': 7,
    'n': 8,
    'ne': 9,
    'w': 4,
    'c': 5,
    'e': 6,
    'sw': 1,
    's': 2,
    'se': 3
}

data['keypad_2'] = {
    'nw': 1,
    'n': 2,
    'ne': 3,
    'w': 4,
    'c': 5,
    'e': 6,
    'sw': 7,
    's': 8,
    'se': 9
}

data['game_wheel'] = {
    'nw': 'THANK',
    'n': 'EMOTE',
    'ne': 'HELLO',
    'w': 'ACKNOWLEDGE',
    'c': None,
    'e': 'NEED HEALING',
    'sw': 'VOICE LINE',
    's': 'ULTIMATE STATUS',
    'se': 'GROUP UP'
}

data['winston_lexigram'] = {
    'nw': 'hello',
    'n': 'computer',
    'ne': 'look',
    'w': 'juice',
    'c': 'room',
    'e': 'friend',
    'sw': 'water',
    's': 'peanut butter',
    'se': 'open'
}

data['blizzard_wheel'] = {
    'nw': 'Cork',
    'n': 'Irvine',
    'ne': 'Austin',
    'w': 'Versailles',
    'c': 'Blizzard',
    'e': 'Seoul',
    'sw': 'Taipei',
    's': 'Shanghai',
    'se': 'Hangzhou'
}

data['computed_directions_as_keypad_1_by_time'] = [data['keypad_1'][k] for k,v in sorted(data['directions'].items(), key=lambda i: i[1]['time'])]

print(json.dumps(data))
