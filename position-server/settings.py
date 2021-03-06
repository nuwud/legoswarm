robot_settings = {
            'sight_range': 300,
            'p_bot_midbase': (-2, -8),
            'p_bot_gripper': (0, 11),
            'p_bot_rear': (0, -15),
            'speed_per_unit_force': .75,
            'turnrate_per_unit_force': 2,
            'ball_close_enough': 18,
            'ball_grab_time': 3,  # s
            'max_balls_in_store': 5,
            'bounce_drive_speed': 4,
            'min_wall_distance': 12,
            'distance_to_purge_location': 27,
            'robot_avoidance_spring': [
            # 0                  b ------------   0 (no force at at 30 cm or beyond)
            #                  /
            #                /
            #              /
            # -20 ---------a                     -20 (push when too close)
            # 
            #          0      30    160     200      
            # 
            #                                     
                [0,  -55], #a
                [45,  0 ], #b
            ],
            'robot_avoidance_spring_inferior': [
            # 0                  b ------------   0 (no force at at 30 cm or beyond)
            #                  /
            #                /
            #              /
            # -20 ---------a                     -20 (push when too close)
            #
            #          0      30    160     200
            #
            #
                [0,  -55], #a
                [30,  0 ], #b
            ],
            'robot_attraction_spring' : [
            #                         c                     15 (pull when far)
            #                        / \
            #                      /     \
            #                    /         \
            # -------- a -------b             d------------   0 (no force at at 200 cm or beyond)
            #
            #          0      30    160     200
            #
            #
                [0,  0], #a
                [30,  0 ], #b
                [60,  20],#c
                [200,  20 ]  #d
            ],
            'spring_to_walls' : [
            #
            #                  b ----------   0 (no force at at 10 cm or beyond)
            #                /        
            #              / 
            #            /
            # ----------a                    -20 (push when too close)
            # 
            #          0      30      
            # 
            #                                     
            #     [-30, 30],
                [0,  -25], #a
                [25, 0 ], #b
            ],
            'short_spring_to_walls' : [
            #
            #                  b ----------   0 (no force at at 10 cm or beyond)
            #                /
            #              /
            #            /
            # ----------a                    -20 (push when too close)
            #
            #          0      30
            #
            #
            #     [-30, 30],
                [0,  -20], #a
                [12, 0 ], #b
            ],
            'spring_to_balls' : [
            #
            # -------a                        10  (Pull when nearer than 5)          
            #         \
            #          \
            #           \
            #            b-----------         0   (no force at at 10 cm or beyond)
            # 
            #        5   10      
            # 
            #                                     
                [0 ,  0], #a
                [10,  10 ], #b
            ],
            'spring_to_depot' : [
                [0 ,  25], #a
                [30,  40], #b
                [50, 15]
            ],
            'spring_to_line' : [
                [0, 0],
                [10, 40]
            ],
            'spring_to_position' : [
                [0, 0],
                [10, 20]
            ]

}

# Server settings
server_settings = {
    'SERVER_BASE_PORT' : 50000,
    'THRESHOLD' : 145,         # Threshold for b/w version of camera image. Higher number means more black
    'WIDTH' : 1920,            # Camera image
    'HEIGHT' : 1080,
    'extra border outside' : -70,
    'extra border inside' : 10,
    'MIN_BALL_RADIUS_PX' : 6,
    'MAX_BALL_RADIUS_PX' : 12,
    'MAX_AGENTS' : 8,
    'depots_world' : [  # all cm relative to center of field:
                        [0, -112],  # +80 along y, 0 along x.
                        # [-150, 0] # -150 cm along x, and in the middle of y
                     ],    
    'p_bot_midbase' : robot_settings['p_bot_midbase'],
    'p_bot_gripper' : robot_settings['p_bot_gripper'],
    'p_bot_rear' : robot_settings['p_bot_rear'],
    'sight_range' : robot_settings['sight_range'],
    'FILE' : '',#'"test_images/error_scenario_too_many_balls.png",#""test_images/1516199702.jpg" #"test_images/test.jpg" # 1920 x 1080 afbeelding. png mag ook.
    'cm_per_ball_px': 0.15, # 263 cm diagonal = 1990 px, on the gound
    'cm_per_marker_px': 0.15*(1936+500-132*0.8)/1936, # Markers are at approx 13.2 cm from ground
    'cm_per_bounding_px': 0.15*(1936+500-60)/1936, # dimensions relevant for bounding box are at approx 6cm above ground
    'ball_info_max_size': 3, # Number of nearest balls each robot should get details of
    'depot_radius': 200, #pixels
    'reload_settings_after_n_loops': 200,
    'bounding_box_cm': [
        # List of points in centimeters, encircling the robot
        # Starting at left wheel, then go counterclockwise
        [-14, 2.5], # Front end of left wheel
        [-14, -2.5], # Back end of left wheel
        [-8, -14], # Left rear wheel caster
        [0, -17], # Motor cable
        [8, -14], # right wheel caster
        [14, -2.5], # Back end of right wheel
        [14, 2.5], # Front end of right wheel
        [5, 22], # Front-right end of gripper
        [-5, 22] # Front-left end of gripper
    ]
}

# Allow Laurens to specify file to debug different scenarios without repeated git conflicts.
import platform
if 'Ubuntu' in platform.platform():
    print('Laurens Mode')
    server_settings['FILE'] = 'test_images/over_the_edge_error_nodump.jpg'
    server_settings['SERVER_BASE_PORT'] = 60000
