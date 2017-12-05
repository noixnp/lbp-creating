# -*- coding: utf-8 -*-
import os
import glob
import numpy as np
import skimage
from skimage import io
from skimage.color import rgb2gray
from skimage.feature import local_binary_pattern

#LBP変換のポイント数，半径，メソッド（ここでパラメータ変更する）
radius = 3
point = 8 * radius
method = "default"

# in_filename の中身をLBP変換して、out_filename に出力する。
def convert_file(in_filename, out_filename):
  fin = open(in_filename, 'r')
  # LBP変換
  print(in_filename)
  image = io.imread(in_filename)
  # image = rgb2gray(image)
  lbp = local_binary_pattern(image, point, radius, method = method)
  lbpmin = lbp.min()
  lbpmax = lbp.max()
  lbpnorm = (lbp - lbpmin).astype(float) / (lbpmax - lbpmin).astype(float) #正規化

  io.imsave(out_filename,lbpnorm)
  fin.close()

#main
directory = os.getcwd()
for filename in glob.glob(directory + '/input/*'):
  path, _ = os.path.splitext(os.path.basename(filename))
  # convert_file(filename, './output/' + path +".jpg")
  convert_file(filename, './output/' + path + "_lbp_" + str(point) + "_" + str(radius) + "_" + method + ".bmp")
  # os.remove(filename)


#以下dumpcode
#image = io.imread('Lenna.png')
#gray = rgb2gray(image)
#lbp = local_binary_pattern(gray, 24, 3, method='default')

#print("gray =")
#print(gray)
#print("lbp =")
#print(lbp)
#print(gray.dtype, lbp.dtype)
#lbpmin = lbp.min()
#lbpmax = lbp.max()
#lbpnorm = (lbp - lbpmin).astype(float) / (lbpmax - lbpmin).astype(float)
#print("lbp2 =")
#print(lbpnorm)


#io.imsave('Lennalbp.png',lbpnorm)


