def love_meet(alice, bob):
    i = set(alice)
    j = set(bob)
    return(i & j)


def affair_meet(bob, alice, silvester):
    i = set(alice)
    j = set(bob)
    k = set(silvester)
    return((i & k)-j)
