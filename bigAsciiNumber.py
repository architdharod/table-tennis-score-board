import os
import shutil
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

def get_terminal_size():
    try:
        # Get terminal size
        size = shutil.get_terminal_size(fallback=(80, 24))
        columns, rows = size.columns, size.lines
    except:
        # Fallback if terminal size can't be determined
        columns, rows = 80, 24
    return columns, rows

ascii_digits = {
    '0': [
"     000000000     ",
"   00:::::::::00   ",
" 00:::::::::::::00 ",
"0:::::::000:::::::0",
"0::::::0   0::::::0",
"0:::::0     0:::::0",
"0:::::0     0:::::0",
"0:::::0 000 0:::::0",
"0:::::0 000 0:::::0",
"0:::::0     0:::::0",
"0:::::0     0:::::0",
"0::::::0   0::::::0",
"0:::::::000:::::::0",
" 00:::::::::::::00 ",
"   00:::::::::00   ",
"     000000000",
    ],
    '1': [
        "  1111111   ",
        " 1::::::1   ",
        "1:::::::1   ",
        "111:::::1   ",
        "   1::::1   ",
        "   1::::1   ",
        "   1::::1   ",
        "   1::::l   ",
        "   1::::l   ",
        "   1::::l   ",
        "   1::::l   ",
        "   1::::l   ",
        "111::::::111",
        "1::::::::::1",
        "1::::::::::1",
        "111111111111",
    ],
    '2': [
        " 222222222222222    ",
        "2:::::::::::::::22  ",
        "2::::::222222:::::2 ",
        "2222222     2:::::2 ",
        "            2:::::2 ",
        "            2:::::2 ",
        "         2222::::2  ",
        "    22222::::::22   ",
        "  22::::::::222     ",
        " 2:::::22222        ",
        "2:::::2             ",
        "2:::::2             ",
        "2:::::2       222222",
        "2::::::2222222:::::2",
        "2::::::::::::::::::2",
        "22222222222222222222",
    ],
    '3': [
        " 333333333333333   ",
        "3:::::::::::::::33 ",
        "3::::::33333::::::3",
        "3333333     3:::::3",
        "            3:::::3",
        "            3:::::3",
        "    33333333:::::3 ",
        "    3:::::::::::3  ",
        "    33333333:::::3 ",
        "            3:::::3",
        "            3:::::3",
        "            3:::::3",
        "3333333     3:::::3",
        "3::::::33333::::::3",
        "3:::::::::::::::33 ",
        " 333333333333333   ",
    ],
    '4': [
"       444444444  ",
"      4::::::::4  ",
"     4:::::::::4  ",
"    4::::44::::4  ",
"   4::::4 4::::4  ",
"  4::::4  4::::4  ",
" 4::::4   4::::4  ",
"4::::444444::::444",
"4::::::::::::::::4",
"4444444444:::::444",
"          4::::4  ",
"          4::::4  ",
"          4::::4  ",
"        44::::::44",
"        4::::::::4",
"        4444444444",
    ],
    '5': [
"555555555555555555 ",
"5::::::::::::::::5 ",
"5::::::::::::::::5 ",
"5:::::555555555555 ",
"5:::::5            ",
"5:::::5            ",
"5:::::5555555555   ",
"5:::::::::::::::5  ",
"555555555555:::::5 ",
"            5:::::5",
"            5:::::5",
"5555555     5:::::5",
"5::::::55555::::::5",
" 55:::::::::::::55 ",
"   55:::::::::55   ",
"     555555555     ",
    ],
    '6': [
"        66666666   ",
"       6::::::6    ",
"      6::::::6     ",
"     6::::::6      ",
"    6::::::6       ",
"   6::::::6        ",
"  6::::::6         ",
" 6::::::::66666    ",
"6::::::::::::::66  ",
"6::::::66666:::::6 ",
"6:::::6     6:::::6",
"6:::::6     6:::::6",
"6::::::66666::::::6",
" 66:::::::::::::66 ",
"   66:::::::::66   ",
"     666666666     ",
    ],
    '7': [
"77777777777777777777",
"7::::::::::::::::::7",
"7::::::::::::::::::7",
"777777777777:::::::7",
"           7::::::7 ",
"          7::::::7  ",
"         7::::::7   ",
"        7::::::7    ",
"       7::::::7     ",
"      7::::::7      ",
"     7::::::7       ",
"    7::::::7        ",
"   7::::::7         ",
"  7::::::7          ",
" 7::::::7           ",
"77777777            ",
    ],
    '8': [
"     888888888     ",
"   88:::::::::88   ",
" 88:::::::::::::88 ",
"8::::::88888::::::8",
"8:::::8     8:::::8",
"8:::::8     8:::::8",
" 8:::::88888:::::8 ",
"  8:::::::::::::8  ",
" 8:::::88888:::::8 ",
"8:::::8     8:::::8",
"8:::::8     8:::::8",
"8:::::8     8:::::8",
"8::::::88888::::::8",
" 88:::::::::::::88 ",
"   88:::::::::88   ",
"     888888888",
    ],
    '9': [
"     999999999     ",
"   99:::::::::99   ",
" 99:::::::::::::99 ",
"9::::::99999::::::9",
"9:::::9     9:::::9",
"9:::::9     9:::::9",
" 9:::::99999::::::9",
"  99::::::::::::::9",
"    99999::::::::9 ",
"         9::::::9  ",
"        9::::::9   ",
"       9::::::9    ",
"      9::::::9     ",
"     9::::::9      ",
"    9::::::9       ",
"   99999999        ",
    ],
}

def generate_ascii_art(number_str):
    # Initialize an empty list for each line of the ASCII art
    ascii_art = ['' for _ in range(16)]  # The new font height is 16
    # Loop through each digit character in the number string
    for digit_char in number_str:
        # Get the ASCII representation of the digit
        digit_art = ascii_digits.get(digit_char, [' ' * 16]*16)
        # Append each line of the digit to the corresponding line in ascii_art
        for i in range(16):
            ascii_art[i] += digit_art[i]
    return ascii_art

def print_numbers(player_a, player_b, color=WHITE):
    columns, rows = get_terminal_size()
    half_columns = columns // 2

    # Convert the player numbers to strings
    player_a_str = str(player_a)
    player_b_str = str(player_b)

    # Generate ASCII art for each player's number
    player_a_art = generate_ascii_art(player_a_str)
    player_b_art = generate_ascii_art(player_b_str)

    # Calculate padding to center the numbers in each half
    player_a_art_width = len(player_a_art[0])
    player_b_art_width = len(player_b_art[0])

    player_a_padding = (half_columns - player_a_art_width) // 2
    player_b_padding = (half_columns - player_b_art_width) // 2

    # Print each line of the ASCII art numbers side by side
    for i in range(len(player_a_art)):
        left_space = ' ' * player_a_padding
        right_space = ' ' * player_b_padding
        # If total columns is odd, adjust right side padding
        if columns % 2 != 0:
            right_half_offset = 1
        else:
            right_half_offset = 0
        # Construct the line for player A
        player_a_line = left_space + player_a_art[i].ljust(half_columns - player_a_padding)
        # Construct the line for player B
        player_b_line = right_space + player_b_art[i].ljust(half_columns - player_b_padding + right_half_offset)
        # Combine and print the lines
        print(color + player_a_line + player_b_line + RESET)

