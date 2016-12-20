screen game_menu_screen(current_screen,parrent,hotspots):
    imagemap:
        auto current_screen+"/imagemap_%s.png"
        for hotspot in hotspots:
            hotspot (hotspot[1], hotspot[2], hotspot[3], hotspot[4]) action Jump(hotspot[0]) alt hotspot[0]
    textbutton "Back" action [ Jump(parrent)] align (.1,.04)
    textbutton "Inventory" action [ Jump( current_screen+"_inventory")] align (.3,.04)
    textbutton "Diary" action [ Show("inventory_screen")] align (.5,.04)
