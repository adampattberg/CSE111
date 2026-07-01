import random

def main():

    name = "a"
    q = 1
    t = "past"
    determiner = get_determiner(q)
    noun = get_noun(q)
    verb = get_verb(q, t)
    cap_word = determiner.capitalize()
    prep_phrase = get_prepositional_phrase(q)
    print(f"{cap_word} {noun} {verb} {prep_phrase}.")

    name = "b"
    q = 1
    t = "present"
    determiner = get_determiner(q)
    noun = get_noun(q)
    verb = get_verb(q, t)
    cap_word = determiner.capitalize()
    prep_phrase = get_prepositional_phrase(q)
    print(f"{cap_word} {noun} {verb} {prep_phrase}.")

    name = "c"
    q = 1
    t = "future"
    determiner = get_determiner(q)
    noun = get_noun(q)
    verb = get_verb(q, t)
    cap_word = determiner.capitalize()
    prep_phrase = get_prepositional_phrase(q)
    print(f"{cap_word} {noun} {verb} {prep_phrase}.")

    name = "d"
    q = 2
    t = "past"
    determiner = get_determiner(q)
    noun = get_noun(q)
    verb = get_verb(q, t)
    cap_word = determiner.capitalize()
    prep_phrase = get_prepositional_phrase(q)
    print(f"{cap_word} {noun} {verb} {prep_phrase}.")

    name = "e"
    q = 2
    t = "present"
    determiner = get_determiner(q)
    noun = get_noun(q)
    verb = get_verb(q, t)
    cap_word = determiner.capitalize()
    prep_phrase = get_prepositional_phrase(q)
    print(f"{cap_word} {noun} {verb} {prep_phrase}.")

    name = "f"
    q = 2
    t = "future"
    determiner = get_determiner(q)
    noun = get_noun(q)
    verb = get_verb(q, t)
    cap_word = determiner.capitalize()
    prep_phrase = get_prepositional_phrase(q)
    print(f"{cap_word} {noun} {verb} {prep_phrase}.")

def get_determiner(quantity):
        if quantity == 1:
            words = ["a", "one", "the"]
        else:
            words = ["some", "many", "the"]
        word = random.choice(words)
        return word

def get_noun(quantity):
        if quantity == 1:
            nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
        else:
            nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
        noun = random.choice(nouns)
        return noun

def get_verb(quantity, tense):
        if tense == "past":
            verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
        elif tense == "present" and quantity == 1:
            verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        elif tense == "present":
            verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
        elif tense == "future":
            verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
        verb = random.choice(verbs)
        return verb

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    phrase = f"{preposition} {determiner} {noun}"
    return phrase

main()