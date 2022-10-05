#from logging import root
import random
from threading import Thread
import tkinter
import win32api
import time
from tkinter import *
from tkinter import messagebox
from xml.dom import xmlbuilder
#from tkinter import Event
#from turtle import bgcolor, color
from Player_class import Player
from tkinter import *
from multiprocessing import Process




#Global vars


class bebek_tools():
    #Classes related to game mechanics such as dice rolling, moving, checking if move was legal etc.
        selected_Char = ""
        seleted_Cell =""
        btn_name =""
        saveWord = "dupa"
        M_check = ""
        global_var ="" 
        
        
            
        
        
        
        def btn_wait4press(button_obj_arr,btn_check_str):
            if any(button_obj_arr):
                pass
            for btn in button_obj_arr:
                btn.wait_variable(btn_check_str)
                print("pressed")
        def NumRandomizer(old_num):
            new_num=old_num+random.randint(1,10)
            return new_num
        def SavePosition(Position_key):
            global btn_name
            btn_name = Position_key.btn_position
            return btn_name       
        def roll_dice(diceType,number_of_dices):
            roll_result=[]
            for number_of_dices in range(number_of_dices):
                match diceType:
                    case 'd6s':
                        roll = random.randint(1,6)
                        roll_result.append(roll)
                    case 'd8s':
                        roll = random.randint(1,8)
                        roll_result.append(roll)
                    case 'd6Block':
                        roll = random.randint(1,6)
                        match roll:
                            case 1:
                                roll_result.append("PB")
                                #Push back
                            case 2:
                                roll_result.append("DS")
                                #Defender Stumbles
                            case 3:
                                roll_result.append("AD")
                                #Attacker Down
                            case 4:
                                roll_result.append("BD")
                                #Both down
                            case 5:
                                roll_result.append("DD")
                                #Defender Dawn
                            case 6:
                                roll_result.append("PB")
                                #Push back
                    case 'd6Weather':
                        roll_1 = random.randint(1,6)
                        roll_2 = random.randint(1,6)
                        roll = roll_1 + roll_2
                        match roll:
                            case 2:
                                roll_result.append('Sweltering Heat')
                            case 3:
                                roll_result.append('Very Sunny')
                            case 4:
                                roll_result.append('Nice')
                            case 5:
                                roll_result.append('Nice')
                            case 6:
                                roll_result.append('Nice')
                            case 7:
                                roll_result.append('Nice')
                            case 8:
                                roll_result.append('Nice')
                            case 9:
                                roll_result.append('Nice')
                            case 11:
                                roll_result.append('Pouring Rain')
                            case 12:
                                roll_result.append('Blizzard')               
            return roll_result    
        def create_cell(X,Y,tk_obj,bebek_obj,pitch_definition,dict_pos):
            #dict_pos=dict()
            global btn_name
            global global_var
            var = tkinter.IntVar() 
            varBtnName = "Button_Cell"+str(X)+":"+str(Y)
            if X == 1 or  X == pitch_definition['size_l']-1 :
                varBtnName = Button(tk_obj, text="", command=lambda:[bebek_tools.SavePosition(varBtnName),print(btn_name), var.set(1)], width=4, height=2,bg="yellow")
                varBtnName.grid(row=X, column=Y)
                varBtnName.cell_taken = False
                varBtnName.btn_position=[str(X)+":"+str(Y)]
                dict_pos[str(X)+":"+str(Y)] =varBtnName
            else:
                varBtnName = Button(tk_obj, text="", command=lambda:[bebek_tools.SavePosition(varBtnName),print(btn_name), var.set(1)],bg="white",width=4, height=2)
                varBtnName.grid(row=X, column=Y)
                varBtnName.cell_taken = False
                varBtnName.btn_position=[str(X)+":"+str(Y)]
                dict_pos[str(X)+":"+str(Y)] =varBtnName
            return dict_pos      
        def get_position_btn(dict_key):
            global selected_Char
            #btn_char['bg'] = "blue"
            selected_Char = dict_key
            #print(dict_key)
            return selected_Char       
        def get_btn_name_by_button(root,frame):
            global btn_name
            r = root.focus_get()
            #rs = root.grid_slaves(row=r, column=c)
            f = frame.focus_get
            #btn_string = "<tkinter.Button object .!frame."+str(event._name)+">"
            #btn_name = btn_string
            print(r)
            return r           
        def set_char(X,Y,tk_obj,bebek_obj,pitch_definition, btn_dict_board):
            #Find Button to update
            var = tkinter.IntVar()
            dictKey = str(X)+":"+str(Y)
            btn = btn_dict_board[dictKey]
            btn_str = str(btn)
            btn_num = [int(i) for i in btn_str if i.isdigit()]
            btn_str = int("".join(map(str,btn_num)))
            btn_tag_press = '<ButtonPress-'+str(btn_str)+'>'
            btn_tag_release = '<ButtonRelease-'+str(btn_str)+'>'
            #Set character vars
            btn.char_type = bebek_obj['type']
            btn.char_health = bebek_obj['health']
            btn.char_move = bebek_obj['move']
            btn.char_armor = bebek_obj['armor']
            btn.char_throw = bebek_obj['throw']
            btn.char_team = bebek_obj['team']
            btn.char_ball = False
            btn.cell_taken = True
            #btn.selected_char =btn.configure(text =bebek_obj['type'], command =lambda:[bebek_tools.get_position_btn(dictKey)])
            btn.selected_char =btn.configure(text =bebek_obj['type'])
            return btn       
        def show_move_options(tk_obj, btn_dict_board,possible_move_dict):
            #start move setup
            global btn_name
            try:
                dictKey = str(btn_name)
                dictKey = dictKey.replace("[","").replace("]","")
                dictKey = dictKey.replace("'","")
                print(dictKey)
            except:
                messagebox.showwarning(title='No character selected', message='You cannot perform this action as you did not selected any character')
            btn = btn_dict_board[dictKey]
            start_position = dictKey
            sX = start_position.split(":")[1]
            sY = start_position.split(":")[0]
            move_range= btn.char_move
            start_btn = btn_dict_board[str(sX)+":"+str(sY)]
            #Get fileds in range
            for move_x in range(move_range):
                ty = move_x+1
                tx = int(sX)+ty
                temp_path = str(sY)+":"+str(tx)
                path_btn = btn_dict_board[temp_path]
                if path_btn.cell_taken == False:
                    path_btn['bg'] = 'green'
                    possible_move_dict[temp_path]=path_btn.cell_taken
                else:
                    path_btn['bg'] = 'red'
                    possible_move_dict[temp_path]=path_btn.cell_taken
                    break
            for move_y in range(move_range):
                ty=int(sY)+move_y+1
                temp_path = str(ty)+":"+str(sX)
                path_btn = btn_dict_board[temp_path]
                if path_btn.cell_taken == False:
                    path_btn['bg'] = 'green'
                    possible_move_dict[temp_path]=path_btn.cell_taken
                else:
                    path_btn['bg'] = 'red'
                    possible_move_dict[temp_path]=path_btn.cell_taken
                    break
            for move_x in range(move_range):
                tx=int(sX)-move_x-1
                temp_path = str(sY)+":"+str(tx)
                path_btn = btn_dict_board[temp_path]
                if path_btn.cell_taken == False:
                    path_btn['bg'] = 'green'
                    possible_move_dict[temp_path]=path_btn.cell_taken
                else:
                    path_btn['bg'] = 'red'
                    possible_move_dict[temp_path]=path_btn.cell_taken
                    break
            for move_y in range(move_range):
                ty=int(sY)-move_y-1
                temp_path = str(ty)+":"+str(sX)
                path_btn = btn_dict_board[temp_path]
                if path_btn.cell_taken == False:
                    path_btn['bg'] = 'green'
                    possible_move_dict[temp_path]=path_btn.cell_taken
                else:
                    path_btn['bg'] = 'red'
                    possible_move_dict[temp_path]=path_btn.cell_taken
                    break
                #output is an action input - you see possible moves and info if there is smth on it already
            return possible_move_dict
        def Clean_Move_Options(move_options_dict, btn_dict_board):
            for cord_cell in move_options_dict:
                btn_cell = btn_dict_board[cord_cell]
                sx = cord_cell.split(":")[0]
                if int(sx) == 1 or int(sx) == 18:
                    try:
                        btn_cell['bg'] = 'yellow'
                    except:
                        pass
                else:
                    try: 
                        btn_cell['bg'] = 'white'
                    except:
                        pass
        
        def thread_var_monitor(old_value):
            global btn_name
            p1 = str(old_value)
            p2 = str(btn_name)
            while p1 == p2:
                try:
                    
                    d = p2
                except:
                    d = p2
                if p1 != d:
                    break
                else:
                    print("awaiting")
                    
                
            print("input recived")
        
        def Make_Move(move_options_dict, btn_dict_board):
            global btn_name
            old_pos = btn_name
            var = tkinter.IntVar()
            check_var = var
            BtnArr = []
            move_to_cord = btn_name
            for btn_cord in move_options_dict:
                if move_options_dict[btn_cord] == False:
                    btn = btn_dict_board[btn_cord]
                    BtnArr.append(btn)
            print("added")
            thread_cpu =Thread(target=bebek_tools.thread_var_monitor(old_pos))
            thread_cpu.start()
            thread_cpu.join()
            
            #bebek_tools.btn_wait4press(BtnArr,var)
            if move_to_cord in move_options_dict:
                move_to_btn = btn_dict_board[move_to_cord]
                
                
                #remove new position from cleaning
                move_options_dict.pop(move_to_cord)
                #add old position
                #move_options_dict[bebek_obj.dictKey]=True
                bebek_tools.Clean_Move_Options(move_options_dict,btn_dict_board)
            else:
                messagebox.showwarning(title='Illegal move', message='Please pick only highlithed filed')
            
            pass
        
                
        
        
            
                 
            
            
            
            
            
            