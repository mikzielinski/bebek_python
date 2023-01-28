#from logging import root
from hashlib import new
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
from Team_class import TeamSquad,bebek_team_picker_menu
from tkinter import *
from tkinter import *
from tkinter import BROWSE, LEFT, Canvas, Message, ttk
from multiprocessing import Process




#Global vars
teams_list =[]

class bebek_tools():
    #Classes related to game mechanics such as dice rolling, moving, checking if move was legal etc.
        selected_Char = ""
        seleted_Cell =""
        btn_name =""
        saveWord = "dupa"
        spawn_loc =""
        picked_position = ""
        global_var =""
        teams_list =[]
        teams_dict =dict()
        

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
            global spawn_loc
            btn_name = Position_key.btn_position
            spawn_loc= Position_key.btn_position
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
        def create_cell(X,Y,tk_obj,bebek_obj,pitch_definition,dict_pos,cell_def):
            #dict_pos=dict()
            global btn_name
            global global_var
            var = tkinter.IntVar() 
            varBtnName = "Button_Cell"+str(X)+":"+str(Y)
            if X == 1 or  X == pitch_definition['size_l']-1 :
                varBtnName = Button(tk_obj, text="", command=lambda:[bebek_tools.SavePosition(varBtnName),print(btn_name), var.set(1)], width=cell_def['width'], height=cell_def['lenght'],bg="yellow",image=cell_def['image'],compound='center')
                varBtnName.grid(row=X, column=Y)
                varBtnName.cell_taken = False
                varBtnName.btn_position=[str(X)+":"+str(Y)]
                dict_pos[str(X)+":"+str(Y)] =varBtnName
            else:
                varBtnName = Button(tk_obj, text="", command=lambda:[bebek_tools.SavePosition(varBtnName),print(btn_name), var.set(1)],bg="white",width=cell_def['width'], height=cell_def['lenght'], image=cell_def['image'],compound='center')
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
        def set_char(X,Y,tk_obj,bebek_obj,pitch_definition, btn_dict_board, char_dict_pic):
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
            image_char = bebek_obj['pic']
            btn.img = image_char
            char_dict_pic[btn] = btn.img
            btn.selected_char =btn.configure(text =bebek_obj['type'], image=btn.img,compound='center')
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
                if tx == 0 or tx == 13:
                    break
                else:
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
                if ty == 0 or ty == 19:
                    break
                else:
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
                if tx == 0 or tx == 13:
                    break
                else:
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
                if ty == 0 or ty ==19:
                    break
                else:
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
            bebek_tools.RewriteCell_Position()
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
        def RewriteCell_Position():
            global btn_name
            global picked_position
            global spawn_loc
            picked_position = btn_name
            spawn_loc = btn_name
            btn_name = ""
        def Clone_char_btn2btn(orgin_position_btn,new_position_btn,btn_pic_dict):
            #null img for remove
            null_image = tkinter.PhotoImage(width=0, height=0)
            #read character data
            btn_pic = btn_pic_dict[orgin_position_btn]
            btn_pos_taken = orgin_position_btn.cell_taken
            btn_char_type = orgin_position_btn.char_type 
            btn_char_health = orgin_position_btn.char_health
            btn_char_move = orgin_position_btn.char_move
            btn_char_armor = orgin_position_btn.char_armor
            btn_char_throw = orgin_position_btn.char_throw
            btn_char_team = orgin_position_btn.char_team
            btn_char_ball = orgin_position_btn.char_ball
            btn_color = orgin_position_btn['bg']
            btn_text = orgin_position_btn['text']
           
            #Null char values from old position
            btn_pic_dict.pop(orgin_position_btn)
            orgin_position_btn.cell_taken = False
            orgin_position_btn.char_type = ""
            orgin_position_btn.char_health = ""
            orgin_position_btn.char_move = ""
            orgin_position_btn.char_armor = ""
            orgin_position_btn.char_throw = ""
            orgin_position_btn.char_team = ""
            orgin_position_btn.char_ball = ""
            orgin_position_btn['bg'] = 'white'
            orgin_position_btn['text'] =""
            orgin_position_btn['image'] = null_image
            btn_pic_dict[orgin_position_btn]=null_image
            
            # Update destination btn with char data
            new_position_btn.cell_taken = btn_pos_taken
            new_position_btn.char_type = btn_char_type
            new_position_btn.char_health = btn_char_health
            new_position_btn.char_move = btn_char_move
            new_position_btn.char_armor = btn_char_armor
            new_position_btn.char_throw = btn_char_throw
            new_position_btn.char_team = btn_char_team
            new_position_btn.char_ball= btn_char_ball
            new_position_btn['bg'] = btn_color
            new_position_btn['text'] = btn_text
            new_position_btn['image'] = btn_pic
            btn_pic_dict[new_position_btn]=btn_pic
            print(btn_char_type+" has moved from: "+str(orgin_position_btn.btn_position[0])+" to: "+str(new_position_btn.btn_position[0]))
        def Make_Move(move_options_dict, btn_dict_board,btn_pic_dict):
            global btn_name
            global picked_position
            try:
                new_pos = str(btn_name[0])
            except:
                messagebox.showwarning(title='Enter destination', message='You have to pick where you want to go before you click make a move')
            try:
                old_pos = str(picked_position[0])
            except:
                messagebox.showwarning(title='You didnt pick a character', message='You have pick which player you want to move before you click on make a move')
            var = tkinter.IntVar()
            check_var = var
            BtnArr = []
            move_to_cord = new_pos
            for btn_cord in move_options_dict:
                if move_options_dict[btn_cord] == False:
                    btn = btn_dict_board[btn_cord]
                    BtnArr.append(btn)
            
            #bebek_tools.btn_wait4press(BtnArr,var)
            if move_to_cord in move_options_dict:
                move_to_cord_btn = btn_dict_board[move_to_cord]
                move_from_cord_btn = btn_dict_board[old_pos]
                #remove new position from cleaning
                move_options_dict.pop(move_to_cord)
                bebek_tools.Clone_char_btn2btn(move_from_cord_btn,move_to_cord_btn,btn_pic_dict)
                
                #add old position
                #move_options_dict[bebek_obj.dictKey]=True
                bebek_tools.Clean_Move_Options(move_options_dict,btn_dict_board)
            else:
                messagebox.showwarning(title='Illegal move', message='Please pick only highlithed filed')
        
        def Char_spawn_wnd(pics_btn_dict,char_dict_pics,picked_position):
            List_of_teams = []
            Json_char_bank=bebek_team_picker_menu.Read_char_bank()
            for team in Json_char_bank:
                List_of_teams.append(team['Team'])
            bebek_team_picker_menu.Check_for_existing_teams()
            spawn_wnd = tkinter.Toplevel()
            spawn_wnd.minsize(width=400, height=400)
            spawn_wnd.title("Dev console - spawn character")
            pop_frame = tkinter.Frame(spawn_wnd, width = 400, height = 400)
            pop_frame.pack(fill='both',  padx=10,  pady=5,  expand=True)
            label_team = tkinter.Label(pop_frame,text="Pick team")
            label_team.pack()
            combo_team = ttk.Combobox(pop_frame)
            combo_team['values']=List_of_teams
            combo_team['state'] ='readonly'
            combo_team.bind("<<ComboboxSelected>>",lambda x=1: [bebek_team_picker_menu.GetPlayers(combo_team,list_pick_char)])
            combo_team.pack(fill='both',  padx=10,  pady=5,  expand=True)

            label_char = tkinter.Label(pop_frame,text="Pick character to spawn")
            label_char.pack()
            list_pick_char = tkinter.Listbox(pop_frame, selectmode=BROWSE)
            list_pick_char.bind('<<ListboxSelect>>',lambda x:bebek_team_picker_menu.GetPlayerDetails_listOnly(list_pick_char))
            list_pick_char.pack(fill='both',  padx=10,  pady=5,  expand=True)
            label_position = tkinter.Label(pop_frame,text="Enter coordinates(like: y:x)")
            label_position.pack(fill='both',  padx=10,  pady=5,  expand=True)
            textbox_coord = tkinter.Entry(pop_frame)
            textbox_coord.pack(fill='both',  padx=10,  pady=5,  expand=True)
            btn_spawn = tkinter.Button(pop_frame,text="Spawn", command= lambda: TeamSquad.spawn_character(pics_btn_dict,spawn_loc))
            btn_spawn.pack(side='left', fill='both',  padx=10,  pady=5,  expand=True)
            btn_spawn_exit = tkinter.Button(pop_frame,text="Exit",command=spawn_wnd.destroy)
            btn_spawn_exit.pack(side='right', fill='both',  padx=10,  pady=5,  expand=True)
                
        
        def spawn_char_onB(btn_dict_board, char_dict_pic):
            global spawn_loc
            global selected_Char
            X,Y = spawn_loc[0], spawn_loc[1]
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
            btn.char_type = selected_Char.type
            btn.char_health = selected_Char.health
            btn.char_move = selected_Char.move
            btn.char_armor = selected_Char.armor
            btn.char_throw = selected_Char.throw
            btn.char_team = selected_Char['team']
            btn.char_ball = False
            btn.cell_taken = True
            image_char = selected_Char.pitch_pic
            btn.img = image_char
            char_dict_pic[btn] = btn.img
            btn.selected_char =btn.configure(text =selected_Char.type, image=btn.img,compound='center')
            return btn       
            
                 
            
            
            
            
            
            