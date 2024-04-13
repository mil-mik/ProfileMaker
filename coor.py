"""Represents simple coordinates system in 2D"""


class Coordinate:
    """Abstract coordinates system 2D representation"""
    def __init__(self, latitude: str, longitude: str):
        self.coor = (latitude, longitude)

    def __str__(self):
        return f"Latitude: {self.coor[0]}, Longitude{self.coor[1]}"
