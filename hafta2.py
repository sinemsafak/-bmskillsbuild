import math

#  Noktalar tanımlandı
points = [(1, 2), (4, 6), (5, 8), (9, 10), (2, 3)]

# öklid mesafesi için kod yazıldı 
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# mesafeleri hesaplama
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# mininmum mesafenin bulunması
min_distance = min(distances)
print(f"Minimum mesafe: {min_distance}")
