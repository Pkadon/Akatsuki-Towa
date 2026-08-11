label avg25265(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7050.ogg"
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1210989)]' (**arg(1, 1210989))
hide p1
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch31.ogg"
get_char('c23') '[convertstrid(1210990)]' (**arg(2, 1210990))
hide p2
play sfx2 "other_7037.ogg"
get_char('c20133') '[convertstrid(1210991)]' (**arg(3, 1210991))
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1210992)]' (**arg(4, 1210992))
hide p1
get_char('c20133') '[convertstrid(1210993)]' (**arg(5, 1210993))
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210994)]' (**arg(6, 1210994))
return "avg25265"