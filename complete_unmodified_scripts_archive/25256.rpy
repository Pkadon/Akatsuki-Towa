label avg25256:

stop music
scene placeholderbackground
$ update_narrator('c20093')
window show
with fade_in
get_char('c20093') '[convertstrid(1210949)]' (**arg(1, 1210949))
play sfx2 "other_7077.ogg"
get_char('c20163') '[convertstrid(1210950)]' (**arg(2, 1210950))
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na23.ogg"
get_char('c13') '[convertstrid(1210951)]' (**arg(3, 1210951))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc002_com_01.ogg"
get_char('c23') '[convertstrid(1210952)]' (**arg(4, 1210952))
return