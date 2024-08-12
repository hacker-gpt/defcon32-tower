import framebuf

def power_on_leds(strip, brightness):
    strip.brightness(brightness)
    strip.set_pixel(0,(255,50,0))
    strip.set_pixel(1,(255,50,0))
    strip.set_pixel(2,(255,50,0))
    strip.set_pixel(3,(255,50,0))
    strip.set_pixel(4,(255,50,0))
    strip.set_pixel(5,(255,50,0))
    strip.set_pixel(6,(255,50,0))
    strip.set_pixel(7,(255,50,0))
    strip.set_pixel(8,(255,50,0))
    strip.set_pixel(9,(255,50,0))

def power_on_leds(strip, brightness):
    strip.brightness(brightness)
    strip.set_pixel(0,(255,50,0))
    strip.set_pixel(1,(255,50,0))
    strip.set_pixel(2,(255,50,0))
    strip.set_pixel(3,(255,50,0))
    strip.set_pixel(4,(255,50,0))
    strip.set_pixel(5,(255,50,0))
    strip.set_pixel(6,(255,50,0))
    strip.set_pixel(7,(255,50,0))
    strip.set_pixel(8,(255,50,0))
    strip.set_pixel(9,(255,50,0))
    strip.show()

# simple scrn function
def scrn(oled, message):
    oled.fill(0)
    oled.text(message, 0, 16)
    oled.show()

def admin_login(press_log, oled):
    admin_pass = "220616"
    if admin_pass == ''.join(press_log[-len(admin_pass):]):
        scrn(oled,"mode change...")
        return True
    else:
        return False
    
def admin_login_final(press_log, oled):
    admin_pass = "69515"
    if admin_pass == ''.join(press_log[-len(admin_pass):]):
        scrn(oled,"admin mode")
        return True
    else:
        return False
    
def select_mode_1(press_log, oled):
    admin_pass = "2600"
    if admin_pass == ''.join(press_log[-len(admin_pass):]):
        scrn(oled,"A secret mode!")
        return True
    else:
        return False
    
def select_mode_2(press_log, oled):
    admin_pass = "5558632"
    if admin_pass == ''.join(press_log[-len(admin_pass):]):
        scrn(oled,"Protovision...")
        return True
    else:
        return False
    
def display_graphic(byte_array, oled, clear=True, x_offset=0, y_offest=0, width=128):
    fb = framebuf.FrameBuffer(byte_array, width, 32, framebuf.MONO_HLSB)
    if clear:
        oled.fill(0)
    oled.blit(fb,x_offset,y_offest)
    oled.show()
