label avg12536(trans=fade_in):

$ play_music("ED6301.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1151765)]' (**arg(1, 1151765))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151766)]' (**arg(2, 1151766))
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151767)]' (**arg(3, 1151767))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1151768)]' (**arg(4, 1151768))
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1151769)]' (**arg(5, 1151769))
return "avg12536"