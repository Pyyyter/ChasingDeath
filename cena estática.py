from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *

################################ JANELA ########################################

# dimensões
gameall_width = 1280
gameall_height = 720

# janela do menu
janela = Window(gameall_width, gameall_height)
janela.set_title("Chasing Death")
background = Sprite("assets/game/bgfinal.png")




################################# GUI ##########################################



GUIlife = Sprite("assets/game/GUIlife.png")
GUIlife.set_position(20,20)



################################ Sprites #######################################



Idle = Sprite("assets/game/Idle.png")
Idle.set_position(250, 500)


Hurt = Sprite("assets/game/Hurt.png")
Hurt.set_position(500,490)

Attack = Sprite("assets/game/Run+Attack.png")
Attack.set_position(380,540)

PAttack = Sprite("assets/game/Attack2.png")
PAttack.set_position(505,400)

fallen = Sprite("assets/game/Dead.png")
fallen.set_position(650,500)

run = Sprite("assets/game/Run.png")
run.set_position(300,540)


####### Game Loop ########

while True:

    # draw all
    
    background.draw()

    GUIlife.draw()
    Hurt.draw()
    fallen.draw()
    run.draw()
    PAttack.draw()
    Idle.draw()
    Attack.draw()

    janela.update()