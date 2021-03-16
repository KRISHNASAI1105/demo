#!/usr/bin/env python
# -- coding: utf-8 --

import random
import math

sample_space = 100

blue = 0
white = 0
red = 0

#simulating the number of marbles picked from the box
for i in range(sample_space) :
  random_variable = random.randint(0,8)
  if random_variable <= 2 :
    blue+= 1
  elif random_variable <= 4 :
    white+= 1
  else :
    red+= 1

#stimulating the experimental prbability of marbles
print("\n No.of blue marbles picked= {}".format(blue))
print("\n No.of white marbles picked = {}".format(white))
print("\n No.of red marbles picked= {}".format(red))        
print("\n Experimental probability of picking blue = {}".format(blue/ sample_space, num = 3/9))
print("\n Experimental probability of picking white = {}".format(white/ sample_space, num = 2/9))
print("\n Experimental probability of picking red = {}".format(red/ sample_space, num = 4/9))
