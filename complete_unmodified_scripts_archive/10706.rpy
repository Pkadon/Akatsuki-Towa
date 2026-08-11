label avg10706(trans=fade_in):

$ play_music("ed7202.ogg")
scene avg_bg_010
$ update_narrator('c13041')
window show
with trans
$ update_portrait('st061_01 5', 'p1304', [l_entrance(-2), light, flip], 6)
play sfx2 "other_7060.ogg"
get_char('c13041') '[convertstrid(1170158)]' (**arg(1, 1170158))
$ update_portrait('st061_01 5', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1170159)]' (**arg(2, 1170159))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1170160)]' (**arg(3, 1170160))
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1170161)]' (**arg(4, 1170161))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1170162)]' (**arg(5, 1170162))
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1170163)]' (**arg(6, 1170163))
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1170164)]' (**arg(7, 1170164))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1170165)]' (**arg(8, 1170165))
hide p1304
hide p1
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1170166)]' (**arg(9, 1170166))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1170167)]' (**arg(10, 1170167))
hide p1
get_char('c0') '[convertstrid(1170168)]' (**arg(11, 1170168))
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1170169)]' (**arg(12, 1170169))
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1170170)]' (**arg(13, 1170170))
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1170171)]' (**arg(14, 1170171))
hide p1304
hide p1
get_char('c0') '[convertstrid(1170172)]' (**arg(15, 1170172))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1170173)]' (**arg(16, 1170173))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1170174)]' (**arg(17, 1170174))
$ update_portrait('oc001_01 15', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1170175)]' (**arg(18, 1170175))
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1170176)]' (**arg(19, 1170176))
return "avg10706"