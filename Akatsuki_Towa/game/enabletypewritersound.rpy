#########################################
###typewriter sound effect, copied from here: 
###https://www.renpy.org/wiki/renpy/doc/FAQ#How_do_I_get_a_sound_to_play_while_the_text_appears.2C_like_Phoenix_Wright.3F
#########################################

default persistent.mute_typewriter = False
default persistent.typewriter_volume = 1.0

init -1 python:
    typewritersound = "<from 0.04 to 0.12>sys_utility_typewriter.ogg"
    typewriter_channels = ["typewriter"]

    for ch in typewriter_channels:
        renpy.music.register_channel(ch, "sfx", True)

    def typewriter(event, interact=True, **kwargs):
        if not persistent.mute_typewriter:
            if not interact:
                return

            if event == "show_done":
                renpy.music.play(typewritersound, channel='typewriter', loop=True, relative_volume=persistent.typewriter_volume)
            elif event == "slow_done":
                for ch in typewriter_channels:
                    renpy.music.stop(channel=ch)
####################################################################################################
return