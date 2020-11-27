#!/usr/include/python3

import pygame
import numpy

# local imports
import camera
import grapher
import cube
import wall

fov = 500


def main():

    # create render window
    window = grapher.Grapher()
    
    # create cube models
    render_models = list()
    render_models.append(cube.Cube())
    render_models.append(cube.Cube())
    render_models.append(cube.Cube())
    render_models.append(cube.Cube())
    render_models[0].set_pos(5, 0, 10)
    render_models[1].set_pos(-5, 0, 10)
    render_models[2].set_pos(5, -4, 13)
    render_models[3].set_pos(-5, -7, 10)
    
    # create walls
    render_models.append(wall.Wall())
    render_models[4].set_pos(0, -8, 25)
    render_models[4].scale = 8
    render_models.append(wall.Wall())
    render_models[5].set_pos(16, -8, 9)
    render_models[5].set_rot(0, 90, 0)
    render_models[5].scale = 8
    
    # create camera
    cam = camera.Camera()
    
    # temp
    r = 0
    s = 0.2

    
    # main loop
    try:
        while True:
            
            # clear grapher
            window.clear()
            
            # render models in render_models list
            for rm in render_models:
                
                # set global model-space stuff here
                rm.set_rot_delta(r, r, r)
                
                # transform model and get transformed coordinate pairs
                coords = rm.process(cam, fov)
                
                # render segments from coordinate pair list
                for i in coords:
                    
                    # gather depth coordinates
                    sz = i[0][2]
                    ez = i[1][2]
                    
                    # if segment is completely behind player, skip rendering
                    if sz < 0 and ez < 0:
                        continue
                        
                    # gather transformed coordinates
                    startx = i[0][0]
                    starty = i[0][1]
                    endx   = i[1][0]
                    endy   = i[1][1]
                    
                    # if segment is partially behind player, clip segment to camera's field of view
                    if sz < 0 or ez < 0:
                        
                        # ffffuuuuuuu
                        pass
                        
                    # draw segment
                    window.draw_line(startx, starty, endx, endy)
                       
            # draw debug text
            coords = "Player: (%f, %f, %f)" % (cam.pos_x, cam.pos_y, cam.pos_z)
            pang = "Player angle: %f" % cam.angle
            options = "Options: ROT: %d, SPD: %d" % (r, s)
            window.console_out("3D Engine test - HalfBurntToast")
            
            window.console_out(coords)
            window.console_out(pang)
            window.console_out(options)
            
            # update grapher
            window.update()    
            
            # get command input
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        r = int(not r)
                    if event.key == pygame.K_p:
                        cam.reset()
                        print("Reset")
            
            # get movement input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                ang = numpy.deg2rad(numpy.abs(360 - cam.angle))
                cam.pos_z -= numpy.cos(ang) * s
                cam.pos_x -= numpy.sin(ang) * s
            if keys[pygame.K_s]:
                ang = numpy.deg2rad(numpy.abs(360 - cam.angle))
                cam.pos_z += numpy.cos(ang) * s
                cam.pos_x += numpy.sin(ang) * s
            if keys[pygame.K_a]:
                ang = numpy.deg2rad(numpy.abs(360 - (cam.angle - 90)))
                cam.pos_z += numpy.cos(ang) * s
                cam.pos_x += numpy.sin(ang) * s
            if keys[pygame.K_d]:
                ang = numpy.deg2rad(numpy.abs(360 - (cam.angle - 90)))
                cam.pos_z -= numpy.cos(ang) * s
                cam.pos_x -= numpy.sin(ang) * s
            if keys[pygame.K_e]:
                cam.angle = (cam.angle - 0.6) % 360
            if keys[pygame.K_q]:
                cam.angle = (cam.angle + 0.6) % 360
            
            # if not using any input handling, uncommon the line below
            #pygame.event.pump()
            
            # temp delay. TODO: replace with FPS regulator
            pygame.time.delay(10)
            
    except KeyboardInterrupt:
        pygame.quit()
        


if __name__ == "__main__":
    main()
