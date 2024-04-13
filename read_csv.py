"""Reads whole .csv file and creates profile from segments"""
from coor import Coordinate
import pandas as pd
import re

# read csv
data = pd.read_csv("data/siec_2.csv")

# single line in .csv
# MULTILINESTRING ((22.0968718274268 50.0491258065111,22.0968638409292 50.0491453290607))

# catch the coordinates
PATTERN = r"(?<=\(\()([^\[\]]*)(?=\)\))"
coor_str = data['WKT'][0]

print(coor_str)
# for wkt in data['WKT']:


result = re.search(PATTERN, coor_str)
if result:
    segment_as_list_2_coor = result.group().split(',')
    for cr in segment_as_list_2_coor:
        start_coor, end_coor = cr.split(' ')
        coor = Coordinate(start_coor, end_coor)

        print(f"start here: {start_coor}, {end_coor}")
        # print(segment_as_list_2_coor)
        # for start_coor, end_coor in segment_as_list_2_coor[0].split(' ')

    # latt_as_str, long_as_str = segment_as_list_2_coor[0].split(' ')

    # coor = Coordinate(latt_as_str, long_as_str)
    # print(coor)

else:
    print("Unsuccessful")


