# hacky script to split images into tiles
# created (literally) for printing image onto tiles ;-)
# uses wand, a wrapper for Image Magik
from wand.image import Image
import os
import math
import argparse

parser = argparse.ArgumentParser("tile_it")
parser.add_argument("filename", help="Input file to tile", type=str)
parser.add_argument('--horizontal', help="Number of horizontal tiles", nargs='?', type=int, default=3)
parser.add_argument(    '--vertical', help="Number of vertical tiles", nargs='?', type=int, default=3)
parser.add_argument('-f', '--format', help="Output format: jpg, tif, png, pdf", nargs='?', type=str, default="jpg")
args = parser.parse_args()
print(args.filename)
print(args.horizontal)
print(args.vertical)

tiles_horz = args.horizontal
tiles_vert = args.vertical

if not args.format in ["pdf", "tif", "png", "jpg"]:
    print("Opps: {} format not supported".format(args.format)) 
    exit

basename = os.path.basename(args.filename)

with Image(filename=args.filename) as img:
    img_width = img.width
    img_height = img.height
    print("Image is: width: {} height: {}".format(img_width, img_height))
    
    tile_width = math.floor(img_width / tiles_horz)
    tile_height = math.floor(img_height / tiles_vert)
    
    print("Tiles: {} wide by {} hight, each {} by {} pixels".format(tiles_horz, tiles_vert, tile_width, tile_height))
    
    for x in range(0, tiles_horz):
        for y in range(0, tiles_vert):
            with img[x*tile_width : (x*tile_width)+tile_width, 
                    y*tile_height : (y*tile_height)+tile_height] as cropped:
                # print(cropped.size)
                output_filename = "splits/{}_{}_{}.{}".format(basename, x, y, args.format)
                print(output_filename)
                cropped.save(filename=output_filename)
            