import arcade

LEFT_MARGIN = 90
BOTTOM_MARGIN = 90
COLUMN_SPACING = 20
ROW_SPACING = 20

arcade.open_window(350,350, "Bord")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for row in range(10):
    for column in range(10):
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN

        if (row+column)%2==0:
                arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.ORANGE, 45)

        else:
                arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.BLACK, 45)


arcade.finish_render()

arcade.run()