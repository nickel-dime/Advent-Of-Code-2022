
points = {}
new_points = set()

blocked_points = set()

Y_VAL = 0

MAX_VAL = 4000000

class RowObject:

    def __init__(self, name) -> None:
        self.range = []
        self.name = name
        
    def add_range(self, range_min, range_max):
        self.range.append([range_min, range_max])

    def empty_squares(self):
        # combine ranges and see if empty squares
        merged_range = self.mergeIntervals(self.range)
        # print(merged_range)
        # new_merged_range = merged_range[0]
        # merged_range[0] = max(new_merged_range[0], 0)
        # merged_range[1] = min(new_merged_range[1], 20)
        if len(merged_range) > 1:
            return merged_range[1][0] - 1
        else:
            return None

    def mergeIntervals(self, intervals):
        if len(intervals) == 0:
            return [(1, 1)]
        # Sort the array on the basis of start values of intervals.
        intervals.sort()
        stack = []
        # insert first interval into stack
        stack.append(intervals[0])
        for i in intervals[1:]:
            # Check for overlapping interval,
            # if interval overlap
            if stack[-1][0] <= i[0] <= stack[-1][-1]+1:
                stack[-1][-1] = max(stack[-1][-1], i[-1])
            else:
                stack.append(i)
 
        # print("The Merged Intervals are :", end=" ")
        # for i in range(len(stack)):
        #     print(stack[i], end=" ")
        
        return stack


for i in range(0, MAX_VAL+1):
    points[i] = RowObject(i)

class Sensor:

    def __init__(self, beacon, sensor) -> None:
        self.sensor = sensor
        self.beacon = beacon
        self.manhattan = self.manhattan(sensor, beacon)

    def manhattan(self, first, second):
        # get manhattan distance
        return sum(abs(val1-val2) for val1, val2 in zip(first,second))

    def add_all_points(self):
        diff = abs(Y_VAL - self.sensor[1])

        if diff <= self.manhattan:
            x_length = self.manhattan - diff

            for x in range(self.sensor[0] - x_length, self.sensor[0] + x_length + 1):
                if (x, Y_VAL) not in blocked_points and x > 0 and x < 4000000:
                    new_points.add((x, Y_VAL))
            

    def get_all_points(self):
        # points = set()

        dis = self.manhattan
        start = 0

        print(dis)

        while (dis >= 0):
            first_x = self.sensor[0] - dis
            last_x = self.sensor[0] + dis

            first_y = self.sensor[1] - start
            last_y = self.sensor[1] + start

            start += 1

            print(first_x, last_x+1)

            for x in range(first_x, last_x+1):
                points.setdefault(first_y,set()).add((x, first_y))
                points.setdefault(last_y,set()).add((x, last_y))

                # points.add((x, first_y))
                # points.add((x, last_y))
        
            dis -= 1
        
        return []

    def mark_grid(self):
        dis = self.manhattan
        start = 0

        while (dis >= 0):
            first_x = self.sensor[0] - dis
            last_x = self.sensor[0] + dis

            first_y = self.sensor[1] - start
            last_y = self.sensor[1] + start

            if first_y < MAX_VAL and first_y > 0:
                first_y_row = points[first_y]
                first_y_row.add_range(first_x, last_x)

            if last_y < MAX_VAL and last_y > 0:
                last_y_row = points[last_y]
                last_y_row.add_range(first_x, last_x)

            start += 1
            dis -= 1

        # for point in all_points:
        #     points.setdefault(point[1],set()).add(point)
        #     # self.mark_point(grid, (point[0] - smallest_x, point[1] - smallest_y))

    def mark_point(self, grid, point):
        if point[1] >= 0 and point[1] < len(grid) and point[0] >= 0 and point[0] < len(grid[0]):
            if grid[point[1]][point[0]] == '.':
                grid[point[1]][point[0]] = '#'
                points.setdefault(point[1],set()).add(point)
        else:
            points.setdefault(point[1],set()).add(point)


largest_y = 0
largest_x = 0

smallest_x = 1000
smallest_y = 1000

sensors = []

with open('day15/input.txt') as f:
    for line in f:
        line = line.strip()

        sensor_x = int(line[12:line.index(',')])
        sensor_y = int(line[line.index('y')+2:line.index(':')])

        beacon_x = int(line[line.index('x', 30)+2:line.index(',', 20)])
        beacon_y = int(line[line.index('y', 30)+2:])

        if max(sensor_x, beacon_x) > largest_x:
            largest_x = max(sensor_x, beacon_x)
        
        if max(sensor_y, beacon_y) > largest_y:
            largest_y = max(sensor_y, beacon_y)

        if min(sensor_x, beacon_x) < smallest_x:
            smallest_x = min(sensor_x, beacon_x)
        
        if min(sensor_y, beacon_y) < smallest_y:
            smallest_y = min(sensor_y, beacon_y)
        
        sensors.append(Sensor((beacon_x, beacon_y), (sensor_x, sensor_y)))
        blocked_points.add((sensor_x, sensor_y))
        blocked_points.add((beacon_x, beacon_y))

if smallest_x > 0:
    smallest_x = 0
if smallest_y > 0:
    smallest_y = 0

largest_x -= smallest_x
largest_y -= smallest_y

# grid = []

# for i in range(largest_y+1):
#     grid.append(['.'] * (largest_x+1))


# for sensor in sensors:
#     sensor_coord = sensor.sensor
#     beacon_coord = sensor.beacon

#     sensor.sensor = (sensor_coord[0] - smallest_x, sensor_coord[1] - smallest_y)
#     sensor.beacon = (beacon_coord[0] - smallest_x, beacon_coord[1] - smallest_y)

#     sensor_coord = sensor.sensor
#     beacon_coord = sensor.beacon

#     grid[sensor_coord[1]][sensor_coord[0]] = 'S'
#     grid[beacon_coord[1]][beacon_coord[0]] = 'B'


for sensor in sensors:
    sensor.mark_grid()
    print("DID ONE")


for row, object in points.items():
    val = object.empty_squares()
    # print(row, val)

    if val:
        print(row, '****BOB****')
        print((val*4000000) + row)

    

# for i in range(0, 4000000):
#     Y_VAL = i
#     for sensor in sensors:
#         sensor.add_all_points()

#     print(i, len(new_points))
#     new_points = set()

#11583882601918
#11583882601918