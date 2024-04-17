import colorgram

colors = colorgram.extract('image.jpg', 10)
print(colors[1].rgb)

rgb_colors = []
for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    rgb_colors.append((red, green, blue))

print(rgb_colors)
color_list = [(211, 154, 98), (53, 107, 131), (242, 249, 246), (235, 240, 244), (177, 78, 33), (198, 142, 35),
              (116, 155, 171), (124, 79, 98)]
