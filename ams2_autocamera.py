import mouse, random, time


def positionx():
    return random.randint(120,640)
    

def positiony():
    return random.randint(0,1920)

running = True

def stopclick():
    print('stop linia 14')
    global running
    running = False

mouse.on_right_click(stopclick)

while running:    
    mouse.get_position()
    mouse.move(250,positionx(), absolute=True,duration=2) 
    mouse.click('left')
    time.sleep(5)

    # if running == False:
    #     break