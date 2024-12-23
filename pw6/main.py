import curses
from domains.university import University

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    SGP = University()
    SGP.execute(stdscr)

curses.wrapper(main)