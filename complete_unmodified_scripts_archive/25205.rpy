label avg25205:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1210700)]' (**arg(1, 1210700))
hide p2
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
play sfx2 "other_7088.ogg"
get_char('c13') '[convertstrid(1210701)]' (**arg(2, 1210701))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_arts_03.ogg"
get_char('c23') '[convertstrid(1210702)]' (**arg(3, 1210702))
return