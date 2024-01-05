#!/usr/bin/python3
"""create the nigerian csv"""


from turtle import Turtle, Screen
import pandas


# screen = Screen()
# screen.screensize(750, 600)

# image = "./nigerian_map.gif"
# screen.addshape(image)

# turtle = Turtle(image)
# turtle.shapesize(stretch_len=0.5, stretch_wid=0.5)

states = ["Sokoto", "Katsina", "Kano", "Jigawa",
          "Yobe", "Gombe", "Kebbi", "Niger",
          "Kaduna", "Bauchi", "Adamawa", "Borno",
          "Kwara", "Abuja", "Plateau", "Taraba",
          "Oyo", "Ogun", "Kogi", "Benue",
          "Osun", "Ondo", "Edo", "Enugu",
          "Cross River", "Lagos", "Delta", "Imo",
          "Akwa Ibom", "Anambra", "Abia", "Ekiti",
          "Ebonyi", "Nasarawa", "Zamfara", "Bayelsa",
          "Rivers"]
x_axis = []
y_axis =[]

num = 0


# def add_to_list(x, y):
#     global num
#     x_axis.append(x)
#     y_axis.append(y)
#     print(states[num], x, y)
#     num += 1

# screen.onscreenclick(add_to_list)



# screen.mainloop()


with open("./cord.txt", 'r', encoding="utf-8") as my_file:
    for line in my_file.readlines():
        line = line.strip()
        line = line.split(' ')
        x_axis.append(line[0])
        y_axis.append(line[1])

print(len(states), len(x_axis), len(y_axis))

data = {
    "states": states,
    "x": x_axis,
    "y": y_axis
}

nigeria = pandas.DataFrame(data)

nigeria.to_csv("./Nigerian_states.csv")

