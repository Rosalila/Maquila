label a1:
    "a1"
    call screen game_menu_screen("a1","a1",[["b1",88, 230, 100, 100],["b2",488, 114, 200, 300]])
    jump a1

label a1_inventory:
    $ store.unlock_successful = False
    call screen inventory_screen([])
    if store.unlock_successful:
        "success"
    else:
        "fail"
    jump a1
