label avg24508(trans=fade_in):

$ play_music("ED6201.ogg")
scene avg_bg_004
$ update_narrator('c23')
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
window show
with trans
$ update_portrait('oc002_01 10', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1206017)]' (**arg(1, 1206017))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1206018)]' (**arg(2, 1206018))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1206019)]' (**arg(3, 1206019))
return "avg24508"