import keyboard
import mouse
import time

#All The Game Skills
skills_states = {0:'q', 1:'w', 2:'e', 3:'r'}

#Selected Skill
actual_state  = 0

def change_actual_state():
    global actual_state
    if(actual_state == 3):
        actual_state = 0
    actual_state += 1

def change_skill():
    #If the mouse is presses, whe change the actual state and press the key related to this state
    if(mouse.is_pressed(mouse.RIGHT)):
        change_actual_state()
        keyboard.press_and_release(skills_states[actual_state])
        print("The State Got Changed to " + str(skills_states[actual_state]))
        time.sleep(0.2)


if __name__ == "__main__":
    while(True):
        change_skill()
