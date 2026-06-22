label avg12674:

$ play_music("ED6105.ogg")
scene avg_bg_023
$ update_narrator('c13351')
window show
with fade_in
get_char('c13351') '[convertstrid(1166880)]' (**arg(1, 1166880))
get_char('c13351') '[convertstrid(1166881)]' (**arg(2, 1166881))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166882)]' (**arg(3, 1166882))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c13351') '[convertstrid(1166883)]' (**arg(4, 1166883))
get_char('c13351') '[convertstrid(1166884)]' (**arg(5, 1166884))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166885)]' (**arg(6, 1166885))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1166886)]' (**arg(7, 1166886))
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1166887)]' (**arg(8, 1166887))
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1166888)]' (**arg(9, 1166888))
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1166889)]' (**arg(10, 1166889))
$ update_portrait('oc003_01 7', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 2', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1166890)]' (**arg(11, 1166890))
hide p3
$ update_portrait('st061_01 2', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1166891)]' (**arg(12, 1166891))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1166892)]' (**arg(13, 1166892))
hide p1304
get_char('c13351') '[convertstrid(1166893)]' (**arg(14, 1166893))
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1166894)]' (**arg(15, 1166894))
return