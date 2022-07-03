'''
    Code to simulate toy robot.
    DEBUG is a verbose flag
    X, Y are the width and height of the grid
'''
DEBUG = False
X, Y = (5, 5)


def get_direction_from_int(i):
    ''' Gets the direction name from its int '''
    if i == 0:
        return 'NORTH'
    elif i == 1:
        return 'EAST'
    elif i == 2:
        return 'SOUTH'
    elif i == 3:
        return 'WEST'


def get_direction_from_str(str):
    ''' Gets the direction int from direction name'''
    if str == 'NORTH':
        return 0
    elif str == 'EAST':
        return 1
    elif str == 'SOUTH':
        return 2
    elif str == 'WEST':
        return 3


def is_position_valid(coords):
    ''' Checks whether x and y are within boundaries '''
    if coords[0] >= 0 and \
        coords[0] < X and \
        coords[1] >= 0 and \
        coords[1] < Y:
            return True
    return False


def report_fn(robot):
    ''' Report the robot current situation '''

    # Robot was never placed
    if robot[0] == False:
        return
    else:
        print('{},{},{}'.format(robot[1][0], robot[1][1], get_direction_from_int(robot[2])))


def place_fn(robot, coords, dir):
    ''' Checks if placement position is valid, if so, places robot '''

    if is_position_valid(coords):
        robot[0] = True
        robot[1][0] = coords[0] # X coord
        robot[1][1] = coords[1] # Y coord
        robot[2] = get_direction_from_str(dir)

    if DEBUG:
        print('\tplaced robot:', robot, get_direction_from_int(robot[2]))


def move_fn(robot):
    ''' Checks if moving forward is possible, if so, moves '''

    # Robot was never placed
    if robot[0] == False:
        return

    new_coords = [-1, -1]

    if robot[2] == 0: # North
        new_coords[0] = robot[1][0]
        new_coords[1] = robot[1][1] - 1

    elif robot[2] == 1: # East
        new_coords[0] = robot[1][0] + 1
        new_coords[1] = robot[1][1]

    elif robot[2] == 2: # South
        new_coords[0] = robot[1][0]
        new_coords[1] = robot[1][1] + 1

    elif robot[2] == 3: # West
        new_coords[0] = robot[1][0] - 1
        new_coords[1] = robot[1][1]

    if is_position_valid(new_coords):
        robot[1] = new_coords
        if DEBUG:
            print('\tmoved robot', robot)
    elif DEBUG:
        print(new_coords, 'are not valid')


def turn_fn(robot, dir):
    ''' Turns the robot LEFT or RIGHT '''

    # Robot was never placed
    if robot[0] == False:
        return

    if dir == 'RIGHT':
        robot[2] = (robot[2] + 1) % 4
    else:
        robot[2] = (robot[2] - 1) % 4
    
    if DEBUG:
        print('\tnew direction:', robot[2], get_direction_from_int(robot[2]))


def process_commands(robot):
    ''' Reads the input and processes each entry '''

    str = input().split()
    while str != None:

        if str[0] == 'REPORT':
            report_fn(robot)

        # Get coordenates and direction before placing robot
        elif str[0] == 'PLACE':
            aux = str[1].split(',')
            x = int(aux[0])
            y = int(aux[1])
            f = aux[2]
            place_fn(robot, (x,y), f)

        # Move forward
        elif str[0] == 'MOVE':
            move_fn(robot)

        # Turn left of right
        else:
            turn_fn(robot, str[0])

        # Kill execution on EOF
        try:
            str = input().split()
        except:
            break


def main():
    # Information about the robot:
    #   is_placed
    #   [coordenates]
    #   direction
    robot_stats = [False, [-1, -1], -1]

    process_commands(robot_stats)


if __name__ == '__main__':
    main()
