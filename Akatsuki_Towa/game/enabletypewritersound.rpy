#########################################
###typewriter sound effect, copied from here: 
###https://www.renpy.org/wiki/renpy/doc/FAQ#How_do_I_get_a_sound_to_play_while_the_text_appears.2C_like_Phoenix_Wright.3F
#########################################

default persistent.mute_typewriter = False

init -1 python:
    renpy.music.register_channel("typewriter", "sfx", True)
    def typewriter(event, interact=True, **kwargs):
        if not persistent.mute_typewriter:
            if not interact:
                return

            if event == "show_done":
                renpy.music.play("<from 0.055 to 0.110>sys_utility_typewriter.ogg", channel='typewriter', loop=True)
            elif event == "slow_done":
                renpy.music.stop(channel='typewriter')
####################################################################################################
return