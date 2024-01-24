class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> int:
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    def __init__(self, clock1: Clock, clock2: Clock) -> None:
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self) -> str:
        time_diff = self.clock1.get_time() - self.clock2.get_time()
        if time_diff < 0:
            time_diff = 0
        hours = time_diff // 3600
        minutes = time_diff % 3600 // 60
        seconds = time_diff % 3600 % 60
        return f'{hours:02}: {minutes:02}: {seconds:02}'

    def __len__(self) -> int:
        time_diff = self.clock1.get_time() - self.clock2.get_time()
        if time_diff < 0:
            time_diff = 0
        return time_diff


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)  # 01: 30: 00
len_dt = len(dt)  # 5400
print(len_dt)
