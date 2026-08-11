label avg22384(trans=fade_in):

$ play_music("ed7201.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7021.ogg"
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1133903)]' (**arg(1, 1133903))
hide p1
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch18.ogg"
get_char('c23') '[convertstrid(1133904)]' (**arg(2, 1133904))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1133905)]' (**arg(3, 1133905))
hide p1
$ update_portrait('oc002_01 18', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1133906)]' (**arg(4, 1133906))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1133907)]' (**arg(5, 1133907))
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1133908)]' (**arg(6, 1133908))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1133909)]' (**arg(7, 1133909))
return "avg22384"