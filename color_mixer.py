# color_mixer.py
# Written by Elias Retzlaff

import webbrowser

import os

def read_color_table(table):

    infile = open('colors.txt')

    for line in infile:

        items = line.split()

        color_name = items[0]

        red = int(items[1])

        green = int(items[2])

        blue = int(items[3])

        table[color_name] = { 'r': red, 'g': green, 'b': blue }

color_table = {}

read_color_table(color_table)

def build_header_code(content):

    template = "<h1>{}</h1>"

    return template.format(content)

def build_color_code(rgb):

    template = "<p style='color:rgb({}, {}, {})'>Sample Color</p>"

    return template.format(rgb['r'], rgb['g'], rgb['b'])

def show_color(color):

    color = color.upper()

    color_values = color_table[color]

    render_color_code(color_values)

def render_color_code(color_dictionary):

    file_name = "color.html"

    outfile = open(file_name, "w")

    outfile.write(build_header_code('Color Display Demo'))

    outfile.write(build_color_code(color_dictionary))

    outfile.close()

    current_folder = os.getcwd()

    full_file_url = "file:" + current_folder + "/" + file_name

    webbrowser.open(full_file_url)

def blue_amount():

    color_x = input("Provide a color from colors.txt: ").upper()

    

    blue_amount_x = color_table[color_x]['b']

    print(f'Amount of blue in {color_x}:', blue_amount_x)

def color_splits():

    color_x = input("Provide a color from colors.txt: ").upper()

    

    red_x = color_table[color_x]['r']

    green_x = color_table[color_x]['g']

    blue_x = color_table[color_x]['b']

    print(f'Red in {color_x}:', red_x)

    print(f'Green in {color_x}:', green_x)

    print(f'Blue in {color_x}:', blue_x)

def num_colors():

    num_colors = len(color_table)

    print("Number of different colors that show_color can display:", num_colors)

def demo_color():

    color_input = input("Enter a color: ").upper()  

    if color_input in color_table:

        color_values = color_table[color_input] 

        print(f"Red: {color_values['r']}")

        print(f"Green: {color_values['g']}")

        print(f"Blue: {color_values['b']}")

        render_color_code(color_values) 

    else:

        print("Color not found in the color table.")

def demo_blend(color1, color2):

    color1 = color1.upper()

    color2 = color2.upper()

    if color1 in color_table and color2 in color_table:

        color1_values = color_table[color1]

        color2_values = color_table[color2]

        avg_red = (color1_values['r'] + color2_values['r']) // 2

        avg_green = (color1_values['g'] + color2_values['g']) // 2

        avg_blue = (color1_values['b'] + color2_values['b']) // 2

        print("Averages of blended color:")

        print(f"Red: {avg_red}")

        print(f"Green: {avg_green}")

        print(f"Blue: {avg_blue}")

        blended_color = {'r': avg_red, 'g': avg_green, 'b': avg_blue}

        render_color_code(blended_color)

    else:

        print("One or both colors not found in the color table.")

def render_color_code(color_dictionary):

    file_name = "color.html"

    outfile = open(file_name, "w")

    outfile.write(build_header_code('Color Display Demo'))

    outfile.write(build_color_code(color_dictionary))

    outfile.close()

    current_folder = os.getcwd()

    full_file_url = "file:" + current_folder + "/" + file_name

    webbrowser.open(full_file_url)
