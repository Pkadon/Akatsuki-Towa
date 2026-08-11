label avg127110(trans=fade_in):

$ play_music("ed7151.ogg")
scene avg_bg_038
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1179182)]' (**arg(1, 1179182))
get_char('c0') '[convertstrid(1179183)]' (**arg(2, 1179183))
get_char('c0') '[convertstrid(1179184)]' (**arg(3, 1179184))
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1179185)]' (**arg(4, 1179185))
$ update_portrait('oc005_01 4', 'p5', [r(-6), dark], 5)
$ update_portrait('st061_01 2', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1179186)]' (**arg(5, 1179186))
hide p1304
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1179187)]' (**arg(6, 1179187))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1179188)]' (**arg(7, 1179188))
$ update_portrait('oc003_01 18', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1179189)]' (**arg(8, 1179189))
$ update_portrait('oc003_01 18', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1179190)]' (**arg(9, 1179190))
$ update_portrait('oc005_01 4', 'p5', [r(-6), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1179191)]' (**arg(10, 1179191))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1179192)]' (**arg(11, 1179192))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1179193)]' (**arg(12, 1179193))
return "avg127110"