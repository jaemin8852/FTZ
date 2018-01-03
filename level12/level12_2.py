import os

loop_sentence = "(python level12_1.py; cat) | ../attackme"

i = 1
while i < 10:
    os.system(loop_sentence)
    i = i + 1