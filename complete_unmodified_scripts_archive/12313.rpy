label avg12313:

$ play_music("ed7305.ogg")
scene avg_bg_051
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
get_char('c41') '[convertstrid(1133256)]' (**arg(1, 1133256))
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133257)]' (**arg(2, 1133257))
hide p4
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133258)]' (**arg(3, 1133258))
hide p1
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133259)]' (**arg(4, 1133259))
hide p3
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133260)]' (**arg(5, 1133260))
hide p2
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('sc051_01 4', 'p58', [l_exit(-32), light, flip], 6)
get_char('c581') '[convertstrid(1133261)]' (**arg(6, 1133261))
hide p58
hide p4
$ update_portrait('oc002_01 12', 'p2', [r_midback(-3), light], 6)
get_char('c23') '[convertstrid(1133262)]' (**arg(7, 1133262))
return