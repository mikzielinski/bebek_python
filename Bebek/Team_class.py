from PIL import Image
from PIL import ImageTk
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