# AdventureGUI
## AdventureScript, featuring buttons :D
this readme is mostly a reference for me, at least for now. will clean up ~~for public releases~~ sometime before 1.0

## Roadmap
- v0.1: full-fledged control panel - done! :D
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

## Instructions
You'll need `pyglet` to use this. Download it using pip.

Run the program with `python main.py`. If you want to run some other game (inside the games folder) that isn't the test game, run `python main.py [gamename]`.