label avg12723:

$ play_music("ED6301.ogg")
scene avg_bg_070
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
$ update_narrator('c13041')
window show
with fade_in
get_char('c13041') '[convertstrid(1171755)]' (**arg(1, 1171755))
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171756)]' (**arg(2, 1171756))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1171757)]' (**arg(3, 1171757))
$ update_portrait('st061_01 5', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171758)]' (**arg(4, 1171758))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1171759)]' (**arg(5, 1171759))
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1171760)]' (**arg(6, 1171760))
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171761)]' (**arg(7, 1171761))
return