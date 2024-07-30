import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the speed typing test!")
    stdscr.addstr("\n Press any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

def wpm(stdscr):
    target = "Hello world this is some test text for this app!"
    current_text = []

    stdscr.clear()
    stdscr.addstr(target)
    stdscr.refresh()
    stdscr.getkey()

def main(stdscr): 
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm(stdscr)
wrapper(main)