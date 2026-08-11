label avg10140(trans=fade_in):

$ play_music("ED6505.ogg")
scene avg_bg_027
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1007442)]' (**arg(1, 1007442))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('uc004_02 4', 'p961', [l(-9), light, flip], 6)
get_char('c9611') '[convertstrid(1007443)]' (**arg(2, 1007443))
hide p961
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007444)]' (**arg(3, 1007444))
hide p2
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1007445)]' (**arg(4, 1007445))
hide p1
$ update_portrait('oc003_01 16', 'p3', [r(-6), dark], 5)
$ update_portrait('uc004_02 4', 'p961', [l(-9), light, flip], 6)
get_char('c9611') '[convertstrid(1007446)]' (**arg(5, 1007446))
hide p3
$ update_portrait('uc004_02 4', 'p961', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007447)]' (**arg(6, 1007447))
return "avg10140"