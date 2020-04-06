#!/usr/bin/env python
# -*- coding: utf-8 -*-

morse_code = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.", 
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": "·---",
    "k": "-.-",
    "l": ".-..", 
    "m": "--",
    "n": "-.",
    "ñ": "--.--",
    "o": "---",
    "p": ".__.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}

translated = ""
import sys
for char in sys.argv[1]:
    if char != " " and char.lower() in morse_code:
        translated += morse_code[char.lower()]
    else:
        translated += char
print(format(translated))