#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    first = sentence[0]
    tup_tup = (len(sentence), first)
    return tup_tup
