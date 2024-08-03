import math

points = []
for i in range(2):  
    x = float(input(f"Please give us x{i+1}: "))
    y = float(input(f"Please give us y{i+1}: "))
    points.append((x, y))

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

if distances:  
    min_distance = min(distances)
    print("Each point distances between pairs:", distances)
    print("Minimum distance:", min_distance)
else:
    print("Not enough points found.")
