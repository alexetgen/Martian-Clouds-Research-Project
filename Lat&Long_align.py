# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 12:41:07 2020

@author: Alex Etgen
"""

import matplotlib.pyplot as plt

ax = plt.gca()

#for red
#x is longitude, y is latitude
y = [-24.2216,-24.2179,-24.2139,-24.0082,
                                     -23.6279,-23.2463,-22.8642,-22.4958,
                                     -22.1269,-21.7573,-21.3872,-21.0172,
                                     -20.6466,-20.2755,-19.9039,-19.5319,
                                     -19.1592,-18.7908,-18.4318,-18.0724,
                                     -17.7124,-17.3512,-16.9855,-16.6332,
                                     -16.208,-15.8456,-15.4579,-15.0852,
                                     -14.7492,-14.358,-14.0286,-13.6699,
                                     -13.3063,-12.761,-12.2154,-11.851,
                                     -11.4866,-11.1221,-10.7575,-10.3937,
                                     -9.83221,-9.26201,-8.88182,-8.50102,
                                     -8.12059,-7.55008,-7.16968,-6.59962,
                                     -6.21943,-5.83135,-5.57569,-5.57551,
                                     -5.77298,-6.16368,-6.54433,-6.92408,
                                     -7.49446,-7.87481,-8.25562,-8.63584,
                                     -9.01729,-9.39899,-9.77978,-10.1579,
                                     -10.7061,-11.0714,-11.4352,-11.8002,
                                     -12.164,-12.5276,-12.8914,-13.2556,
                                     -13.6204,-13.9795,-14.3119,-14.6731,
                                     -14.8723,-15.2181,-15.776,-16.1528,
                                     -16.5867,-16.947,-17.4851,-17.8469,
                                     -18.2064,-18.7455,-19.2987,-19.6716,
                                     -20.0439,-20.416,-20.7877,-21.3427,
                                     -21.713,-22.0827,-22.4522,-22.8208,
                                     -23.3925,-23.7738,-24.1545,-24.2216]
x = [306.569,306.194,305.901,305.756,
                                     305.765,305.773,305.78,305.788,305.795,
                                     305.801,305.807,305.814,305.82,305.826,
                                     305.831,305.836,305.841,305.846,305.85,
                                     305.854,305.858,305.861,305.863,305.869
                                     ,305.872,305.874,305.868,305.866,
                                     305.878,305.869,305.883,305.886,305.887
                                     ,305.888,305.89,305.89,305.89,305.89,
                                     305.89,305.89,305.889,305.887,305.886,
                                     305.884,305.883,305.88,305.878,305.875,
                                     305.873,305.87,306.141,306.518,306.879,
                                     306.877,306.875,306.874,306.871,306.869
                                     ,306.868,306.866,306.864,306.862,
                                     306.861,306.859,306.857,306.856,306.856
                                     ,306.854,306.854,306.853,306.852,
                                     306.852,306.85,306.851,306.862,306.862,
                                     306.855,306.861,306.855,306.849,306.845
                                     ,306.845,306.846,306.845,306.845,
                                     306.845,306.845,306.845,306.845,306.845
                                     ,306.845,306.846,306.846,306.846,
                                     306.846,306.847,306.847,306.847,306.848
                                     ,306.569]

#for blue
y1 = [-24.1464,-24.1441,-24.1406,-23.9395,
                                     -23.5665,-23.1931,-22.8195,-22.4456,
                                     -22.0713,-21.6968,-21.3222,-20.9474,
                                     -20.5723,-20.197,-19.8263,-19.4651,
                                     -19.1037,-18.7422,-18.3806,-17.8379,
                                     -17.476,-17.2298,-16.8679,-16.5077,
                                     -16.1453,-15.7828,-15.4144,-14.8754,
                                     -14.3242,-13.9707,-13.4273,-13.0649,
                                     -12.5215,-11.9783,-11.6162,-11.2542,
                                     -10.6933,-10.1289,-9.75244,-9.37651,
                                     -8.81291,-8.4373,-8.062,-7.68693,
                                     -7.31211,-6.92973,-6.54109,-6.15266,
                                     -5.76448,-5.52576,-5.52578,-5.52571,
                                     -5.52619,-5.91443,-6.3029,-6.69153,
                                     -7.26997,-7.64495,-8.02014,-8.39558,
                                     -8.77118,-9.33547,-9.71168,-10.276,
                                     -10.6524,-11.2154,-11.5774,-11.9397,
                                     -12.3018,-12.6642,-13.0266,-13.3893,
                                     -13.9332,-14.2879,-14.6496,-15.1943,
                                     -15.5563,-15.9256,-16.2897,-16.834,
                                     -17.1964,-17.4408,-17.9838,-18.3458,
                                     -18.7077,-19.0695,-19.4311,-19.7926,
                                     -20.162,-20.5377,-20.9131,-21.2881,
                                     -21.6631,-22.0379,-22.4124,-22.7867,
                                     -23.1607,-23.5345,-23.9079,-24.1464]
x1 = [306.654,306.397,306.07,305.771,305.778
                                     ,305.786,305.793,305.8,305.807,305.813,
                                     305.819,305.825,305.831,305.836,305.841
                                     ,305.846,305.85,305.854,305.858,305.864
                                     ,305.867,305.867,305.87,305.876,305.878
                                     ,305.88,305.873,305.883,305.874,305.888
                                     ,305.89,305.891,305.892,305.892,305.892
                                     ,305.892,305.892,305.891,305.889,
                                     305.888,305.886,305.884,305.882,305.88,
                                     305.878,305.876,305.873,305.871,305.868
                                     ,306.008,306.236,306.579,306.887,
                                     306.884,306.882,306.88,306.877,306.875,
                                     306.873,306.871,306.869,306.866,306.864
                                     ,306.861,306.86,306.857,306.856,306.855
                                     ,306.854,306.853,306.852,306.851,
                                     306.849,306.86,306.861,306.859,306.859,
                                     306.847,306.844,306.842,306.842,306.842
                                     ,306.841,306.841,306.84,306.84,306.84,
                                     306.839,306.839,306.839,306.838,306.838
                                     ,306.838,306.838,306.838,306.838,
                                     306.838,306.837,306.837,306.654]

#for green
y2 = [-24.1077,-24.1045,-24.0997,-23.7241,
                                     -23.3482,-22.9723,-22.5961,-22.2199,
                                     -21.8435,-21.4671,-21.0905,-20.7137,
                                     -20.3424,-19.7989,-19.2553,-18.8928,
                                     -18.5304,-17.9868,-17.5608,-17.1995,
                                     -16.8371,-16.4736,-16.1115,-15.7495,
                                     -15.392,-15.0297,-14.4886,-14.1248,
                                     -13.579,-13.2177,-12.8566,-12.4957,
                                     -12.1349,-11.7743,-11.2152,-10.8408,
                                     -10.4666,-10.0929,-9.71957,-9.34632,
                                     -8.97339,-8.6008,-8.22849,-7.85654,
                                     -7.47652,-7.09098,-6.70578,-6.32103,
                                     -5.93671,-5.5529,-5.49677,-5.4971,
                                     -5.49797,-5.88182,-6.26617,-6.65102,
                                     -7.03633,-7.42202,-7.80423,-8.17626,
                                     -8.54871,-8.92136,-9.29416,-9.66739,
                                     -10.041,-10.4151,-10.7892,-11.1637,
                                     -11.7252,-12.086,-12.447,-12.8081,
                                     -13.1693,-13.5306,-13.8921,-14.2586,
                                     -14.6216,-15.164,-15.5267,-15.8854,
                                     -16.2462,-16.789,-17.3328,-17.6956,
                                     -18.3032,-18.6659,-19.0286,-19.3912,
                                     -19.9352,-20.479,-21.0443,-21.4212,
                                     -21.7981,-22.1748,-22.5514,-22.9278,
                                     -23.3041,-23.6803,-24.0564,-24.1077]
x2 = [306.563,306.248,305.769,305.777,
                                     305.785,305.792,305.799,305.805,305.811
                                     ,305.817,305.823,305.829,305.834,
                                     305.841,305.848,305.852,305.856,305.862
                                     ,305.865,305.866,305.869,305.875,
                                     305.877,305.879,305.87,305.873,305.871,
                                     305.878,305.887,305.888,305.889,305.889
                                     ,305.889,305.889,305.889,305.889,
                                     305.888,305.887,305.885,305.884,305.882
                                     ,305.88,305.879,305.876,305.874,305.872
                                     ,305.869,305.866,305.863,305.86,306.176
                                     ,306.618,306.891,306.888,306.886,
                                     306.883,306.881,306.879,306.877,306.875
                                     ,306.873,306.87,306.868,306.866,306.864
                                     ,306.862,306.86,306.859,306.857,306.856
                                     ,306.855,306.853,306.852,306.851,
                                     306.849,306.859,306.861,306.858,306.858
                                     ,306.849,306.845,306.841,306.84,306.84,
                                     306.839,306.839,306.838,306.837,306.837
                                     ,306.836,306.835,306.835,306.835,
                                     306.834,306.834,306.834,306.833,306.833
                                     ,306.833,306.563]


plt.plot(x,y,'r-')
plt.plot(x1,y1,'b-')
plt.plot(x2,y2, 'g-')

plt.show()