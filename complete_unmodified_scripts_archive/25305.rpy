label avg25305(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with trans
play sfx2 "other_7080.ogg"
get_char('c0') '[convertstrid(1211175)]' (**arg(1, 1211175))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_hurt_02.ogg"
get_char('c23') '[convertstrid(1211176)]' (**arg(2, 1211176))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1211177)]' (**arg(3, 1211177))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_arts_03.ogg"
get_char('c23') '[convertstrid(1211178)]' (**arg(4, 1211178))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1211179)]' (**arg(5, 1211179))
return "avg25305"