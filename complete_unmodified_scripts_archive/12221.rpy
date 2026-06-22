label avg12221:

$ play_music("ED6103.ogg")
scene avg_bg_072
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7047.ogg"
get_char('c0') '[convertstrid(1120960)]' (**arg(1, 1120960))
$ update_portrait('oc001_01 1', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120961)]' (**arg(2, 1120961))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c6873') '[convertstrid(1120962)]' (**arg(3, 1120962))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120963)]' (**arg(4, 1120963))
hide p2
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120964)]' (**arg(5, 1120964))
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
get_char('c6873') '[convertstrid(1120965)]' (**arg(6, 1120965))
get_char('c6873') '[convertstrid(1120966)]' (**arg(7, 1120966))
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1120967)]' (**arg(8, 1120967))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
get_char('c6873') '[convertstrid(1120968)]' (**arg(9, 1120968))
get_char('c6873') '[convertstrid(1121573)]' (**arg(10, 1121573))
return