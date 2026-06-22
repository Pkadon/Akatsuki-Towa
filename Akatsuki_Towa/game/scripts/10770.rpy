label avg10770:

$ play_music("ed7304.ogg")
scene avg_bg_209
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1175389)]' (**arg(1, 1175389))
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1175390)]' (**arg(2, 1175390))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l_entrance(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1175391)]' (**arg(3, 1175391))
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1175392)]' (**arg(4, 1175392))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 2', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1175393)]' (**arg(5, 1175393))
hide p1304
hide p1
get_char('c0') '[convertstrid(1175394)]' (**arg(6, 1175394))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1175395)]' (**arg(7, 1175395))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1175396)]' (**arg(8, 1175396))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1175397)]' (**arg(9, 1175397))
$ update_portrait('st061_01 5', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1175398)]' (**arg(10, 1175398))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1175399)]' (**arg(11, 1175399))
hide p1304
hide p1
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1175400)]' (**arg(12, 1175400))
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1175401)]' (**arg(13, 1175401))
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1175402)]' (**arg(14, 1175402))
return