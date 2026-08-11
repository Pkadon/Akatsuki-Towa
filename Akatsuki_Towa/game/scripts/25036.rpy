label avg25036(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "other_7080.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
get_char('c23') '[convertstrid(1210093)]' (**arg(1, 1210093))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210094)]' (**arg(2, 1210094))
return "avg25036"