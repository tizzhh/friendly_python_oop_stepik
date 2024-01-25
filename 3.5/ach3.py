from typing import List, Tuple, Union

from typing_extensions import Self


class TrackLine:
    def __init__(
        self, to_x: Union[int, float], to_y: Union[int, float], max_speed: int
    ) -> None:
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:
    def __init__(
        self, start_x: Union[int, float] = 0, start_y: Union[int, float] = 0
    ) -> None:
        self.tracks: List[TrackLine] = []
        self.start_x = start_x
        self.start_y = start_y

    def __eq__(self, other: Self) -> bool:
        return self.get_track_length() == other.get_track_length()

    def __lt__(self, other: Self) -> bool:
        return self.get_track_length() < other.get_track_length()

    def __len__(self) -> int:
        return int(self.get_track_length())

    def get_track_length(self) -> float:
        res = 0.0
        prev_x, prev_y = self.start_x, self.start_y
        for track in self.tracks:
            res += (
                (track.to_x - prev_x) ** 2 + (track.to_y - prev_y) ** 2
            ) ** 0.5
            prev_x, prev_y = track.to_x, track.to_y
        return res

    def add_track(self, tr: TrackLine) -> None:
        self.tracks.append(tr)

    def get_tracks(self) -> Tuple[TrackLine]:
        return tuple(self.tracks)


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
print(res_eq)
