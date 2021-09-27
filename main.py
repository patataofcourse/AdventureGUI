import adventurescript
import threading
import sys

import pyglet
pyglet.resource.path = ['resources']
pyglet.resource.reindex()

import window

import events
import asgui_io as io
import res

def run_as():
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

as_thread = threading.Thread(target=run_as)

as_thread.start()
pyglet.app.run()