# -------------------------------
# Name: Shivansh Vaid
# Assignment: PROJECT_SV.py
# -------------------------------

import pickle
from graphics import *
import sys
from math import radians, sin, cos, sqrt, asin

# Displays the choices and the corresponding functions to the user.
# Asks the user for their choice
def message():
    print("\n      Edmonton Transit System\n------------------------------------\n(1) Load shape IDs from GTFS file\n(2) Load shapes from GTFS file\n(3) Load stops from GTFS file\n\n(4) Print shape IDs for a route\n(5) Print points for a shape ID\n(6) Print stops for a location\n\n(7) Save shapes, shape IDs, and stops in a pickle\n(8) Load shapes, shape IDs and stops from a pickle\n\n(9) Display interactive map\n\n(0) Quit")
    
    command_prompt = int(input("\nEnter command: "))
    return command_prompt

# Main method
# Controls all the choices that the user inputs
def main():
    shape_dict = {}
    route_dict = {}
    stop_dict = {}
    while True:
        command_prompt = message()
        if command_prompt == 1:
            route_dict = load_shape_IDs(route_dict)
        elif command_prompt == 2:
            shape_dict = load_shape_points(shape_dict)
        elif command_prompt == 3:
            stop_dict = load_stops(stop_dict)
        elif command_prompt == 4:
            print_shape_IDs(route_dict)
        elif command_prompt == 5:
            print_points(shape_dict)
        elif command_prompt == 6:
            print_stops(stop_dict)
        elif command_prompt == 7:
            save_shapes(shape_dict, route_dict, stop_dict)
        elif command_prompt == 8:
            load_shapes()
        elif command_prompt == 9:
            display_map(shape_dict, route_dict, stop_dict)
        elif command_prompt == 0:
            break
        else:
            print("Invalid option")
            main()
            break

# Purpose: Loads the shape IDs for the routes from the ETS open data system
# Parameters: route_dict - the dictionary to store the data in
# Return: route_dict
def load_shape_IDs(route_dict):
    filename = input("\nEnter a file name [data/trips.txt]: ")   
    if filename == "":
        shape_ID_file = open("data/trips.txt", "r")
    else:
        shape_ID_file = open(filename, "r")
        try:
            shape_ID_file = open(filename, 'r')
        except FileNotFoundError:
            return None         
    content = shape_ID_file.readlines()[1:]
    route_dict = {}
    shape_ID_file.close()
    for line in content:
        line = line.rstrip('\n').split(',')
        if line[0] in route_dict:
            route_dict[line[0]].add(line[6])
        else:
            route_dict[line[0]] = {line[6]}     
    print("\nLoaded route shapes")
    return route_dict

# Purpose: Takes the dictionary of the routes and route shapes from
# 'load_shape_IDs()' and prints the specified shapes from the route entered
# by the user.
# Parameters: route_dict - the dictionary of routes and their shapes
# Return: None if the route in route_dict exists, but a blank line if it
# doesn't exist
def print_shape_IDs(route_dict):
    route_number = input("\nRoute? ")
    if route_number not in route_dict.keys():
        print("Shape IDs for", route_number + ":\n\t** NOT FOUND **")
    else:
        print("Shape IDs for", route_number + ":")
        for val in route_dict[route_number]:
            print("\t", val)

# Purpose: Loads the shape ids and the points from the file
# Parameters: shape_dict - the dictionary to store the data in
# Return: shape_dict
def load_shape_points(shape_dict):
    filename = input("\nEnter a file name [data/shapes.txt]: ")
    if filename == "":
        shape_ID_file = open("data/shapes.txt", "r")
    else:
        shape_ID_file = open(filename, "r")
        try:
            shape_ID_file = open(filename, "r")
        except FileNotFoundError:
            return None
    content = shape_ID_file.readlines()[1:]
    shape_lst = []
    shape_dict = {}
    shape_ID_file.close()
    for line in content:
        line = line.rstrip('\n').split(',')
        if line[0] in shape_dict:
            shape_lst.append((float(line[1]), float(line[2])))
            shape_dict[line[0]] = shape_lst
        else:
            shape_lst = []
            shape_dict[line[0]] = {(line[1], line[2])}
    print("\nLoaded shape IDs")
    return shape_dict

# Purpose: prints the shape ids and points
# Parameters: shape_dict - the dictionary to print
# Return: none
def print_points(shape_dict):
    shape_number = input("\nShape ID? ")
    if shape_number not in shape_dict.keys():
        print("Shape for no-shape-id:\n\t** NOT FOUND **")
    else:
        print("\nShape for", shape_number + ":")
        for val in shape_dict[shape_number]:
            print("\t", val)

#___________________________________________________________________________    

# Purpose: Loads the stops from the data file into a dictionary
# Parameters: stop_dict - the dictionary that contains the stops
# Return: stop_dict
def load_stops(stop_dict):
    filename = input("\nEnter a file name [data/stops.txt]: ")
    if filename == "":
        stop_file = open("data/stops.txt", "r")
    else:
        stop_file = open(filename, "r")
        try:
            stop_file = open(filename, "r")
        except FileNotFoundError:
            return None
    
    content = stop_file.readlines()[1:]
    stop_dict = {}
    stop_list = []
    stop_file.close()
    for line in content:
        line = line.rstrip('\n').split(',')
        if (float(line[4]), float(line[5])) in stop_dict:
            stop_list.append((line[0], line[2]))
            stop_dict[(float(line[4]), float(line[5]))] = stop_list
        else:
            stop_list = []
            stop_dict[(float(line[4]), float(line[5]))] = (line[0], line[2])
    print("\nLoaded stops")
    return stop_dict
main
# Purpose: Asks the user for the location in terms of latitude and
# longitude, and prints the 5 closest stops
# Parameters: stop_dict - the dictionary that contains the stops
# from which to get the location and print the stops
# Return: none
def print_stops(stop_dict): 
    stop_coords = input("\nLocation as 'lat,lon'? ").split(', ')
    stop_coords1 = (float(stop_coords[0]), float(stop_coords[1]))
    print(stop_coords1)
    print(stop_coords)
    if stop_coords1 not in stop_dict.keys():
        print("\nStops for " + str(stop_coords1) + ":\n\t** NOT FOUND **")
    else:
        print("\nStops for " + str(stop_coords1) + ":")
        for val in stop_dict[stop_coords1]:
            print("\t", val, end = "")
        print()

#___________________________________________________________________________    

# Purpose: saves the shape ids and points in a pickle
# Parameters: shape_dict - the data to write to the pickle
# Return: none
def save_shapes(shape_dict, route_dict, stop_dict):
    filename = input("Enter a file name [etsdata.p]: ")
    if filename == "":
        shape_ID_file = open("etsdata.p", "w")
    else:
        shape_ID_file = open(filename, "w")
    try:
        shape_ID_file = open(filename, "w")
    except FileNotFoundError:
        return None
    pickle.dump((shape_dict, route_dict, stop_dict), open(filename, 'w'))
    print("\nSaved shapes, points, and stops in a pickle")
    shape_ID_file.close()

# Purpose: Loads the shape ids and points from a pickle
# Parameters: none
# Return: none
def load_shapes():
    filename = input("Enter a file name [etsdata.p]: ")
    if filename == "":
        shape_ID_file = open("etsdata.p", "r")
    else:
        shape_ID_file = open(filename, "r")
    try:
        shape_ID_file = open(filename, "r")
    except FileNotFoundError:
        return None
    shape_dict, route_dict, stop_dict = pickle.load(filename)
    shape_ID_file.close()
    print("\nLoaded shapes, points, and stops from the pickle")
    return shape_dict, route_dict, stop_dict

# Purpose: Finds the shape id with the most points
# Parameters: shape_dict - the dictionary from which to get the longest
#             shapes - the set of shapes
# Return: the longest shape id
def get_longest(shape_dict, shapes):
    longest = []
    for shape in shapes:
        if len(shape_dict[shape]) > len(longest):
            longest = shape_dict[shape]
    return longest

# Purpose: Checks if the button is clicked
# Parameters: Button - the button to be clicked
#             pt - the point at which the user clicks
#             win - the graphics window
# Return: True if the button is clicked, False otherwise
def button_clicked(button, pt, win):
    x, y = win.toScreen(pt.x, pt.y)
    ul = button.getP1()
    lr = button.getP2()
    if ul.x <= x <= lr.x and ul.y <= y <= lr.y:
        return True
    else:
        return False

# Purpose: Displays a map of Edmonton with an entrybox to enter a route number
# and a button to generate the route map.
# Syntax: shape_dict - the dictionary of the shapes and the points
#         route_dict - the dictionary of the routes and the shapes
# Return: None
def display_map(shape_dict, route_dict, stop_dict):    
    win = GraphWin("Edmonton Transit System", 630, 768)
    route_entry = Entry(Point(80, 20), 10)
    route_entry.draw(win)
    yeg_map = Image(Point(315, 384), "background.gif")
    yeg_map.draw(win)
    button = Rectangle(Point(150, 10), Point(200, 30))
    button.setFill("white")
    button.draw(win) 
    button_text = Text(Point(175, 20), "Plot")
    button_text.draw(win)
    win.setCoords(-113.7136, 53.39576, -113.2714, 53.71605)
    dist_dict = {}
    dist_lst = []
    while True:
        try:
            point = win.getMouse()
        except GraphicsError:
            return None
        if button_clicked(button, point, win) == False:
            for key in stop_dict.keys():
                distance = round(haversine(point.y, point.x, key[0], key[1]) * 1000, 1)
                dist_lst.append([distance, key, stop_dict[key]])
            # learned next line of code from https://wiki.python.org/moin/HowTo/Sorting
            sorted_dist_lst = sorted(dist_lst, key = lambda x: x[0])
            for elem in sorted_dist_lst[:4]:
                dist_dict[elem[0]] = elem[2]
                points1 = Point(elem[1][0], elem[1][1])
                points1.draw(win)
            print("\nNearest stops:\n\tDistance\tStop\t    Description")
            for key in dist_dict:
                print("\t" + str(key) + "          " + str(dist_dict[key]).replace("'", "").replace(",", "      ").strip("()").replace('"', ""))
            sys.stdout.flush()
        if button_clicked(button, point, win) == False:
            print("\n\nGeographic (lat, lon): " + str((point.x, point.y)))
            point.x, point.y = win.toScreen(point.x, point.y)
            print("Pixel (x, y): " + str((point.x, point.y)) + "\n")
            sys.stdout.flush()  
        else:
            route = route_entry.getText()
            if route in route_dict.keys():
                shape = route_dict[route]
                coords = get_longest(shape_dict, shape)
                for i in range(1, len(coords)):
                    pt1 = coords[i - 1]
                    pt2 = coords[i]
                    lines = Line(Point(pt1[1], pt1[0]), Point(pt2[1], pt2[0]))
                    lines.setFill("gray50")
                    lines.setWidth(3)
                    lines.draw(win)
    
# Obtained from: https://rosettacode.org/wiki/Haversine_formula#Python
def haversine(lat1, lon1, lat2, lon2):
 
    R = 6372.8 # Earth radius in kilometers

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    
    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))
    
    return R * c

                    
