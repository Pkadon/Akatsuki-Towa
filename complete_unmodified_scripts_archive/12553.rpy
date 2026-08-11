label avg12553(trans=fade_in):

$ play_music("ED6523.ogg")
scene avg_bg_081
$ update_narrator('c12411')
window show
with trans
get_char('c12411') '[convertstrid(1153036)]' (**arg(1, 1153036))
get_char('c12423') '[convertstrid(1153037)]' (**arg(2, 1153037))
get_char('c12431') '[convertstrid(1153038)]' (**arg(3, 1153038))
get_char('c12443') '[convertstrid(1153039)]' (**arg(4, 1153039))
get_char('c12451') '[convertstrid(1153040)]' (**arg(5, 1153040))
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1153041)]' (**arg(6, 1153041))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1153042)]' (**arg(7, 1153042))
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1153043)]' (**arg(8, 1153043))
hide p4
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1153044)]' (**arg(9, 1153044))
hide p3
hide p2
$ update_narrator('c12411')
with fade
get_char('c12411') '[convertstrid(1153045)]' (**arg(10, 1153045))
return "avg12553"