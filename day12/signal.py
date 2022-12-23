class VideoScreen(object):

    def __init__(self) -> None:
        self._cycle = 1
        self.x = 1
        self.signal_strengh = 0

    def check_cycle(self, cycle_val):
        if (cycle_val % 40) == 20:
            print(cycle_val, self.x)
            self.signal_strengh += cycle_val * self.x

    def incremenet_x(self, value):
        self.x += value

    @property
    def cycle(self):
        return self._cycle

    @cycle.setter
    def cycle(self, value):
        self._cycle = value
        self.check_cycle(value)

    def noop(self):
        self.cycle += 1

    def addx(self, value):
        self.cycle += 1
        self.incremenet_x(value)
        self.cycle += 1

# python if increment cycle do somethign
video = VideoScreen()

with open('day10/input.txt') as f:
    for line in f:
        # split by space
        line = line.strip().split(' ')

        operation = line[0]
        if operation == 'noop':
            video.noop()
        elif operation == 'addx':
            value = line[1]
            video.addx(int(value))

print(video.signal_strengh)