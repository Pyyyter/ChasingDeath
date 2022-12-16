# Game Setup
WIDTH    = 1920
HEIGTH   = 1080
FPS      = 60
TILESIZE = 32

# UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'assets/font/joystix.ttf'
UI_FONT_SIZE = 18 

# General colors
WATER_COLORS = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# UI COLORS
HEALTH_COLOR='red'
ENERGY_COLOR='blue'
UI_BORDER_COLOR_ACTIVE='gold'

# ARMAS
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15,'graphic':'assets/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30,'graphic':'assets/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic':'assets/weapons/axe/full.png'},
    'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'assets/weapons/rapier/full.png'},
    'sai':{'cooldown': 80, 'damage': 10, 'graphic':'assets/weapons/sai/full.png'}}

magic_data = {
    'flame': {'strength': 5,'cost': 20,'graphic':'assets/particles/flame/fire.png'},
    'heal' : {'strength': 20,'cost': 10,'graphic':'assets/particles/heal/heal.png'}}
