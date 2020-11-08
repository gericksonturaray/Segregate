'''
title           : Segregate.py
description     : Implementation of Index of Dissimilarity and Schelling Model
author          : Gerickson Turaray
date_created    : 08112020
date_modified   : 08112020
version         : 1.0
python_version  : 3.9

REFERENCE:
https://en.wikipedia.org/wiki/Index_of_dissimilarity
http://nifty.stanford.edu/2014/mccown-schelling-model-segregation/
http://adilmoujahid.com/posts/2020/05/streamlit-python-schelling/
'''

import os
import random


class Segregation:
    def __init__(self):
        self.table = []
        self.sub_tables = []
        self.IoD = 0
        self.threshold = 0
        self.is_segregated = True
        self.clear_data()

    # Populate data using LIST input
    def load_list_data(self, data, col):
        if col == 0:
            col = len(data[0])

        for inner_list in data:
            if col != len(inner_list):
                self.table = []
                print("Failed to load data: {}".format(data))
                return
            self.table.append(inner_list)

    # Populate data using STRING input
    def load_string_data(self, data, col):
        if col == 0 or len(data) % col != 0:
            print("Failed to load data: {}".format(data))
            return

        start = 0
        end = col
        length = len(data)

        while start != length:
            temp = []
            temp[:0] = data[start:end]
            self.table.append(temp)
            start = end
            end += col

    # MAIN load_data function
    def load_data(self, data, col=0):
        # load fail when data is empty
        if not data:
            print("Failed to load data: {}".format(data))
            return

        # check for input type
        # separate function for readability purposes
        if type(data) == list:
            self.load_list_data(data, col)
        elif type(data) == str:
            self.load_string_data(data, col)

    # get sub table in table using 2 points
    def add_sub_table(self, point1, point2):
        if not self.table:
            print("Failed to create sub table: missing data table")
            return

        # same X or Y axis for both point forms a LINE
        # if point1[0] == point2[0] or point1[1] == point2[1]:
        #     print("Failed to create sub table: point1 {}, point2 {}".format(point1, point2))
        #     return

        # use min and max to not limit the input to the values of point1 and point2
        # point1 can be (0,0) and point2 can be (2,2)
        # point1 can be (2,2) and point1 can be (0,0)
        sub_table = []
        for y in range(min(point1[1], point2[1]), max(point1[1], point2[1]) + 1):
            temp = []
            for x in range(min(point1[0], point2[0]), max(point1[0], point2[0]) + 1):
                temp.append(self.table[y][x])
            sub_table.append(temp)

        # list of sub_tables
        self.sub_tables.append(sub_table)

    def normalize_list(self, vector, count):
        normalize = []
        for x in vector:
            normalize.append((1 / count) * x)
        return normalize

    def compute_index_of_dissimilarity(self, list_1, list_2):
        # list1 - list2
        total = 0
        for index in range(len(list_1)):
            total += (abs(list_1[index] - list_2[index]))
        return total / 2

    # MAIN index of dissimilarity function
    def get_index_of_dissimilarity(self):
        if not self.sub_tables:
            print("Failed to compute: missing sub tables")
            return

        # count x and o occurrence in sub_tables
        count_x = 0
        count_o = 0
        list_x = []
        list_o = []

        for sub_table in self.sub_tables:
            for line in sub_table:
                x = sum(my_list.count('x') for my_list in line)
                o = sum(my_list.count('o') for my_list in line)

                # list of sum of x and o for each sub_table in sub_tables
                list_x.append(x)
                list_o.append(o)

                # total number of x and o in sub_tables
                count_x += x
                count_o += o

        # need 2 groups 'x' and 'o' to compute index of dissimilarity
        if count_x == 0 or count_o == 0:
            print("Failed to compute: only 1 group is present")
            return

        # compute the index using the normalize list
        return self.compute_index_of_dissimilarity(self.normalize_list(list_x, count_x), self.normalize_list(list_o, count_o))

    # set threshold for SCHELLING MODEL use
    def set_threshold(self, threshold):
        self.threshold = threshold

    # get list of adjacent node
    def get_adjacent_XY(self, t, x, y):
        length_x = len(t[0]) -1
        length_y = len(t) - 1
        location = [(y2, x2) for x2 in range(x - 1, x + 2)
                    for y2 in range(y - 1, y + 2)
                    if (-1 < x <= length_x and
                    -1 < y <= length_y and
                    (x != x2 or y != y2) and
                    (0 <= x2 <= length_x) and
                    (0 <= y2 <= length_y))]

        my_list = []
        for x, y in location:
            my_list.append(t[x][y])
        return my_list

    def is_happy(self, t, x, y):
        node_value = t[y][x]
        # condition for empty node
        if node_value == ' ':
            return True

        # create list of all adjacent node
        list_of_adjacent = self.get_adjacent_XY(t, x, y)
        # count all 'x' and 'x' in list of adjacent node
        count_x = sum(my_list.count('x') for my_list in list_of_adjacent)
        count_o = sum(my_list.count('o') for my_list in list_of_adjacent)

        if count_x == 0 and count_o == 0:
            return False

        # check if HAPPY
        # self.threshold -> % set by user. criteria for node to be happy
        # (count_x / count_x + count_y) * 100 -> calculate happiness %
        # will return TRUE if calculated happiness >= than threshold
        if node_value == 'x':
            return ((count_x / (count_x+count_o))*100) >= self.threshold
        elif node_value == 'o':
            return ((count_o / (count_x+count_o)) * 100) >= self.threshold

        return False

    # get x, y with empty value for new location
    def random_empty_location(self, t):
        empty_spot = [(i_y, i_x) for i_x, row in enumerate(t) for i_y, val in enumerate(row) if val == ' ']
        r = random.randint(0, len(empty_spot) - 1)
        return empty_spot[r][0], empty_spot[r][1]

    # move node location until condition is satisfied
    def update_node(self, t, x, y):
        node_value = t[y][x]
        if node_value != ' ':
            while not self.is_happy(t, x, y):
                self.is_segregated = False
                past_x = x
                past_y = y
                x, y = self.random_empty_location(t)
                t[y][x] = node_value
                t[past_y][past_x] = ' '

    # MAIN schelling model function
    def run_schelling_model(self, threshold=None):
        if threshold:
            self.set_threshold(threshold)

        # counter how many loop to get the segregated data
        count = 0
        for sub_table in self.sub_tables:
            while True:
                self.is_segregated = True

                # loop through table
                for index_y in range(len(sub_table)):
                    for index_x in range(len(sub_table[index_y])):
                        self.update_node(sub_table, index_x, index_y)
                if self.is_segregated:
                    break
                count +=1

        return self.sub_tables

    # reset tables in sub_tables
    def clear_sub_tables(self):
        self.sub_tables = []

    # reset data
    def clear_data(self):
        self.table = []
        self.clear_sub_tables()


s = Segregation()


def show_menu():
    print()
    print("*"* 50)
    print("X - EXIT")
    print("L - LOAD DATA - DIR/FILE or STRING")
    print("T - ENTER 2 POINTS FOR SUB TABLE")
    print("V - VIEW TABLE")
    print("C - CLEAR")
    print("I - INDEX OF DISSIMILARIRY")
    print("S - SCHELLING MODEL")
    print("*" * 50)


def beautify_tables(table):
    for l1 in table:
        for l2 in l1:
            print(''.join(l2))


def load_data():
    data = input("Enter filename or string: ")
    if os.path.isfile(data):
        my_list = []
        with open(data) as f:
            line = f.readline()
            while line:
                sub_list = []
                for c in line:
                    if c != '\n':
                        sub_list.append(c)
                my_list.append(sub_list)
                line = f.readline()
        s.load_data(my_list)
    else:
        col = int(input("How many characters per line: "))
        s.load_data(dir, col)
    print("Data is Loaded!")


def view_table():
    print("Main Table")
    if s.table:
        for l in s.table:
            print(''.join(l))
    else:
        print("Main Table is empty, please load data")

    print("Sub Table")
    if s.sub_tables:
        beautify_tables(s.sub_tables)
    else:
        print("Sub Table is empty, please add sub tables")


def create_sub_table():
    print("Set x and y of 1st point")
    x = int(input("Point 1 X-axis: "))
    y = int(input("Point 1 Y-axis: "))
    p1 = (x, y)

    print("Set x and y of 2nd point")
    x = int(input("Point 2 X-axis: "))
    y = int(input("Point 2 Y-axis: "))
    p2 = (x, y)

    s.add_sub_table(p1, p2)
    print("Sub table is created!")


def schelling_model():
    ratio = int(input("Threshold (1-100): "))
    print("Schelling Model New Table")
    beautify_tables(s.run_schelling_model(ratio))


def main():
    command = ''
    while command != 'X':
        show_menu()
        command = input("Command: ").upper()
        if command == 'L':
            load_data()
        elif command == 'T':
            create_sub_table()
        elif command == 'V':
            view_table()
        elif command == 'C':
            s.clear_data()
        elif command == 'I':
            print("Index of Dissimilarity using the sub table data is : {}".format(s.get_index_of_dissimilarity()))
        elif command == 'S':
            schelling_model()


if __name__ == "__main__":
    main()
