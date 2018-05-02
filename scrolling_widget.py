import sys
import curses
import traceback

notes = ['one',
         'two',
         'three',
         'four',
         'five',
         'six',
         'seven',
         'eight',
         'nine',
         'ten',
         'eleven',
         'twelve',
         'a',
         'b',
         'c',
         'd',
         'e',
         'f',
         ]

LIST_POINTER = 0


TOP_LINE = 0
BOTTOM_LINE = 6
POINTER = 1

BOUND = '-'*20

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)


def render(list_top):
    print_arrow(POINTER)
    for line_y in range(TOP_LINE, BOTTOM_LINE):
        if line_y == TOP_LINE:
            screen.addstr(line_y, 2, BOUND)
        elif line_y == BOTTOM_LINE - 1:
            screen.addstr(line_y, 2, BOUND)
        else:
            screen.addstr(line_y, 5, notes[list_top])
            list_top += 1



def print_arrow(y):
    arrow = ' -->'
    screen.addstr(y, 1, arrow)


def key_press():
    global POINTER, LIST_POINTER
    char = screen.getch()
    if char == ord('q'):
        exit()

    # This Implements the Jump to top and bottom.
    if char == ord('G'):
        LIST_POINTER = len(notes) - 1
        POINTER = BOTTOM_LINE - 2
        return len(notes) - (BOTTOM_LINE - 1 - TOP_LINE - 1)
    if char == ord('g'):
        LIST_POINTER = 0
        POINTER = 1
        return 0


    elif char == curses.KEY_UP:
        if LIST_POINTER <= 0:
            LIST_POINTER = len(notes) - 1
            POINTER = BOTTOM_LINE - 2
            return len(notes) - (BOTTOM_LINE - 1 - TOP_LINE - 1)
        if POINTER == TOP_LINE + 1:
            LIST_POINTER = LIST_POINTER - 1
            return list_top - 1
        else:
            POINTER = POINTER - 1
            LIST_POINTER = LIST_POINTER - 1
            return list_top


    elif char == curses.KEY_DOWN:
        if LIST_POINTER == len(notes) - 1:
            LIST_POINTER = 0
            POINTER = 1
            return 0
        elif POINTER == BOTTOM_LINE - 2:
            LIST_POINTER = LIST_POINTER + 1
            return list_top + 1
        else:
            POINTER = POINTER + 1
            LIST_POINTER = LIST_POINTER + 1
            return list_top

try:
    list_top = 0
    while True:
        screen.clear()
        render(list_top)
        list_top = key_press()
except Exception:
    print(sys.exc_info()[0])
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()

    print(traceback.format_exc())
    print(sys.exc_info())
    active_item = notes[LIST_POINTER]
    print(active_item)

