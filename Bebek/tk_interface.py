#GUI for PoC
from tkinter import *
from string import ascii_lowercase as alc
import tkinter
from turtle import width
from Tools_class import bebek_tools
import Tools_class
import Team_class


def draw_pitch(pitch_config_dict,cell_definition,Master_frame,position_dict):
    #root = Tk()
    #root.title =('Bebek Project GUI')
    #root.geometry("1920x1020")
    position_dict = dict()

    #wideget code here - main board grid
    #frame = Frame(root)
    frame = Master_frame

    
    #draw and set columns
    for j in range(pitch_config_dict['size_l']):
        Label(frame, text =j,width=cell_definition['width'],height=cell_definition['lenght']).grid(row=j,column=0)
        j+1
        if j == pitch_config_dict['size_l']:
            break
    #draw and set rows
    for index, i in enumerate(alc):   
        Label(frame, text =i,width=cell_definition['width'], height=cell_definition['lenght']).grid(row=0,column=index+1)
        if index == pitch_config_dict['size_w']:
            break
    #X
    board_position_dict = dict()
    r=1
    for r in range(index+1):
        #Y
        c=1
        for c in range(j):
               dict_obj= Tools_class.bebek_tools.create_cell(c+1,r+1,frame,"empty",pitch_config_dict,board_position_dict)
                
    
    #Tools_class.bebek_tools.create_cell(1,4,"d",frame)
    frame.grid()
    orc = Team_class.bebek_character.orc_runner()
    #bb =  board_position_dict["4:6"]
    d =Tools_class.bebek_tools.set_char(4,6,frame,orc,pitch_config_dict,board_position_dict)
    board_position_dict["4:6"]= d
    
    dwarf = Team_class.bebek_character.dwarf_elder()
    d =Tools_class.bebek_tools.set_char(5,6,frame,dwarf,pitch_config_dict,board_position_dict)
    board_position_dict["5:6"]= d
    
    position_dict = board_position_dict
    return position_dict

    #frame.grid()
    #run GUI

    #root.mainloop()