label b2:
    "b2"
    if "b2" in unlocked_areas:
        call screen game_menu_screen("b2_unlocked","a1",[])
    else:
        call screen game_menu_screen("b2","a1",[])

label b2_unlocked_inventory:
    python:
        ui.add(minigame_b2())
        result = ui.interact(suppress_overlay=True, suppress_underlay=True)
    jump b2
label b2_inventory:
    $ store.unlock_successful = False
    call screen inventory_screen([["b2","drops/1.png"]])
    if store.unlock_successful:
        "success"
        $ unlocked_areas.append("b2")
        "you unlocked this area (b2)"
    else:
        "fail"
    jump b2
