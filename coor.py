class Coordinate:

    def __init__(self, latitude: str, longitude: str):
        self.coor = (latitude, longitude)

    def __str__(self):
        return f"Latitude: {self.coor[0]}, Longitude{self.coor[1]}"
