# Christopher Tscheschlog
import pygame
import piece

# This program will be a text based chess game.

# It will be reprinted to the console after each move.

# Score counter for each player based off of the piece captured.

# MAYBE a basic ai player. We'll see...


# INTRODUCTION
def set_screen(num):

    if num == 1:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((500, 500))

    pygame.display.set_caption('Chess Game')


    pygame.display.flip()
    running = False
    while not running:
        render_screen(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                running = True
                pygame.quit()
                quit()
            pygame.display.update()

def render_screen(screen):

    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    screen.fill(white)

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('GeeksForGeeks', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (500 // 2, 500 // 2)



def num_players():

    num_players = int(input("How many players are playing, 1 or 2? "))

    return num_players



def main():

    pygame.init()

    full_screen = int(input("Would you like to play in fullscreen or windowed? (1 or 2): "))

    set_screen(full_screen)

    print("Hello player 1!", end="\n")

    user_name_1 = input("What is your name? ")

    if (user_name_1 < "Chris"):

        print("By the way... Chris is a cooler name.")

    elif(user_name_1 != "Harrison"):
        print(user_name_1, "is an ok name.")

    else:

        print(user_name_1, "is a cool name!", sep=" ", end="\n\n")

    print("Hello", user_name_1 + "! Welcome to chess!")

    # Ask if one player or two player

    players = num_players()


    # This will be incased in a while loop

    while players != 1 and players !=2:

        players = num_players()

    # END OF WHILE LOOP


    if (players == 1):

        user_name_2 = "Chad Bot"

        print(user_name_1, "will be playing against Chad the chess bot!")



    else:

        user_name_2 = input("What is the name of the second player? ")

        print("Both players are locked in... It will be", user_name_1, "v.s.", user_name_2, "!")

    print("\n")

    # This is where I would need to innitialize the gameboard

    # I will use a 2D array to store the board

    # As of now (with my very basic understanding) I assume I can create objects fo the pieces as well


    # This is how the board will be displayed in the finished product

    # THE BOARD DOES NOT HAVE ANY FUNCTIONALITY AT THE MOMENT


    captured_pieces_1 = ""

    captured_pieces_2 = ""

    points_1 = 0

    points_2 = 0

    print(user_name_1, "Black", sep=" ")

    print("\n", "Captured Pieces:", captured_pieces_1, "\n Points:", points_1)

    print("\n")

    print("Rk Kn Bi Qn Ki Bi Kn Rk")

    print("Pn " + "Pn " * 7)

    for x in range(4):
        print("-- -- -- -- -- -- -- --")

    print("Pn Pn Pn Pn Pn Pn Pn Pn")

    print("Rk Kn Bi Qn Ki Bi Kn Rk")

    print("\n")

    print(user_name_2, "White", sep=" ")

    print("\n", "Captured Pieces:", captured_pieces_2, "\n Points:", points_2)

    next = int(input("Input '1' to see test movement: "))

    if (next == 1):

        print(user_name_1, "Black", sep=" ")

        print("\n", "Captured Pieces:", captured_pieces_1, "\n Points:", points_1)

        print("\n")

        print("Rk Kn Bi Qn Ki Bi Kn Rk")

        print("Pn Pn Pn Pn -- Pn Pn Pn")

        print("-- -- -- -- -- -- -- --")

        print("-- -- -- -- Qn -- -- --", "Black is in check!", sep=" " * 5)

        print("-- -- -- -- Pn -- -- --")

        print("-- -- -- -- -- -- -- --")

        print("Pn Pn Pn Pn -- Pn Pn Pn")

        print("Rk Kn Bi Qn Ki Bi Kn Rk")

        print("\n")

        print(user_name_2, "White", sep=" ")

        captured_pieces_2 = "Pn"

        points_2 = 10 / 10

        print("\n", "Captured Pieces: " + captured_pieces_2, "\n Points:", points_2)



    else:

        print("Really?", next, "is not a 1...", sep=" ")

    next = int(input("Enter '1' to continue: "))

    print("\n")

    if (next == 1):

        print("There are", 8 ** 2, "squares on a chess board.", sep=" ")

        print("Along with 5,362 distict chess positions...")

        print("But there are between", 10 ** 43, "\nand", 10 ** 50, "\npossible positions!!!", sep=" ")

    else:

        print("Really?", next, "...", sep=" ")

    # Pawn

    # Can move 2 spaces on the first turn, otherwise, moves one space forward at a time

    # User can choose what piece the pawn transitions to after reaching the other side.


    #

    #                       O

    #                       O                               O

    #                       P                               P

    #                   FIRST MOVE                     NORMAL MOVE

    #                     ONLY

    #


    # Rook

    # Can move in straight lines in any direction until obstructed/edge of board


    #                                           O

    #                                           O

    #                                           O

    #                                     O O O R O O O

    #                                           O

    #                                           O

    #                                           O


    # Knight

    # Moves 3 tiles stright in any direction, then left or right from the ends of those.


    #                                         O O O

    #                                           O

    #                                     O     O     O

    #                                     O O O K O O O

    #                                     O     O     O

    #                                           O

    #                                         O O O

    # Bishop

    # Moves on the diagnals in any direction until obstructed edge of board


    #                                     O           O

    #                                       O       O

    #                                         O   O

    #                                           B

    #                                         O   O

    #                                       O       O

    #                                     O           O


    # Queen

    # Can move in straight lines and on diagnals until obstructed/edge of board


    #                                     O     O     O

    #                                       O   O   O

    #                                         O O O

    #                                     O O O Q O O O

    #                                         O O O

    #                                       O   O   O

    #                                     O     O     O


    # King

    # Can move one space in bot straight lines and on diagnals


    #

    #

    #                                         O O O

    #                                         O K O

    #                                         O O O

    #

    #


    # Important classes:


    # check_checker

    # check_mate_checker


    # Remove Piece

    # Function for taking captured pieces off the board


    # check_space

    # Is the space empty?

    # Yes - Done


    # No

    # Your own piece is in the square

    # print("Your own piece prevents that move!") or something...


    # Opponents piece is in the square

    # Romove piece

    # points_1 or points_2 += the value of the piece

main()
