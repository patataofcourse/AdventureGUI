import adventurescript
import threading
import sys

import pygame
pygame.init()

import window

import asgui_io as io
import events

def run_as():
    try:
        name = "test"
        if len(sys.argv) > 1:
            name = sys.argv[1]
        print("Returned: " + adventurescript.parse_sync(name,
            show= io.show,
            wait= io.wait,
            query= io.query,
            load_file= io.load_file
        ))
        window.closed = True
    except Exception as e:
        window.buttons.hide()
        print(e)

as_thread = threading.Thread(target=run_as)

as_thread.start()
window.run()