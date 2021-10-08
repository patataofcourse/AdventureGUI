import adventurescript
import threading
import traceback
import sys

import pygame
pygame.init()

import window

import asgui_io as io

def run_as():
    try:
        print("\n\n")
        name = "test"
        if len(sys.argv) > 1:
            name = sys.argv[1]
        print("Returned: " + adventurescript.parse_sync(name,
            io = io.io
        ))
        window.closed = True
    except Exception as e:
        window.buttons.hide()
        print("".join(traceback.format_exception(type(e), e, e.__traceback__)))

as_thread = threading.Thread(target=run_as)

as_thread.start()
window.run()