label avg24028(trans=fade_in):

$ play_music("ed7300.ogg")
scene avg_bg_071
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
$ update_narrator('c43')
window show
with trans
get_char('c43') '[convertstrid(1200117)]' (**arg(1, 1200117))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1200118)]' (**arg(2, 1200118))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1200119)]' (**arg(3, 1200119))
return "avg24028"