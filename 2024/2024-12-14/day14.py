#!/usr/bin/env python
import argparse
import re
INPUT = "input.txt"
# Should these maybe be one less so it starts at 0?

class Map:
    def __init__(self, dimentions: tuple[int, int]):
        self.x_size = dimentions[0]
        self.y_size = dimentions[1]
    def __str__(self):
        return f"Map with x size: {self.x_size} and y size: {self.y_size}"

SMALL_MAP: tuple[int, int] = (11, 7)
NORMAL_MAP: tuple[int, int] = (101, 103)
MAP_DIMENSIONS = Map(NORMAL_MAP)


class RobotPositionVelocity:
    def __init__(self, id: int, x: int, y: int, x_velocity: int, y_velocity: int):
        self.id = id
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

def parse_input(path_to_file: str) -> list[RobotPositionVelocity]:
    robots: list[RobotPositionVelocity] = []
    with open(path_to_file, 'r') as file:
        #p=0,4 v=3,-3
        #p=6,3 v=-1,-3
        for i, line in enumerate(file, start=1):
            integers_in_line = re.findall(r'-?\b\d+\b', line.strip())
            robot= RobotPositionVelocity(
                id=i,
                x=int(integers_in_line[0]),
                y=int(integers_in_line[1]),
                x_velocity=int(integers_in_line[2]),
                y_velocity=int(integers_in_line[3]),
            )
            robots.append(robot)

    return robots

def traverse_map(current_location: int, velocity: int, edge: int) -> int:
    return (current_location + velocity) % edge

def print_map(robots: list[RobotPositionVelocity]):
    for y in range(MAP_DIMENSIONS.y_size):
        for x in range(MAP_DIMENSIONS.x_size):
            robot_count = 0
            for robot in robots:
                if robot.x == x and robot.y == y:
                    robot_count += 1
            if robot_count > 0:
                print(robot_count, end="")
            else:
                print(".", end="")
        print()


def calculate_safety_factor(robots: list[RobotPositionVelocity]):
    '''
    Safety factor
    '''
    robots_updated = robots.copy()
    middle_x = MAP_DIMENSIONS.x_size // 2
    middle_y = MAP_DIMENSIONS.y_size // 2
    for robot in robots_updated:
        if robot.x == middle_x and robot.y == middle_y:
            robots_updated.remove(robot)
    # split robots into 4 groups one for each quadrant
    top_left_group = []
    top_right_group = []
    bottom_left_group = []
    bottom_right_group = []
    for robot in robots_updated:
        if robot.x < middle_x and robot.y < middle_y:
            top_left_group.append(robot)
        elif robot.x > middle_x and robot.y < middle_y:
            top_right_group.append(robot)
        elif robot.x < middle_x and robot.y > middle_y:
            bottom_left_group.append(robot)
        elif robot.x > middle_x and robot.y > middle_y:
            bottom_right_group.append(robot)

    return len(top_left_group) * len(top_right_group) * len(bottom_left_group) * len(bottom_right_group)

def predict_safety_factor(robots: list[RobotPositionVelocity], seconds_elapsed: int):
    robots_updated = robots.copy()
    #print("Initial state:")
    #print(print_map(robots_updated))
    print()
    for i in range(seconds_elapsed):
        for robot in robots_updated:
            robot.x = traverse_map(robot.x, robot.x_velocity, MAP_DIMENSIONS.x_size)
            robot.y = traverse_map(robot.y, robot.y_velocity, MAP_DIMENSIONS.y_size)
        #print(print_map(robots_updated))
    return calculate_safety_factor(robots_updated)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict robot locations.")
    parser.add_argument("--predict_safety_factor", action='store_true',
                       help="Predict the robot safety pattern after 100 seconds.")
    args = parser.parse_args()

    robots = parse_input(INPUT)
    print(MAP_DIMENSIONS)
    if args.predict_safety_factor:
        # 91536300 is correct for large input.
        # 12 is correct for small input
        seconds_elapsed = 100
        result = predict_safety_factor(robots, seconds_elapsed=seconds_elapsed)
        print(f"The safety factor after {seconds_elapsed} seconds is {result}")
