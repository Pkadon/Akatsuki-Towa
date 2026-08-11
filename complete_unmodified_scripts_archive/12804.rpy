label avg12804(trans=fade_in):

$ play_music("ed6564.ogg")
scene avg_bg_004
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1181332)]' (**arg(1, 1181332))
get_char('c0') '[convertstrid(1181333)]' (**arg(2, 1181333))
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1181334)]' (**arg(3, 1181334))
$ update_portrait('st061_01 4', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1181335)]' (**arg(4, 1181335))
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1181336)]' (**arg(5, 1181336))
hide p1304
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1181337)]' (**arg(6, 1181337))
hide p1
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1181338)]' (**arg(7, 1181338))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
get_char('c7011') '[convertstrid(1181339)]' (**arg(8, 1181339))
get_char('c7011') '[convertstrid(1181340)]' (**arg(9, 1181340))
get_char('c7011') '[convertstrid(1181341)]' (**arg(10, 1181341))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1181342)]' (**arg(11, 1181342))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c7011') '[convertstrid(1181343)]' (**arg(12, 1181343))
hide p1
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1181344)]' (**arg(13, 1181344))
hide p3
play sfx2 "other_7080.ogg"
get_char('c0') '[convertstrid(1181345)]' (**arg(14, 1181345))
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1181346)]' (**arg(15, 1181346))
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
play sfx2 "fight_6025.ogg"
get_char('c31') '[convertstrid(1181347)]' (**arg(16, 1181347))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1181348)]' (**arg(17, 1181348))
return "avg12804"