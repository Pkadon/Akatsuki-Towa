label avg25065:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_ch20.ogg"
get_char('c23') '[convertstrid(1210195)]' (**arg(1, 1210195))
hide p2
play sfx2 "fight_6016.ogg"
play sfxvoice "avg_vocal_ch27.ogg"
get_char('c0') '[convertstrid(1210196)]' (**arg(2, 1210196))
$ update_portrait('oc002_01 20', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch21.ogg"
get_char('c23') '[convertstrid(1210198)]' (**arg(3, 1210198))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210199)]' (**arg(4, 1210199))
hide p1
$ update_portrait('oc002_01 19', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210200)]' (**arg(5, 1210200))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210201)]' (**arg(6, 1210201))
return