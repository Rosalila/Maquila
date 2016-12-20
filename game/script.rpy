# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:

    $ items = []
    $ unlocked_areas = []
    jump a1
    #python:
    #    ui.add(minigame_b2())
    #    result = ui.interact(suppress_overlay=True, suppress_underlay=True)

    return
