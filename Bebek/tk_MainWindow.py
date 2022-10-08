from distutils.cmd import Command
from tkinter import *
import sys
from turtle import position
from Tools_class import bebek_tools
import Pitch_class
import Tools_class
import tk_interface


MainWindow = Tk()
MainWindow.title =('Bebek Main Window')
MainWindow.geometry("1920x1020")
menubar = Menu(MainWindow)
frameMain = Frame(MainWindow)

cell_def = Pitch_class.bebek_pitch.cell.cell_definition()
pc = Pitch_class.bebek_pitch.create_pitch("252, 247, 247")
poitions = dict()
possible_move =dict()


action_menu =Menu(menubar, tearoff= 0)
menubar.add_cascade(label='Actions', menu= action_menu)
action_menu.add_command(label="Move char", command=lambda:bebek_tools.show_move_options(frameMain,poitions_dict))

label_Menu = Label(MainWindow, text="Actions").grid(column=2, row=10)
poitions_dict=tk_interface.draw_pitch(pc,cell_def,frameMain,poitions)
btn_move = Button(MainWindow, text="Show Move Options", command= lambda:bebek_tools.show_move_options(frameMain,poitions_dict,possible_move)).grid(column=2,row=11)
btn_move = Button(MainWindow, text="Make a move", command= lambda:bebek_tools.Make_Move(possible_move,poitions_dict)).grid(column=2,row=12)
btn_move = Button(MainWindow, text="Clean Move", command= lambda:bebek_tools.Clean_Move_Options(possible_move,poitions_dict)).grid(column=2,row=13)



MainWindow.config(menu= menubar)
frameMain.grid()
MainWindow.mainloop()
