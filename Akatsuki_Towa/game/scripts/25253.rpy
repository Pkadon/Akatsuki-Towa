label avg25253(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "other_7076.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1210932)]' (**arg(1, 1210932))
hide p2
get_char('c20153') '[convertstrid(1210933)]' (**arg(2, 1210933))
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na19.ogg"
get_char('c13') '[convertstrid(1210934)]' (**arg(3, 1210934))
hide p1
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch20.ogg"
get_char('c23') '[convertstrid(1210935)]' (**arg(4, 1210935))
hide p2
play sfx2 "other_7007.ogg"
get_char('c20153') '[convertstrid(1210936)]' (**arg(5, 1210936))
play sfx2 "other_7086.ogg"
get_char('c0') '[convertstrid(1210937)]' (**arg(6, 1210937))
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210938)]' (**arg(7, 1210938))
return "avg25253"