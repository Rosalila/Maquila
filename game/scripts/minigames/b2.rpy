init:

    #image bg pong field = "paris.png"

    python:

        class minigame_b2(renpy.Displayable):

            def __init__(self):

                renpy.Displayable.__init__(self)

                self.image_width = 200
                self.image_height = 200
                self.grid_width = 3
                self.grid_height = 3

                self.images = {}
                for image_x in range(0, self.grid_width):
                    for image_y in range(0, self.grid_height):
                      self.images[image_x,image_y] = Image("minigames/b2/"+`image_x`+`image_y`+".png")

                self.positions = {}
                for image_x in range(0, self.grid_width):
                    for image_y in range(0, self.grid_height):
                        self.positions[image_x,image_y] = (image_x*self.image_width,image_y*self.image_height)

                self.rotations = {}
                self.rotations[0,0] = 0
                self.rotations[0,1] = 0
                self.rotations[0,2] = 0
                self.rotations[1,0] = 0
                self.rotations[1,1] = 0
                self.rotations[1,2] = 0
                self.rotations[2,0] = 0
                self.rotations[2,1] = 0
                self.rotations[2,2] = 0

            def render(self, width, height, st, at):
                r = renpy.Render(width, height)

                for x in range(0, self.grid_width):
                    for y in range(0, self.grid_height):
                        pi = renpy.render(Transform(self.images[x,y],rotate=self.rotations[x,y]), 800, 600, st, at)
                        r.blit(pi, self.positions[x,y])

                renpy.redraw(self, 0)
                return r

            def isClicked(self, x, y,image_position):
              return x>=image_position[0] and x<=image_position[0]+self.image_width and y>=image_position[1] and y<=image_position[1]+self.image_height

            def event(self, ev, x, y, st):
                import pygame
                if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                    for image_x in range(0, self.grid_width):
                        for image_y in range(0, self.grid_height):
                            if self.isClicked(x,y,self.positions[image_x,image_y]):
                                self.rotations[image_x,image_y]+=90
                                self.rotations[image_x,image_y]=self.rotations[image_x,image_y]%360
                    solved = True
                    for image_x in range(0, self.grid_width):
                        for image_y in range(0, self.grid_height):
                            if self.rotations[image_x,image_y] != 0:
                                solved = False
                    if solved:
                        return "success"
