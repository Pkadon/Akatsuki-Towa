#This is just for testing music loops for popping.
#The only way to access this label should be to enter "bgmtest" on the codeinput screen.

label bgmtest:
python:
    while True:
        bgmcode = renpy.input("{color=#fff}ENTER BGM NAME HERE: {/color}")

        if bgmcode == '':
            renpy.hide_screen("inputdescription")
            renpy.jump("bgmtestend")

        if not bgmcode.endswith('.ogg'): bgmcode += '.ogg'

        if bgmcode in bgm_loop_dict:
            renpy.hide_screen("inputdescription")
            renpy.call('actualbgmtest', bgmcode)
        else:
            renpy.say(None, "That bgm does not exist, please try again")
        renpy.jump('bgmtest')
return


label bgmtestend:
return


screen countdown_timer(length=10.0):
    timer 1.0 repeat True action SetVariable("lencopy", lencopy - 1)
    text "[lencopy]" xalign 0.9 yalign 0.1

label actualbgmtest(bgmname):
python:

    play_music(bgmname)
    renpy.pause(0.1)
    length = renpy.music.get_duration()
    entry = bgm_loop_dict[bgmname]
    if entry['to']: length -= entry['to']

    lencopy = int(abs(length))

    renpy.pause(1.0)
    renpy.music.stop()

$ play_music(bgmname, start=(lencopy-4))

$ lencopy = 4
show screen countdown_timer()
nobody '[renpy.music.get_playing()]'

hide screen countdown_timer
stop music
jump  bgmtest
return