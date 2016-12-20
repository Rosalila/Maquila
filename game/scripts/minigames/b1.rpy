init:

    #image bg pong field = "paris.png"

    python:

        class minigame_b1(renpy.Displayable):

            def __init__(self):

                renpy.Displayable.__init__(self)

                # Some displayables we use.
                self.moving_ball = Image("minigames/b1/moving_ball.png")
                self.moving_ball_win_area = Image("minigames/b1/moving_ball_win_area.png")
                self.player = Text(_("Player"), size=36)
                self.eileen = Text(_("Eileen"), size=36)
                self.ctb = Text(_("Click to Begin"), size=36)

                self.moving_ball_width = 50
                self.moving_ball_height = 50

                self.velocity = 5
                self.boundary_width = 300
                self.boundary_left = 800/2 - self.boundary_width/2
                self.boundary_right = self.boundary_left + self.boundary_width
                self.center = self.boundary_left+(self.boundary_right-self.boundary_left)/2
                self.win_area_size = 70

                self.moving_ball_x = self.boundary_left
                self.moving_ball_y = 400
                self.moving_bal_orientation = "right"

                self.winner = None

            def isBallInWinArea(self):
                return self.moving_ball_x>self.center-self.win_area_size/2 and self.moving_ball_x<self.center+self.win_area_size/2
            def visit(self):
                return [ self.player, self.eileen, self.ctb ]
            def render(self, width, height, st, at):
                r = renpy.Render(width, height)
                #Lockpick
                pi = renpy.render(self.moving_ball, 800, 600, st, at)
                r.blit(pi, (int(self.moving_ball_x)-self.moving_ball_width/2, int(self.moving_ball_y)-self.moving_ball_height/2))

                if self.isBallInWinArea():
                    pi = renpy.render(self.moving_ball_win_area, 800, 600, st, at)
                    r.blit(pi, (int(self.moving_ball_x)-self.moving_ball_width/2, int(self.moving_ball_y)-self.moving_ball_height/2))

                if self.moving_ball_x > self.boundary_right:
                    self.moving_bal_orientation = "left"

                if self.moving_ball_x < self.boundary_left:
                    self.moving_bal_orientation = "right"

                if self.moving_bal_orientation == "right":
                    self.moving_ball_x+=self.velocity

                if self.moving_bal_orientation == "left":
                    self.moving_ball_x-=self.velocity

                renpy.redraw(self, 0)
                return r

            def event(self, ev, x, y, st):
                import pygame
                if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                    if self.isBallInWinArea():
                        return "success"
                    else:
                        return "fail"
