from tkinter import *
# РёРјРїРѕСЂС‚РёСЂСѓРµРј Р±РёР±Р»РёРѕС‚РµРєСѓ random
import random
 
# Р”РѕР±Р°РІР»СЏРµРј РіР»РѕР±Р°Р»СЊРЅС‹Рµ РїРµСЂРµРјРµРЅРЅС‹Рµ

# РіР»РѕР±Р°Р»СЊРЅС‹Рµ РїРµСЂРµРјРµРЅРЅС‹Рµ
# РЅР°СЃС‚СЂРѕР№РєРё РѕРєРЅР°
WIDTH = 900
HEIGHT = 300
 
# РЅР°СЃС‚СЂРѕР№РєРё СЂР°РєРµС‚РѕРє
 
# С€РёСЂРёРЅР° СЂР°РєРµС‚РєРё
PAD_W = 10
# РІС‹СЃРѕС‚Р° СЂР°РєРµС‚РєРё
PAD_H = 100
 
# РЅР°СЃС‚СЂРѕР№РєРё РјСЏС‡Р°
# РќР°СЃРєРѕР»СЊРєРѕ Р±СѓРґРµС‚ СѓРІРµР»РёС‡РёРІР°С‚СЊСЃСЏ СЃРєРѕСЂРѕСЃС‚СЊ РјСЏС‡Р° СЃ РєР°Р¶РґС‹Рј СѓРґР°СЂРѕРј
BALL_SPEED_UP = 1.05
# РњР°РєСЃРёРјР°Р»СЊРЅР°СЏ СЃРєРѕСЂРѕСЃС‚СЊ РјСЏС‡Р°
BALL_MAX_SPEED = 40
# СЂР°РґРёСѓСЃ РјСЏС‡Р°
BALL_RADIUS = 30

INITIAL_SPEED = 20
BALL_X_SPEED = INITIAL_SPEED
BALL_Y_SPEED = INITIAL_SPEED

# РЎС‡РµС‚ РёРіСЂРѕРєРѕРІ
PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0

# Р”РѕР±Р°РІРёРј РіР»РѕР±Р°Р»СЊРЅСѓСЋ РїРµСЂРµРјРµРЅРЅСѓСЋ РѕС‚РІРµС‡Р°СЋС‰СѓСЋ Р·Р° СЂР°СЃСЃС‚РѕСЏРЅРёРµ
# РґРѕ РїСЂР°РІРѕРіРѕ РєСЂР°СЏ РёРіСЂРѕРІРѕРіРѕ РїРѕР»СЏ
right_line_distance = WIDTH - PAD_W

def update_score(player):
    global PLAYER_1_SCORE, PLAYER_2_SCORE
    if player == "right":
        PLAYER_1_SCORE += 1
        c.itemconfig(p_1_text, text=PLAYER_1_SCORE)
    else:
        PLAYER_2_SCORE += 1
        c.itemconfig(p_2_text, text=PLAYER_2_SCORE)
 
def spawn_ball():
    global BALL_X_SPEED
    # Р’С‹СЃС‚Р°РІР»СЏРµРј РјСЏС‡ РїРѕ С†РµРЅС‚СЂСѓ
    c.coords(BALL, WIDTH/2-BALL_RADIUS/2,
             HEIGHT/2-BALL_RADIUS/2,
             WIDTH/2+BALL_RADIUS/2,
             HEIGHT/2+BALL_RADIUS/2)
    # Р—Р°РґР°РµРј РјСЏС‡Сѓ РЅР°РїСЂР°РІР»РµРЅРёРµ РІ СЃС‚РѕСЂРѕРЅСѓ РїСЂРѕРёРіСЂР°РІС€РµРіРѕ РёРіСЂРѕРєР°,
    # РЅРѕ СЃРЅРёР¶Р°РµРј СЃРєРѕСЂРѕСЃС‚СЊ РґРѕ РёР·РЅР°С‡Р°Р»СЊРЅРѕР№
    BALL_X_SPEED = -(BALL_X_SPEED * -INITIAL_SPEED) / abs(BALL_X_SPEED)

# С„СѓРЅРєС†РёСЏ РѕС‚СЃРєРѕРєР° РјСЏС‡Р°
def bounce(action):
    global BALL_X_SPEED, BALL_Y_SPEED
    # СѓРґР°СЂРёР»Рё СЂР°РєРµС‚РєРѕР№
    if action == "strike":
        BALL_Y_SPEED = random.randrange(-10, 10)
        if abs(BALL_X_SPEED) < BALL_MAX_SPEED:
            BALL_X_SPEED *= -BALL_SPEED_UP
        else:
            BALL_X_SPEED = -BALL_X_SPEED
    else:
        BALL_Y_SPEED = -BALL_Y_SPEED

# СѓСЃС‚Р°РЅР°РІР»РёРІР°РµРј РѕРєРЅРѕ
root = Tk()
root.title("PythonicWay Pong")
 
# РѕР±Р»Р°СЃС‚СЊ Р°РЅРёРјР°С†РёРё
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
c.pack()
 
# СЌР»РµРјРµРЅС‚С‹ РёРіСЂРѕРІРѕРіРѕ РїРѕР»СЏ
 
# Р»РµРІР°СЏ Р»РёРЅРёСЏ
c.create_line(PAD_W, 0, PAD_W, HEIGHT, fill="white")
# РїСЂР°РІР°СЏ Р»РёРЅРёСЏ
c.create_line(WIDTH-PAD_W, 0, WIDTH-PAD_W, HEIGHT, fill="white")
# С†РµРЅС‚СЂР°Р»СЊРЅР°СЏ Р»РёРЅРёСЏ
c.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, fill="white")
 
# СѓСЃС‚Р°РЅРѕРІРєР° РёРіСЂРѕРІС‹С… РѕР±СЉРµРєС‚РѕРІ
 
# СЃРѕР·РґР°РµРј РјСЏС‡
BALL = c.create_oval(WIDTH/2-BALL_RADIUS/2,
                     HEIGHT/2-BALL_RADIUS/2,
                     WIDTH/2+BALL_RADIUS/2,
                     HEIGHT/2+BALL_RADIUS/2, fill="white")
 
# Р»РµРІР°СЏ СЂР°РєРµС‚РєР°
LEFT_PAD = c.create_line(PAD_W/2, 0, PAD_W/2, PAD_H, width=PAD_W, fill="yellow")
 
# РїСЂР°РІР°СЏ СЂР°РєРµС‚РєР°
RIGHT_PAD = c.create_line(WIDTH-PAD_W/2, 0, WIDTH-PAD_W/2, 
                          PAD_H, width=PAD_W, fill="yellow")


p_1_text = c.create_text(WIDTH-WIDTH/6, PAD_H/4,
                         text=PLAYER_1_SCORE,
                         font="Arial 20",
                         fill="white")
 
p_2_text = c.create_text(WIDTH/6, PAD_H/4,
                          text=PLAYER_2_SCORE,
                          font="Arial 20",
                          fill="white")

# РґРѕР±Р°РІРёРј РіР»РѕР±Р°Р»СЊРЅС‹Рµ РїРµСЂРµРјРµРЅРЅС‹Рµ РґР»СЏ СЃРєРѕСЂРѕСЃС‚Рё РґРІРёР¶РµРЅРёСЏ РјСЏС‡Р°
# РїРѕ РіРѕСЂРёР·РѕРЅС‚Р°Р»Рё
BALL_X_CHANGE = 20
# РїРѕ РІРµСЂС‚РёРєР°Р»Рё
BALL_Y_CHANGE = 0
 
def move_ball():
    # РѕРїСЂРµРґРµР»СЏРµРј РєРѕРѕСЂРґРёРЅР°С‚С‹ СЃС‚РѕСЂРѕРЅ РјСЏС‡Р° Рё РµРіРѕ С†РµРЅС‚СЂР°
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_center = (ball_top + ball_bot) / 2
 
    # РІРµСЂС‚РёРєР°Р»СЊРЅС‹Р№ РѕС‚СЃРєРѕРє
    # Р•СЃР»Рё РјС‹ РґР°Р»РµРєРѕ РѕС‚ РІРµСЂС‚РёРєР°Р»СЊРЅС‹С… Р»РёРЅРёР№ - РїСЂРѕСЃС‚Рѕ РґРІРёРіР°РµРј РјСЏС‡
    if ball_right + BALL_X_SPEED < right_line_distance and \
            ball_left + BALL_X_SPEED > PAD_W:
        c.move(BALL, BALL_X_SPEED, BALL_Y_SPEED)
    # Р•СЃР»Рё РјСЏС‡ РєР°СЃР°РµС‚СЃСЏ СЃРІРѕРµР№ РїСЂР°РІРѕР№ РёР»Рё Р»РµРІРѕР№ СЃС‚РѕСЂРѕРЅРѕР№ РіСЂР°РЅРёС†С‹ РїРѕР»СЏ
    elif ball_right == right_line_distance or ball_left == PAD_W:
        # РџСЂРѕРІРµСЂСЏРµРј РїСЂР°РІРѕР№ РёР»Рё Р»РµРІРѕР№ СЃС‚РѕСЂРѕРЅС‹ РјС‹ РєР°СЃР°РµРјСЃСЏ
        if ball_right > WIDTH / 2:
            # Р•СЃР»Рё РїСЂР°РІРѕР№, С‚Рѕ СЃСЂР°РІРЅРёРІР°РµРј РїРѕР·РёС†РёСЋ С†РµРЅС‚СЂР° РјСЏС‡Р°
            # СЃ РїРѕР·РёС†РёРµР№ РїСЂР°РІРѕР№ СЂР°РєРµС‚РєРё.
            # Р РµСЃР»Рё РјСЏС‡ РІ РїСЂРµРґРµР»Р°С… СЂР°РєРµС‚РєРё РґРµР»Р°РµРј РѕС‚СЃРєРѕРє
            if c.coords(RIGHT_PAD)[1] < ball_center < c.coords(RIGHT_PAD)[3]:
                bounce("strike")
            else:
                # РРЅР°С‡Рµ РёРіСЂРѕРє РїСЂРѕРїСѓСЃС‚РёР» - С‚СѓС‚ РѕСЃС‚Р°РІРёРј РїРѕРєР° pass, РµРіРѕ РјС‹ Р·Р°РјРµРЅРёРј РЅР° РїРѕРґСЃС‡РµС‚ РѕС‡РєРѕРІ Рё СЂРµСЃРїР°СѓРЅ РјСЏС‡РёРєР°
                update_score("left")
                spawn_ball()
        else:
            # РўРѕ Р¶Рµ СЃР°РјРѕРµ РґР»СЏ Р»РµРІРѕРіРѕ РёРіСЂРѕРєР°
            if c.coords(LEFT_PAD)[1] < ball_center < c.coords(LEFT_PAD)[3]:
                bounce("strike")
            else:
                update_score("right")
                spawn_ball()
    # РџСЂРѕРІРµСЂРєР° СЃРёС‚СѓР°С†РёРё, РІ РєРѕС‚РѕСЂРѕР№ РјСЏС‡РёРє РјРѕР¶РµС‚ РІС‹Р»РµС‚РµС‚СЊ Р·Р° РіСЂР°РЅРёС†С‹ РёРіСЂРѕРІРѕРіРѕ РїРѕР»СЏ.
    # Р’ С‚Р°РєРѕРј СЃР»СѓС‡Р°Рµ РїСЂРѕСЃС‚Рѕ РґРІРёРіР°РµРј РµРіРѕ Рє РіСЂР°РЅРёС†Рµ РїРѕР»СЏ.
    else:
        if ball_right > WIDTH / 2:
            c.move(BALL, right_line_distance-ball_right, BALL_Y_SPEED)
        else:
            c.move(BALL, -ball_left+PAD_W, BALL_Y_SPEED)
    # РіРѕСЂРёР·РѕРЅС‚Р°Р»СЊРЅС‹Р№ РѕС‚СЃРєРѕРє
    if ball_top + BALL_Y_SPEED < 0 or ball_bot + BALL_Y_SPEED > HEIGHT:
        bounce("ricochet")

# Р·Р°РґР°РґРёРј РіР»РѕР±Р°Р»СЊРЅС‹Рµ РїРµСЂРµРјРµРЅРЅС‹Рµ СЃРєРѕСЂРѕСЃС‚Рё РґРІРёР¶РµРЅРёСЏ СЂР°РєРµС‚РѕРє
# СЃРєРѕСЂРѕСЃСЊ СЃ РєРѕС‚РѕСЂРѕР№ Р±СѓРґСѓС‚ РµР·РґРёС‚СЊ СЂР°РєРµС‚РєРё
PAD_SPEED = 20
# СЃРєРѕСЂРѕСЃС‚СЊ Р»РµРІРѕР№ РїР»Р°С‚С„РѕСЂРјС‹
LEFT_PAD_SPEED = 0
# СЃРєРѕСЂРѕСЃС‚СЊ РїСЂР°РІРѕР№ СЂР°РєРµС‚РєРё
RIGHT_PAD_SPEED = 0
 
# С„СѓРЅРєС†РёСЏ РґРІРёР¶РµРЅРёСЏ РѕР±РµРёС… СЂР°РєРµС‚РѕРє
def move_pads():
    # РґР»СЏ СѓРґРѕР±СЃС‚РІР° СЃРѕР·РґР°РґРёРј СЃР»РѕРІР°СЂСЊ, РіРґРµ СЂР°РєРµС‚РєРµ СЃРѕРѕС‚РІРµС‚СЃС‚РІСѓРµС‚ РµРµ СЃРєРѕСЂРѕСЃС‚СЊ
    PADS = {LEFT_PAD: LEFT_PAD_SPEED, 
            RIGHT_PAD: RIGHT_PAD_SPEED}
    # РїРµСЂРµР±РёСЂР°РµРј СЂР°РєРµС‚РєРё
    for pad in PADS:
        # РґРІРёРіР°РµРј СЂР°РєРµС‚РєСѓ СЃ Р·Р°РґР°РЅРЅРѕР№ СЃРєРѕСЂРѕСЃС‚СЊСЋ
        c.move(pad, 0, PADS[pad])
        # РµСЃР»Рё СЂР°РєРµС‚РєР° РІС‹Р»РµР·Р°РµС‚ Р·Р° РёРіСЂРѕРІРѕРµ РїРѕР»Рµ РІРѕР·РІСЂР°С‰Р°РµРј РµРµ РЅР° РјРµСЃС‚Рѕ
        if c.coords(pad)[1] < 0:
            c.move(pad, 0, -c.coords(pad)[1])
        elif c.coords(pad)[3] > HEIGHT:
            c.move(pad, 0, HEIGHT - c.coords(pad)[3])

 
def main():
    move_ball()
    move_pads()
    # РІС‹Р·С‹РІР°РµРј СЃР°РјСѓ СЃРµР±СЏ РєР°Р¶РґС‹Рµ 30 РјРёР»Р»РёСЃРµРєСѓРЅРґ
    root.after(30, main)

# РЈСЃС‚Р°РЅРѕРІРёРј С„РѕРєСѓСЃ РЅР° Canvas С‡С‚РѕР±С‹ РѕРЅ СЂРµР°РіРёСЂРѕРІР°Р» РЅР° РЅР°Р¶Р°С‚РёСЏ РєР»Р°РІРёС€
c.focus_set()
 
# РќР°РїРёС€РµРј С„СѓРЅРєС†РёСЋ РѕР±СЂР°Р±РѕС‚РєРё РЅР°Р¶Р°С‚РёСЏ РєР»Р°РІРёС€
def movement_handler(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym == "w":
        LEFT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "s":
        LEFT_PAD_SPEED = PAD_SPEED
    elif event.keysym == "Up":
        RIGHT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "Down":
        RIGHT_PAD_SPEED = PAD_SPEED
 
# РџСЂРёРІСЏР¶РµРј Рє Canvas СЌС‚Сѓ С„СѓРЅРєС†РёСЋ
c.bind("<KeyPress>", movement_handler)
 
# РЎРѕР·РґР°РґРёРј С„СѓРЅРєС†РёСЋ СЂРµР°РіРёСЂРѕРІР°РЅРёСЏ РЅР° РѕС‚РїСѓСЃРєР°РЅРёРµ РєР»Р°РІРёС€Рё
def stop_pad(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym in "ws":
        LEFT_PAD_SPEED = 0
    elif event.keysym in ("Up", "Down"):
        RIGHT_PAD_SPEED = 0
 
# РџСЂРёРІСЏР¶РµРј Рє Canvas СЌС‚Сѓ С„СѓРЅРєС†РёСЋ
c.bind("<KeyRelease>", stop_pad)

# Р·Р°РїСѓСЃРєР°РµРј РґРІРёР¶РµРЅРёРµ
main()
 
# Р·Р°РїСѓСЃРєР°РµРј СЂР°Р±РѕС‚Сѓ РѕРєРЅР°
root.mainloop()