coordinates = (10.0, 20.0)
x,y = coordinates
print(x)
print(y)

def square (n):
    return n * n

for i in range(10):
    print(f"The square of {i} is {square(i)}")

class Point():
    def __init__(self,input1,input2):
        self.x = input1
        self.y = input2
p = Point(2,8)
print(p.x)
print(p.y)


# from pyproj import Transformer

# # Define the source and target coordinate systems
# transformer = Transformer.from_crs("EPSG:3857", "EPSG:4326")

# # Transform coordinates
# x, y = -11705274.6374, 4826473.6922
# lat, lon = transformer.transform(x, y)
# print(f"Latitude: {lat}, Longitude: {lon}")

# from pyproj import Transformer

# # Define the source and target coordinate systems
# transformer = Transformer.from_crs("EPSG:3857", "EPSG:4326")

# # Transform coordinates
# x, y = -11705274.6374, 4826473.6922
# lat, lon = transformer.transform(x, y)
# print(f"Latitude: {lat}, Longitude: {lon}")

