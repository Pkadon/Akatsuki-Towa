label avg14037(trans=fade_in):

$ play_music("ed7110.ogg")
scene avg_bg_015
$ update_narrator('c7521')
window show
with trans
get_char('c7521') '[convertstrid(1202723)]' (**arg(1, 1202723))
get_char('c7521') '[convertstrid(1202724)]' (**arg(2, 1202724))
get_char('c7521') '[convertstrid(1202725)]' (**arg(3, 1202725))
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202726)]' (**arg(4, 1202726))
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
get_char('c7521') '[convertstrid(1202727)]' (**arg(5, 1202727))
hide p2
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202728)]' (**arg(6, 1202728))
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202729)]' (**arg(7, 1202729))
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202730)]' (**arg(8, 1202730))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202731)]' (**arg(9, 1202731))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202732)]' (**arg(10, 1202732))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l_exit(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202733)]' (**arg(11, 1202733))
hide p2
$ update_portrait('oc001_01 18', 'p1', [r_exit(-2), light], 6)
get_char('c13') '[convertstrid(1202734)]' (**arg(12, 1202734))
hide p1
get_char('c7521') '[convertstrid(1202735)]' (**arg(13, 1202735))
get_char('c7521') '[convertstrid(1202736)]' (**arg(14, 1202736))
get_char('c7521') '[convertstrid(1202737)]' (**arg(15, 1202737))
return "avg14037"