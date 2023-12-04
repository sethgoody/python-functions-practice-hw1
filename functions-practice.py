def Hello():
    name="Seth"
    print("Hello, " + name)

Hello()

def pack(arg1, arg2, arg3):
    return[arg1, arg2, arg3]

pack("fruit1", "fruit2", "fruit3")

def eatLunch(lunchbox):

    noLunch = "My lunchbox is empty!"

    if len(lunchbox) == 0:
        print(noLunch)
    else:
        print("First I eat " + lunchbox[0])

        for item in lunchbox[1:]:
            print("Next I eat " + item)
    
    print(noLunch)


eatLunch(["apples", "sandwich", "granola bar"])
