init python:
    def invetory_item_dragged(drags, drop):
        if not drop:
            return
        #store.detective = drags[0].drag_name
        store.unlock_successful = True
        return True

screen inventory_screen(drops):
  draggroup:
    if "item1" in items:
        drag:
            drag_name "i1"
            child "items/1.png"
            droppable False
            dragged invetory_item_dragged
            xpos 000 ypos 500


    for drop in drops:
        drag:
            drag_name drop[0]
            child drop[1]
            draggable False
            xpos 450 ypos 400

  textbutton "Back" action [ Return("fail")] align (.2,.04)
