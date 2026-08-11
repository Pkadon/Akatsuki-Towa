label avg25306(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with trans
play sfx2 "fight_6015.ogg"
get_char('c0') '[convertstrid(1211180)]' (**arg(1, 1211180))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1211181)]' (**arg(2, 1211181))
hide p2
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_02.ogg"
get_char('c13') '[convertstrid(1211182)]' (**arg(3, 1211182))
return "avg25306"