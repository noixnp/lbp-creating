# -*- coding: utf-8 -*-
import os
import glob
from skimage import io

 # 2点(x1,y1),(x2,y2)を通る矩形部分を切り抜き
def clip_image(in_filename):
  image = open(in_filename, 'r')
  print(in_filename)
  img = io.imread(in_filename)
  height, width = img.shape
  #  clp = img[y1:y2, x1:x2]

  #aquare
  clp = img[0:height/2, 0:width/2]
  io.imsave('./output/clip/' + "tl_" + path + ".bmp", clp)

  clp = img[0:height/2, width/2:width]
  io.imsave('./output/clip/' + "tr_" + path + ".bmp", clp)

  clp = img[height/2:height, 0:width/2]
  io.imsave('./output/clip/' + "ul_" + path + ".bmp", clp)

  clp = img[height/2:height, width/2:width]
  io.imsave('./output/clip/' + "ur_" + path + ".bmp", clp)

  #border
  clp = img[0:height/4, 0:width]
  io.imsave('./output/clip/' + "b1_" + path + ".bmp", clp)

  clp = img[height/4:height/2, 0:width]
  io.imsave('./output/clip/' + "b2_" + path + ".bmp", clp)

  clp = img[height/2:3*height/4, 0:width]
  io.imsave('./output/clip/' + "b3_" + path + ".bmp", clp)

  clp = img[3*height/4:height, 0:width]
  io.imsave('./output/clip/' + "b4_" + path + ".bmp", clp)

  #line
  clp = img[0:height, 0:width / 4]
  io.imsave('./output/clip/' + "l1_" + path + ".bmp", clp)

  clp = img[0:height, width / 4:width / 2]
  io.imsave('./output/clip/' + "l2_" + path + ".bmp", clp)

  clp = img[0:height, width / 2:3*width / 4]
  io.imsave('./output/clip/' + "l3_" + path + ".bmp", clp)

  clp = img[0:height, 3*width / 4:width]
  io.imsave('./output/clip/' + "l4_" + path + ".bmp", clp)

  image.close()

#main
directory = os.getcwd()
for filename in glob.glob(directory + '/input/*'):
  path, _ = os.path.splitext(os.path.basename(filename))
  clip_image(filename,)
  # os.remove(filename)