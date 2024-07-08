import math

# Nokta tanımlama
points = [(3, 3), (5, 3), (5, 10)]

# Öklid fonksiyonu yazma
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Mesafe hesaplama
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma
min_distance = min(distances)

print("Minimum mesafe:", min_distance)
