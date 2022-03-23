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


# ziskavanie suradnic z polygonu nakresleneho na mape
# https://codepen.io/jhawes/pen/xxBVZY

# arr = [[40.88536, -73.92709], [40.82255, -73.9673], [40.76683, -74.0082], [40.70862, -74.02717], [40.68595, -74.04399], [40.67784, -74.01653], [40.70222, -73.99069], [40.70438, -73.96747], [40.7454, -73.95312],
#        [40.77691, -73.92211], [40.78652, -73.92812], [40.7951, -73.92194], [40.80537, -73.92022], [40.80953, -73.93327], [40.82641, -73.93327], [40.83833, -73.93198], [40.8505, -73.92451], [40.86125, -73.9155], [40.87277, -73.90889]]
# for i in arr:
#     print('['+str(i[1])+', '+str(i[0])+'],')
