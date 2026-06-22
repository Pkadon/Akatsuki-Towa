label avg25237:

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7080.ogg"
get_char('c0') '[convertstrid(1210843)]' (**arg(1, 1210843))
get_char('c6123') '[convertstrid(1210844)]' (**arg(2, 1210844))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1210845)]' (**arg(3, 1210845))
hide p2
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na24.ogg"
get_char('c13') '[convertstrid(1210846)]' (**arg(4, 1210846))
return