label avg29117:

stop music
scene placeholderbackground
$ update_portrait('sc001_01 5', 'p9', [mid(-11), light], 6)
$ update_narrator('c93')
window show
with fade_in
get_char('c93') '[convertstrid(1218052)]' (**arg(1, 1218052))
$ update_portrait('sc001_01 6', 'p9', [mid(-11), light], 6)
get_char('c93') '[convertstrid(1218053)]' (**arg(2, 1218053))
hide p9
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc002_c05_01.ogg"
get_char('c13') '[convertstrid(1218054)]' (**arg(3, 1218054))
hide p1
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 6)
get_char('c93') '[convertstrid(1218055)]' (**arg(4, 1218055))
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 6)
get_char('c93') '[convertstrid(1218056)]' (**arg(5, 1218056))
hide p9
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
get_char('c13') '[convertstrid(1218057)]' (**arg(6, 1218057))
return