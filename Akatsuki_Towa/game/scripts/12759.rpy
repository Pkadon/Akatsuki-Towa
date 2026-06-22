label avg12759:

$ play_music("ed6564.ogg")
scene avg_bg_004
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with fade_in
get_char('c31') '[convertstrid(1174464)]' (**arg(1, 1174464))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174465)]' (**arg(2, 1174465))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1174466)]' (**arg(3, 1174466))
hide p3
hide p1
get_char('c0') '[convertstrid(1174467)]' (**arg(4, 1174467))
return