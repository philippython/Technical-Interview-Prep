import re

txt = "The rain in spain"
sub = "substitute player in the game"
print(re.findall("^The.*spain$", txt))

def substitution(txt):
    return lambda player : re.sub("player", player, txt, 1)
substitute = substitution(sub)
print(substitute("ronaldo"))

