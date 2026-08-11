label avg12027(trans=fade_in):

$ play_music("ed7106.ogg")
scene avg_bg_016
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
play sfx2 "other_7056.ogg"
get_char('c21') '[convertstrid(1120078)]' (**arg(1, 1120078))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc011_01 1', 'p19', [r(-1), light], 6)
get_char('c193') '[convertstrid(1120079)]' (**arg(2, 1120079))
hide p2
$ update_portrait('sc011_01 1', 'p19', [r(-1), dark], 5)
$ update_portrait('sc012_01 1', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1120080)]' (**arg(3, 1120080))
$ update_portrait('sc012_01 1', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1120081)]' (**arg(4, 1120081))
$ update_portrait('sc012_01 1', 'p20', [l(-16), dark, flip], 5)
$ update_portrait('sc011_01 1', 'p19', [r(-1), light], 6)
get_char('c193') '[convertstrid(1120082)]' (**arg(5, 1120082))
hide p20
$ update_portrait('sc011_01 1', 'p19', [r(-1), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120083)]' (**arg(6, 1120083))
hide p19
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc012_01 1', 'p20', [r(-16), light], 6)
get_char('c203') '[convertstrid(1120084)]' (**arg(7, 1120084))
$ update_portrait('sc012_01 1', 'p20', [r(-16), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120085)]' (**arg(8, 1120085))
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc012_01 1', 'p20', [r(-16), light], 6)
get_char('c203') '[convertstrid(1120086)]' (**arg(9, 1120086))
hide p20
$ update_portrait('sc011_01 1', 'p19', [r(-1), light], 6)
get_char('c193') '[convertstrid(1120087)]' (**arg(10, 1120087))
hide p1
$ update_portrait('sc011_01 1', 'p19', [r(-1), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120088)]' (**arg(11, 1120088))
return "avg12027"