#0. Make a variable which holds the coordinates (hnit)
#1. Print out where user can travel
#2. Recive input from user
#2.1 If input is not acceptable write out "Not a valid direction!"
#3. Change coordinates according to input
#3.1 If coordinates are the winning coordinates then print out Victory! and stop trunning
#4. Repeat steps 1. to 3.
def tile_mover(input):
    if input == "N" or input == "n":
        return x, y + 1
    elif input == "S" or input == "s":
        return x, y - 1
    elif input == "E" or input == "e":
        return x + 1, y
    elif input == "W" or input == "w":
        return x -1, y
    
def start_tile():
    print("You can travel: (N)orth.")
    while True:
        ui = str(input("Direction: "))
        if ui == "n" or ui == 'N':
            x,y = tile_mover(ui)
            break
        else:
            print("Not a valid direction!")
    return x,y

def middle_left():
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    while True:
        ui = str(input("Direction: "))
        if ui == "n" or ui == 'N' or ui == "S" or ui == "s" or ui == "E" or ui == "e":
            x,y = tile_mover(ui)
            break
        else:
            print("Not a valid direction!")
    return x,y


def top_left():
    print("You can travel: (E)ast or (S)outh.")
    while True:
        ui = str(input("Direction: "))
        if ui == "S" or ui == "s" or ui == "E" or ui == "e":
            x,y = tile_mover(ui)
            break
        else:
            print("Not a valid direction!")
    return x,y

def middle_top():
    print("You can travel: (E)ast or (W)est.")
    while True:
        ui = str(input("Direction: "))
        if ui == "W" or ui == "w" or ui == "E" or ui == "e":
            x,y = tile_mover(ui)
            break
        else:
            print("Not a valid direction!")
    return x,y

def middle():
    print("You can travel: (S)outh or (W)est.")
    while True:
        ui = str(input("Direction: "))
        if ui == "W" or ui == "w" or ui == "S" or ui == "s":
            x,y = tile_mover(ui)
            break
        else:
            print("Not a valid direction!")
    return x,y

def middle_bottom():
    print("You can travel: (N)orth.")
    while True:
        ui = str(input("Direction: "))
        if ui == "N" or ui == "n":
            x,y = tile_mover(ui)
            break
        else:
            print("Not a valid direction!")
    return x,y


def top_right():
    print("You can travel: (S)outh or (W)est.")
    while True:
        ui = str(input("Direction: "))
        if ui == "S" or ui == "s" or ui == "W" or ui == "w":
            x,y = tile_mover(ui)
            break
        else:
            print("Not a valid direction!")
    return x,y

def middle_right():
    print("You can travel: (N)orth or (S)outh.")
    while True:
        ui = str(input("Direction: "))
        if ui == "S" or ui == "s" or ui == "N" or ui == "n":
            x,y = tile_mover(ui)
            break
        else:
            print("Not a valid direction!")
    return x,y

x,y = 1,1

while (x == 3 and y == 1) == False:
    if x == 1 and y == 1:
        x, y = start_tile()
    elif x == 1 and y == 2:
        x, y = middle_left()
    elif x == 1 and y == 3:
        x, y =top_left()
    elif x == 2 and y == 1:
        x, y = middle_bottom()
    elif x == 2 and y == 2:
        x, y = middle()
    elif x == 2 and y == 3:
        x, y = middle_top()
    elif x == 3 and y == 2:
        x, y = middle_right()
    elif x == 3 and y == 3:
        x, y = top_right()
print("Victory!")
