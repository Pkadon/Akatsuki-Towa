label avg12179(trans=fade_in):

$ play_music("ed7111.ogg")
scene avg_bg_003
$ update_narrator('c0')
window show
with trans
play sfx2 "other_7046.ogg"
get_char('c0') '[convertstrid(1120572)]' (**arg(1, 1120572))
$ update_portrait('oc005_01 5', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1120573)]' (**arg(2, 1120573))
$ update_portrait('oc005_01 5', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120574)]' (**arg(3, 1120574))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 5', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1120575)]' (**arg(4, 1120575))
hide p1
$ update_portrait('oc005_01 5', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120576)]' (**arg(5, 1120576))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc005_01 14', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1120577)]' (**arg(6, 1120577))
hide p2
$ update_portrait('oc005_01 14', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1120578)]' (**arg(7, 1120578))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1120580)]' (**arg(8, 1120580))
hide p3
$ update_portrait('oc005_01 1', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120581)]' (**arg(9, 1120581))
hide p1
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1120582)]' (**arg(10, 1120582))
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120583)]' (**arg(11, 1120583))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc005_01 21', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1120584)]' (**arg(12, 1120584))
$ update_portrait('oc005_01 21', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120585)]' (**arg(13, 1120585))
hide p5
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120586)]' (**arg(14, 1120586))
hide p2
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1120587)]' (**arg(15, 1120587))
return "avg12179"