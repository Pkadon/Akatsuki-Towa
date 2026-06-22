label avg1116:

$ play_music("ed7200.ogg")
scene avg_bg_010
$ update_portrait('oc004_01 13', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
get_char('c41') '[convertstrid(2102890)]' (**arg(1, 2102890))
$ update_portrait('oc004_01 13', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102891)]' (**arg(2, 2102891))
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102892)]' (**arg(3, 2102892))
hide p4
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('st004_01 6', 'p204', [l(4), light, flip], 6)
get_char('c2041') '[convertstrid(2102893)]' (**arg(4, 2102893))
hide p1
$ update_portrait('st004_01 6', 'p204', [l(4), dark, flip], 5)
get_char('c9773') '[convertstrid(2102894)]' (**arg(5, 2102894))
hide p204
$ update_portrait('oc004_01 21', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2102895)]' (**arg(6, 2102895))
return