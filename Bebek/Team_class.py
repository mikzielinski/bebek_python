from PIL import Image
from PIL import ImageTk
import json
import tkinter as tk
from tkinter import BROWSE, LEFT, ttk

player_list = []
picked_char = ""

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
    
    def Read_char_bank():
        with open("Bebek\char_pack.json","r") as file:
            str_json = file.read().rstrip()
        json_chars = json.loads(str_json)
        chars_data_json = json_chars['Players_char']
        return chars_data_json
    
    def GetPlayers(Combobox_teamPick,Json_chars_data,list_Box):
        #Get picked team
        global player_list
        list_of_players=[]
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
        player_class = listbox_players.get(listbox_players.curselection())
        list_of_players = player_list
        for pl_cl in list_of_players:
            picked_class=pl_cl.cl
            if picked_class == player_class:
                picked_char = pl_cl
                break
        bebek_team_picker_menu.Update_players(txt_box_class,txt_box_cost,txt_box_type,txt_box_health,txt_box_move,txt_box_armor,txt_box_throw,txt_box_text,txt_box_dext)
        ## test module
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
        
    
        
        #GUI
        Window = tk.Toplevel(Mian_window)
        Window.title("Char picker")
        
        Window.maxsize(width=500, height=500)
        w_char_pic = tk.Canvas(Window, width=300, height=500)
        
        frame_left = tk.Frame(Window, width = 100, height = 500, bg='gray')
        frame_left.pack(side='left',  fill='both',  padx=10,  pady=5,  expand=True)
        
        right_frame  =  tk.Frame(Window,  width=650,  height=400,  bg='grey')
        right_frame.pack(side='right',  fill='both',  padx=10,  pady=5,  expand=True)
        
        
        #label_part1
        Label_Action_Menu = tk.Label(frame_left, text="Pick team").pack(fill=tk.X,padx=5,pady=5)
        #Combobox - pick team
        combo_pick_team = ttk.Combobox(frame_left)
        combo_pick_team['values']=List_of_teams
        combo_pick_team['state'] ='readonly'
        combo_pick_team.bind("<<ComboboxSelected>>", lambda x: bebek_team_picker_menu.GetPlayers(combo_pick_team,Json_char_bank,players_listbox))
        combo_pick_team.pack(fill=tk.X,padx=5,pady=5)
        ###Listbox
        players_listbox = tk.Listbox(frame_left, selectmode=BROWSE)
        players_listbox.bind('<<ListboxSelect>>',lambda x:bebek_team_picker_menu.GetPlayerDetails(players_listbox,txt_box_class,txt_box_cost,txt_box_type,txt_box_health,txt_box_move,txt_box_armor,txt_box_throw,txt_box_text,txt_box_dext))
        players_listbox.pack(fill=tk.BOTH,expand=True)
        
        
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
        
        label_char_skills = tk.Label(right_frame, text="Skills", bg="gray").pack()
        
        label_char_mutation = tk.Label(right_frame, text="Mutations", bg="gray").pack()
        
        label_char_body = tk.Label(right_frame, text="Body", bg="gray").pack()
        
        label_char_img = tk.Label(right_frame, text="Miniature", bg="gray").pack()
        
        
        ###test button
        #btn_test = tk.Button(Window, text="test_btn").pack()
        
        frame_left.pack()
        right_frame.pack()
        Window.mainloop()
        #w_char_pic.pack()
        #Window renderer
        

        
   
        

        
  