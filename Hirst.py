import random

import colorgram
import turtle as turtle_module
# rgb_colors=[]
# colors=colorgram.extract('hirst.jpg',30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)



turtle_module.colormode(255)
tim=turtle_module.Turtle()
color_list=[(233, 222, 92), (211, 158, 105), (116, 177, 210), (226, 57, 131), (181, 78, 33), (210, 135, 174), (41, 103, 161), (12, 21, 62), (184, 46, 111), (186, 164, 23), (43, 182, 112), (122, 187, 155), (25, 32, 158), (173, 16, 67), (234, 164, 199), (229, 75, 43), (22, 179, 205), (11, 41, 23), (49, 126, 73), (146, 218, 196), (51, 21, 11), (227, 220, 10), (106, 95, 206), (133, 215, 229), (175, 177, 227), (59, 16, 31)]

tim.penup()

tim.speed("fastest")
tim.setheading(125)
tim.fd(300)
tim.setheading(0)

for i in range(10):
    for x in range(10):
        tim.dot(20, random.choice(color_list))
        if x==9:
            break
        else:
            tim.fd(40)

    if i==9:
        break
    else:
        if i%2!=0:
            tim.lt(90)
            tim.fd(40)
            tim.lt(90)
        else:
            tim.rt(90)
            tim.fd(40)
            tim.rt(90)



screen=turtle_module.Screen()
screen.exitonclick()
