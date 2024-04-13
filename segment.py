from coor import Coordinate


class Segment:
    """representation of single segment in a profile
    e.g. | pole <--> plot edge |
    """
    def __init__(self):
        self.start: Coordinate = None
        self.end: Coordinate = None
        self.plot_nr: str = ""
        self.id: str = ""
        self.elevation_gain: list[str | float]
