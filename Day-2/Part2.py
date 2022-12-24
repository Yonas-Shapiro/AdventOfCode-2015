with open("Day-2\input.txt", 'r') as q:
    boxes = q.read().strip().split("\n")
    q.close()


# Ribbon Calculations
def ribbonCalculations(dimensions):
    # Getting the length, width, and height
    l, w, h = (int(val) for val in dimensions.split("x"))

    # Sorting the side lengths by length to determine how much ribbon is needed
    ordered = [l,w,h]
    ordered.sort()

    # Calculating and returning the appropriate values of ribbon length
    add = ordered[0]*2
    add += ordered[1]*2
    add += l*w*h
    return add


ribbon = 0


for box in boxes:
    ribbon += ribbonCalculations(box)

print(ribbon, "feet of ribbon need to be ordered.")