label avg10364(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_050
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
get_char('c21') '[convertstrid(1131987)]' (**arg(1, 1131987))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131988)]' (**arg(2, 1131988))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1131989)]' (**arg(3, 1131989))
hide p4
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1131990)]' (**arg(4, 1131990))
return "avg10364"