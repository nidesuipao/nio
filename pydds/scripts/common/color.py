# import curses

class color:
    data_colors = [
        'red', 'green', 'blue', 'purple', 'black', 'darkcyan', 'yellow'
    ]
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def info() -> str:
    return color.GREEN + '[info] ' + color.END

def info_all(info_str) -> str:
    return color.GREEN + '[info] ' + info_str + color.END

def warn() -> str:
    return color.YELLOW + '[warn] ' + color.END

def error() -> str:
    return color.RED + '[error] ' + color.RED