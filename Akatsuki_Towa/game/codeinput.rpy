screen inputdescription():
    text 'Jump to a scene directly, by typing its avg code here, then press Enter.\nTo exit, press Enter without typing anything.\nTo jump to 遊撃士の認定試験 1/12, you would type "10001" (without quotes)':

        size 23
        xcenter 0.5

        if renpy.variant('touch'):
            ypos quick_button_height
        else:
            ycenter 0.5

label codeinput:
stop music
scene avg_bg_518

python:
    while True:
        renpy.show_screen("inputdescription")
        avgcode = renpy.input("{color=#fff}ENTER HERE: {/color}")

        if avgcode == '':
            renpy.hide_screen("inputdescription")
            renpy.jump("codeinputend")
        else:
            if avgcode[0].isdigit():
                avglabel = f'avg{str(avgcode)}'
            else:
                avglabel = avgcode

            if avglabel in renpy.get_all_labels():
                renpy.hide_screen("inputdescription")
                renpy.call(avglabel)
            else:
                renpy.say(None, "That scene does not exist, please try again")
jump codeinput

label codeinputend:
return