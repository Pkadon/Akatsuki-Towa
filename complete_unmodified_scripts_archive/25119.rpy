label avg25119:

stop music
scene placeholderbackground
$ update_narrator('c6123')
window show
with fade_in
play sfx2 "fight_6030.ogg"
get_char('c6123') '[convertstrid(1210349)]' (**arg(1, 1210349))
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_arts_03.ogg"
get_char('c23') '[convertstrid(1210350)]' (**arg(2, 1210350))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210351)]' (**arg(3, 1210351))
return