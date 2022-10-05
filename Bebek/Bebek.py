#This project is about creating of AI based board game
import sys
import tkinter
import Pitch_class
import Tools_class
import tk_interface



#pitch_config=Pitch_class.bebek_pitch
#print(pitch_config.pitch_weather)

MainWindow = tkinter.Tk()

list_obj=[]
cell_def = Pitch_class.bebek_pitch.cell.cell_definition()
pc = Pitch_class.bebek_pitch.create_pitch("252, 247, 247")
tk_interface.draw_pitch(pc,cell_def,MainWindow)

