import math
import matplotlib.path as mplPath
import numpy as np

manhattan_coords = [[-73.92709, 40.88536],
                    [-73.9673, 40.82255],
                    [-74.0082, 40.76683],
                    [-74.02717, 40.70862],
                    [-74.04399, 40.68595],
                    [-74.01653, 40.67784],
                    [-73.99069, 40.70222],
                    [-73.96747, 40.70438],
                    [-73.95312, 40.7454],
                    [-73.92211, 40.77691],
                    [-73.92812, 40.78652],
                    [-73.92194, 40.7951],
                    [-73.92022, 40.80537],
                    [-73.93327, 40.80953],
                    [-73.93327, 40.82641],
                    [-73.93198, 40.83833],
                    [-73.92451, 40.8505],
                    [-73.9155, 40.86125],
                    [-73.90889, 40.87277]]

# central_park_coords = [
#     [-73.96104, 40.80676],
#     [-73.99138, 40.76524],
#     [-73.97022, 40.75649],
#     [-73.93988, 40.79796]
# ]


def central_park_coords():
    return {"type": "Feature",
            "geometry": {
                "type": "MultiPolygon",
                "coordinates":
                [[[[-73.96104, 40.80676],
                   [-73.99138, 40.76524],
                   [-73.97022, 40.75649],
                   [-73.93988, 40.79796],
                   [-73.96104, 40.80676]]]]},
            "properties": {
                "address": "Central park",
                           "block": 999999
            }
            }


dataset_headers = ['BOROUGH',
                   'NEIGHBORHOOD',
                   'BUILDING CLASS CATEGORY',
                   'TAX CLASS AT PRESENT',
                   'BLOCK',
                   'LOT',
                   'EASE-MENT',
                   'BUILDING CLASS AT PRESENT'
                   'ADDRESS',
                   'APARTMENT NUMBER',
                   'ZIP CODE',
                   'RESIDENTIAL UNITS',
                   'COMMERCIAL UNITS',
                   'TOTAL UNITS',
                   'LAND SQUARE FEET',
                   'GROSS SQUARE FEET',
                   'YEAR BUILT',
                   'TAX CLASS AT TIME OF SALE',
                   'BUILDING CLASS AT TIME OF SALE',
                   'SALE PRICE',
                   'SALE DATE']


def is_point_located_in_polygon(point, coords=manhattan_coords):

    bbPath = mplPath.Path(np.array(coords))

    return bbPath.contains_point(point)


def remove_non_manhattan_neighbourhoods(geo_map):
    geo_map['features'] = [x for x in geo_map['features']
                           if is_point_located_in_polygon(x['geometry']['coordinates'][0][0][0])
                           and x['properties']['ntacode'] not in ['MN01', 'MN99', 'QN71', 'QN68', 'BK38']]

    return geo_map
