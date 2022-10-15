# Importing Modules
import numpy as np
import random
# Use 'conda install shapely' to import the shapely library.
from shapely.geometry import Polygon, Point

# Sample Sub Region Polygons
# Sample Polygons created with https://www.keene.edu/campus/maps/tool/
ne1Poly = Polygon([(-69.0380859, 47.2792290),(-69.1809082, 47.4429500),(-69.5434570, 47.1747783),(-70.0158691, 46.6795945),(-70.6091309, 45.6063521),(-70.9057617, 45.3598653),(-71.3342285, 45.2748864),(-71.4990234, 45.0114186),(-73.1250000, 44.9647979),(-73.3227539, 42.7873385),(-71.9824219, 42.6985859),(-70.7189941, 42.5935326),(-70.7080078, 42.8115217),(-70.1806641, 43.4848121),(-69.3237305, 43.9611906),(-67.1484375, 44.6530242),(-67.4340820, 45.1820368),(-67.7416992, 45.7061793),(-67.9394531, 47.0701218),(-68.7304688, 47.2195681),(-69.0325928, 47.2792290)])
ne2Poly = Polygon([(-73.2458496, 45.0191851),(-73.2348633, 42.6985859),(-70.7080078, 42.6501218),(-70.5212402, 41.7958881),(-71.2353516, 41.4344903),(-72.9052734, 41.2447723),(-73.5205078, 41.0379306),(-73.7402344, 40.8636797),(-73.4545898, 40.9135126),(-72.2900391, 41.1124688),(-72.7954102, 40.7139558),(-74.2236328, 40.5137992),(-74.4213867, 41.2447723),(-75.1245117, 41.7713117),(-76.3110352, 42.0492926),(-79.7607422, 41.9839943),(-79.7497559, 42.2610492),(-79.0576172, 42.6985859),(-79.0905762, 43.2131833),(-78.8269043, 43.3331694),(-77.5744629, 43.2452027),(-76.8713379, 43.2932003),(-76.2890625, 43.5405848),(-76.3549805, 44.1270280),(-75.9100342, 44.3827658),(-74.8828125, 44.9803424),(-73.2513428, 45.0075350)])
ne3Poly = Polygon([(-80.1013184, 42.1226732),(-80.5078125, 41.9839943),(-80.5297852, 39.7240886),(-78.2666016, 39.7071867),(-77.3657227, 38.3847277),(-76.3659668, 38.0999826),(-76.5527344, 38.6168705),(-76.4099121, 39.1854332),(-76.2506104, 39.0874360),(-76.0253906, 38.4277735),(-75.4486084, 38.0567422),(-75.0695801, 38.7583669),(-75.3332520, 38.9935721),(-75.5474854, 39.4701251),(-75.0640869, 39.2620314),(-74.9542236, 39.1087514),(-74.9157715, 38.9252290),(-74.2456055, 39.6056882),(-74.1137695, 39.9939557),(-74.0698242, 40.4051307),(-74.2510986, 40.4678455),(-74.2456055, 40.5555479),(-74.2016602, 41.1579783),(-74.9652100, 41.4962353),(-75.3662109, 41.9921602),(-79.7497559, 42.0003251),(-79.7607422, 42.2610492),(-80.0793457, 42.1471145)])
se1Poly = Polygon([(-75.8056641, 36.5096362),(-76.9921875, 38.2036553),(-80.5078125, 39.7071867),(-80.5957031, 41.8859210),(-82.5073242, 41.3603187),(-84.8364258, 39.8254131),(-87.4511719, 36.6331621),(-81.1450195, 36.5272948),(-75.7617188, 36.4743068)])
se2Poly = Polygon([(-89.6484375, 36.4743068),(-75.9155273, 36.5096362),(-76.4208984, 35.3173663),(-78.0249023, 33.9068956),(-80.7495117, 31.9894418),(-90.9008789, 32.1570125),(-91.0986328, 33.4497766),(-90.5932617, 34.6332079),(-89.6264648, 36.4566360)])
se3Poly = Polygon([(-90.8569336, 32.3057060),(-85.2319336, 32.0080760),(-80.8374023, 31.8775576),(-81.4086914, 30.8456474),(-80.5737305, 28.4590330),(-80.0244141, 26.6474587),(-80.4199219, 25.2248202),(-80.9912109, 25.1651734),(-82.5512695, 27.2350946),(-82.9687500, 29.2097132),(-84.0454102, 30.0310554),(-85.1220703, 29.7262223),(-86.1767578, 30.2400864),(-87.2534180, 30.3539164),(-89.3847656, 30.3159877),(-89.7802734, 29.6689625),(-90.5053711, 29.4013195),(-93.8012695, 29.7643774),(-93.6035156, 31.0905741),(-94.0209961, 32.4356130),(-94.0649414, 32.9533681),(-91.0986328, 32.9533681),(-90.8349609, 32.3428414)])
c1Poly = Polygon([(-93.8232422, 29.7262223),(-93.9990234, 32.9533681),(-89.5825195, 36.1556178),(-90.2856445, 36.4743068),(-94.5483398, 36.4743068),(-94.7460938, 36.9850031),(-103.0297852, 36.8971945),(-103.0957031, 32.0639556),(-106.5893555, 31.9708039),(-103.1616211, 28.9023972),(-102.0849609, 29.8025179),(-100.6567383, 28.9793120),(-99.3603516, 26.9416595),(-97.3168945, 25.8592236),(-97.4047852, 27.5277582),(-96.5478516, 28.3624017),(-93.8452148, 29.7262223)])
c2Poly = Polygon([(-102.2167969, 36.9498918),(-94.6582031, 36.8444607),(-87.8027344, 37.6838203),(-84.6386719, 38.9594088),(-83.3203125, 41.6729118),(-84.3310547, 45.6447682),(-91.7138672, 46.7398606),(-92.6367188, 45.6754822),(-91.4062500, 43.4529189),(-96.5478516, 43.4529189),(-94.8559570, 39.9097362),(-101.9531250, 39.9939557),(-102.1508789, 37.0025527)])
c3Poly = Polygon([(-103.6230469, 40.9798981),(-101.7773438, 40.8470604),(-101.6894531, 39.5718222),(-94.6582031, 39.7071867),(-93.6035156, 40.7805414),(-90.5273438, 41.1786540),(-92.0214844, 44.7155137),(-92.5488281, 46.4378569),(-91.0546875, 47.3388227),(-89.5605469, 47.9899217),(-95.0976563, 49.3251220),(-96.8554688, 48.9224993),(-115.3125000, 48.8068635),(-111.4453125, 44.7155137),(-110.7421875, 40.9135126),(-104.5898438, 40.8470604)])
w1Poly = Polygon([(-102.3046875, 40.8470604),(-109.1601563, 40.9135126),(-110.9179688, 40.8470604),(-111.0937500, 41.7713117),(-113.9062500, 41.7713117),(-114.1699219, 36.8796206),(-114.5214844, 32.6208702),(-108.6328125, 31.2034050),(-108.1054688, 31.8028926),(-106.4355469, 31.7281671),(-102.9199219, 31.6533814),(-102.9199219, 36.8092847),(-101.8652344, 36.8796206),(-101.9531250, 40.7139558)])
w2Poly = Polygon([(-114.0161133, 42.0166518),(-119.0039063, 42.0492926),(-124.2773438, 41.9022770),(-124.0356445, 41.1455697),(-124.4091797, 40.4302236),(-123.5742188, 38.7198047),(-122.9589844, 38.0826895),(-122.5854492, 37.6142314),(-121.9482422, 36.3151251),(-120.4980469, 34.1618182),(-119.1137695, 34.0890613),(-117.9492188, 33.6146193),(-117.2460938, 32.4726950),(-114.6972656, 32.5468132),(-114.1699219, 34.5246615),(-114.2578125, 36.1023764),(-114.0380859, 41.9349765)])
w3Poly = Polygon([(-125.1562500, 48.5747899),(-123.9257813, 45.5217439),(-124.4531250, 42.0329743),(-110.8740234, 42.0982224),(-111.0937500, 44.2766713),(-112.9394531, 44.4023918),(-114.4335938, 45.5832898),(-116.1914063, 48.8647148),(-122.6513672, 49.1242192),(-123.0468750, 48.2246726),(-125.0683594, 48.5166043)])



#Defining the randomization generator
def polygon_random_points (poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds
    points = []
    while len(points) < num_points:
        random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if (random_point.within(poly)):
            points.append(random_point)
    return points

# Choose the number of points desired. This example uses 2 points. 
tpoints = polygon_random_points(ne1Poly, 2)

# Printing the results.
for p in tpoints:
    print(p.x,",",p.y)

