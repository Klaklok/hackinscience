def love_meet(alice, bob):
    i = set(alice)
    j = set(bob)
    return(i & j)


def affair_meet(alice, bob, silvester):
    i = set(alice)
    j = set(bob)
    k = set(silvester)
    l = i & k
    m = l-j
    return(m)
