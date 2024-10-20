import os
import shutil

def get_terminal_size():
    try:
        # Get terminal size
        size = shutil.get_terminal_size(fallback=(80, 24))
        columns, rows = size.columns, size.lines
    except:
        # Fallback if terminal size can't be determined
        columns, rows = 80, 24
    return columns, rows

winner = {
    'PlayerA': [
"██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗      ██╗",
"██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ███║",
"██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ╚██║",
"██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗     ██║",
"██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║     ██║",
"╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝     ╚═╝",
"                                                         ",
"██╗    ██╗██╗███╗   ██╗███████╗    ██╗                   ",
"██║    ██║██║████╗  ██║██╔════╝    ██║                   ",
"██║ █╗ ██║██║██╔██╗ ██║███████╗    ██║                   ",
"██║███╗██║██║██║╚██╗██║╚════██║    ╚═╝                   ",
"╚███╔███╔╝██║██║ ╚████║███████║    ██╗                   ",
" ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝    ╚═╝                   ",
    ],
    'PlayerB': [
"██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗     ██████╗ ",
"██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ╚════██╗",
"██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝     █████╔╝",
"██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗    ██╔═══╝ ",
"██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║    ███████╗",
"╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚══════╝",
"                                                             ",
"██╗    ██╗██╗███╗   ██╗███████╗    ██╗                       ",
"██║    ██║██║████╗  ██║██╔════╝    ██║                       ",
"██║ █╗ ██║██║██╔██╗ ██║███████╗    ██║                       ",
"██║███╗██║██║██║╚██╗██║╚════██║    ╚═╝                       ",
"╚███╔███╔╝██║██║ ╚████║███████║    ██╗                       ",
" ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝    ╚═╝                       ",
    ]
}

def print_winner(player, color):
    columns, rows = get_terminal_size()
    ascii_text = winner[player]
    art_height = len(ascii_text)
    art_width = max(len(line) for line in ascii_text)
    
    # Calculate vertical padding to center the art
    top_padding = max((rows - art_height) // 2, 0)
    
    # Print empty lines for vertical centering
    for _ in range(top_padding):
        print()
    
    # Print each line with horizontal centering
    for line in ascii_text:
        left_padding = max((columns - len(line)) // 2, 0)
        print(color+' ' * left_padding + line + RESET)

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

