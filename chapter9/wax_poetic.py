import random

qualifier = random.choice(["A", "An"])
nouns = random.choice(["fossil", "horse", "aardvark", "judge", "chef", "mango",
                       "extrovert", "gorilla"])
verbs = random.choice(["kicks", "jingles", "bounce", "slurps", "meows",
                       "explodes", "curdles"])
adjectives = random.choice(["furry", "balding", "incredulous", "fragrant",
                            "exuberant", "glistening"])
prepositions = random.choice(["against", "after", "into", "beneath", "upon",
                              "for", "in", "like", "over", "within"])
adverbs = random.choice(["curiously", "extravagantly", "tantalizingly",
                         "furiously", "sensuously"])

print(f"\n{qualifier} {adjectives} {nouns}")
print(f"\n{adjectives} {nouns} {verbs} {prepositions} the {adjectives} {nouns} {adverbs} the {nouns} {verbs}")
print(f"\nthe {nouns} {verbs} {prepositions} a {adjectives} {nouns}")
