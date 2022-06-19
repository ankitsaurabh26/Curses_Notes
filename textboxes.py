from cgitb import text
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time
from turtle import st

def main(stdscr):
    # Adding colours
    curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_RED, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    ORANGE_AND_WHITE = curses.color_pair(3)

    win = curses.newwin(3,18,2,2)
    box = Textbox(win)


    rectangle(stdscr,1,1,5,20)
    stdscr.refresh()

    box.edit()
    text = box.gather().strip().replace("\n","")

    stdscr.addstr(10,40,text)

    stdscr.getch()

wrapper(main)
