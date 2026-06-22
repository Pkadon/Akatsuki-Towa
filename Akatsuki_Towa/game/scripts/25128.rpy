label avg25128:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1210382)]' (**arg(1, 1210382))
hide p1
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1210383)]' (**arg(2, 1210383))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1210384)]' (**arg(3, 1210384))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210385)]' (**arg(4, 1210385))
return