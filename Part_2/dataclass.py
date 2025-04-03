from dataclasses import dataclass


@dataclass
class Coordinate:
    x: int
    y: int
    z: int


matrix = [Coordinate(i, j, k) for i in range(3) for j in range(3) for k in range(3)]


@dataclass
class Space:
    coordinates: list[Coordinate]


matrix_m = Space(matrix)


@dataclass
class SpaceTime:
    point: Coordinate = (0, 0, 0)
    time: int = 0


@dataclass
class Vector:
    Start: Coordinate
    End: Coordinate
    time: int = 0


x3y = Vector(Coordinate(1, 2, 3), Coordinate(4, 5, 6))
