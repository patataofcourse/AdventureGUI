# AdventureGUI
## AdventureScript, featuring buttons :D
this readme is mostly a reference for me, at least for now. will clean up for public releases

## Roadmap
- v0.1: full-fledged control panel
    * buttons!!!
    * wait event
    * query event
    * saving and restoring
    * saveon/saveoff
    * quitting
- v0.2: printing tm
- v0.3: scroll area
- v0.4: title screen, achievement screen, credits screen
- v1.0 alpha: all required features, including images and button colors
- v1.0 beta: includes fixes found in the alpha
- v1.0: includes fixes found in the beta

## Files
* main.py: launches everything, game should be located @ games/test for now
* asgui_io.py: the adventurescript events (show, wait, query, load_file)
* events.py: manages button handlers
* window.py: all the proper pyglet window code
* res.py: loads the files inside resources, like images and such