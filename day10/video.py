class VideoScreen(object):

    def __init__(self) -> None:
        self._cycle = 0
        self.x = 1
        self.current_row = ''

    def draw(self):
        if (self._cycle % 40) == 0:
            self.current_row += '\n'

        zeroed_x = self.x % 40
        zeroed_cycle = self.cycle % 40
        print(self.x, self._cycle)
        if abs(zeroed_x - zeroed_cycle) <= 1:
            self.current_row += '#'
        else:
            self.current_row += '.'

        print(self.current_row)

    def increment_x(self, value):
        self.x += value

    @property
    def cycle(self):
        return self._cycle

    @cycle.setter
    def cycle(self, value):
        self.draw()
        self._cycle = value

    def noop(self):
        self.cycle += 1

    def addx(self, value):
        self.cycle += 1
        self.cycle += 1
        self.increment_x(value)


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

print(video.current_row)