import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_snowflake(order, size=300):
    """
    Малює повну сніжинку Коха з 3 кривих.
    :param order: рівень рекурсії
    :param size: довжина сторони сніжинки
    """
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)  # Початкова точка
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    t.hideturtle()
    screen.mainloop()

# --- Запуск ---
if __name__ == "__main__":
    try:
        order = int(input("Введіть рівень рекурсії (наприклад, 0–5): "))
        draw_snowflake(order)
    except ValueError:
        print("Будь ласка, введіть ціле число.")
