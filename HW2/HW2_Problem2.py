#Sheila Robles
#Assignment 2 Problem 2
#Python Version 3.0.1

def world_initializer(width, height, initial_char=" "):
    if len(initial_char) >= 2 or type(initial_char) != str:
	    return("None")
    else:
	    game_world = []
	    for h in range(height):
		    game_world.append([])
		    for w in range(width):
			    game_world[h].append(initial_char)
    return(game_world)

w = int(input("Width: "))
h = int(input("Height: "))
default_char = input("Initial Character: ")

game_world = world_initializer(w,h,default_char)
print(game_world)

