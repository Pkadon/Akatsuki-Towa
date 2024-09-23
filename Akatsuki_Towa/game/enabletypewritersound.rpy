label enabletypewriter:
#########################################
###typewriter sound effect, copied from here: 
###https://www.renpy.org/wiki/renpy/doc/FAQ#How_do_I_get_a_sound_to_play_while_the_text_appears.2C_like_Phoenix_Wright.3F
#########################################
init -1 python:
    def typewriter(event, interact=True, **kwargs):
        if not interact:
            return

###########I couldn't get it to sound right without an audio recording of the game
###########if you want the typewriter sound, uncomment the single #'s below,
###########name your recording 'sys_utility_typewriter.ogg',
###########and place it in the 'audio' folder

#        if event == "show_done":
#            renpy.sound.play("sys_utility_typewriter.ogg", loop=True)
#        elif event == "slow_done":
#            renpy.sound.stop()
####################################################################################################
return