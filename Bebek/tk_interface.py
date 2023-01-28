#GUI for PoC
from tkinter import *
from string import ascii_lowercase as alc
import tkinter
from turtle import width
from Tools_class import bebek_tools
import Tools_class
import Team_class
char_dict_pics=dict()


def Temp_method_get_char_pics():
    global char_dict_pics
    return char_dict_pics

def draw_pitch(pitch_config_dict,cell_definition,Master_frame,position_dict,char_dict_pic):
    #root = Tk()
    #root.title =('Bebek Project GUI')
    #root.geometry("1920x1020")

    position_dict = dict()
    global char_dict_pics
    #wideget code here - main board grid
    #frame = Frame(root)
    
    frame = Master_frame

    Pitch_Frame = tkinter.Frame(frame, width = 40, height = 100, bg='gray')
    Pitch_Frame.pack(fill='both',  padx=10,  pady=5,  expand=True)
    
    #draw and set columns
    for j in range(pitch_config_dict['size_l']):
        Label(Pitch_Frame, text =j,width=cell_definition['width'],height=cell_definition['lenght'],image=cell_definition['image'],compound='center').grid(row=j,column=0)
        j+1
        if j == pitch_config_dict['size_l']:
            break
    #draw and set rows
    for index, i in enumerate(alc):   
        Label(Pitch_Frame, text =i,width=cell_definition['width'], height=cell_definition['lenght'],image=cell_definition['image'],compound='center').grid(row=0,column=index+1)
        if index == pitch_config_dict['size_w']:
            break
    #X
    board_position_dict = dict()
    r=1
    for r in range(index+1):
        #Y
        c=1
        for c in range(j):
               dict_obj= Tools_class.bebek_tools.create_cell(c+1,r+1,Pitch_Frame,"empty",pitch_config_dict,board_position_dict,cell_definition)
                
    
    #Tools_class.bebek_tools.create_cell(1,4,"d",frame)
    #Pitch_Frame.grid()
    orc = Team_class.bebek_character.orc_runner()
    #bb =  board_position_dict["4:6"]
    d =Tools_class.bebek_tools.set_char(4,6,Pitch_Frame,orc,pitch_config_dict,board_position_dict,char_dict_pic)
    board_position_dict["4:6"]= d
    
    dwarf = Team_class.bebek_character.dwarf_elder()
    d =Tools_class.bebek_tools.set_char(5,6,Pitch_Frame,dwarf,pitch_config_dict,board_position_dict,char_dict_pic)
    board_position_dict["5:6"]= d
    
    position_dict = board_position_dict
    char_dict_pics = char_dict_pic
    return position_dict

    #frame.grid()
    #run GUI

    #root.mainloop()