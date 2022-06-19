import curses
from curses import wrapper
import time

def main(stdscr):
    # Adding colours
    curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2,curses.COLOR_GREEN, curses.COLOR_BLACK)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)

    # stdscr.clear()

    # #place text at different locations
    # stdscr.addstr(10,10,"Hello Ankit") #Can't use print statement bcz we are on top of terminal screen; the first two parameters are rows and column
    # # stdscr.addstr(10,12,"Overwritten")

    # # stdscr.addstr(0,0,"Overwritten", curses.A_UNDERLINE)  ;for attributes

    # # stdscr.addstr(0,0,"Overwritten", curses.A_REVERSE) ; for reversing background and foreground colour of the string

    # #Adding colours
    # stdscr.addstr(0,0,"Hello Ankit",BLUE_AND_YELLOW)
    # stdscr.addstr("Hello",BLUE_AND_YELLOW | curses.A_BOLD) #Combining attributes


#Update the screen
    for i in range(100):
        stdscr.clear()
        color = BLUE_AND_YELLOW

        if i%2==0:
            color = GREEN_AND_BLACK

            stdscr.addstr(f"Count: {i}", color)
        stdscr.refresh()
        time.sleep(0.1)

    # stdscr.refresh()
    stdscr.getch()

wrapper(main)
