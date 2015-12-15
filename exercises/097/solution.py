def love_meet(alice, bob):
    i = set(alice)
    j = set(bob)
    return(i & j)


def affair_meet(alice, bob, sylvester):
    i = set(alice)
    j = set(bob)
    k = set(sylvester)
    l = i & k
    m = l-j
    return(m)
