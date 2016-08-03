import base64
import binascii
import json

data = dict()

data['cipher_base64'] = """U2FsdGVkX1+vupppZksvRf5pq5g5XjFRlipRkwB0K1Y96Qsv2Lm+31cmzaAILwytX/z66ZVWEQM/ccf1g+9m5Ubu1+sit
+A9cenDxxqklaxbm4cMeh2oKhqlHhdaBKOi6XX2XDWpa6+P5o9MQw=="""
decoded = base64.b64decode(data['cipher_base64'])
data['cipher_salt_hex'] = str(binascii.hexlify(decoded[8:16]))
data['cipher_text_hex'] = str(binascii.hexlify(decoded[16:]))

data['maps'] = {
    'anubis': {
        'name': 'Anubis',
        'location': 'Egypt'
    },
    'nepal': {
        'name': 'Nepal',
        'location': 'Nepal'
    }
}

data['characters'] = {
    'mercy': {
        'name': 'Mercy',
        'real_name': 'Angela Ziegler'
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
        'time': 35
    }
}

data['airline_boards'] = [
    {'time': '20:00', 'origin': 'seoul', 'flight': 'HG 0614', 'on_time': True, 'changed': []},
    {'time': '20:30', 'origin': 'moscow', 'flight': 'ES 4R41', 'on_time': False, 'changed': ['on_time']},
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
}

data['winston_lexigram'] = {
    'nw': 'hello',
    'n': 'computer'
}

data['blizzard_wheel'] = {
    'nw': 'Cork',
    'n': 'Irvine'
}

data['computed_directions_as_keypad_1_by_time'] = [data['keypad_1'][k] for k,v in sorted(data['directions'].items(), key=lambda i: i[1]['time'])]

print(json.dumps(data))
