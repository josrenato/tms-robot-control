import time

from robot.robots.universal_robot.universal_robot import UniversalRobot

ip = "192.168.5.5"

robot = UniversalRobot(
    ip=ip,
)

# Test the robot movement in both directions.
for movement_direction in [-1, 1]:
    # Connect to the robot.
    success = robot.connect()
    print("Connected: ", success)

    robot.initialize()

    # Get the current pose of the robot.
    current_pose = robot.get_pose()

    print("")
    print("Current pose: X = {:.2f}, Y = {:.2f}, Z = {:.2f}, Rx = {:.2f}, Ry = {:.2f}, Rz = {:.2f}".format(
        current_pose[0], current_pose[1], current_pose[2], current_pose[3], current_pose[4], current_pose[5],
    ))

    ## Test linear movement.
    print("")
    print("Press enter to test linear movement")
    input()

    # Send the movement command to the robot.
    target = current_pose[:]
    target[0] += 0.04 * movement_direction

    speed_ratio = 0.01

    response = robot.move_linear(
        target=target,
        speed_ratio=speed_ratio,
    )

    # Wait until the robot has started moving.
    moving = False
    print("")
    print("Waiting for the robot to start moving...")
    while not moving:
        moving = robot.is_moving()
        time.sleep(0.1)

    print("Robot is moving")

    # Wait until the robot has stopped moving.
    print("")
    print("Waiting for the robot to stop moving...")
    while moving:
        moving = robot.is_moving()
        time.sleep(0.1)

    print("Robot has stopped moving")

    ## Test circular movement.
    print("")
    print("Press enter to test circular movement")
    input()

    # Send the movement command to the robot.
    current_pose = robot.get_pose()

    waypoint = current_pose[:]
    waypoint[0] += 0.02 * movement_direction
    waypoint[1] += 0.02 * movement_direction
    waypoint[2] += 0.02 * movement_direction

    target = waypoint[:]
    target[0] += 0.02 * movement_direction
    target[1] += 0.02 * movement_direction
    target[2] += 0.02 * movement_direction

    speed_ratio = 0.01

    response = robot.move_circular(
        start_position=current_pose,
        waypoint=waypoint,
        target=target,
        speed_ratio=speed_ratio,
    )

    # Wait until the robot has started moving.
    moving = False
    print("")
    print("Waiting for the robot to start moving...")
    while not moving:
        moving = robot.is_moving()
        time.sleep(0.1)

    print("Robot is moving")

    # Wait until the robot has stopped moving.
    print("")
    print("Waiting for the robot to stop moving...")
    while moving:
        moving = robot.is_moving()
        time.sleep(0.1)

    print("Robot has stopped moving")

    # Disconnect from the robot.
    connected = robot.is_connected()
    print("Robot connection status before disconnect: ", connected)

    success = robot.disconnect()
    print("")
    if success:
        print("Disconnected successfully")
    else:
        print("Failed to disconnect")
    print("")

    connected = robot.is_connected()
    print("Robot connection status after disconnect: ", connected)
