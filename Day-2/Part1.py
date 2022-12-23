with open("Day-2\input.txt", 'r') as q:
    boxes = q.read().strip().split("\n")
    q.close()

def paperCalculations(dimensions):
    l, w, h = (int(val) for val in dimensions.split("x"))
    lw = 2*l*w
    lh = 2*l*h
    wh = 2*w*h
    temp = [lw, lh, wh]
    temp.sort()
    smallest = int(temp[0]/2)
    add = lw+lh+wh+smallest
    return add


paper = 0

for box in boxes:
    paper += paperCalculations(box)

print(paper, "square feet of paper need to be ordered.")