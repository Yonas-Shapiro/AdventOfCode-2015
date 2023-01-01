def test(lst, depth, input, checked = []):
    
    if depth == len(lst):
        input
    
    next = []
    result = []
    checked.append(-1)

    if depth == 0:
        depth += 1
        for i in range(len(lst)):
            next.append(0)
        for j in next:
            result += test(lst, depth, j, checked)
        result.sort()
        print(result[0])


    for i in range(len(lst)):
        if i in checked:
            continue
        checked[-1] = i
        next.append(input + lst[checked[-2][checked[-1]]])
    depth += 1
    for j in next:
        result += test(lst, depth, j, checked)
        return result






l1 = ["sdf", "qwe", "rty"]
l2 = []

l2 += l1
print(l2)