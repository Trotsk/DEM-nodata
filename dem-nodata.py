"""
Reads elevation models, finds nodata values in interior tiles

Requires Python 3.x

If you're getting a ModuleNotFound error, you're probably missing
GDAL and rasterio. Navigate to G:\software_and_licenses\python
and pip install

"""

import os
from glob import glob
import rasterio


def log(tile):
    with open('report.txt', 'a') as log_file:
        log_file.write(tile + '\n')

# script will loop through filenames with these extensions
ext = glob('*.tif')
ext.extend(glob('*.img'))
ext.extend(glob('*.asc'))

os.getcwd()
for tile in list(ext):
    with rasterio.open(tile) as raster:
        if raster.nodata is None:
            print('nodata value not assigned')
            break
        # rudimentary way to discard border tiles, but it's quick
        elif raster.width != raster.height:
            continue
        else:
            # if your raster has more than one band, it's imagery not a DEM
            cell_val = raster.read(1)
            if raster.nodata in cell_val:
                print(tile + ' holds nodata value ' + str(raster.nodata))
                log(tile)
            else:
                continue

print('complete')