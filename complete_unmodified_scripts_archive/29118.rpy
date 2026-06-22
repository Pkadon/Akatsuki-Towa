label avg29118:

stop music
scene placeholderbackground
$ update_portrait('sc001_01 4', 'p9', [mid(-11), light], 6)
$ update_narrator('c93')
window show
with fade_in
get_char('c93') '[convertstrid(1218059)]' (**arg(1, 1218059))
hide p9
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc002_get_02.ogg"
get_char('c13') '[convertstrid(1218060)]' (**arg(2, 1218060))
hide p1
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 6)
get_char('c93') '[convertstrid(1218061)]' (**arg(3, 1218061))
hide p9
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
get_char('c13') '[convertstrid(1218062)]' (**arg(4, 1218062))
hide p1
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 6)
get_char('c93') '[convertstrid(1218063)]' (**arg(5, 1218063))
hide p9
get_char('c0') '[convertstrid(1218064)]' (**arg(6, 1218064))
return