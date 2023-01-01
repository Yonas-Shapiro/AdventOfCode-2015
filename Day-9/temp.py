def temp(checked, lst, getRoutes, vals)
    global counter
        next = []
        if len(checked) == 0:
            for i in range(len(lst)):
                print("i", i)
                intChecked = []
                if i in checked:
                    continue
                intChecked.append(i)
                checked.append("...")
                next.append(0)
                print(i)
                for j in next:
                    nChecked, smallest = getRoutes(lst, intChecked, next)
        if nChecked == 6:
            return smallest
        if len(checked) != 0:
            for i in range(len(lst)):
                if i in checked:
                    continue
                for j in range(len(vals)):
                    next.append(lst[checked[-1]][j])
                    nChecked, smallest = getRoutes(lst, checked, next)
        return len(checked)
