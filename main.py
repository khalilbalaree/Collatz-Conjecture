import matplotlib.pyplot as plt
from tqdm import tqdm

def cal(x, tested, len_to_note):
    if x == 1:
        return 0, len_to_note
    
    for i in reversed(tested):
        if x == i:
            return i, len_to_note

    if x % 2 == 0:
        x /=2
    else:
        x = 3 * x + 1
    return cal(x, tested, len_to_note+1)

tries = 10000

nested_x = []
nested_y = []
tested = []
lens_to_note = []
for i in tqdm(range(1, tries)):
    nest_num, len_to_note = cal(i, tested, 0)
    tested.append(i)
    if nest_num != 0:
        nested_x.append(i)
        nested_y.append(nest_num)
        lens_to_note.append(len_to_note)

fig, axs = plt.subplots(2)
axs[0].plot(nested_x, nested_y, "o", ms=0.5, c="black")
axs[1].plot(nested_x, lens_to_note, "o", ms=0.5, c="blue")
plt.show()