import curses
from curses import wrapper
import time

def main(stdscr):
    # Adding colours
    curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_RED, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    ORANGE_AND_WHITE = curses.color_pair(3)

    pad = curses.newpad(100,100)
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(67+j) #ASCII A-->67
            pad.addstr(char, GREEN_AND_BLACK)

    for i in range(50):

        stdscr.clear()
        stdscr.refresh()
        #you can move the content or move the pad
        # # move the content
        # pad.refresh(0,i,5,5,10,25) #first two row and column of padded content next two top left from where we want to display the content last two bottom right upto where we want to display the content 
        
        # move the pad 
        pad.refresh(0,0,5,i,10,25+i)
        time.sleep(0.2)
    stdscr.getch()


wrapper(main)
