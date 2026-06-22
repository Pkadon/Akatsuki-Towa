label avg25229:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1210813)]' (**arg(1, 1210813))
hide p1
play sfx2 "other_7082.ogg"
get_char('c20173') '[convertstrid(1210814)]' (**arg(2, 1210814))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfx2 "elc_5004.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1210815)]' (**arg(3, 1210815))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210816)]' (**arg(4, 1210816))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210817)]' (**arg(5, 1210817))
return