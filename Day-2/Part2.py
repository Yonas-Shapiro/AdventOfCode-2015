with open("Day-2\input.txt", 'r') as q:
    boxes = q.read().strip().split("\n")
    q.close()

def ribbonCalculations(dimensions):
    l, w, h = (int(val) for val in dimensions.split("x"))
    ordered = [l,w,h]
    ordered.sort()
    add = ordered[0]*2
    add += ordered[1]*2
    add += l*w*h
    return add


ribbon = 0


for box in boxes:
    ribbon += ribbonCalculations(box)

print(ribbon, "feet of ribbon need to be ordered.")