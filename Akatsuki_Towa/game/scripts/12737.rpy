label avg12737:

$ play_music("ED6200.ogg")
scene avg_bg_010
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1172848)]' (**arg(1, 1172848))
play sfx2 "other_7014.ogg"
get_char('c0') '[convertstrid(1172849)]' (**arg(2, 1172849))
$ update_portrait('st061_01 2', 'p1304', [l_entrance(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1172850)]' (**arg(3, 1172850))
$ update_portrait('st061_01 2', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1172851)]' (**arg(4, 1172851))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172852)]' (**arg(5, 1172852))
hide p1304
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c14401') '[convertstrid(1172853)]' (**arg(6, 1172853))
get_char('c14401') '[convertstrid(1172854)]' (**arg(7, 1172854))
hide p1
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1172855)]' (**arg(8, 1172855))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
get_char('c14401') '[convertstrid(1172856)]' (**arg(9, 1172856))
hide p3
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1172857)]' (**arg(10, 1172857))
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
get_char('c14401') '[convertstrid(1172858)]' (**arg(11, 1172858))
hide p1304
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
play sfx2 "fight_6025.ogg"
get_char('c33') '[convertstrid(1172859)]' (**arg(12, 1172859))
return