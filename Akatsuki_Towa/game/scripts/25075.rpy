label avg25075(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "other_7079.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
get_char('c23') '[convertstrid(1210229)]' (**arg(1, 1210229))
hide p2
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na23.ogg"
get_char('c13') '[convertstrid(1210230)]' (**arg(2, 1210230))
return "avg25075"