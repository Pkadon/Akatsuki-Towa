label avg25063(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfxvoice "avg_vocal_ch19.ogg"
get_char('c23') '[convertstrid(1210184)]' (**arg(1, 1210184))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210185)]' (**arg(2, 1210185))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_ch16.ogg"
get_char('c23') '[convertstrid(1210186)]' (**arg(3, 1210186))
hide p2
play sfx2 "fight_6003.ogg"
play sfxvoice "avg_vocal_ch27.ogg"
get_char('c0') '[convertstrid(1210187)]' (**arg(4, 1210187))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch23.ogg"
get_char('c23') '[convertstrid(1210188)]' (**arg(5, 1210188))
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1210189)]' (**arg(6, 1210189))
return "avg25063"