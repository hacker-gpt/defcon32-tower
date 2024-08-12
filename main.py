from machine import Pin, I2C, UART
from ssd1306 import SSD1306_I2C
import time
import utime
import framebuf
import kp
from rylr89x import RYLR896
from neopixel import Neopixel

from utils import *
from shows import *
from towers import *
import graphics
import random

# WTF ARE YOU DOING HERE!?! You're not supposed to be here...

# I know you're looking a flag to capture, but I ran out of flags years ago...

# Also Sammy, get out of here! >:D

strip = Neopixel(10, 0, 26, "RGB")

power_on_leds(strip, 100)

lora = RYLR896(0)

time.sleep_ms(1000)

print("Initial UART test (Okay if fails first test)")

lora.test()

print("Final UART test...")

lora.test()

lora.cmd("AT+PARAMETER=8,8,4,8")

lora.cmd("AT+PARAMETER?")

network_pass = "ADD10005E3DCD13047980402E3D52790"

lora.cmd(f"AT+CPIN={network_pass}")

lora.cmd("AT+CPIN?")

lora.set_addr(422)

lora.cmd("AT+ADDRESS?")

# initialize oled screens

i2c=I2C(1,sda=Pin(6), scl=Pin(7), freq=400000)

devices = i2c.scan()

print(devices)

try:
    oled = SSD1306_I2C(128, 32, i2c,addr=devices[1])
    oled.text("Set tower #", 0, 16)
    oled.show()

except Exception as err:
    print(f"Unable to initialize oled: {err}")

tower_number = False
while not tower_number:
    key = kp.keypad(kp.col_list, kp.row_list)
    if key != None:
        if key == "*":
            key = "10"
        elif key == "0":
            key = "11"
        elif key == "#":
            key = "12"
    print("Tower: "+key)
    tower_number = int(key)
    utime.sleep(0.3)

scrn(oled, f"Tower {tower_number}")
utime.sleep(2)

admin_mode = False

select_mode_1_state = False

select_mode_2_state = False

take_over_code = "1234567890"

start = time.ticks_ms()

current_show = "nu_shimmer_show"

press_log = []

offset = 0

if str(tower_number) == "1":
    in_control = True
else:
    in_control = False

display_graphic(graphics.dc_logo, oled)

while True:
    # if in_control:
    #     current_show = "cots_show"
    #     locals()[current_show](time.ticks_ms()-offset, tower_number, strip, take_over=take_over_code)
    # else:
    #     locals()[current_show](time.ticks_ms()-offset, tower_number, strip)
    key = kp.keypad(kp.col_list, kp.row_list)
    msg = lora.read_msg()
    if time.ticks_diff(time.ticks_ms(), start) > 3000:
        if current_show == "first_show":
            if time.ticks_ms()%500 > 250:
                display_graphic(graphics.nyan, oled)
            else:
                display_graphic(graphics.nyan2, oled)
        elif current_show == "milk_marquee_show":
            if time.ticks_ms()/100%100 > 50:
                oled.fill(0)
                oled.text("See something", 2, 0)
                oled.text("suspicious...", 2, 16)
                oled.show()
        elif current_show == "rccola_show":
            oled.fill(0)
            oled.text("GOON DETECTED", 4, 16)
            oled.show()
        elif current_show == "pink_twinkle_show":
            display_graphic(graphics.hari_cut, oled)
        elif current_show == "yo_ping_show":
            display_graphic(graphics.zips, oled)
        elif current_show == "select_matrix_show":
            display_graphic(graphics.dank, oled)
        elif "select_" in current_show:
            display_graphic(graphics.drink, oled)
        elif "solid_" in current_show:
            display_graphic(graphics.protovision, oled)
        elif current_show == "water_show":
            display_graphic(graphics.hatchan, oled)
        elif current_show == "siren_show" or current_show == "five_oh_show" or current_show == "red_step_show":
            display_graphic(graphics.notacamera, oled)
        else:
            display_graphic(graphics.dc_logo, oled)
        
        if key != None and time.ticks_diff(time.ticks_ms(), start) > 240:
            press_log.append(key)
            press_log = press_log[-10:]

            if take_over_code == ''.join(press_log) and not in_control:
                in_control = True
                scrn(oled, "In control")
                take_over_code = ''.join([str(random.randint(0,9)) for x in range(10)])
                lora.send_msg(422, current_show + "|" + "1234567890")
                utime.sleep(1)
                press_log = []
                start = time.ticks_ms()
            
            initial_handshake = admin_login(press_log, oled)
            while initial_handshake:
                key = kp.keypad(kp.col_list, kp.row_list)
                if key != None and time.ticks_diff(time.ticks_ms(), start) > 240:
                    if key == "*":
                        break
                        press_log.append(key)
                    press_log.append(key)
                    press_log = press_log[-10:]
                    print(press_log)
                    admin_mode = admin_login_final(press_log, oled)
                    if admin_mode:
                        power_on_leds(strip, 100)
                        initial_handshake = False
                    start = time.ticks_ms()

            while admin_mode:
                key = kp.keypad(kp.col_list, kp.row_list)
                press_log = press_log[-10:]
                #ADMIN: Change Tower Number
                if key == "1" :
                    scrn(oled,"Set tower #")
                    start = time.ticks_ms()
                    while True:
                        key = kp.keypad(kp.col_list, kp.row_list)
                        if key != None and time.ticks_diff(time.ticks_ms(), start) > 240:
                             # fix key input
                            if key == "*":
                                key = "10"
                            elif key == "0":
                                key = "11"
                            elif key == "#":
                                key = "12"
                            print("Tower: "+key)
                            scrn(oled, f"Tower {key}")
                            tower_number = int(key)
                            utime.sleep(1)
                            admin_mode = False
                            press_log = []
                            break
                    # ADMIN: Change Lora Params
                elif key == "2":
                    scrn(oled, "Set Lora Params")
                    lora.cmd("AT+PARAMETER?")
                    start = time.ticks_ms()
                    params_input = []
                    while len(params_input) < 4:
                        key = kp.keypad(kp.col_list, kp.row_list)
                        if key != None and time.ticks_diff(time.ticks_ms(), start) > 240:
                            params_input.append(key)
                            print(params_input)
                            start = time.ticks_ms()
                            if len(params_input) == 4:
                                lora.cmd(f"AT+PARAMETER={params_input[0]},{params_input[1]},{params_input[2]},{params_input[3]}")
                                lora.cmd("AT+PARAMETER?")
                                scrn(oled, "Params set")
                                utime.sleep(0.3)
                                admin_mode = False
                                press_log = []
                                break
                

                    # ADMIN: Toggle in_control mode
                
                elif key == "3":
                    if in_control:
                        in_control = False
                        scrn(oled, "Lost control")
                    else:
                        in_control = True
                        scrn(oled, "In control")
                    utime.sleep(0.3)
                    admin_mode = False
                    press_log = []

                elif key == "4":
                    rick_roll = 

            if select_mode_1(press_log, oled):
                if in_control:
                    select_mode_1_state = True if not select_mode_1_state else False
                    select_mode_2_state= False if select_mode_1 else True
                    utime.sleep(1)
                elif select_mode_2(press_log, oled):
                    if in_control:
                        select_mode_2_state = True if not select_mode_2_state else False
                        select_mode_1_state= False if select_mode_2_state else True
                        utime.sleep(1)


        print(press_log)
        if not in_control:
            press_log_str = ''.join(press_log)
            scrn(oled, press_log_str)
            display_graphic(graphics.lock_icon_small, oled, clear=False, x_offset=96, width=32)

        if in_control:
            try:
                # fix key input
                if key == "*":
                    key = "10"
                elif key == "0":
                    key = "11"
                elif key == "#":
                    key = "12"

                # lookup show
                if select_mode_1_state:
                    lookup = tower_list[13-1]['shows'][int(key)-1]
                elif select_mode_2_state:
                    lookup = tower_list[14-1]['shows'][int(key)-1]
                else:
                    lookup = tower_list[tower_number-1]['shows'][int(key)-1]

                # should never be blank, but just in case
                if lookup:
                    current_show = lookup
            except:
                pass
            press_log_str = ''.join(press_log)
            scrn(oled, press_log_str)
            if not select_mode_1_state and not select_mode_2_state:
                display_graphic(graphics.dc_logo_small, oled, clear=False, x_offset=96, width=32)
            else:
                display_graphic(graphics.middle_finger_small, oled, clear=False, x_offset=96, width=32)

            # SENDING LORA MESSAGE
            lora.send_msg(422, current_show + "|" + take_over_code)

            offset = time.ticks_ms()
        start = time.ticks_ms()
    if msg:
        offset = time.ticks_ms()
        try:
            lora_msg = msg.split(',')[2]
            msg_parts = lora_msg.split('|')
            current_show = msg_parts[0]
            take_over_code = msg_parts[1]
            in_control = False
        except:
            lora_msg = " "
        # scrn(oled,lora_msg)
        print(take_over_code)
        display_graphic(graphics.lock_icon_small, oled, clear=False, x_offset=96, width=32)

        if not in_control:
            locals()[current_show](time.ticks_ms()-offset, tower_number, strip)
            strip.show()

    if in_control:
        current_show = "cots_show"
        locals()[current_show](time.ticks_ms()-offset, tower_number, strip, take_over=take_over_code)
    else:
        locals()[current_show](time.ticks_ms()-offset, tower_number, strip)