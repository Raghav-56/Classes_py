from dataclasses import dataclass

from r_dataclass import SpaceTime, Vector


@dataclass
class Movement:
    Start: SpaceTime
    End: SpaceTime

    def distance(self):
        return self.End.point - self.Start.point

    def time(self):
        return self.End.time - self.Start.time

    def speed(self):
        return self.distance() / self.time()


Movement_1 = Movement(SpaceTime((1, 2, 3), 0), SpaceTime((4, 5, 6), 4))
