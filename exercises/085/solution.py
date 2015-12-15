def sort_a_list(l):
    num = len(l)-1
    temp = 0
    while num > 0:
        for i in range(num):
            if l[i] > l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
        num -= 1
    return(l)
        

def sort_by_mark(my_class):
    return sorted(my_class, reverse=True)


from operator import itemgetter


def sort_by_name(my_class):
    return sorted(my_class, key=itemgetter(1))
