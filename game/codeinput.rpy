screen inputdescription():
    text 'Jump to a scene directly, by typing its avg code here.\n (Example) To jump to 遊撃士の認定試験 1/12, type "10001" (without quotes) and press enter\nTo exit, press enter without typing anything.':
        size 25
        xycenter (0.5, 0.5)

label codeinput:
stop music
scene avg_bg_518

python:
    while True:
        renpy.show_screen("inputdescription")
        avgcode = renpy.input("ENTER HERE: ")

        if avgcode == '':
            renpy.hide_screen("inputdescription")
            renpy.jump("codeinputend")
        else:
            avglabel = f'avg{str(avgcode)}'
            if avglabel in renpy.get_all_labels():
                renpy.hide_screen("inputdescription")
                renpy.call(avglabel)
            else:
                renpy.say(None, "That scene does not exist, please try again")
jump codeinput

label codeinputend:
return