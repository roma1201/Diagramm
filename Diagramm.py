from turtle import Turtle, Screen
from itertools import cycle


lst=['cpp', 'python', 'python', 'c++', 'c++', 'java']
n_list=set(lst)
unique_list=dict()
for lst_item in lst:
    unique_list[lst_item]=lst.count(lst_item)
print(unique_list)
res=dict()
for i in unique_list:
    res[i]=360/len(lst)*unique_list[i]    
print(res)
letter_frequencies = res.items()


COLORS = cycle(['yellow', 'green', 'red', 'blue'])

RADIUS = 175
LABEL_RADIUS = RADIUS * 1.33
FONTSIZE = 18
FONT = ("Ariel", FONTSIZE, "bold")


total = sum(fraction for _, fraction in letter_frequencies)

baker = Turtle()
baker.penup()
baker.sety(-RADIUS)
baker.pendown()

for _, fraction in letter_frequencies:
    baker.fillcolor(next(COLORS))
    baker.begin_fill()
    baker.circle(RADIUS, fraction * 360 / total)
    position = baker.position()
    baker.goto(0, 0)
    baker.end_fill()
    baker.setposition(position)


baker.penup()
baker.sety(-LABEL_RADIUS)

for label, fraction in letter_frequencies:
    baker.circle(LABEL_RADIUS, fraction * 360 / total / 2)
    baker.write(label, align="center", font=FONT)
    baker.circle(LABEL_RADIUS, fraction * 360 / total / 2)

baker.hideturtle()

screen = Screen()
screen.exitonclick()
