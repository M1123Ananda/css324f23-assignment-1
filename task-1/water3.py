def initial_state():
    return (8, 0, 0)

def is_goal(s):
    # if s[0:2] == (4,4):
    #     return True
    # return False
    if s == (0,5,3):
        return True
    return False
    

def successors(s):
    a, b, c = s
    t = 8 - a
    if (b > 0 and t > 0): # check if cup "b" has water and a needs water ( t > 0 )
        if b > t:
            yield((a+t, b-t, c), t)
        else:
            yield((a+b, 0, c), b)

    if (c > 0 and t > 0): # check if cup "c" has water and a needs water ( t > 0 )
        if c > t:
            yield((a+t, b, c-t), t)
        else:
            yield((a+c, b, 0), b)

    t = 5-b
    if (a > 0 and t > 0): # check if cup "a" has water and b needs water ( t > 0 )
        if a > t:
            yield((a-t, b+t, c), t)
        else:
            yield((0, b+a, c), a)

    if (c > 0 and t > 0): # check if cup "c" has water and b needs water ( t > 0 )
        if c > t:
            yield((a, b+t, c-t), t)
        else:
            yield((a, b+c, 0), c)


    t = 3 - c # "c" cup need "t" amount of water
    if (a > 0 and t > 0): # check if cup "a" has water and c needs water ( t > 0 )
        if a > t:
            yield((a-t, b, c+t), t)
        else:
            yield((0, b, c+a), a)

    if (b > 0 and t > 0): # check if cup "b" has water and c needs water ( t > 0 )
        if b > t:
            yield((a, b-t, c+t), t)
        else:
            yield((a, 0, c+b), b)
    return []