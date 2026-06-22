label avg25322:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1211243)]' (**arg(1, 1211243))
hide p1
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1211244)]' (**arg(2, 1211244))
hide p2
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_na18.ogg"
get_char('c13') '[convertstrid(1211245)]' (**arg(3, 1211245))
return