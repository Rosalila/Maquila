label b1:
    "b1"
    call screen game_menu_screen("b1","a1",[])

label b1_inventory:
    #window hide None
    python:
        ui.add(minigame_b1())
        result = ui.interact(suppress_overlay=True, suppress_underlay=True)
    #window show None
    if result=="success":
        "success"
        $ items.append("item1")
        "you fund item1"
    else:
        "fail"
    jump b1
