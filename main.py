import time
import matplotlib.pyplot as plt

def cal(x, tested, is_reversd_nested):
    if x == 1:
        return 0
    
    if is_reversd_nested:
        for i in reversed(tested):
            if x == i:
                return i
    else:
        for i in tested:
            if x == i:
                return i

    if x % 2 == 0:
        x /=2
    else:
        x = 3 * x + 1
    return cal(x, tested, is_reversd_nested)

tries = 100

t = time.time()
nested_x = []
nested_y = []
tested = []
for i in range(1, tries):
    nest_num_from_high = cal(i, tested, True)
    nest_num_from_low = cal(i, tested, False)
    assert nest_num_from_high == nest_num_from_low
    tested.append(i)
    if nest_num_from_high != 0:
        nested_x.append(i)
        nested_y.append(nest_num_from_high)

print(time.time()-t)
plt.plot(nested_x, nested_y, "o", ms=1, c="black")
plt.show()