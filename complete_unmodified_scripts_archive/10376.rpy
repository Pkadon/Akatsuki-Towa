label avg10376(trans=fade_in):

$ play_music("ed7151.ogg")
scene avg_bg_023
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1132156)]' (**arg(1, 1132156))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132157)]' (**arg(2, 1132157))
$ update_portrait('sc048_01 1', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132158)]' (**arg(3, 1132158))
hide p55
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132159)]' (**arg(4, 1132159))
return "avg10376"