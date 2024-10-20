# main.py
import os
import sys
import bigAsciiNumber
import winner_text

os.system('color')
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m' # called to return to standard terminal text color

# Cross-platform single-character input
def getch():
    try:
        # Windows
        import msvcrt
        return msvcrt.getch().decode('utf-8')
    except ImportError:
        # Unix-like systems (macOS, Linux)
        import tty
        import termios

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            return ch
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function for winner evaluation logic
def eval_winner(player_a, player_b):
    if abs(player_a - player_b) >= 2:
        if player_a > 10:
            return 'PlayerA'
        elif player_b > 10:
            return 'PlayerB'
    else:
        return None

# Main function
def main():
    PlayerA = 0
    PlayerB = 0
    Winner = None

    # Instructions
    print("Press 'J' to increase PlayerA's score.")
    print("Press 'K' to increase PlayerB's score.")
    print("Press 'R' to reset the score board.")
    print("Press 'Q' to quit.\n")
    bigAsciiNumber.print_numbers(PlayerA, PlayerB, YELLOW)

    # Function to listen for key presses and update scores
    def key_listener():
        nonlocal PlayerA, PlayerB, running, Winner
        while running:
            ch = getch()
            ch = ch.lower()
            if Winner is not None:
                PlayerA = 0
                PlayerB = 0
                Winner = None
            elif ch == 'j':
                PlayerA += 1
            elif ch == 'k':
                PlayerB += 1
            elif ch == 'r':
                PlayerA = 0
                PlayerB = 0
                Winner = None
            elif ch == 'q':
                running = False

            # Update the display
            clear_screen()
            print("Press 'J' to increase PlayerA's score.")
            print("Press 'K' to increase PlayerB's score.")
            print("Press 'R' to reset the score board.")
            print("Press 'Q' to quit.\n")
            bigAsciiNumber.print_numbers(PlayerA, PlayerB, YELLOW )

            #evaluate the score
            Winner = eval_winner(PlayerA, PlayerB)
            if Winner is not None:
                #winner sequence
                clear_screen()
                color = BLUE
                if Winner is 'PlayerA':
                    color = GREEN
                winner_text.print_winner(Winner, color )

    # Variable to control the loop
    running = True

    # Clear the screen and display initial scores
    clear_screen()
    print("Press 'J' to increase PlayerA's score.")
    print("Press 'K' to increase PlayerB's score.")
    print("Press 'R' to reset the score board.")
    print("Press 'Q' to quit.\n")
    bigAsciiNumber.print_numbers(PlayerA, PlayerB, YELLOW)

    # Run the key listener
    key_listener()

if __name__ == "__main__":
    main()

