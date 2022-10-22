from distutils.cmd import Command
from tkinter import * 
import sys
import tkinter
from turtle import position
import Team_class
from Team_class import bebek_team_picker_menu
from Pitch_class import bebek_pitch
from Tools_class import bebek_tools
import Pitch_class
import Tools_class
import tk_interface


MainWindow = Tk()
MainWindow.title('Bebek Main Window')
MainWindow.geometry("1920x1020")
w = Scrollbar(MainWindow)
menubar = Menu(MainWindow)
frameMain = Frame(MainWindow)

#globals
cell_def = Pitch_class.bebek_pitch.cell.cell_definition()
pc = Pitch_class.bebek_pitch.create_pitch("252, 247, 247")
poitions = dict()
possible_move =dict()
pics_btn_dict = dict()

#test zone

#bebek_team_picker_menu.Read_char_bank()
#function
def GetPics_dic_btn():
    global pics_btn_dict
    pics_btn_dict = tk_interface.Temp_method_get_char_pics()
    return pics_btn_dict
    

#GUI
action_menu =Menu(menubar, tearoff= 0)
menubar.add_cascade(label='Actions', menu= action_menu)
action_menu.add_command(label="Move char", command=lambda:bebek_tools.show_move_options(frameMain,poitions_dict))
label_Menu = Label(MainWindow, text="Actions menu").grid(column="2", row="0")
poitions_dict=tk_interface.draw_pitch(pc,cell_def,frameMain,poitions,pics_btn_dict)
btn_show_move = Button(MainWindow, text="Show Move Options", command= lambda:bebek_tools.show_move_options(frameMain,poitions_dict,possible_move)).grid(column="2",row="4")
btn_move = Button(MainWindow, text="Make a move", command= lambda:[GetPics_dic_btn(),bebek_tools.Make_Move(possible_move,poitions_dict,pics_btn_dict)]).grid(column="2",row="5")
btn_clean_move = Button(MainWindow, text="Clean Move", command= lambda:bebek_tools.Clean_Move_Options(possible_move,poitions_dict)).grid(column="2",row="6")
btn_team_picker = Button(MainWindow, text="Team Picker", command= lambda:bebek_team_picker_menu.char_picker(MainWindow)).grid(column="3",row="3")
#null_image = tkinter.PhotoImage(width=0, height=0)
#test_btn = Button(MainWindow,width="50",height="50", image=null_image).grid(column=3, row=3)


MainWindow.config(menu= menubar)
frameMain.grid()
MainWindow.mainloop()
