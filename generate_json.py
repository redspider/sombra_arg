import base64
import binascii
import json

data = dict()

data['cipher_base64'] = """U2FsdGVkX1+vupppZksvRf5pq5g5XjFRlipRkwB0K1Y96Qsv2Lm+31cmzaAILwytX/z66ZVWEQM/ccf1g+9m5Ubu1+sit+A9cenDxxqklaxbm4cMeh2oKhqlHhdaBKOi6XX2XDWpa6+P5o9MQw=="""
decoded = base64.b64decode(data['cipher_base64'])
data['cipher_salt_hex'] = str(binascii.hexlify(decoded[8:16]))
data['cipher_text_hex'] = str(binascii.hexlify(decoded[16:]))

data['alphabet'] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

data['grid_binary'] = """1001101011001011
1101011010111010
0101101011010100"""

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
    'genji': {
        'name': 'Genji',
        'real_name': 'Genji Shimada',
        'voice_artist': 'Gaku Space',
        'base': 'Hanamura? Japan?'
    },
    'mccree': {
        'name': 'McCree',
        'real_name': 'Jesse McCree',
        'voice_artist': 'Matthew Mercer',
        'base': 'Santa Fe, New Mexico'
    },
    'pharah': {
        'name': 'Pharah',
        'real_name': 'Fareeha Amari',
        'voice_artist': 'Jen Cohn',
        'base': 'Giza Plateau'
    },
    'reaper': {
        'name': 'Reaper',
        'real_name': 'Gabriel Reyes',
        'voice_artist': 'Keith Ferguson',
        'base': 'Los Angeles?'
    },
    'soldier76': {
        'name': 'Soldier: 76',
        'real_name': 'John Morrison',
        'alias': 'Jack Morrison',
        'voice_artist': 'Fred Tatasciore',
        'base': 'Indiana?'
    },
    'tracer': {
        'name': 'Tracer',
        'real_name': 'Lena Oxton',
        'voice_artist': 'Cata Theobold',
        'base': 'London'
    },

    'bastion': {
        'name': 'Bastion',
        'real_name': 'Bastion',
        'voice_artist': 'Chris Metzen',
        'base': None,
        'bird': 'Ganymede'
    },
    'hanzo': {
        'name': 'Hanzo',
        'real_name': 'Hanzo Shimada',
        'voice_artist': 'Paul Nakauchi',
        'base': 'Hanamura? Japan?'
    },
    'junkrat': {
        'name': 'Junkrat',
        'real_name': 'Jamison Fawkes',
        'voice_artist': 'Chris Parson',
        'base': 'Australia'
    },
    'mei': {
        'name': 'Mei',
        'real_name': 'Mei-Ling Zhou',
        'voice_artist': 'Zhang Yu',
        'base': 'China? Antarctica?'
    },
    'torbjorn': {
        'name': 'Torbjorn',
        'real_name': 'Torbjorn Lindholm',
        'voice_artist': 'Kevin Silverstein',
        'base': 'Sweden?'
    },
    'widowmaker': {
        'name': 'Widowmaker',
        'real_name': 'Amelie Lacroix',
        'voice_artist': 'Chloe Hollings',
        'base': 'France? Talon?'
    },


    'd.va': {
        'name': 'D.va',
        'real_name': 'Hana Song',
        'voice_artist': 'Charlet Chung',
        'base': 'South Korea'
    },
    'reinhardt': {
        'name': 'Reinhardt',
        'real_name': 'Reinhardt Wilhelm',
        'voice_artist': 'Darin De Paul',
        'base': 'Stuttgart'
    },
    'roadhog': {
        'name': 'Roadhog',
        'real_name': 'Mako Rutledge',
        'voice_artist': 'Fred Tatasciore',
        'base': 'Australia'
    },
    'winston': {
        'name': 'Winston',
        'full_name': 'Winston',
        'voice_artist': 'Crispin Freeman',
        'base': 'Gibraltar'
    },
    'zarya': {
        'name': 'Zarya',
        'full_name': 'Aleksandra Zaryanova',
        'voice_artist': 'Dolya Gavanski',
        'base': 'Siberia'
    },

    'ana': {
        'name': 'Ana',
        'full_name': 'Ana Amari',
        'voice_artist': 'Shohreh Aghdashloo',
        'base': 'Cairo'
    },
    'lucio': {
        'name': 'Lucio',
        'real_name': 'Lucio Correia dos Santos',
        'voice_artist': 'Jonny Cruz',
        'base': 'Rio de Janeiro'
    },
    'mercy': {
        'name': 'Mercy',
        'real_name': 'Angela Ziegler',
        'voice_artist': 'Lucie Pohl',
        'base': 'Switzerland'
    },
    'symmetra': {
        'name': 'Symmetra',
        'real_name': 'Satya Vaswani',
        'voice_artist': 'Anjali Bhimani',
        'base': 'Utopaea, Southern India'
    },
    'zenyatta': {
        'name': 'Zenyatta',
        'real_name': 'Tekhartha Zenyatta',
        'voice_artist': 'Feodor Chin',
        'base': 'Himalayas, Nepal'
    },

    'sombra': {
        'name': 'Sombra',
        'real_name': None,
        'possible_real_name': 'Maria Estrada',  # See https://www.reddit.com/r/Overwatch/comments/4vyxji/sombra_is_not_mexican_she_is_from_spain_real_name/
        'voice_artist': None,
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

# Encodings taking from these images: https://puu.sh/qoTnQ/0adc3d7923.jpg
# Encoded by @catnipp#8350

data['card_tours'] = """- - - -  --- - - ---   - - --- -
- --- - -  --- - - - --- - -
- - ---  - - --- - - - ---
- - - -  --- - - ---   - - --- -
- --- - -  --- - - - --- - -
- --- - -  ---       --- - -"""
data['card_numbani_travel'] = """- - - -  --- - - ---   - - --- - - -
- --- - -  --- - - - --- - -   --- - -
- - ---  - - --- - - - ---
- - - -  --- - - ---   - - --- - - - ---  - -
- --- - -  --- - - - --- - -   --- - - ---
- --- - -  ---       --- - -   --- - - --- -
- - ---  - - ---   - - ---"""
data['card_numbani_airlines'] = """---   - - --- - - - ---   - - --- -
- - --- - -   --- - -  ---  - -
---   - - --- - - - ---   - - --- -
---   - - --- - - - ---   - - --- -
- - --- - -   --- - -  ---  - -
---   - - --- - - - ---   - - --- -
- - --- - -   --- - -  ---  - -
---   - - --- - - - ---   - - --- -
---   - - --- - - - ---   - - --- -"""

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

data['genji_directions'] = ['sw','ne','e','s','se','c','nw','w','n']

data['computed_directions_as_keypad_1_by_time'] = [data['keypad_1'][k] for k,v in sorted(data['directions'].items(), key=lambda i: i[1]['time'])]

data['genji_order'] = [data['directions'][k]['character'] for k in data['genji_directions']]

print(json.dumps(data))
