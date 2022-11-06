from cmath import polar
import tkinter
from turtle import title
from PIL import Image
from PIL import ImageTk
import matplotlib.pyplot as plt
import numpy as np
import json
import os
import tkinter as tk
from tkinter import TOP, messagebox
from tkinter import BROWSE, LEFT, Canvas, Message, ttk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

player_list = []
picked_char = ""
player_chart = ""
teams_list = []
teams_dict = dict()
selected_team=""

class Playable_char(object):
    #Class for player definition
    def __init__(self,player_def):
        self.cl = player_def["class"]
        self.cost = player_def["cost"]
        self.type = player_def["type"]
        self.health = player_def["health"]
        self.move = player_def["move"]
        self.armor = player_def["armor"]
        self.throw = player_def["throw"]
        self.text = player_def["text"]
        self.dexterity = player_def["dexterity"]
        self.pitch_pic = player_def["pitch_pic"]
        self.portret_pic = player_def["portret_pic"]
        self.skills = player_def["skills"]
        self.mutations = player_def["mutations"]
        self.body = player_def["body"]

class bebek_character(object):
    
    def orc_runner():
        character_prop = dict()
        character_prop['type'] = 'orc'
        character_prop['health'] = 2
        character_prop['move'] = 3
        character_prop['armor'] = 1
        character_prop['throw'] = 5
        character_prop['text'] = 'OR'
        character_prop['team'] = ''
        img_pic = Image.open(r'D:\Programming\kurs\projekty\bebek\Bebek\char_pic\orc.png')
        character_prop['pic'] = ImageTk.PhotoImage(img_pic)
        return character_prop
    
    def dwarf_elder():
        character_prop = dict()
        character_prop['type'] = 'dwarf'
        character_prop['health'] = 1
        character_prop['move'] = 5
        character_prop['armor'] = 4
        character_prop['throw'] = 3
        character_prop['text'] = 'DE'
        character_prop['team'] = ''
        img_pic= Image.open(r'D:\Programming\kurs\projekty\bebek\Bebek\char_pic\dwarf.png')
        character_prop['pic'] = ImageTk.PhotoImage(img_pic)
        return character_prop
    
class bebek_team_picker_menu():
    def Check_for_existing_teams():
        global teams_list
        global teams_dict
        for file in os.listdir("Bebek/Teams_"):
            if file.endswith(".json"):
                team_name = file.split(".")[0]
                teams_dict[team_name]=file
                teams_list.append(team_name)
            
    def char_traits_graph(wnd,fig_canv):
        #stats block
        global picked_char
        global player_chart
        fig_canv = player_chart
        character_data = picked_char
        int_health = character_data.health
        int_armor = character_data.armor
        int_throw = character_data.throw
        int_dexterity = character_data.dexterity
        int_move = character_data.move
        title_str = character_data.cl
        
        data_in = [int_health,int_armor,int_throw,int_dexterity,int_move]
        data_labales = ["Health","Armor","Throw","Dexterity","Move"]
        data_chart = title_str
        max_val = 8
        angles=np.linspace(0,2*np.pi,len(data_labales), endpoint=False)
        fig=plt.figure(figsize=(6,6))
        ax = fig.add_subplot(polar=True)
        ax.plot(angles,data_in, 'o--', color='g', label=title_str)
        ax.fill(angles, data_in, alpha=0.25, color='g')
        ax.set_thetagrids(angles * 180/np.pi, data_labales)
        ax.set_ylim([0,6])
        plt.grid(True)
        plt.tight_layout()
        plt.legend()
        plt.close()
        
        
        fig_canv.destroy()
        
        fig_canv = FigureCanvasTkAgg(fig, master= wnd)
        fig_canv.draw()
        fig_canv.get_tk_widget().pack(fill=tk.BOTH,expand=True)
        
        fig.char_name = title_str
        player_chart = fig
        
    def Read_char_bank():
        with open("Bebek\char_pack.json","r") as file:
            str_json = file.read().rstrip()
        json_chars = json.loads(str_json)
        chars_data_json = json_chars['Players_char']
        return chars_data_json
        
    
    def GetPlayers(Combobox_teamPick,list_Box):
        #Get picked team
        global player_list
        global dict_of_teams
        list_of_players=[]
        Json_chars_data = bebek_team_picker_menu.Read_char_bank()
        picked_team = Combobox_teamPick.get()
        #Get list of players for picked team
        for team in Json_chars_data:
            if picked_team == team['Team']:
                players_json = team['Players']
                break
        
        #Parse Player data
        for player in players_json:
            p=Playable_char(player)
            list_of_players.append(p)
        player_list = list_of_players
        
        for idx,p in enumerate(player_list):
            p_class = p.cl
            list_Box.insert(idx,p_class )
        list_Box.pack()
        
    def GetPlayerDetails(listbox_players,txt_box_class,txt_box_cost,txt_box_type,txt_box_health,txt_box_move,txt_box_armor,txt_box_throw,txt_box_text,txt_box_dext):
        global player_list
        global picked_char
        char_picked = picked_char
        player_class = listbox_players.get(listbox_players.curselection())
        list_of_players = player_list
        for pl_cl in list_of_players:
            picked_class=pl_cl.cl
            if picked_class == player_class:
                picked_char = pl_cl
                break
        bebek_team_picker_menu.Update_players(txt_box_class,txt_box_cost,txt_box_type,txt_box_health,txt_box_move,txt_box_armor,txt_box_throw,txt_box_text,txt_box_dext)

    def Update_players(txt_box_class,txt_box_cost,txt_box_type,txt_box_health,txt_box_move,txt_box_armor,txt_box_throw,txt_box_text,txt_box_dext):
        txt_box_class.configure(state=tk.NORMAL)
        txt_box_class.delete(0,"end")
        txt_box_class.pack()
        
        txt_box_cost.configure(state=tk.NORMAL)
        txt_box_cost.delete(0,"end")
        txt_box_cost.pack()
       
        txt_box_type.configure(state=tk.NORMAL) 
        txt_box_type.delete(0,"end")
        txt_box_type.pack()
        
        txt_box_health.configure(state=tk.NORMAL)        
        txt_box_health.delete(0,"end")
        txt_box_health.pack()
        
        txt_box_move.configure(state=tk.NORMAL)
        txt_box_move.delete(0,"end")
        txt_box_move.pack()
        
        txt_box_armor.configure(state=tk.NORMAL)
        txt_box_armor.delete(0,"end")
        txt_box_armor.pack()
        
        txt_box_throw.configure(state=tk.NORMAL)
        txt_box_throw.delete(0,"end")
        txt_box_throw.pack()
        
        txt_box_text.configure(state=tk.NORMAL)
        txt_box_text.delete(0,"end")
        txt_box_text.pack()
        
        txt_box_dext.configure(state=tk.NORMAL)
        txt_box_dext.delete(0,"end")
        txt_box_dext.pack()
        
        try:
            class_char = str(picked_char.cl)
        except:
            class_char = ""
        txt_box_class.insert(0,class_char)
        txt_box_class.configure(state=tk.DISABLED)
        txt_box_class.pack()
        try:
            cost_char = picked_char.cost
        except:
            cost_char = ""
        txt_box_cost.insert(0,cost_char)
        txt_box_cost.configure(state=tk.DISABLED)
        txt_box_cost.pack()
        try:
            type_char=picked_char.type
        except:
            type_char=""
        txt_box_type.insert(0,type_char)
        txt_box_type.configure(state=tk.DISABLED)
        txt_box_type.pack()
        try:
            health_char = picked_char.health
        except:
            health_char = ""
        txt_box_health.insert(0,health_char)
        txt_box_health.configure(state=tk.DISABLED)
        txt_box_health.pack()
        try:
            move_char = picked_char.move
        except:
            move_char =""
        txt_box_move.insert(0,move_char)
        txt_box_move.configure(state=tk.DISABLED)
        txt_box_move.pack()
        try:
            armor_char = picked_char.armor
        except:
            armor_char = ""
        txt_box_armor.insert(0,armor_char)
        txt_box_armor.configure(state=tk.DISABLED)
        txt_box_armor.pack()
        try:
            throw_char = picked_char.throw
        except:
            throw_char = ""
        txt_box_throw.insert(0,throw_char)
        txt_box_throw.configure(state=tk.DISABLED)
        txt_box_throw.pack()
        
        try:
            text_char = picked_char.text
        except:
            text_char = ""
        txt_box_text.insert(0,text_char)
        txt_box_text.configure(state=tk.DISABLED)
        txt_box_text.pack()
        try:
            dexterity_char = picked_char.dexterity
        except:
            dexterity_char = ""
        txt_box_dext.insert(0,dexterity_char)
        txt_box_dext.configure(state=tk.DISABLED)
        txt_box_dext.pack()   

    def Refresh_obj(root_window):
        for c in sorted(root_window.children):
            root_window.children[c].pack()    
    
    def char_picker(Mian_window):
        global player_list
        
        
        #list of teams
        List_of_teams=[]
        Json_char_bank=bebek_team_picker_menu.Read_char_bank()
        for team in Json_char_bank:
            List_of_teams.append(team['Team'])
        
        bebek_team_picker_menu.Check_for_existing_teams()
        
        
        #GUI
        Window = tk.Toplevel(Mian_window)
        Window.title("Char picker")
        
        Window.maxsize(width=500, height=500)
        w_char_pic = tk.Canvas(Window, width=300, height=500)
        
        top_frame = tk.Frame(Window, width = 100, height = 500, bg='gray')
        top_frame.pack(side='top',  fill='both',  padx=10,  pady=5,  expand=True)
        
        mid_frame = tk.Frame(Window, width = 100, height = 500, bg='gray')
        mid_frame.pack(side='bottom',  fill='both',  padx=10,  pady=5,  expand=True)
        
        frame_left = tk.Frame(mid_frame, width = 100, height = 500, bg='gray')
        frame_left.pack(side='left',  fill='both',  padx=10,  pady=5,  expand=True)
        
        right_frame  =  tk.Frame(mid_frame,  width=650,  height=400,  bg='grey')
        right_frame.pack(side='right',  fill='both',  padx=10,  pady=5,  expand=True)
        
        #bottom_frame= tk.Frame(Window, width = 100, height = 500, bg='gray')
        #bottom_frame.pack(side='bottom',  fill='both',  padx=10,  pady=5,  expand=True)
        
        fig_canv = ""
        
        
        
        #Pick player team
        Label_Pick_Menu = tk.Label(top_frame, text="Pick your team", bg="gray").pack(fill=tk.X,padx=5,pady=5)
        combo_pick_player_team = ttk.Combobox(top_frame)
        combo_pick_player_team['values']=teams_list
        combo_pick_player_team['state'] ='readonly'
        combo_pick_player_team.bind("<<ComboboxSelected>>", lambda x: TeamSquad.read_team(combo_pick_player_team))
        combo_pick_player_team.pack(fill=tk.X,padx=5,pady=5, side="top")
        ### Your Founds
        
        
        #label_part1
        
        #Combobox - pick team players
        Label_Player_Clan = tk.Label(frame_left, text="Pick player fraction", bg="gray").pack(fill=tk.X,padx=5,pady=5)
        combo_pick_team = ttk.Combobox(frame_left)
        combo_pick_team['values']=List_of_teams
        combo_pick_team['state'] ='readonly'
        combo_pick_team.bind("<<ComboboxSelected>>", lambda x: bebek_team_picker_menu.GetPlayers(combo_pick_team,players_listbox))
        combo_pick_team.pack(fill=tk.X,padx=5,pady=5)
        

        
        ###Listbox
        Label_Player_to_buy = tk.Label(frame_left, text="players to can hire:", bg="gray").pack(fill=tk.X,padx=5,pady=5)
        players_listbox = tk.Listbox(frame_left, selectmode=BROWSE)
        players_listbox.bind('<<ListboxSelect>>',lambda x:bebek_team_picker_menu.GetPlayerDetails(players_listbox,txt_box_class,txt_box_cost,txt_box_type,txt_box_health,txt_box_move,txt_box_armor,txt_box_throw,txt_box_text,txt_box_dext))
        players_listbox.pack(fill=tk.BOTH,expand=True)
        #player_chart

        label_char_class = tk.Label(right_frame, text="Class", bg="gray", anchor='w').pack()
        txt_box_class = tk.Entry(right_frame)
        try:
            class_char = str(picked_char.cl)
        except:
            class_char = ""
        txt_box_class.insert(0,class_char)
        txt_box_class.pack()
        
        label_char_cost = tk.Label(right_frame, text="Cost", bg="gray").pack()
        txt_box_cost = tk.Entry(right_frame)
        try:
            cost_char = picked_char.cost
        except:
            cost_char = ""
        txt_box_cost.insert(0,cost_char)
        txt_box_cost.pack()
        
        label_char_type = tk.Label(right_frame, text="Type", bg="gray").pack()
        txt_box_type = tk.Entry(right_frame)
        try:
            type_char=picked_char.type
        except:
            type_char=""
        txt_box_type.insert(0,type_char)
        txt_box_type.pack()
        
        label_char_health = tk.Label(right_frame, text="HP", bg="gray").pack()
        txt_box_health = tk.Entry(right_frame)
        try:
            health_char = picked_char.health
        except:
            health_char = ""
        txt_box_health.insert(0,health_char)
        txt_box_health.pack()
        
        label_char_move = tk.Label(right_frame, text="SPD", bg="gray").pack()
        txt_box_move = tk.Entry(right_frame)
        try:
            move_char = picked_char.move
        except:
            move_char =""
        txt_box_move.insert(0,move_char)
        txt_box_move.pack()
        
        label_char_armor = tk.Label(right_frame, text="DEF", bg="gray").pack()
        txt_box_armor = tk.Entry(right_frame)
        try:
            armor_char = picked_char.armor
        except:
            armor_char = ""
        txt_box_armor.insert(0,armor_char)
        txt_box_armor.pack()
        
        label_char_throw = tk.Label(right_frame, text="Throw", bg="gray").pack()
        txt_box_throw = tk.Entry(right_frame)
        try:
            throw_char = picked_char.throw
        except:
            throw_char = ""
        txt_box_throw.insert(0,throw_char)
        txt_box_throw.pack()
        
        label_char_text = tk.Label(right_frame, text="STR", bg="gray").pack()
        txt_box_text = tk.Entry(right_frame)
        try:
            text_char = picked_char.text
        except:
            text_char = ""
        txt_box_text.insert(0,text_char)
        txt_box_text.pack()
        
        label_char_dext = tk.Label(right_frame, text="DEX", bg="gray").pack()
        txt_box_dext = tk.Entry(right_frame)
        try:
            dexterity_char = picked_char.dexterity
        except:
            dexterity_char = ""
        txt_box_dext.insert(0,dexterity_char)
        txt_box_dext.pack()
        
        #label_char_skills = tk.Label(right_frame, text="Skills", bg="gray").pack()
        
        #label_char_mutation = tk.Label(right_frame, text="Mutations", bg="gray").pack()
        
        #label_char_body = tk.Label(right_frame, text="Body", bg="gray").pack()
        
        #label_char_img = tk.Label(right_frame, text="Miniature", bg="gray").pack()
        
        button_recruit_player =  tk.Button(right_frame, text="Sign contract", command= lambda: [TeamSquad.recruit_player(combo_pick_player_team)])
        button_recruit_player.pack(fill=tk.BOTH,expand=True)
        ###test button
        #chart_frame = tk.Frame(Window,  width=1000,  height=400,  bg='grey')
        #chart_frame.pack(side='right',  fill='both',  padx=10,  pady=5,  expand=True)
        #temp_canva = FigureCanvasTkAgg(master=chart_frame)
        #global player_chart
        #player_chart = temp_canva
        
        
        frame_left.pack()
        right_frame.pack()
        #chart_frame.pack()
        Window.mainloop()
        #w_char_pic.pack()
        #Window renderer
class TeamSquad(object):
    
    def BuildTeam_Window(Mian_window):
        Window = tk.Toplevel(Mian_window)
        Window.title("Register New Team")
        Window.maxsize(width=400, height=120)
        
        frame_main = tk.Frame(Window, width = 400, height = 120, bg='white')
        frame_main.pack(side='left',  fill='both',  padx=10,  pady=5,  expand=True)
        label_teamname = tk.Label(master=frame_main, text="Enter Team name:", bg='white')
        label_teamname.pack()
        txt_box_health = tk.Entry(master=frame_main)
        txt_box_health.pack()
        btn_registerteam = tk.Button(master=frame_main, text="Register", command= lambda:[TeamSquad.BuildTeam(txt_box_health,Window)])
        btn_registerteam.pack()
        Window.mainloop()
        
    
    def BuildTeam(TeamName_textBox, Window):
        team_name = TeamName_textBox.get()
        with open("Bebek/team_schema.json","r") as file:
            str_json = file.read().rstrip()
            json_team_schema = json.loads(str_json)
        try:
            json_team_schema["TeamName"]=team_name
            messagebox.showinfo(title="Team creator", message = "Your team: "+str(team_name)+" has been created")
        except:
            messagebox.showerror(title="Team creator", message = "Your team: "+team_name+" has not been created due to an error")
        
        #save team file
        
        with open("Bebek/Teams_/"+team_name+".json","w") as outputfile:
            json.dump(json_team_schema,outputfile)
        Window.destroy()
    
    def read_team(Combobox_teamPick):
        global teams_dict
        global selected_team
        picked_team_name = Combobox_teamPick.get()
        json_team_file = teams_dict[picked_team_name]
        with open("Bebek/Teams_/"+json_team_file,"r") as file:
            str_json = file.read().rstrip()
        json_chars = json.loads(str_json)
        #team_data_json = json_chars['Players']
        return json_chars

    def playable_char_to_json(playable_char_obj):
        player_def_json = dict()
        player_def_json["class"] = playable_char_obj.cl
        player_def_json["cost"] = playable_char_obj.cost
        player_def_json["type"] = playable_char_obj.type
        player_def_json["health"] = playable_char_obj.health 
        player_def_json["move"] = playable_char_obj.move
        player_def_json["armor"] = playable_char_obj.armor 
        player_def_json["throw"] = playable_char_obj.throw
        player_def_json["text"] = playable_char_obj.text
        player_def_json["dexterity"] = playable_char_obj.dexterity  
        player_def_json["pitch_pic"] = playable_char_obj.pitch_pic
        player_def_json["portret_pic"] = playable_char_obj.portret_pic
        player_def_json["skills"] = playable_char_obj.skills
        player_def_json["mutations"] = playable_char_obj.mutations
        player_def_json["body"] = playable_char_obj.body
        return player_def_json
    
    def recruit_player(Teams_combobox):
        global picked_char
        global teams_dict
        json_team_data = TeamSquad.read_team(Teams_combobox)
        team_name = teams_dict[json_team_data['TeamName'].lower()]
        team_cash = json_team_data["TeamBudget"]
        player_cost =picked_char.cost
        if team_cash >= player_cost:
            player_json_string = TeamSquad.playable_char_to_json(picked_char)
            json_team_data["Players"].append(player_json_string)
            json_team_data["TeamBudget"] = team_cash - player_cost
            messagebox.showinfo(title = "Recrutaion status", message="You manage to sign contract with: "+picked_char.cl)
            
            with open("Bebek/Teams_/"+team_name,"w") as outputfile:
                json.dump(json_team_data,outputfile)
        else:
            messagebox.showwarning(title= "Recrutaion status", message="You dont have enough money to sign contract with this player")
        
        

        
   
        

        
  