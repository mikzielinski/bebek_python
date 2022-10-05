from Tools_class import bebek_tools
from string import ascii_lowercase as alc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class bebek_pitch(object):
        
        #pitch setup class and events
        def create_pitch(player_RGB_color):
                pitch = dict()
                pitch['size_w'] = 11
                pitch['size_l'] = 19
                x = pitch['size_w']
                y = pitch['size_l']
                pitch['size_mid'] =y/2
                pitch['size_goal']=[0,19]
                pitch['pitch_weather'] = bebek_tools.roll_dice("d6Weather",1)
                pitch['bckg_color_player'] = player_RGB_color
                pitch['cell_colorBase'] = "252, 247, 247"
                pitch['cell_lineBase'] = "0, 0, 0"
                return pitch 

        class cell(object):
                def cell_definition():
                        cell_def=dict()
                        type_prop=dict()
                        cell_def['width']=4
                        cell_def['lenght']=2
                        cell_def['type']='cell'
                        cell_def['properties']=type_prop
                        
                        return cell_def 
       
                def ActiveCell(selected, rgb_color,X,Y):
                        if selected == True:
                                cell_color = rgb_color
                        else:
                                cell_color = "252, 247, 247"
                        