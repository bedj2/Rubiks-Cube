from pylab import *
from numpy import *
from string import *
import random as rd
from matplotlib.pylab import plt
import matplotlib.animation as animation
import matplotlib.patches as patches

'''
Version History:
1.3.1 - Corrected FrameShiftLeft & added it to step2A
      - Made FrameShiftUp
1.3.2 - imshow plot implimentation
1.4.0 - findingFace function now applies to shifted reference frame
1.4.1 - Adding answer_key.append to each of the rotation functions
      - Rearrangeed order of definitions 
           from:            to:
        1.rotations     1.rotations
        2.modifiers     2.processors
        3.processors    3.modifiers
      - Architect References 
      - re_dm() or reiteration demolisher
1.4.2 - Step2A complete
2.1.0 - step2B complete
      - step2C complete
      - step2D complete
3.1.0 - step3A complete
4.1.0 - step4A complete
5.1.0 - step5A complete
5.2.0 - step5B complete
Beta 1.0.0 - created "seedling" variable
           - killed all printOut()'s; to revert back to v5.2.0 find "#1 printOut(cube)"
           - created "check()" function
Beta 1.0.1 - killed all non-formated (ie ['FF','CW']) appends from answer_key
           - added steps (ie ['Step','1A']to answer_key
Beta 1.0.3 - Reformated printing to accomadate frome 'Canopy' IDE to 'Anaconda' IDE
           - Deleted first randStateMoves amount of frames from the animation grid, 
             as the compilation of the random state was unnecessarily displayed on 
             the animation grid.

'''



######################################################################################
######################################################################################
######################################################################################

#NOTE: RED SIDE IS FACING YOU, so all moves must be done with red middle piece 
#      facing you and green middle piece pointing up at all times.


#              (Demonstrational Cube)                                  (Actual Cube List)

#           [         GG GG GG         ]                             [0,0,0,10,11,12,0,0,0],
#           [         GG GG GG         ]                             [0,0,0,13,14,15,0,0,0],       
#           [         GG GG GG         ]    green      10's          [0,0,0,16,17,18,0,0,0],
#           [YY YY YY RR RR RR WW WW WW]    yellow     20's       [20,21,22,30,31,32,40,41,42], 
#           [YY YY YY RR RR RR WW WW WW]    red        30's       [23,24,25,33,34,35,43,44,45], 
#           [YY YY YY RR RR RR WW WW WW]    white      40's       [26,27,28,36,37,38,46,47,48],
#           [         BB BB BB         ]    blue       50's          [0,0,0,50,51,52,0,0,0],       
#           [         BB BB BB         ]    orange     60's          [0,0,0,53,54,55,0,0,0],       
#           [         BB BB BB         ]                             [0,0,0,56,57,58,0,0,0],
#           [         OO OO OO         ]                             [0,0,0,60,61,62,0,0,0],       
#           [         OO OO OO         ]                             [0,0,0,63,64,65,0,0,0],       
#           [         OO OO OO         ]                             [0,0,0,66,67,68,0,0,0]


               
#LEGEND

# Connectors: @,$,&,%
# Directions: ^,>,v,<

#    (Color associated with side) (Side) (Shortcut)
#              (ClockWise)                  (Counter-ClockWise)


#                         'Yellow' LEFT 'l'
#                  CW                               CCW

#     [         v  GG GG         ]     [         ^  GG GG         ]
#     [         v  GG GG         ]     [         ^  GG GG         ]
#     [         v  GG GG         ]     [         ^  GG GG         ]
#     [>  >  v  v  RR RR WW WW WW]     [v  <  <  ^  RR RR WW WW WW]
#     [^  YY v  v  RR RR WW WW WW]     [v  YY ^  ^  RR RR WW WW WW]
#     [^  <  <  v  RR RR WW WW WW]     [>  >  ^  ^  RR RR WW WW WW]
#     [         v  BB BB         ]     [         ^  BB BB         ]
#     [         v  BB BB         ]     [         ^  BB BB         ]     
#     [         v  BB BB         ]     [         ^  BB BB         ]
#     [         v  OO OO         ]     [         ^  OO OO         ]
#     [         v  OO OO         ]     [         ^  OO OO         ]
#     [         v  OO OO         ]     [         ^  OO OO         ]

#                           'Red' FRONT 'f'
#                  CW                               CCW

#     [         GG GG GG         ]     [         GG GG GG         ]
#     [         GG GG GG         ]     [         GG GG GG         ]
#     [         >  >  >          ]     [         <  <  <          ]
#     [YY YY ^  >  >  v  v  WW WW]     [YY YY v  <  <  ^  ^  WW WW]
#     [YY YY ^  ^  RR v  v  WW WW]     [YY YY v  v  RR ^  ^  WW WW]
#     [YY YY ^  ^  <  <  v  WW WW]     [YY YY v  v  >  >  ^  WW WW]
#     [         <  <  <          ]     [         >  >  >          ]
#     [         BB BB BB         ]     [         BB BB BB         ]     
#     [         BB BB BB         ]     [         BB BB BB         ]
#     [         OO OO OO         ]     [         OO OO OO         ]
#     [         OO OO OO         ]     [         OO OO OO         ]
#     [         OO OO OO         ]     [         OO OO OO         ]

#                         'White' RIGHT 'r'
#                  CW                               CCW

#     [         GG GG ^          ]     [         GG GG v          ]
#     [         GG GG ^          ]     [         GG GG v          ]
#     [         GG GG ^          ]     [         GG GG v          ]
#     [YY YY YY RR RR ^  >  >  v ]     [YY YY YY RR RR v  <  <  ^ ]
#     [YY YY YY RR RR ^  ^  WW v ]     [YY YY YY RR RR v  v  WW ^ ]
#     [YY YY YY RR RR ^  ^  <  < ]     [YY YY YY RR RR v  v  >  > ]
#     [         BB BB ^          ]     [         BB BB v          ]
#     [         BB BB ^          ]     [         BB BB v          ]     
#     [         BB BB ^          ]     [         BB BB v          ]
#     [         OO OO ^          ]     [         OO OO v          ]
#     [         OO OO ^          ]     [         OO OO v          ]
#     [         OO OO ^          ]     [         OO OO v          ]

#                         'Green' UPPER 'u',
#                  CW                               CCW

#     [         >  >  v          ]     [         <  <  ^          ]
#     [         ^  GG v          ]     [         v  GG ^          ]
#     [         ^  <  <          ]     [         v  >  >          ]
#     [<@ <  <  <  <  <  <  <  <$]     [@> >  >  >  >  >  >  >  >$]
#     [YY YY YY RR RR RR WW WW WW]     [YY YY YY RR RR RR WW WW WW]
#     [YY YY YY RR RR RR WW WW WW]     [YY YY YY RR RR RR WW WW WW]
#     [         BB BB BB         ]     [         BB BB BB         ]
#     [         BB BB BB         ]     [         BB BB BB         ]     
#     [         BB BB BB         ]     [         BB BB BB         ]
#     [         OO OO OO         ]     [         OO OO OO         ]
#     [         OO OO OO         ]     [         OO OO OO         ]
#     [         >@ >> >$         ]     [         <@ << <$         ]

#                         'Orange' BACK 'b' 
#                  CW                               CCW

#     [         &< << <%         ]     [         &> >> >%         ]
#     [         GG GG GG         ]     [         GG GG GG         ]
#     [         GG GG GG         ]     [         GG GG GG         ]
#     [&v YY YY RR RR RR WW WW ^%]     [&^ YY YY RR RR RR WW WW v%]
#     [vv YY YY RR RR RR WW WW ^^]     [^^ YY YY RR RR RR WW WW vv]
#     [@v YY YY RR RR RR WW WW ^$]     [$^ YY YY RR RR RR WW WW v@]
#     [         BB BB BB         ]     [         BB BB BB         ]
#     [         BB BB BB         ]     [         BB BB BB         ]     
#     [         >@ >> >$         ]     [         $< << <@         ]
#     [         >  >  v          ]     [         v  <  <          ]
#     [         ^  OO v          ]     [         v  OO ^          ]
#     [         ^  <  <          ]     [         >  >  ^          ]

#                          'Blue' BOTTOM 'd'
#                  CW                               CCW

#     [         GG GG GG         ]     [         GG GG GG         ]
#     [         GG GG GG         ]     [         GG GG GG         ]
#     [         GG GG GG         ]     [         GG GG GG         ]
#     [YY YY YY RR RR RR WW WW WW]     [YY YY YY RR RR RR WW WW WW]
#     [YY YY YY RR RR RR WW WW WW]     [YY YY YY RR RR RR WW WW WW]
#     [@> >  >  >  >  >  >  >  >$]     [@< <  <  <  <  <  <  <  <$]
#     [         >  >  v          ]     [         v  <  <          ]
#     [         ^  BB v          ]     [         v  BB ^          ]     
#     [         ^  <  <          ]     [         >  >  ^          ]
#     [         <@ << <$         ]     [         >@ >> >$         ]
#     [         OO OO OO         ]     [         OO OO OO         ]
#     [         OO OO OO         ]     [         OO OO OO         ]
#
#
#

# FrameShiftLeft

#           [         ^  >  >          ]                          
#           [         ^  GG v          ]                            
#           [         <  <  v          ]  
#           [%  <  <  <  <  <  <  <  $ ] 
#           [&  YY <  <  RR <  <  WW @ ] 
#           [*  <  <  <  <  <  <  <  ! ] 
#           [         <  <  ^          ]      
#           [         v  BB ^          ]       
#           [         v  >  >          ]
#           [         *  >  !          ]      
#           [         &  OO @          ]      
#           [         %  >  $          ]  




#Global Variables

#determines the amount of rotations of different faces in randState()
#also helps with giving and exact number of rows to extract/rollover loading files in POF
randStateMoves = 30
answer_key = []
#seedling = np.random.randint(0,10000)
seedling = 3806
anim_grid = []
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#
#-------------------------------------(Rotations)----------------------------------------#
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#          
def bottomFaceCW(cube):
    mirror = array(cube)
    #always start with Leftmost Facelet
    #   (new) <-- (old)
    # new loc <-- moved to
    # Bottom is blue
    
    #R out
    cube[5][6] = mirror[5][3]
    cube[5][7] = mirror[5][4]
    cube[5][8] = mirror[5][5]
    
    #W out
    cube[9][5] = mirror[5][6]
    cube[9][4] = mirror[5][7]
    cube[9][3] = mirror[5][8]
    
    #O out
    cube[5][0] = mirror[9][5]
    cube[5][1] = mirror[9][4]
    cube[5][2] = mirror[9][3]
    
    #Y out
    cube[5][3] = mirror[5][0]
    cube[5][4] = mirror[5][1]
    cube[5][5] = mirror[5][2]
    
    
    #R in
    cube[6][5] = mirror[6][3]
    cube[7][5] = mirror[6][4]
    cube[8][5] = mirror[6][5]
    #W in
    cube[8][5] = mirror[6][5]
    cube[8][4] = mirror[7][5]
    cube[8][3] = mirror[8][5]
    #O in
    cube[8][3] = mirror[8][5]
    cube[7][3] = mirror[8][4]
    cube[6][3] = mirror[8][3]
    #Y in
    cube[6][3] = mirror[8][3]
    cube[6][4] = mirror[7][3]
    cube[6][5] = mirror[6][3]  
    answer_key.append(['DF','CW'])
    anim_grid.append(np.copy(cube))

            
    
def bottomFaceCCW(cube):
    mirror = array(cube)
    #always start with Leftmost Facelet
    #   (new) <-- (old)
    # new loc <-- moved to
    # Bottom is Blue
    
    
    #R out
    cube[5][0] = mirror[5][3]
    cube[5][1] = mirror[5][4]
    cube[5][2] = mirror[5][5]
    
    #W out
    cube[9][5] = mirror[5][0]
    cube[9][4] = mirror[5][1]
    cube[9][3] = mirror[5][2]
    
    #O out
    cube[5][6] = mirror[9][5]
    cube[5][7] = mirror[9][4]
    cube[5][8] = mirror[9][3]
    
    #Y out
    cube[5][3] = mirror[5][6]
    cube[5][4] = mirror[5][7]
    cube[5][5] = mirror[5][8]
    
    
    #R in
    cube[8][3] = mirror[6][3]
    cube[7][3] = mirror[6][4]
    cube[6][3] = mirror[6][5]
    #W in
    cube[8][5] = mirror[8][3]
    cube[8][4] = mirror[7][3]
    cube[8][3] = mirror[6][3]
    #O in
    cube[6][5] = mirror[8][5]
    cube[7][5] = mirror[8][4]
    cube[8][5] = mirror[8][3]
    #Y in
    cube[6][3] = mirror[6][5]
    cube[6][4] = mirror[7][5]
    cube[6][5] = mirror[8][5]
    answer_key.append(['DF','CCW'])
    anim_grid.append(np.copy(cube))
            
            
            
            
            
            
def upperFaceCCW(cube):
    Check = True
    mirror = array(cube)
    #always start with Leftmost Facelet
    #   (new) <-- (old)
    # new loc <-- moved to
    # Top is Green
            
    #O out
    cube[3][2] = mirror[11][3]
    cube[3][1] = mirror[11][4]
    cube[3][0] = mirror[11][5]
    
    #Y out
    cube[3][5] = mirror[3][2]
    cube[3][4] = mirror[3][1]
    cube[3][3] = mirror[3][0]
    
    #R out
    cube[3][8] = mirror[3][5]
    cube[3][7] = mirror[3][4]
    cube[3][6] = mirror[3][3]
    
    #W out
    cube[11][3] = mirror[3][8]
    cube[11][4] = mirror[3][7]
    cube[11][5] = mirror[3][6]
    
    
    #
    cube[2][3] = mirror[0][3]
    cube[1][3] = mirror[0][4]
    cube[0][3] = mirror[0][5]
    #
    cube[2][5] = mirror[2][3]
    cube[2][4] = mirror[1][3]
    cube[2][3] = mirror[0][3]
    #
    cube[0][5] = mirror[2][5]
    cube[1][5] = mirror[2][4]
    cube[2][5] = mirror[2][3]
    #
    cube[0][3] = mirror[0][5]
    cube[0][4] = mirror[1][5]
    cube[0][5] = mirror[2][5]
    answer_key.append(['UF','CCW'])
    anim_grid.append(np.copy(cube))
    
    
    
            
def upperFaceCW(cube):
    Check = True
    mirror = array(cube)
    #always start with Leftmost Facelet
    #   (new) <-- (old)
    # new loc <-- moved to
    # Top is Green
    
    #O out
    cube[3][8] = mirror[11][3]
    cube[3][7] = mirror[11][4]
    cube[3][6] = mirror[11][5]
    
    #W out
    cube[3][5] = mirror[3][8]
    cube[3][4] = mirror[3][7]
    cube[3][3] = mirror[3][6]
    
    #R out
    cube[3][2] = mirror[3][5]
    cube[3][1] = mirror[3][4]
    cube[3][0] = mirror[3][3]
    
    #Y in
    cube[11][3] = mirror[3][2]
    cube[11][4] = mirror[3][1]
    cube[11][5] = mirror[3][0]
    
    
    #O in
    cube[0][5] = mirror[0][3]
    cube[1][5] = mirror[0][4]
    cube[2][5] = mirror[0][5]
    #W in
    cube[2][5] = mirror[0][5]
    cube[2][4] = mirror[1][5]
    cube[2][3] = mirror[2][5]
    #R in
    cube[2][3] = mirror[2][5]
    cube[1][3] = mirror[2][4]
    cube[0][3] = mirror[2][3]
    #Y in
    cube[0][3] = mirror[2][3]
    cube[0][4] = mirror[1][3]
    cube[0][5] = mirror[0][3]
    answer_key.append(['UF','CW'])
    anim_grid.append(np.copy(cube))
    

            
def leftFaceCCW(cube):
    Check = True
    mirror = array(cube)
    #always start with Leftmost Facelet
    #   (new) <-- (old)
    # new loc <-- moved to
    
    #G out
    cube[9][3] = mirror [0][3]
    cube[10][3] = mirror [1][3]
    cube[11][3] = mirror [2][3]
    
    #R out
    cube[6][3] = mirror [9][3]
    cube[7][3] = mirror [10][3]
    cube[8][3] = mirror [11][3]
    
    #B out
    cube[3][3] = mirror [6][3]
    cube[4][3] = mirror [7][3]
    cube[5][3] = mirror [8][3]
    
    #O out
    cube[0][3] = mirror [3][3]
    cube[1][3] = mirror [4][3]
    cube[2][3] = mirror [5][3]
    
    
    #G in
    cube[5][0] = mirror [3][0]
    cube[4][0] = mirror [3][1]
    cube[3][0] = mirror [3][2]
    
    #R in
    cube[5][2] = mirror [5][0]
    cube[5][1] = mirror [4][0]
    cube[5][0] = mirror [3][0]
    
    #B in
    cube[3][2] = mirror [5][2]
    cube[4][2] = mirror [5][1]
    cube[5][2] = mirror [5][0]
    
    #O in
    cube[3][0] = mirror [3][2]
    cube[3][1] = mirror [4][2]
    cube[3][2] = mirror [5][2]
    answer_key.append(['LF','CCW'])
    anim_grid.append(np.copy(cube))
    
    
    
            
def leftFaceCW(cube):
    Check = True
    mirror = array(cube)
    #always start with Leftmost Facelet
    #   (new) <-- (old)
    # new loc <-- moved to
    #G out
    cube[3][3] = mirror[0][3]
    cube[4][3] = mirror[1][3]
    cube[5][3] = mirror[2][3]
    #R out
    cube[6][3] = mirror[3][3]
    cube[7][3] = mirror[4][3]
    cube[8][3] = mirror[5][3]
    #B out
    cube[9][3] = mirror[6][3]
    cube[10][3] = mirror[7][3]
    cube[11][3] = mirror[8][3]
    #O out
    cube[0][3] = mirror[9][3]
    cube[1][3] = mirror[10][3]
    cube[2][3] = mirror[11][3]
    
    
    #G in
    cube[3][2] = mirror[3][0]
    cube[4][2] = mirror[3][1]
    cube[5][2] = mirror[3][2]
    #R in
    cube[5][2] = mirror[3][2]
    cube[5][1] = mirror[4][2]
    cube[5][0] = mirror[5][2]
    #B in
    cube[5][0] = mirror[5][2]
    cube[4][0] = mirror[5][1]
    cube[3][0] = mirror[5][0]
    #O out
    cube[3][0] = mirror[5][0]
    cube[3][1] = mirror[4][0]
    cube[3][2] = mirror[3][0]
    answer_key.append(['LF','CW'])
    anim_grid.append(np.copy(cube))
    
    
    
            
def backFaceCCW(cube):
    Check = True
    mirror = array(cube)
    #always start with Leftmost Facelet
    #   (new) <-- (old)
    # new loc <-- moved to
            
    #B out
    cube[3][0] = mirror[8][3]
    cube[4][0] = mirror[8][4]
    cube[5][0] = mirror[8][5]
            
    #Y out
    cube[0][5] = mirror[3][0]
    cube[0][4] = mirror[4][0]
    cube[0][3] = mirror[5][0]
            
    #G out
    cube[5][8] = mirror[0][5]
    cube[4][8] = mirror[0][4]
    cube[3][8] = mirror[0][3]
            
    #W out
    cube[8][3] = mirror[5][8]
    cube[8][4] = mirror[4][8]
    cube[8][5] = mirror[3][8]
    
    #B in
    cube[11][3] = mirror[9][3]
    cube[10][3] = mirror[9][4]
    cube[9][3] = mirror[9][5]
            
    #Y in
    cube[11][5] = mirror[11][3]
    cube[11][4] = mirror[10][3]
    cube[11][3] = mirror[9][3]
            
    #G in
    cube[9][5] = mirror[11][5]
    cube[10][5] = mirror[11][4]
    cube[11][5] = mirror[11][3]
            
    #W in
    cube[9][3] = mirror[9][5]
    cube[9][4] = mirror[10][5]
    cube[9][5] = mirror[11][5]
    answer_key.append(['BF','CCW'])
    anim_grid.append(np.copy(cube))
    
    
    
    
def backFaceCW(cube):
    Check = True
    mirror = array(cube)
    #always start with Leftmost Facelet
    #   (new) <-- (old)
    # new loc <-- moved to
        
    #B out
    cube[5][8] = mirror[8][3]
    cube[4][8] = mirror[8][4]
    cube[3][8] = mirror[8][5]
            
    #W out
    cube[0][5] = mirror[5][8]
    cube[0][4] = mirror[4][8]
    cube[0][3] = mirror[3][8]
            
    #G out
    cube[3][0] = mirror[0][5]
    cube[4][0] = mirror[0][4]
    cube[5][0] = mirror[0][3]
            
    #Y out
    cube[8][3] = mirror[3][0]
    cube[8][4] = mirror[4][0]
    cube[8][5] = mirror[5][0]
    
    #B in
    cube[9][5] = mirror[9][3]
    cube[10][5] = mirror[9][4]
    cube[11][5] = mirror[9][5]
            
    #W in
    cube[11][5] = mirror[9][5]
    cube[11][4] = mirror[10][5]
    cube[11][3] = mirror[11][5]
            
    #G in
    cube[11][3] = mirror[11][5]
    cube[10][3] = mirror[11][4]
    cube[9][3] = mirror[11][3]
            
    #Y in
    cube[9][3] = mirror[11][3]
    cube[9][4] = mirror[10][3]
    cube[9][5] = mirror[9][3]
    answer_key.append(['BF','CW'])
    anim_grid.append(np.copy(cube))
    
    
    
def rightFaceCCW(cube):
    Check = True
    mirror = array(cube)
    #always start with Leftmost Facelet
    #   (new) <-- (old)
    # new loc <-- moved to
    
    #G out
    cube[5][5] = mirror[2][5]
    cube[4][5] = mirror[1][5]
    cube[3][5] = mirror[0][5]
        
    #R out
    cube[8][5] = mirror[5][5]
    cube[7][5] = mirror[4][5]
    cube[6][5] = mirror[3][5]
        
    #B out
    cube[11][5] = mirror[8][5]
    cube[10][5] = mirror[7][5]
    cube[9][5] = mirror[6][5]
        
    #O out
    cube[2][5] = mirror[11][5]
    cube[1][5] = mirror[10][5]
    cube[0][5] = mirror[9][5]
    

    #G in
    cube[5][6] = mirror[3][6]
    cube[4][6] = mirror[3][7]
    cube[3][6] = mirror[3][8]
        
    #R in
    cube[5][8] = mirror[5][6]
    cube[5][7] = mirror[4][6]
    cube[5][6] = mirror[3][6]
        
    #B in
    cube[3][8] = mirror[5][8]
    cube[4][8] = mirror[5][7]
    cube[5][8] = mirror[5][6]
        
    #O in
    cube[3][6] = mirror[3][8]
    cube[3][7] = mirror[4][8]
    cube[3][8] = mirror[5][8]
    answer_key.append(['RF','CCW'])
    anim_grid.append(np.copy(cube))

def rightFaceCW(cube):
    Check = True
    mirror = array(cube)
    #always start with Leftmost Facelet
    #   (new) <-- (old)
    # new loc <-- moved to
    #G out
    cube[11][5] = mirror[2][5]
    cube[10][5] = mirror[1][5]
    cube[9][5] = mirror[0][5]
    
    #Y out
    cube[8][5] = mirror[11][5]
    cube[7][5] = mirror[10][5]
    cube[6][5] = mirror[9][5]
    
    #B out
    cube[5][5] = mirror[8][5]
    cube[4][5] = mirror[7][5]
    cube[3][5] = mirror[6][5]
    #R out
    cube[2][5] = mirror[5][5]
    cube[1][5] = mirror[4][5]
    cube[0][5] = mirror[3][5]
    
    #G in
    cube[3][8] = mirror[3][6]
    cube[4][8] = mirror[3][7]
    cube[5][8] = mirror[3][8]
    
    #O in
    cube[5][8] = mirror[3][8]
    cube[5][7] = mirror[4][8]
    cube[5][6] = mirror[5][8]
    #B in
    cube[5][6] = mirror[5][8]
    cube[4][6] = mirror[5][7]
    cube[3][6] = mirror[5][6]
    #R in
    cube[3][6] = mirror[5][6]
    cube[3][7] = mirror[4][6]
    cube[3][8] = mirror[3][6]
    answer_key.append(['RF','CW'])
    anim_grid.append(np.copy(cube))
    
def frontFaceCCW(cube):
    Check = True
    mirror = array(cube)
    #   (new) <-- (old)
    # new loc <-- moved to

    
    #G Out
    cube[5][2] = mirror[2][3]
    cube[4][2] = mirror[2][4]
    cube[3][2] = mirror[2][5]

    #W out
    cube[6][5] = mirror[5][2]
    cube[6][4] = mirror[4][2]
    cube[6][3] = mirror[3][2]
    
    #B out
    cube[3][6] = mirror[6][5]
    cube[4][6] = mirror[6][4]
    cube[5][6] = mirror[6][3]
    
    #Y out
    cube[2][3] = mirror[3][6]
    cube[2][4] = mirror[4][6]
    cube[2][5] = mirror[5][6]
    
    #G in 
    cube[5][3] = mirror[3][3]
    cube[4][3] = mirror[3][4]
    cube[3][3] = mirror[3][5]
    
    #W in
    cube[5][5] = mirror[5][3]
    cube[5][4] = mirror[4][3]
    cube[5][3] = mirror[3][3]
    
    #B in
    cube[3][5] = mirror[5][3]
    cube[4][5] = mirror[5][4]
    cube[5][5] = mirror[5][3]
    
    #Y in 
    cube[3][3] = mirror[3][5]
    cube[3][4] = mirror[4][5]
    cube[3][5] = mirror[5][5]
    answer_key.append(['FF','CCW'])
    anim_grid.append(np.copy(cube))
            
def frontFaceCW(cube):
    Check = True
    mirror = array(cube)
    #   (new) <-- (old)
    # new loc <-- moved to

    
    #G Out
    cube[3][6] = mirror[2][3]
    cube[4][6] = mirror[2][4]
    cube[5][6] = mirror[2][5]

    #W out
    cube[6][5] = mirror[3][6]
    cube[6][4] = mirror[4][6]
    cube[6][3] = mirror[5][6]
    
    #B out
    cube[5][2] = mirror[6][5]
    cube[4][2] = mirror[6][4]
    cube[3][2] = mirror[6][3]
    
    #Y out
    cube[2][3] = mirror[5][2]
    cube[2][4] = mirror[4][2]
    cube[2][5] = mirror[3][2]
    
    #G in 
    cube[3][5] = mirror[3][3]
    cube[4][5] = mirror[3][4]
    cube[5][5] = mirror[3][5]
    
    #W in
    cube[5][5] = mirror[3][5]
    cube[5][4] = mirror[4][5]
    cube[5][3] = mirror[5][5]
    
    #B in
    cube[5][3] = mirror[5][5]
    cube[4][3] = mirror[5][4]
    cube[3][3] = mirror[5][3]
    
    #Y in 
    cube[3][3] = mirror[5][3]
    cube[3][4] = mirror[4][3]
    cube[3][5] = mirror[3][3]
    answer_key.append(['FF','CW'])
    anim_grid.append(np.copy(cube))


def FrameShiftLeft(cube):
    Check = True
    mirror = array(cube)
    
    #TopCW
    #O in
    cube[0][5] = mirror[0][3]
    cube[1][5] = mirror[0][4]
    cube[2][5] = mirror[0][5]
    #W in
    cube[2][5] = mirror[0][5]
    cube[2][4] = mirror[1][5]
    cube[2][3] = mirror[2][5]
    #R in
    cube[2][3] = mirror[2][5]
    cube[1][3] = mirror[2][4]
    cube[0][3] = mirror[2][3]
    #Y in
    cube[0][3] = mirror[2][3]
    cube[0][4] = mirror[1][3]
    cube[0][5] = mirror[0][3]
     
    #BottomCCW
    #R in
    cube[6][5] = mirror[8][5]
    cube[7][5] = mirror[8][4]
    cube[8][5] = mirror[8][3]
    #W in
    cube[8][5] = mirror[8][3]
    cube[8][4] = mirror[7][3]
    cube[8][3] = mirror[6][3]
    #O in
    cube[8][3] = mirror[6][3]
    cube[7][3] = mirror[6][4]
    cube[6][3] = mirror[6][5]
    #Y in
    cube[6][3] = mirror[6][5]
    cube[6][4] = mirror[7][5]
    cube[6][5] = mirror[8][5]  

    #Y<-R
    cube[3][0] = mirror[3][3]
    cube[3][1] = mirror[3][4]
    cube[3][2] = mirror[3][5]

    cube[4][0] = mirror[4][3]
    cube[4][1] = mirror[4][4]
    cube[4][2] = mirror[4][5]

    cube[5][0] = mirror[5][3]
    cube[5][1] = mirror[5][4]
    cube[5][2] = mirror[5][5]
    
    
    #R<-W
    cube[3][3] = mirror[3][6]
    cube[3][4] = mirror[3][7]
    cube[3][5] = mirror[3][8]

    cube[4][3] = mirror[4][6]
    cube[4][4] = mirror[4][7]
    cube[4][5] = mirror[4][8]

    cube[5][3] = mirror[5][6]
    cube[5][4] = mirror[5][7]
    cube[5][5] = mirror[5][8]
    
    
    #W<-O
    cube[3][6] = mirror[11][5]
    cube[3][7] = mirror[11][4]
    cube[3][8] = mirror[11][3]

    cube[4][6] = mirror[10][5]
    cube[4][7] = mirror[10][4]
    cube[4][8] = mirror[10][3]

    cube[5][6] = mirror[9][5]
    cube[5][7] = mirror[9][4]
    cube[5][8] = mirror[9][3]
    
    #O<-Y
    cube[11][5] = mirror[3][0]
    cube[11][4] = mirror[3][1]
    cube[11][3] = mirror[3][2]

    cube[10][5] = mirror[4][0]
    cube[10][4] = mirror[4][1]
    cube[10][3] = mirror[4][2]

    cube[9][5] = mirror[5][0]
    cube[9][4] = mirror[5][1]
    cube[9][3] = mirror[5][2]
    answer_key.append(['FS','L'])
    anim_grid.append(np.copy(cube))
    
    
def FrameShiftUp(cube):
    mirror = array(cube)
    
    #RightFaceCW
    #G in
    cube[3][8] = mirror[3][6]
    cube[4][8] = mirror[3][7]
    cube[5][8] = mirror[3][8]
    
    #O in
    cube[5][8] = mirror[3][8]
    cube[5][7] = mirror[4][8]
    cube[5][6] = mirror[5][8]
    #B in
    cube[5][6] = mirror[5][8]
    cube[4][6] = mirror[5][7]
    cube[3][6] = mirror[5][6]
    #R in
    cube[3][6] = mirror[5][6]
    cube[3][7] = mirror[4][6]
    cube[3][8] = mirror[3][6]
    
    
    #LeftFaceCCW
    #G in
    cube[5][0] = mirror [3][0]
    cube[4][0] = mirror [3][1]
    cube[3][0] = mirror [3][2]
    
    #R in
    cube[5][2] = mirror [5][0]
    cube[5][1] = mirror [4][0]
    cube[5][0] = mirror [3][0]
    
    #B in
    cube[3][2] = mirror [5][2]
    cube[4][2] = mirror [5][1]
    cube[5][2] = mirror [5][0]
    
    #O in
    cube[3][0] = mirror [3][2]
    cube[3][1] = mirror [4][2]
    cube[3][2] = mirror [5][2]
    
    #R^G
    cube[0][3] = mirror[3][3]
    cube[1][3] = mirror[4][3]
    cube[2][3] = mirror[5][3]

    cube[0][4] = mirror[3][4]
    cube[1][4] = mirror[4][4]
    cube[2][4] = mirror[5][4]

    cube[0][5] = mirror[3][5]
    cube[1][5] = mirror[4][5]
    cube[2][5] = mirror[5][5]
    
    #G^O
    cube[9][3] = mirror[0][3]
    cube[10][3] = mirror[1][3]
    cube[11][3] = mirror[2][3]
    
    cube[9][4] = mirror[0][4]
    cube[10][4] = mirror[1][4]
    cube[11][4] = mirror[2][4]
    
    cube[9][5] = mirror[0][5]
    cube[10][5] = mirror[1][5]
    cube[11][5] = mirror[2][5]

    
    #O^B
    cube[6][3] = mirror[9][3]
    cube[7][3] = mirror[10][3]
    cube[8][3] = mirror[11][3]


    cube[6][4] = mirror[9][4]
    cube[7][4] = mirror[10][4]
    cube[8][4] = mirror[11][4]
    
    cube[6][5] = mirror[9][5]
    cube[7][5] = mirror[10][5]
    cube[8][5] = mirror[11][5]

    
    #B^R
    cube[3][3] = mirror[6][3]
    cube[4][3] = mirror[7][3]
    cube[5][3] = mirror[8][3]
    
    
    cube[3][4] = mirror[6][4]
    cube[4][4] = mirror[7][4]
    cube[5][4] = mirror[8][4]
    
    
    cube[3][5] = mirror[6][5]
    cube[4][5] = mirror[7][5]
    cube[5][5] = mirror[8][5]
    answer_key.append(['FS','U'])
    anim_grid.append(np.copy(cube))
    
def FrameShiftCW(cube):
    mirror = array(cube)
    
    #G Out
    cube[3][6] = mirror[2][3]
    cube[4][6] = mirror[2][4]
    cube[5][6] = mirror[2][5]

    #W out
    cube[6][5] = mirror[3][6]
    cube[6][4] = mirror[4][6]
    cube[6][3] = mirror[5][6]
    
    #B out
    cube[5][2] = mirror[6][5]
    cube[4][2] = mirror[6][4]
    cube[3][2] = mirror[6][3]
    
    #Y out
    cube[2][3] = mirror[5][2]
    cube[2][4] = mirror[4][2]
    cube[2][5] = mirror[3][2]
    
    #G in 
    cube[3][5] = mirror[3][3]
    cube[4][5] = mirror[3][4]
    cube[5][5] = mirror[3][5]
    
    #W in
    cube[5][5] = mirror[3][5]
    cube[5][4] = mirror[4][5]
    cube[5][3] = mirror[5][5]
    
    #B in
    cube[5][3] = mirror[5][5]
    cube[4][3] = mirror[5][4]
    cube[3][3] = mirror[5][3]
    
    #Y in 
    cube[3][3] = mirror[5][3]
    cube[3][4] = mirror[4][3]
    cube[3][5] = mirror[3][3]
    
    #B out
    cube[3][0] = mirror[8][3]
    cube[4][0] = mirror[8][4]
    cube[5][0] = mirror[8][5]
            
    #Y out
    cube[0][5] = mirror[3][0]
    cube[0][4] = mirror[4][0]
    cube[0][3] = mirror[5][0]
            
    #G out
    cube[5][8] = mirror[0][5]
    cube[4][8] = mirror[0][4]
    cube[3][8] = mirror[0][3]
            
    #W out
    cube[8][3] = mirror[5][8]
    cube[8][4] = mirror[4][8]
    cube[8][5] = mirror[3][8]
    
    #B in
    cube[11][3] = mirror[9][3]
    cube[10][3] = mirror[9][4]
    cube[9][3] = mirror[9][5]
            
    #Y in
    cube[11][5] = mirror[11][3]
    cube[11][4] = mirror[10][3]
    cube[11][3] = mirror[9][3]
            
    #G in
    cube[9][5] = mirror[11][5]
    cube[10][5] = mirror[11][4]
    cube[11][5] = mirror[11][3]
            
    #W in
    cube[9][3] = mirror[9][5]
    cube[9][4] = mirror[10][5]
    cube[9][5] = mirror[11][5]
    
    #BLA
    cube[3][7] = mirror[1][3]
    cube[4][7] = mirror[1][4]
    cube[5][7] = mirror[1][5]
    
        #BLA
    cube[7][5] = mirror[3][7]
    cube[7][4] = mirror[4][7]
    cube[7][3] = mirror[5][7]
    
        #BLA
    cube[5][1] = mirror[7][5]
    cube[4][1] = mirror[7][4]
    cube[3][1] = mirror[7][3]
    
        #BLA
    cube[1][3] = mirror[5][1]
    cube[1][4] = mirror[4][1]
    cube[1][5] = mirror[3][1]
    answer_key.append(['FS','CW'])
    anim_grid.append(np.copy(cube))

    











    

    
    
    
    
    
    
    
    
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#
#-------------------------------------(Processors)---------------------------------------#
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------# 
    
    
    
    
    

        


















def step1A(cube, scribe):
        answer_key.append(['Step','1A'])
        print ('''
        ----------------------------------------------------------------------------
        ----------------------------------------------------------------------------
        ------------------------------------Step 1A---------------------------------
        ----------------------------------------------------------------------------
        ----------------------------------------------------------------------------
        ''')
        '''Objective is to form a white cross on WW (White) side'''
        randState(cube, scribe)
        trial = {
        1: 'u',
        2: 'd',
        3: 'f',
        4: 'b',
        5: 'r',
        6: 'l'
        }
        #print "Part 1.A.i. loc 47 = ", index_2d(cube,47)
        #print "Part 1.A.i. loc 55 = ", index_2d(cube,55)
    #Part 1.A.i. (finding B/W edge piece and getting that to White Face)
        attempts = 1
        trialType = 1
        found = False
        while not found:
            if attempts == 5:
                for remove in range(4):
                    answer_key.pop()
                attempts = 1
                if trialType < 5:
                    trialType += 1
                if trialType == 5:
                    found = True
            if (findingFace(cube, 47) == 'w') or (findingFace(cube,55) == 'w'):
                found= True
    
            while (attempts < 5) and (found == False):
                #IF YOU DECIDE TO CHANGE THE 2nd argument in action remember that it has tags to the Reitorator Demolisher
                action(trial[trialType],'cw',cube)
                #Condition that looks for B/W facelet on White face    
                if (findingFace(cube, 47) == 'w') or (findingFace(cube,55) == 'w'):
                    #print 'Found!'
                    #print '''47 is on (%s) Face and 55 is on (%s)''' %(findingFace(cube,47), findingFace(cube,55))
                    #print 'trial[%d]' %(trialType)
                    #print 'rotation = ',attempts
                    found = True
                if found == False:
                    attempts +=1
            
            
    #Part 1.A.ii. (Facelet is now on the top, and now corrected to position)
        #print "Part 1.A.ii. loc 47 = ", index_2d(cube,47)
        #print "Part 1.A.ii. loc 55 = ", index_2d(cube,55)
        goodPosition = False
        reiterations = 1
        
        rowFacelet47, colFacelet47 = index_2d(cube,47)
        rowFacelet55, colFacelet55 = index_2d(cube,55)
        #searches to see if facelet is already in position
        if ((rowFacelet47 == 5) or (rowFacelet55 == 5)):
            pass
            
        else:
            #print "Checkpoint A"
            rowFacelet, colFacelet = index_2d(cube,47)
            if colFacelet == 7:
                for i in range(2):
                    action('r', 'cw',cube)
                goodPosition = True       
            while not goodPosition:
                rowFacelet47, colFacelet47 = index_2d(cube,47)
                rowFacelet55, colFacelet55 = index_2d(cube,55)
                if ((rowFacelet47 == 5) or(rowFacelet55 == 5)):
                    goodPosition = True
                    break
                    
                else:
                    rotation = 'cw'
                    action('r',rotation,cube)
                    reiterations+=1
            
            
    #Part 1.A.iii.
        #print "Part 1.A.iii. loc 47 = ", index_2d(cube,47)
        #print "Part 1.A.iii. loc 55 = ", index_2d(cube,55)
        rowFacelet, colFacelet = index_2d(cube,47)
        if rowFacelet == 7:
            bottomFaceCCW(cube)
            rightFaceCCW(cube)
            frontFaceCCW(cube)
            rightFaceCW(cube)
            #check:
            goodPosition = False
            #reiteration of above method in Part1.A.ii
            while not goodPosition:
                rowFacelet47, colFacelet47 = index_2d(cube,47)
                rowFacelet55, colFacelet55 = index_2d(cube,55)
                if (rowFacelet47 == 5):
                    goodPosition = True
                    break
                    
                else:
                    rotation = 'cw'
                    action('r',rotation,cube)
                    reiterations+=1
        else:
            pass
        rowFacelet, colFacelet = index_2d(cube,47)
        if (rowFacelet==5) and (colFacelet == 7):
            print ("Success: Part1.A " )
        else: 
            print ("Failure: Part1.A")
            failure(scribe)
        #print "answer_key[] = ", answer_key
        #printOut(cube)
        step1B(cube,scribe)
        
def step1B(cube,scribe):
        answer_key.append(['Step','1B'])
    #Part 1.B.i.
        print ('''
        ----------------------------------------------------------------------------
        ----------------------------------------------------------------------------
        ------------------------------------Step 1B---------------------------------
        ----------------------------------------------------------------------------
        ----------------------------------------------------------------------------
        ''')
        #Check for other W/Adj on Blue Face
        facelet45 = findingFace(cube, 45)
        facelet65 = findingFace(cube, 65)
        if ((facelet45 == 'b') or (facelet65 == 'b')):
            rowFacelet45, colFacelet45 = index_2d(cube,45)
            rowFacelet65, colFacelet65 = index_2d(cube,65)
            if ((colFacelet45 == 3) or (colFacelet65 == 3)):
                leftFaceCW(cube)
            elif ((rowFacelet45 == 8) or (rowFacelet65 == 8)):
                backFaceCCW(cube)
            else:
                frontFaceCW(cube)
#        if ((facelet45 != 'b') or (facelet65 != 'b')):
#            print "W/O Outside B Face"
#        else:
#            print "Failure: W/O B Face Ejection"
    #Part 1.B.ii
        #Manipulating W/O edge piece to correct Face
        goodPosition = False
        while not goodPosition:
            facelet45 = findingFace(cube, 45)
            facelet65 = findingFace(cube, 65)
            if ((facelet45 == 'w') or (facelet65 == 'w')):
                if (facelet65 == 'o'):
                    goodPosition = True
                    break
                elif (facelet45 == 'o'):
                    backFaceCCW(cube)
                    rightFaceCW(cube)
                    bottomFaceCCW(cube)
                    rightFaceCCW(cube)
                    goodPosition = True
                    break
                elif ((facelet45 == 'g') or (facelet65 == 'g')):
                    for i in range(2):
                        rotation = 'cw'
                        action('u',rotation,cube)
                elif ((facelet45 == 'r') or (facelet65 == 'r')):
                    for i in range(2):
                        rotation = 'cw'
                        action('f',rotation,cube)

                else:
                    rotation = 'cw'
                    action('b',rotation,cube)
            elif((facelet45 == 'o') or (facelet65 == 'o')):
                #If you change 'cw' you have to change the Reitorator Demolisher
                verdict = False
                while not verdict:
                    if ((facelet45 == 'w') or (facelet65 == 'w')):
                        verdict = True
                    else:
                        rotation = 'cw'
                        action('b',rotation,cube)
                        facelet45 = findingFace(cube, 45)
                        facelet65 = findingFace(cube, 65)

                
 
            elif((facelet45 == 'y') or (facelet65 == 'y')):
                rotation = 'cw'
                action('l',rotation,cube)
            elif ((facelet45 == 'r') or (facelet65 == 'r')):
                if ((facelet45 == 'g') or (facelet65 == 'g')):
                    frontFaceCCW(cube)
                    answer_key.append('frontccw')
                
        #printOut(cube)
        #print 'answer_key = ', answer_key
        if index_2d(cube,45) == (4,8):
            print ("Success: Part1.B")
        else: 
            print ("Failure: Part1.B")
            failure(scibe)
        #print "Cube BEFORE: "
        #printOut(cube)
        step1C(cube,scribe)
        
def step1C(cube,scribe): 
        answer_key.append(['Step','1C'])
        print ('''
        ----------------------------------------------------------------------------
        ----------------------------------------------------------------------------
        ------------------------------------Step 1C---------------------------------
        ----------------------------------------------------------------------------
        ----------------------------------------------------------------------------
        ''')
    #Part1.C.i
        goodPosition = False
        while not goodPosition:
            facelet41 = findingFace(cube, 41)
            facelet15 = findingFace(cube, 15)
            if ((facelet41 == 'w') or (facelet15 == 'w')):
                if (facelet15 == 'g'):
                    goodPosition = True
                    break
                elif (facelet41 == 'g'):
                    upperFaceCW(cube)
                    frontFaceCCW(cube)
                    leftFaceCCW(cube)
                    upperFaceCCW(cube)
                    upperFaceCCW(cube)
                    goodPosition = True
                    break
                elif ((facelet41 == 'r') or (facelet15 == 'r')):
                        rotation = 'ccw'
                        action('f',rotation,cube)
                        action('u',rotation,cube)
            elif((facelet41 == 'g') or (facelet15 == 'g')):
                #If you change 'cw' you have to change the Reitorator Demolisher
                verdict = False
                while not verdict:
                    if ((facelet41 == 'w') or (facelet15 == 'w')):
                        verdict = True
                    else:
                        rotation = 'cw'
                        action('u',rotation,cube)
                        facelet41 = findingFace(cube, 41)
                        facelet15 = findingFace(cube, 15)
            
                
            
            elif((facelet41 == 'y') or (facelet15 == 'y')):
                    rotation = 'cw'
                    action('l',rotation,cube)
            elif ((facelet41 == 'b') or (facelet15 == 'b')):
                if ((facelet41 == 'r') or (facelet15 == 'r')):
                    frontFaceCW(cube)
                elif((facelet41 == 'o') or (facelet15 == 'o')):
                    backFaceCCW(cube)
                    leftFaceCW(cube)
                    backFaceCW(cube)

        step1D(cube,scribe)



def step1D(cube,scribe):
    answer_key.append(['Step','1D'])
    print ('''
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ------------------------------------Step 1D---------------------------------
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ''')
    #def Step1D(cube,scribe):
    goodPosition = False
    while not goodPosition:
        facelet43 = findingFace(cube, 43)
        facelet35 = findingFace(cube, 35)
        if ((facelet43 == 'w') or (facelet35 == 'w')):
            if (facelet35 == 'r'):
                goodPosition = True
                break
            elif (facelet43 == 'r'):
                frontFaceCCW(cube)
                upperFaceCW(cube)
                leftFaceCW(cube)
                upperFaceCCW(cube)
                frontFaceCW(cube)
                frontFaceCW(cube)
                goodPosition = True
                break
        elif((facelet43 == 'r') or (facelet35 == 'r')):
            #If you change 'cw' you have to change the Reitorator Demolisher
            verdict = False
            while not verdict:
                if ((facelet43 == 'w') or (facelet35 == 'w')):
                    verdict = True

                else:
                    rotation = 'cw'
                    action('f',rotation,cube)
                    facelet43 = findingFace(cube, 43)
                    facelet35 = findingFace(cube, 35)
        elif((facelet43 == 'y') or (facelet35 == 'y')):
            rotation = 'cw'
            action('l',rotation,cube)
        elif ((facelet43 == 'o') or (facelet35 == 'o')):
            if ((facelet43 == 'b') or (facelet35 == 'b')):
                backFaceCCW(cube)
                leftFaceCW(cube)
                leftFaceCW(cube)
                backFaceCW(cube)
            else:#green
                upperFaceCCW(cube)
                leftFaceCW(cube)
                upperFaceCW(cube)
    #printOut(cube)
            
                            
def step2A(cube):
    answer_key.append(['Step','2A'])
    #Corner pieces have 3 facelets
        
            #    # WOB 48,62,58
    #    f48 = facelet_detail(cube,48)
    #    f62 = facelet_detail(cube,62)
    #    f58 = facelet_detail(cube,58) 
    print ('''
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ------------------------------------Step 2A---------------------------------
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ''')
    #shifting frame reference so that white is in the center
    FrameShiftLeft(cube)
    scribe.append('FSL:WHITE')
    goodPosition = False
    #printOut(cube)
    while not goodPosition:   
    
        #perfect scenario
        if (findingFace(cube,48) == 'w') and (findingFace(cube,42)=='w') and (findingFace(cube,40) == 'w'):
            #print 'wrong loop'
            goodPosition = True
            break
        
        #Objective: to find if corner piece BOW is on white face and if it is, relocates cublete to bottom face
        if (index_2d(cube,48) == (3,5)) or (index_2d(cube,62) == (3,5)) or (index_2d(cube,58) == (3,5)):
            rightFaceCW(cube)
            backFaceCW(cube)
            rightFaceCCW(cube)
        elif (index_2d(cube,48) == (3,3)) or (index_2d(cube,62) == (3,3)) or (index_2d(cube,58)==(3,3)):
            leftFaceCCW(cube)
            backFaceCW(cube)
            leftFaceCW(cube)
        elif (index_2d(cube,48) == (5,5)) or (index_2d(cube,62) == (5,5)) or (index_2d(cube,58) == (5,5)):
            rightFaceCCW(cube)
            backFaceCW(cube)
            rightFaceCW(cube)
        elif (index_2d(cube,48) == (5,3)) or (index_2d(cube,62) == (5,3)) or (index_2d(cube,58)==(5,3)):
            leftFaceCW(cube)
            backFaceCW(cube)
            leftFaceCCW(cube)
        else:
            pass
        
        pass
        #Objective: Cublete is on bottom face, we will now align it to target position on white face
        counter = 1
        while True:
            #printOut(cube)
            #print "finding face:",'48 = ', findingFace(cube,48),'58 = ',findingFace(cube,58),'62 = ',findingFace(cube,62)
            if (findingFace(cube,48) =='b') or (findingFace(cube,58)=='b') or (findingFace(cube,62) == 'b') :
                #print 'inside'
                if (index_2d(cube,48)[1] == 5) or (index_2d(cube,58)[1] == 5) or (index_2d(cube,62)[1] == 5):
                    break
                else:
                    backFaceCW(cube)
            else:
                backFaceCW(cube)
            if counter == 4:
                break
            else:
                pass
            counter +=1
            #print counter
        goodPosition = True
            ##all corners in correct position but not orientation
            #elif(facelet46 or facelet52 or facelet38 == 'w'):
            #    if(facelet48 or facelet62 or facelet58 == 'w'):
            #        if(facelet42 or facelet68 or facelet12 == 'w'):
            #            if(facelet40 or facelet18 or facelet32 == 'w'):
            #                rightFaceCCW(cube)
            #                bottomFaceCW(cube)
            #                rightFaceCW(cube)
            #    
        
    #printOut(cube)
    #Objective: now that cublet is in place, apply algroithm
    while True:
        rightFaceCCW(cube)
        backFaceCCW(cube)
        rightFaceCW(cube)
        if (findingFace(cube,48) == 'w'):
            break
        else:
            backFaceCW(cube)
    #printOut(cube)
    step2B(cube)
    
    
def step2B(cube):
    answer_key.append(['Step','2B'])
    #    # WOG 42,68,12
    #    f42 = facelet_detail(cube,42)
    #    f68 = facelet_detail(cube,68)
    #    f12 = facelet_detail(cube,12) 
    print ('''
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ------------------------------------Step 2B---------------------------------
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ''')
    #shifting frame reference so that white is in the center
    FrameShiftCW(cube)
    goodPosition = False
    #printOut(cube)
    while not goodPosition:   
        
        #Objective: to find if corner piece BOW is on white face and if it is, relocates cublete to bottom face
        if (index_2d(cube,42) == (3,5)) or (index_2d(cube,68) == (3,5)) or (index_2d(cube,12) == (3,5)):
            rightFaceCW(cube)
            backFaceCW(cube)
            rightFaceCCW(cube)
        elif (index_2d(cube,42) == (3,3)) or (index_2d(cube,68) == (3,3)) or (index_2d(cube,12)==(3,3)):
            leftFaceCCW(cube)
            backFaceCW(cube)
            leftFaceCW(cube)
        elif (index_2d(cube,42) == (5,5)) or (index_2d(cube,68) == (5,5)) or (index_2d(cube,12) == (5,5)):
            rightFaceCCW(cube)
            backFaceCW(cube)
            rightFaceCW(cube)
        elif (index_2d(cube,42) == (5,3)) or (index_2d(cube,68) == (5,3)) or (index_2d(cube,12)==(5,3)):
            leftFaceCW(cube)
            backFaceCW(cube)
            leftFaceCCW(cube)
        else:
            pass
        
        pass
        #Objective: Cublete is on bottom face, we will now align it to target position on white face
        counter = 1
        while True:
            #printOut(cube)
            #print "finding face:",'42 = ', findingFace(cube,42),'68 = ',findingFace(cube,68),'12 = ',findingFace(cube,12)
            if (findingFace(cube,42) =='o') or (findingFace(cube,68)=='o') or (findingFace(cube,12) == 'o') :
                #print 'inside'
                if (index_2d(cube,42)[1] == 5) or (index_2d(cube,68)[1] == 5) or (index_2d(cube,12)[1] == 5):
                    break
                else:
                    backFaceCW(cube)
            else:
                backFaceCW(cube)
            if counter == 4:
                break
            else:
                pass
            counter +=1
            #print counter
        goodPosition = True

        
    #printOut(cube)
    #Objective: now that cublet is in place, apply algroithm
    while True:
        rightFaceCCW(cube)
        backFaceCCW(cube)
        rightFaceCW(cube)
        if (findingFace(cube,42) == 'w'):
            break
        else:
            backFaceCW(cube)
    #printOut(cube)
    step2C(cube)
    
def step2C(cube):
    answer_key.append(['Step','2C'])
    #    # WGR 40,18,32
    #    f40 = facelet_detail(cube,40)
    #    f18 = facelet_detail(cube,18)
    #    f32 = facelet_detail(cube,32) 
    print ('''
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ------------------------------------Step 2C---------------------------------
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ''')
    #shifting frame reference so that white is in the center
    FrameShiftCW(cube)
    goodPosition = False
    #printOut(cube)
    while not goodPosition:   
        
        #Objective: to find if corner piece BOW is on white face and if it is, relocates cublete to bottom face
        if (index_2d(cube,40) == (3,5)) or (index_2d(cube,18) == (3,5)) or (index_2d(cube,32) == (3,5)):
            rightFaceCW(cube)
            backFaceCW(cube)
            rightFaceCCW(cube)
        elif (index_2d(cube,40) == (3,3)) or (index_2d(cube,18) == (3,3)) or (index_2d(cube,32)==(3,3)):
            leftFaceCCW(cube)
            backFaceCW(cube)
            leftFaceCW(cube)
        elif (index_2d(cube,40) == (5,5)) or (index_2d(cube,18) == (5,5)) or (index_2d(cube,32) == (5,5)):
            rightFaceCCW(cube)
            backFaceCW(cube)
            rightFaceCW(cube)
        elif (index_2d(cube,40) == (5,3)) or (index_2d(cube,18) == (5,3)) or (index_2d(cube,32)==(5,3)):
            leftFaceCW(cube)
            backFaceCW(cube)
            leftFaceCCW(cube)
        else:
            pass
        
        pass
        #Objective: Cublete is on bottom face, we will now align it to target position on white face
        counter = 1
        while True:
            #printOut(cube)
            #print "finding face:",'40 = ', findingFace(cube,40),'18 = ',findingFace(cube,18),'32 = ',findingFace(cube,32)
            if (findingFace(cube,40) =='g') or (findingFace(cube,18)=='g') or (findingFace(cube,32) == 'g') :
                #print 'inside'
                if (index_2d(cube,40)[1] == 5) or (index_2d(cube,18)[1] == 5) or (index_2d(cube,32)[1] == 5):
                    break
                else:
                    backFaceCW(cube)
            else:
                backFaceCW(cube)
            if counter == 4:
                break
            else:
                pass
            counter +=1
            #print counter
        goodPosition = True

        
    #printOut(cube)
    #Objective: now that cublet is in place, apply algroithm
    while True:
        rightFaceCCW(cube)
        backFaceCCW(cube)
        rightFaceCW(cube)
        if (findingFace(cube,40) == 'w'):
            break
        else:
            backFaceCW(cube)
    #printOut(cube)
    step2D(cube)
    

def step2D(cube):
    answer_key.append(['Step','2D'])
    #    # WBR 46,52,38
    #    f46 = facelet_detail(cube,46)
    #    f52 = facelet_detail(cube,52)
    #    f38 = facelet_detail(cube,38)  
    print ('''
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ------------------------------------Step 2D---------------------------------
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ''')
    #shifting frame reference so that white is in the center
    FrameShiftCW(cube)
    goodPosition = False
    #printOut(cube)
    while not goodPosition:   
        
        #Objective: to find if corner piece BOW is on white face and if it is, relocates cublete to bottom face
        if (index_2d(cube,46) == (3,5)) or (index_2d(cube,52) == (3,5)) or (index_2d(cube,38) == (3,5)):
            rightFaceCW(cube)
            backFaceCW(cube)
            rightFaceCCW(cube)
        elif (index_2d(cube,46) == (3,3)) or (index_2d(cube,52) == (3,3)) or (index_2d(cube,38)==(3,3)):
            leftFaceCCW(cube)
            backFaceCW(cube)
            leftFaceCW(cube)
        elif (index_2d(cube,46) == (5,5)) or (index_2d(cube,52) == (5,5)) or (index_2d(cube,38) == (5,5)):
            rightFaceCCW(cube)
            backFaceCW(cube)
            rightFaceCW(cube)
        elif (index_2d(cube,46) == (5,3)) or (index_2d(cube,52) == (5,3)) or (index_2d(cube,38)==(5,3)):
            leftFaceCW(cube)
            backFaceCW(cube)
            leftFaceCCW(cube)
        else:
            pass
        
        pass
        #Objective: Cublete is on bottom face, we will now align it to target position on white face
        counter = 1
        while True:
            #printOut(cube)
            #print "finding face:",'46 = ', findingFace(cube,46),'52 = ',findingFace(cube,52),'38 = ',findingFace(cube,38)
            if (findingFace(cube,46) =='r') or (findingFace(cube,52)=='r') or (findingFace(cube,38) == 'r') :
                #print 'inside'
                if (index_2d(cube,46)[1] == 5) or (index_2d(cube,52)[1] == 5) or (index_2d(cube,38)[1] == 5):
                    break
                else:
                    backFaceCW(cube)
            else:
                backFaceCW(cube)
            if counter == 4:
                break
            else:
                pass
            counter +=1
            #print counter
        goodPosition = True

        
    #printOut(cube)
    #Objective: now that cublet is in place, apply algroithm
    while True:
        rightFaceCCW(cube)
        backFaceCCW(cube)
        rightFaceCW(cube)
        if (findingFace(cube,46) == 'w'):
            break
        else:
            backFaceCW(cube)
    #printOut(cube)
    FrameShiftUp(cube)
    FrameShiftUp(cube)
    FrameShiftUp(cube)
    #printOut(cube)
    step3(cube)

def step3(cube):
    answer_key.append(['Step','3'])
    print ('''
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ------------------------------------Step 3---------------------------------
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ''')
    
    while True:
        #if perfect
        if (facelet_color(cube[4][0]) == facelet_color(cube[4][1])) and (facelet_color(cube[4][2]) == facelet_color(cube[4][1])) and (facelet_color(cube[4][3]) == facelet_color(cube[4][4])) and (facelet_color(cube[4][5]) == facelet_color(cube[4][4])) and (facelet_color(cube[4][6]) == facelet_color(cube[4][7])) and (facelet_color(cube[4][8]) == facelet_color(cube[4][7])) and (facelet_color(cube[10][3]) == facelet_color(cube[10][4])) and (facelet_color(cube[10][5]) == facelet_color(cube[10][4])):
            break
        # if the top cubelet on current face is non-yellow, 
        # it will find a face to match it,then place it
        elif (facelet_color(cube[2][4]) != 'y') and (facelet_color(cube[3][4])!='y'):
            if (facelet_color(cube[3][4]) == facelet_color(cube[4][4])):
                if (facelet_color(cube[2][4]) == facelet_color(cube[4][1])) :
                #left side
                    upperFaceCCW(cube)
                    leftFaceCCW(cube)
                    upperFaceCW(cube)
                    leftFaceCW(cube)
                    upperFaceCW(cube)
                    frontFaceCW(cube)
                    upperFaceCCW(cube)
                    frontFaceCCW(cube)
                elif(facelet_color(cube[2][4]) == facelet_color(cube[4][7])):
                #right side
                    upperFaceCW(cube)
                    rightFaceCW(cube)
                    upperFaceCCW(cube)
                    rightFaceCCW(cube)
                    upperFaceCCW(cube)
                    frontFaceCCW(cube)
                    upperFaceCW(cube)
                    frontFaceCW(cube)
            elif (facelet_color(cube[3][4]) == facelet_color(cube[4][1])):
                upperFaceCW(cube)
                FrameShiftLeft(cube)
                FrameShiftLeft(cube)
                FrameShiftLeft(cube)
            elif (facelet_color(cube[3][4]) == facelet_color(cube[10][4])):
                upperFaceCW(cube)
                upperFaceCW(cube)
                FrameShiftLeft(cube)
                FrameShiftLeft(cube)
            elif (facelet_color(cube[3][4]) == facelet_color(cube[4][7])):
                upperFaceCCW(cube)
                FrameShiftLeft(cube)
        #check to see if there is any upper options remaining, and rotate upper face
        elif ((facelet_color(cube[3][1])!='y') and (facelet_color(cube[1][3])!='y'))     or     ((facelet_color(cube[0][4])!='y') and (facelet_color(cube[11][4])!='y'))    or     ((facelet_color(cube[1][5])!='y') and (facelet_color(cube[3][7])!='y')):
            if (facelet_color(cube[3][1])!='y') and (facelet_color(cube[1][3])!='y'):
                upperFaceCCW(cube)
            elif (facelet_color(cube[0][4])!='y') and (facelet_color(cube[11][4])!='y'):
                upperFaceCW(cube) 
                upperFaceCW(cube)
            else:
                upperFaceCW(cube)
        #purging: else check to see if any edge pieces on current face are non-yellow
        else:
            if (facelet_color(cube[4][2])!='y') and (facelet_color(cube[4][3]) != 'y'):
                #left side
                upperFaceCCW(cube)
                leftFaceCCW(cube)
                upperFaceCW(cube)
                leftFaceCW(cube)
                upperFaceCW(cube)
                frontFaceCW(cube)
                upperFaceCCW(cube)
                frontFaceCCW(cube)
            elif (facelet_color(cube[4][5])!='y') and (facelet_color(cube[4][6]) !='y'):
                #right side
                upperFaceCW(cube)
                rightFaceCW(cube)
                upperFaceCCW(cube)
                rightFaceCCW(cube)
                upperFaceCCW(cube)
                frontFaceCCW(cube)
                upperFaceCW(cube)
                frontFaceCW(cube)
            else:
                FrameShiftLeft(cube)
        #printOut(cube)
    #printOut(cube)
    step4A(cube)


def step4A(cube):
    answer_key.append(['Step','4A'])
    print ('''
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ------------------------------------Step 4A---------------------------------
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ''')
    while True:
        #state 1
        if (facelet_color(cube[1][3])=='y') and (facelet_color(cube[1][5])=='y') and (facelet_color(cube[0][4])=='y') and (facelet_color(cube[2][4])=='y'):
            break
        #state 2
        elif (facelet_color(cube[1][3])!='y') and (facelet_color(cube[1][5])!='y') and (facelet_color(cube[0][4])!='y') and (facelet_color(cube[2][4])!='y'):
            frontFaceCW(cube)
            upperFaceCW(cube)
            rightFaceCW(cube)
            upperFaceCCW(cube)
            rightFaceCCW(cube)
            frontFaceCCW(cube)
        #state 4
        elif ((facelet_color(cube[1][3])=='y') and (facelet_color(cube[1][5])=='y')) or ((facelet_color(cube[0][4])=='y') and (facelet_color(cube[2][4])=='y')):
            if ((facelet_color(cube[1][3])=='y') and (facelet_color(cube[1][5])=='y')):
                pass
            else:
                upperFaceCW(cube)   
            frontFaceCW(cube)
            rightFaceCW(cube)
            upperFaceCW(cube)
            rightFaceCCW(cube)
            upperFaceCCW(cube)
            frontFaceCCW(cube)
        #state 3
        else:
            for _ in range(4):
                if (facelet_color(cube[0][4]) == 'y') and (facelet_color(cube[1][3]) == 'y'):
                    break
                else:
                    upperFaceCW(cube)
            frontFaceCW(cube)
            upperFaceCW(cube)
            rightFaceCW(cube)
            upperFaceCCW(cube)
            rightFaceCCW(cube)
            frontFaceCCW(cube)
    #printOut(cube)
    step4B(cube)
    
def step4B(cube):
    answer_key.append(['Step','4B'])
    print ('''
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ------------------------------------Step 4B---------------------------------
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ''')

    while True:
        corners_yellow = 0
        if (facelet_color(cube[0][3]) == 'y'):
            corners_yellow+=1
            #print "cube[0][3] = y"
        if (facelet_color(cube[0][5]) == 'y'):
            corners_yellow+=1
            #print "cube[0][5] = y"
        if (facelet_color(cube[2][3]) == 'y'):
            corners_yellow+=1
            #print "cube[2][3] = y"
        if (facelet_color(cube[2][5]) == 'y'):
            corners_yellow+=1
            #print "cube[2][5] = y"
        #print "Corners Yellow = ", corners_yellow
        
        if corners_yellow == 4:
            break
        #state 1
        elif corners_yellow == 0:
            for _ in range(4):
                if (facelet_color(cube[3][2]) == 'y'):
                    break
                else:
                    upperFaceCW(cube)
            #algorithm
        #state 2
        elif corners_yellow == 1:
            for _ in range(4):
                if (facelet_color(cube[2][3]) == 'y'):
                    break
                else:
                    upperFaceCW(cube)
            #algorithm
        elif corners_yellow == 2:
            for _ in range(4):
                if (facelet_color(cube[3][3]) == 'y'):
                    break
                else:
                    upperFaceCW(cube)
            print
        rightFaceCW(cube)
        upperFaceCW(cube)
        rightFaceCCW(cube)
        upperFaceCW(cube)
        rightFaceCW(cube)
        upperFaceCW(cube)
        upperFaceCW(cube)
        rightFaceCCW(cube)
    #1 #printOut(cube)
    step5A(cube)

def step5A(cube):
    answer_key.append(['Step','5A'])
    print ('''
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ------------------------------------Step 5A---------------------------------
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ''')
    #print"Before WHILE 1"
    #while True:
    #    correct_corners = 0
    #    if (facelet_color(cube[3][3]) == facelet_color(cube[4][4])):
    #        correct_corners+=1
    #    if (facelet_color(cube[3][5]) == facelet_color(cube[4][4])):
    #        correct_corners+=1
    #    if (facelet_color(cube[11][3]) == facelet_color(cube[10][4])):
    #        correct_corners+=1
    #    if (facelet_color(cube[11][5]) == facelet_color(cube[10][4])):
    #        correct_corners+=1
    #    if correct_corners<=2:
    #        break
    #    else:
    #        upperFaceCW(cube)
    #printOut(cube)
    #print"After While 1"

    correct_corner = 0
    #print "Before While 2"
    rot=0
    while True:
        if (facelet_color(cube[3][0]) == facelet_color(cube[4][1])) and (facelet_color(cube[3][2]) == facelet_color(cube[4][1])):
            correct_corner+=1
            FrameShiftLeft(cube)
        elif (facelet_color(cube[3][3]) == facelet_color(cube[4][4])) and (facelet_color(cube[3][5]) == facelet_color(cube[4][4])):
            correct_corner+=1
            FrameShiftLeft(cube)
            FrameShiftLeft(cube)
        elif (facelet_color(cube[3][6]) == facelet_color(cube[4][7])) and (facelet_color(cube[3][8]) == facelet_color(cube[4][7])):
            correct_corner+=1
            FrameShiftLeft(cube)
            FrameShiftLeft(cube)
            FrameShiftLeft(cube)
        elif (facelet_color(cube[11][3]) == facelet_color(cube[10][4])) and (facelet_color(cube[11][5]) == facelet_color(cube[10][4])):
            correct_corner+=1
        else:
            rot+=1
            upperFaceCW(cube)
        if correct_corner == 1:
            break
        if rot == 4:
                rightFaceCCW(cube)
                frontFaceCW(cube)
                rightFaceCCW(cube)
                backFaceCW(cube)
                backFaceCW(cube)
                rightFaceCW(cube)
                frontFaceCCW(cube)
                rightFaceCCW(cube)
                backFaceCW(cube)
                backFaceCW(cube)
                rightFaceCW(cube)
                rightFaceCW(cube)
                upperFaceCCW(cube)
    correct_corner = 0
    if (facelet_color(cube[3][0]) == facelet_color(cube[4][1])) and (facelet_color(cube[3][2]) == facelet_color(cube[4][1])):
        correct_corner+=1
    if (facelet_color(cube[3][3]) == facelet_color(cube[4][4])) and (facelet_color(cube[3][5]) == facelet_color(cube[4][4])):
        correct_corner+=1
    if (facelet_color(cube[3][6]) == facelet_color(cube[4][7])) and (facelet_color(cube[3][8]) == facelet_color(cube[4][7])):
        correct_corner+=1
    if (facelet_color(cube[11][3]) == facelet_color(cube[10][4])) and (facelet_color(cube[11][5]) == facelet_color(cube[10][4])):
        correct_corner+=1
    if correct_corner !=4:
        #print "After While 2"
        rightFaceCCW(cube)
        frontFaceCW(cube)
        rightFaceCCW(cube)
        backFaceCW(cube)
        backFaceCW(cube)
        rightFaceCW(cube)
        frontFaceCCW(cube)
        rightFaceCCW(cube)
        backFaceCW(cube)
        backFaceCW(cube)
        rightFaceCW(cube)
        rightFaceCW(cube)
        upperFaceCCW(cube)
    #1 printOut(cube)
   # IF ALL GOES ACCORDING TO PLAN, THEN WE SHOULD ALWAYS HAVE AT LEAST TWO CORRECT POSITIONS
   # IF two corners are correct and diagonal, apply algorithm as is, 
   #     then orient upper face to align those two corners to correct orientation
   # Make sure correct corners are in the back,
   #    then apply algorithm
   # Orient corners to correct orientation
    step5B(cube)
def step5B(cube):
    answer_key.append(['Step','5B'])
    print ('''
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ------------------------------------Step 5B---------------------------------
    ----------------------------------------------------------------------------
    ----------------------------------------------------------------------------
    ''')
    incorrect_corners = 0
    while True:
        #if peferct
        if (facelet_color(cube[3][1]) == facelet_color(cube[4][1])) and (facelet_color(cube[3][4]) == facelet_color(cube[4][4])) and (facelet_color(cube[3][7]) == facelet_color(cube[4][7])) and (facelet_color(cube[11][4]) == facelet_color(cube[10][4])):
            break
        #putting correct corner in back
        elif (facelet_color(cube[3][1]) == facelet_color(cube[4][1])) or (facelet_color(cube[3][4]) == facelet_color(cube[4][4])) or (facelet_color(cube[3][7]) == facelet_color(cube[4][7])) or (facelet_color(cube[11][4]) == facelet_color(cube[10][4])):
            if (facelet_color(cube[3][1]) == facelet_color(cube[4][1])):
                FrameShiftLeft(cube)
            elif (facelet_color(cube[3][4]) == facelet_color(cube[4][4])):
                FrameShiftLeft(cube)
                FrameShiftLeft(cube)
            elif (facelet_color(cube[3][7]) == facelet_color(cube[4][7])):
                FrameShiftLeft(cube)
                FrameShiftLeft(cube)
                FrameShiftLeft(cube)
            elif (facelet_color(cube[11][4]) == facelet_color(cube[10][4])):
                pass
        #no corners are good
        else: 
            frontFaceCW(cube)
            frontFaceCW(cube)
            upperFaceCW(cube)
            leftFaceCW(cube)
            rightFaceCCW(cube)
            frontFaceCW(cube)
            frontFaceCW(cube)
            leftFaceCCW(cube)
            rightFaceCW(cube)
            upperFaceCW(cube)
            frontFaceCW(cube)
            frontFaceCW(cube)
            
        if (facelet_color(cube[3][1]) == facelet_color(cube[4][4])):
            frontFaceCW(cube)
            frontFaceCW(cube)
            upperFaceCCW(cube)
            leftFaceCW(cube)
            rightFaceCCW(cube)
            frontFaceCW(cube)
            frontFaceCW(cube)
            leftFaceCCW(cube)
            rightFaceCW(cube)
            upperFaceCCW(cube)
            frontFaceCW(cube)
            frontFaceCW(cube)
        elif (facelet_color(cube[3][7]) == facelet_color(cube[4][4])):
            frontFaceCW(cube)
            frontFaceCW(cube)
            upperFaceCW(cube)
            leftFaceCW(cube)
            rightFaceCCW(cube)
            frontFaceCW(cube)
            frontFaceCW(cube)
            leftFaceCCW(cube)
            rightFaceCW(cube)
            upperFaceCW(cube)
            frontFaceCW(cube)
            frontFaceCW(cube)
    printOut(cube, 'Randomized Cube - [Solved] [After State]')
   

        
    
# reminder: 
#
# green      10's               G
# yellow     20's           Y   R   W
# red        30's               B
# white      40's               O
# blue       50's
# orange     60's'
















#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#
#-------------------------------------(Modifiers)----------------------------------------#
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------# 
















def facelet_color(num):
    if (num<=18):
        color = 'g'
    elif (num>18) and (num<=28):
        color = 'y'
    elif (num>28) and (num<=38):
        color = 'r'
    elif (num>38) and (num<=48):
        color = 'w'
    elif (num>48) and (num<=58):
        color = 'b'
    elif (num>58) and (num<=68):
        color = 'o'
    else:
        pass
    return color
            
def randState(cube, scribe):
    del(answer_key[0:randStateMoves])
    face = {
    1: 'u',
    2: 'd',
    3: 'f',
    4: 'b',
    5: 'r',
    6: 'l'
    }
    rot = {
    1: 'cw',
    2: 'ccw'
    }
    rd.seed(seedling)
    #sampled 1-> 35   ; v5.1.0 problem: NONE
    #sampled 1-> 10  ; v4.1.0 problem: NONE
    #sampled 1-> 40  ; v3.1.0 problem: NONE
    for reiterations in range(randStateMoves):
        randFace = rd.randint(1,6)
        randRot = randint(1,2)
        scribe[0].append(face[randFace])
        scribe[1].append(rot[randRot])
        action(face[randFace], rot[randRot], cube)
    del(answer_key[0:randStateMoves])
        
    printOut(cube, 'Randomized Cube - [Unsolved] [Before State]')
    #print scribe
    return scribe


def failure(scribe):
    '''Documents (failed) runs, but it is up to the user to execute this function for documentation.\n
    Scribe refers to the initial state of the cube after randState Function'''
    scribe
    #POF stands for Point of failure
    
    #POF for new running on new computer
    #for first time change 'a' to 'w'
    f = open('/Users/bedj2/Documents/Programming/Python/Rubiks/POF.txt', 'a+')
    #dimscribe = (number of row, number of col)
    dimScribe = shape(scribe)
    
    lines = 0
    for line in open('/Users/bedj2/Documents/Programming/Python/Rubiks/POF.txt'):
        lines += 1
    print ("lines = ",lines)
    errorNum = (lines/(randStateMoves+2)) +1
    print ("errorNum = ", errorNum)
    
    for j in range(dimScribe[1]):
        if j ==0:
            f.write('#Error %d\n' %(errorNum))
            f.write('#face, row\n')
        f.write('%s, %s\n' % (scribe[0][j], scribe[1][j]))
    f.close()
    
def error(num,cube):
    '''Pulls up documented errors from "Rubiks" folder\n
    (desired error #, cube)'''
    if num >= 1:
        skip = (num-1)*(randStateMoves+2)
    else:
        skip = 0
    #print "skip = ", skip
    #http://stackoverflow.com/questions/34294742/numpy-mismatch-in-size-of-old-and-new-data-descriptor
    pof = genfromtxt('/Users/bedj2/Documents/School/Physics/Physics 40/Rubiks/POF.txt', 
                skip_header = skip,delimiter = ', ', dtype = [('face','S1'),('rot', 'S4')],
                comments = '#')
    pof = pof.tolist()        
    pofList = []
    pofList.append([])
    pofList.append([])
    #print "length of 'pof' before= ", len(pof)
    flag = False
    if len(pof) > randStateMoves:
        space = randStateMoves
        flag = True
    else:
        space = 0 
    for i in range(len(pof)-space):
        if flag == True:
            pof.pop()
        for j in range(2):
            pofList[j].append(pof[i][j])
    #print pof

    #print "length of 'pof' after= ", len(pof)
    #print "shape of 'pof' = ", shape(pof)
    #print "pofList = ", pofList
    #action(pofList[:,0], pofList[,:], cube)
    return pofList
    
    
        
def maniState(cube):
    '''Stands for Manipulated State; In this state the
    cube is configured to the called rotating functions'''
    #Cube can be rotated from solved state to desired state.
    
    #Desired State:
    rightFaceCW(cube)
    frontFaceCW(cube)
    leftFaceCCW(cube)
    
    print ('maniState(cube) = ')
    printOut(cube)
    
def manualMode(cube):
    '''This mode allows for a manual manipulation of the cube in Console'''
    
    tries = 0
    while True:
        
        face = raw_input('What Face? ')
        if face.lower() == ('e' or 'exit'):
            break
        rotation = raw_input('Rotation? ')
        if rotation.lower() == ('e' or 'exit'):
            break
    
        action(face, rotation, cube)
        printOut(cube)
        
        ###########################################idea#
        #if bla == True:
        #    blala = True
        #else:
        #    print "Please enter Valid input"
        #    print "
        #    if tries >=1:
        #        print "Integers only"
        #    if tries >=2:
        #        print "example: 85,90,101"
        #    tries+=1
        ################################################

    


def action(face,rot,cube):
    face_dictionary = {
    'r': 'right',
    'l': 'left',
    'f': 'front',
    'b': 'back',
    'u': 'upper',
    'd': 'bottom',
    
    'right' : 'right',
    'left': 'left',
    'front' : 'front',
    'back': 'back',
    'top': 'upper',
    'up': 'upper',
    'upper': 'upper',
    'bot': 'bottom',
    'bottom': 'bottom',
    'low': 'bottom',
    'lower': ' bottom',
     
    }
    
    rot_dictionary = {
    'ccw': 'ccw',
    'i': 'ccw',
    
    'cw': 'cw',
    '': 'cw'
    }
    
    face1 = face.lower()
    rot1 = rot.lower()
    
    face_ans = face_dictionary[face1]
    rot_ans = rot_dictionary[rot1]
    
    print (face_ans, rot_ans)
    
    if face_ans == 'right':
        if rot_ans == 'cw':
            rightFaceCW(cube)
        else:
            rightFaceCCW(cube)
    elif face_ans == 'left':
        if rot_ans == 'cw':
            leftFaceCW(cube)
        else:
            leftFaceCCW(cube)
    elif face_ans == 'front':
        if rot_ans == 'cw':
            frontFaceCW(cube)
        else:
            frontFaceCCW(cube)
    elif face_ans == 'back':
        if rot_ans == 'cw':
            backFaceCW(cube)
        else:
            backFaceCCW(cube)
    elif face_ans == 'upper':
        if rot_ans == 'cw':
            upperFaceCW(cube)
        else:
            upperFaceCCW(cube)
    elif face_ans == 'bottom':
        if rot_ans == 'cw':
            bottomFaceCW(cube)
        else:
            bottomFaceCCW(cube)
    return face_ans, rot_ans
            
def findingFace(cube,num):
    '''This version of findingFace accounts for the rotation of the faces
         To find the focal the facelet location to a face the regions are defined
         as follows:
             [1]            [x-1,y-1]  [x-1,y]  [x-1,y+1]
          [2][3][4]          [x,y-1]    [x,y]    [x,y+1]
             [5]            [x+1,y-1]  [x+1,y]  [x+1,y+1]
             [6]
             
             checks the surrounding facelets for the center facelets color identity
             '''
    #Center facelets will always be in 1/6 spots
    face_identity = {
        14:'g',
        24:'y',
        34:'r',
        44:'w',
        54:'b',
        64:'o',
        }
    try:
       return face_identity[num]
    except:
        centers = [[1,4], [4,1],[4,4],[4,7],[7,4],[10,4]]
        row, col = index_2d(cube,num) 
        for x,y in centers:
            try: 
                if ((x-1) == row) and ((y-1) == col):
                    break
            except:
                pass
            try:
                if ((x-1) == row) and (y == col):
                    break
            except:
                pass
            try:
                if ((x-1) == row) and ((y+1) == col):
                    break
            except:
                pass
            try:
                if (x == row) and ((y+1) == col):
                    break
            except:
                pass
            try:
                if ((x+1) == row) and ((y+1) == col):
                    break
            except:
                pass
            try:
                if ((x+1) == row) and (y == col):
                    break
            except:
                pass
            try:
                if ((x+1)== row) and ((y-1) == col):
                    break
            except:
                pass
            try:
                if (x == row) and ((y-1) == col):
                    break
            except:
                pass
        return face_identity[cube[x][y]]
        
            
def index_2d(myList, v):
    '''Main Search Function of finding exact index of desired number "v"'''
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))
            
def printOut(cube, header = ''):
    '''Prints'''
    mirror = array(cube)
    for i in range(12):
        print (mirror[i,:])
    grid = np.zeros(np.shape(mirror))
    for i in range(np.shape(mirror)[0]):
        #           G = 79
        # Y = 136  R = 191   W =255
        #           B = 31
        #           O = 169
        for j in range(np.shape(mirror)[1]):
            if (mirror[i][j] == 0):
                grid[i][j] = 5
            elif (mirror[i][j]<=18):
                grid[i][j] = 79
            elif (mirror[i][j]>18) and (mirror[i][j]<=28):
                grid[i][j] = 136
            elif (mirror[i][j]>28) and (mirror[i][j]<=38):
                grid[i][j] = 191
            elif (mirror[i][j]>38) and (mirror[i][j]<=48):
                grid[i][j] = 255
            elif (mirror[i][j]>48) and (mirror[i][j]<=58):
                grid[i][j] = 31
            elif (mirror[i][j]>58) and (mirror[i][j]<=68):
                grid[i][j] = 169
            else:
                pass
    plt.figure(header)            
    plt.imshow(grid, cmap=plt.get_cmap('gist_ncar'), vmin=0, vmax=255, interpolation='nearest')
    plt.show()
    
def coloring(cube):
    '''Prints'''
    mirror = array(cube)
    #for i in range(12):
    #    print mirror[i,:]
    grid = np.zeros(np.shape(mirror))
    for i in range(np.shape(mirror)[0]):
        #           G = 79
        # Y = 136  R = 191   W =255
        #           B = 31
        #           O = 169
        for j in range(np.shape(mirror)[1]):
            if (mirror[i][j] == 0):
                grid[i][j] = 5
            elif (mirror[i][j]<=18):
                grid[i][j] = 79
            elif (mirror[i][j]>18) and (mirror[i][j]<=28):
                grid[i][j] = 136
            elif (mirror[i][j]>28) and (mirror[i][j]<=38):
                grid[i][j] = 191
            elif (mirror[i][j]>38) and (mirror[i][j]<=48):
                grid[i][j] = 255
            elif (mirror[i][j]>48) and (mirror[i][j]<=58):
                grid[i][j] = 31
            elif (mirror[i][j]>58) and (mirror[i][j]<=68):
                grid[i][j] = 169
            else:
                pass
    return grid

def re_dm(List):
    '''
    Deletes the three CW or CCW iso-rotations and replaces 
    it with CCW or CW respectively:
        i.e. [[LF,CW], [LF,CW], [LF,CW]] ---> [[LF,CCW]]
    '''
    
    # ******DONT FORGET ABOUT FrameShift's *********
    i = 0
    while i < (len(List)-2):
        if (List[i] == List[i+1]) and (List[i] == List[i+2]):
            del(List[i+1:i+3])
            if (List[i][1] == 'CW'):
                List[i][1] = 'CCW'
            else:
                List[i][1] = 'CW'
                
        i+=1
    return List    
    
def check(cube):
    face_correct=0
    if (facelet_color(cube[0][3]) == facelet_color(cube[1][4])) and (facelet_color(cube[0][4]) == facelet_color(cube[1][4])) and (facelet_color(cube[0][5]) == facelet_color(cube[1][4])) and (facelet_color(cube[1][3]) == facelet_color(cube[1][4])) and (facelet_color(cube[1][5]) == facelet_color(cube[1][4])) and (facelet_color(cube[2][3]) == facelet_color(cube[1][4])) and (facelet_color(cube[2][4]) == facelet_color(cube[1][4])) and (facelet_color(cube[2][5]) == facelet_color(cube[1][4])):
        face_correct+=1
        print("top is good")
    if (facelet_color(cube[3][3]) == facelet_color(cube[4][4])) and (facelet_color(cube[3][4]) == facelet_color(cube[4][4])) and (facelet_color(cube[3][5]) == facelet_color(cube[4][4])) and (facelet_color(cube[4][3]) == facelet_color(cube[4][4])) and (facelet_color(cube[4][5]) == facelet_color(cube[4][4])) and (facelet_color(cube[5][3]) == facelet_color(cube[4][4])) and (facelet_color(cube[5][4]) == facelet_color(cube[4][4])) and (facelet_color(cube[5][5]) == facelet_color(cube[4][4])):
        face_correct+=1
        print("mid is good")
    if (facelet_color(cube[6][3]) == facelet_color(cube[7][4])) and (facelet_color(cube[6][4]) == facelet_color(cube[7][4])) and (facelet_color(cube[6][5]) == facelet_color(cube[7][4])) and (facelet_color(cube[7][3]) == facelet_color(cube[7][4])) and (facelet_color(cube[7][5]) == facelet_color(cube[7][4])) and (facelet_color(cube[8][3]) == facelet_color(cube[7][4])) and (facelet_color(cube[8][4]) == facelet_color(cube[7][4])) and (facelet_color(cube[8][5]) == facelet_color(cube[7][4])):
        face_correct+=1
        print("midbot is good")
    if (facelet_color(cube[9][3]) == facelet_color(cube[10][4])) and (facelet_color(cube[9][4]) == facelet_color(cube[10][4])) and (facelet_color(cube[9][5]) == facelet_color(cube[10][4])) and (facelet_color(cube[10][3]) == facelet_color(cube[10][4])) and (facelet_color(cube[10][5]) == facelet_color(cube[10][4])) and (facelet_color(cube[11][3]) == facelet_color(cube[10][4])) and (facelet_color(cube[11][4]) == facelet_color(cube[10][4])) and (facelet_color(cube[11][5]) == facelet_color(cube[10][4])):
        face_correct+=1
        print("bot is good")
    print ("faces correct = ", face_correct)


#architect references  
options = ['rot = rotations', 'proc = processes', 'mod = modifiers']
rot = ['bottomFaceCW(cube)', 'upperFaceCW(cube)', 'leftFaceCW(cube)', 'backFaceCW(cube)', 'rightFaceCW(cube)', 'frontFaceCW(cube)', 'FrameShiftLeft(cube)', 'FrameShiftUp(cube)', 'FrameShiftCW(cube)']
proc = ['step1A(cube, scribe)', 'step1B(cube, scribe)', 'step1C(cube, scribe)','step1D(cube, scribe)','step2A(cube, scribe)']
mod = ['facelet_detail(cube, num)', 'randState(cube, scribe)', 'failure(scribe)', 'error(num, cube)', 'maniState(cube)', 'manualMode(cube)', 'action(face, rot, cube)', 'findingFace(cube, num)', 'index_2d(myList, v)', 'printOut(cube)']   

    

        
        


#cubeRep = [                           [0,0,0,    10,11,12,    0,0,0],
#                                      [0,0,0,    13,GG,15,    0,0,0],       
#                                      [0,0,0,    16,17,18,    0,0,0],

#                                   [20,21,22,    30,31,32,    40,41,42], 
#                                   [23,YY,25,    33,RR,35,    43,WW,45], 
#                                   [26,27,28,    36,37,38,    46,47,48],

#                                      [0,0,0,    50,51,52,    0,0,0],       
#                                      [0,0,0,    53,BB,55,    0,0,0],       
#                                      [0,0,0,    56,57,58,    0,0,0],

#                                      [0,0,0,    60,61,62,    0,0,0],       
#                                      [0,0,0,    63,OO,65,    0,0,0],       
#                                      [0,0,0,    66,67,68,    0,0,0]]


cube = [                             [0,0,0,10,11,12,0,0,0],
                                     [0,0,0,13,14,15,0,0,0],       
                                     [0,0,0,16,17,18,0,0,0],
                                   [20,21,22,30,31,32,40,41,42], 
                                   [23,24,25,33,34,35,43,44,45], 
                                   [26,27,28,36,37,38,46,47,48],
                                      [0,0,0,50,51,52,0,0,0],       
                                      [0,0,0,53,54,55,0,0,0],       
                                      [0,0,0,56,57,58,0,0,0],
                                      [0,0,0,60,61,62,0,0,0],       
                                      [0,0,0,63,64,65,0,0,0],       
                                      [0,0,0,66,67,68,0,0,0]]

scribe = [[],[]]
answer_key = []
step1A(cube,scribe)

print(' ')
step2A(cube)

print ("shape of answer_key",np.shape(answer_key))
print ("seedling = ", seedling)
check(cube)

agm = []
for i in range(randStateMoves, np.shape(anim_grid)[0]):
    agm.append(coloring(anim_grid[i]))

ims = [] #to append 'Artists'
fig = plt.figure('Randomized Cube - [Solving] [Transistion State]')
ax = fig.add_subplot(111)

for imgNum in range(np.shape(agm)[0]):
    img = agm[imgNum] 
    frame =  ax.imshow(img,cmap=plt.get_cmap('gist_ncar'), vmin=0, vmax=255, interpolation='nearest') 
    int_percent =  int(round(float(imgNum)/np.shape(agm)[0] * 100))
    #for drawing different types of objects (proper terminology: adding 'Artists')
    # reference - http://matplotlib.org/users/artists.html
    text1 = int_percent
    text2 = '%'
    a1 = ax.annotate(text1,(0,0.25)) # adding text
    a2 = ax.annotate(text2,(0.5,0.25))
    box = ax.add_patch(
        patches.Rectangle((-0.25, -0.25), 1.5 , 0.75, facecolor="white",alpha=0.5
        )# adding rectangle
        # arguments ( loc,width,height,transparency -> 1.0=filled)
        # reference - http://matthiaseisen.com/pp/patterns/p0203/
    )
    ims.append([frame,box,a1,a2]) # add both the image and the text to the list of artists 


anim = animation.ArtistAnimation(fig, ims,  repeat_delay=1000,interval=100, blit=True)

plt.show()