This repo contains resources useful for the Overwatch SOMBRA ARG.

MAPPINGS ARE INCOMPLETE, CONTRIBUTIONS WELCOME

The file `generate_json.py` produces a JSON file containing a wide variety of information sourced by the community, allowing developers to attempt to combine various pieces to find new insights or generate good sequences to try brute forcing the puzzle. The following keys are available.


`maps` : a dictionary of maps, containing data about `name` and `location`

`characters` : a dictionary of characters, containing `name`, `real_name`

`directions` : a dictionary of directions found in a video, associated to `character`, `map` and time index in the video in seconds

`airline_boards_original` and `airline_boards_changed`: a list of the airline arrivals boards, dictionaries for each containing `time`, `origin`, `flight`, `status` (bool), and `side`.

`keypad_1` : a simple map between cardinal directions and a computer keypad

`keypad_2` : upside down version (phones etc)

`game_wheel` : emotes on the game wheel by direction

`winston_lexigram` : parts of winstons lexigram spray by direction

`blizzard_wheel` : locations from the blizzard location wheel by direction

`cipher_base64` : the original cipher in base64

`cipher_salt_hex` : the salt from the cipher extracted and hexed

`cipher_text_hex` : the ciphertext extracted and hexed

A set of computed keys are available too, for example

`computed_directions_as_keypad_1_by_time` will give the number sequence when taking the directions in time order and returning the related keypad_1 number
 
