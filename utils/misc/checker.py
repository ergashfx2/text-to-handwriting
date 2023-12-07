async def compare(list1, list2):
    listfree = list()
    n = 0
    for a in list1:
        if a != list2[n]:
            listfree.append(n)
        else:
            pass
        n += 1
    return listfree
