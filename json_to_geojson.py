"""
Tool for converting a JSON out from the LLM to GeoJSON
"""
import json
from geojson import Point, Polygon, Feature
import os
from pathlib import Path

def dms2dd(degrees, minutes, seconds):
    #print(seconds)
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    #if direction == 'E' or direction == 'S':
    #    dd *= -1
    return dd

def decode_coords(coord):
    """
    Decode the NOTAM coordinates notation to decimal degrees format
    """
    degrees = 0
    minutes = 0
    seconds = 0
    length_coord = 0

    if "." in coord:
        splits = coord.split(".")
        length_coord = len(splits[0])
    else:
        length_coord = len(coord[0:-1])    

    just_numbers = coord[0:-1]

    if length_coord == 6:
        degrees = just_numbers[0:2]
        minutes = just_numbers[2:4]
        seconds = just_numbers[4:]
    elif length_coord == 7:
        degrees = just_numbers[0:3]
        minutes = just_numbers[3:5]
        seconds = just_numbers[5:]
    
    return dms2dd(degrees, minutes, seconds)
    

def get_properties(json_obj):
    """
    Get Properties from the json_obj for populating the GeoJSON object.
    """
    keys = ["Location_Names", "Coordinates"]
    r = {}
    for k in json_obj:
        if k not in keys:
            r[k] = json_obj[k]
    
    return r

def get_filepath(j_obj, dest_dir):
    """
    Get the output filename for the GeoJSON file
    """
    notam = j_obj["NOTAM Number"]
    notam = notam.replace("/","_")
    return os.path.join(dest_dir, notam+".geojson")

def create_polygon(decode_coords, get_properties, get_filepath, j):
    coords = [ [decode_coords(c["Longitude"]), decode_coords(c["Latitude"])] for c in j["Coordinates"] ]
    c1 = coords[0]
    coords.append(c1)
                    #coords = coords.append(coords[0])
                    #print(coords)
    p = Polygon([coords])
                    #print(p.is_valid)
                    #print(p.errors())
    f = Feature(geometry=p, properties=get_properties(j))
                    #print(f)                
    Path(get_filepath(j, "./output")).write_text(str(f), encoding="utf8")

def create_point(decode_coords, get_properties, get_filepath, j, coordinates):
    point = [decode_coords(coordinates["Longitude"]), decode_coords(coordinates["Latitude"])]
    p = Point(point)
    f = Feature(geometry=p, properties=get_properties(j))
                #print(f)                
    Path(get_filepath(j, "./output")).write_text(str(f), encoding="utf8")

if __name__ == "__main__":
    filename = "notam12.json"

    with open(filename, encoding="utf8") as f:
        json_obj = json.load(f)
        for j in json_obj:
            #print(j)

            coordinates = j["Coordinates"]

            if type(coordinates) == list:
                if len(coordinates) > 2:
                    #3 points and above we create a Polygon Feature

                    create_polygon(decode_coords, get_properties, get_filepath, j)                
                elif len(coordinates) ==1:                    
                    # Only one point we create a Point Feature

                    create_point(decode_coords, get_properties, get_filepath, j, coordinates[0])
                else:
                    print("Error - "+str(j))
            elif type(coordinates) == dict:
                create_point(decode_coords, get_properties, get_filepath, j, coordinates)

