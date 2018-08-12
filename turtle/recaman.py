import turtle

N = 10000
K = 2

turtle.setup(width=800, height=800)
#turtle.tracer(0, 0)
turtle.penup()
turtle.setpos(-325, -325)
turtle.pendown()
turtle.color('gray')
turtle.bgcolor('black')
turtle.right(45)

x = 0
is_down = True
seq = {0}
for dx in range(1, N+1):
    if (x-dx > 0) and (x-dx not in seq):
        dx = -dx

    if is_down:
        turtle.circle(dx*K, 180)
    else:
        turtle.circle(-dx*K, 180)

    is_down = not is_down

    x += dx
    seq.add(x)

#turtle.update()
turtle.exitonclick()
