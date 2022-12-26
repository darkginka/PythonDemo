import geopy.distance

coords_1 = (72.9566658, 19.200768)
coords_2 = (72.9620346, 19.1984872)

print(geopy.distance.geodesic(coords_1, coords_2))