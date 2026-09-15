label avg24059(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_050
$ update_narrator('c7583')
window show
with trans
get_char('c7583') '[convertstrid(1200243)]' (**arg(1, 1200243))
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200244)]' (**arg(2, 1200244))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
get_char('c7583') '[convertstrid(1200245)]' (**arg(3, 1200245))
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1200246)]' (**arg(4, 1200246))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
get_char('c7583') '[convertstrid(1200247)]' (**arg(5, 1200247))
return "avg24059"