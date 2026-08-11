label avg10723(trans=fade_in):

$ play_music("ed7515.ogg")
scene avg_bg_023
show memoryoverlay zorder 2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1171509)]' (**arg(1, 1171509))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1171510)]' (**arg(2, 1171510))
$ update_portrait('oc004_01 14', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1171511)]' (**arg(3, 1171511))
$ update_portrait('oc004_01 14', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171512)]' (**arg(4, 1171512))
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1171513)]' (**arg(5, 1171513))
get_char('c0') '[convertstrid(1171514)]' (**arg(6, 1171514))
get_char('c0') '[convertstrid(1171515)]' (**arg(7, 1171515))
get_char('c0') '[convertstrid(1171516)]' (**arg(8, 1171516))
get_char('c0') '[convertstrid(1171517)]' (**arg(9, 1171517))
$ play_music("ed7111.ogg")
scene avg_bg_061
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
$ update_narrator('c51')
with fade
get_char('c51') '[convertstrid(1171518)]' (**arg(10, 1171518))
$ update_portrait('oc005_01 1', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1171519)]' (**arg(11, 1171519))
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1171520)]' (**arg(12, 1171520))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc005_01 10', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1171521)]' (**arg(13, 1171521))
$ update_portrait('oc005_01 10', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1171522)]' (**arg(14, 1171522))
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('oc005_01 15', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1171523)]' (**arg(15, 1171523))
$ update_portrait('oc005_01 4', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1171524)]' (**arg(16, 1171524))
$ update_portrait('oc005_01 4', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1171525)]' (**arg(17, 1171525))
$ play_music("ed7564.ogg")
hide p5
hide p2
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1171526)]' (**arg(18, 1171526))
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1171527)]' (**arg(19, 1171527))
get_char('c0') '[convertstrid(1171528)]' (**arg(20, 1171528))
get_char('c0') '[convertstrid(1171529)]' (**arg(21, 1171529))
get_char('c0') '[convertstrid(1171530)]' (**arg(22, 1171530))
scene avg_bg_061
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
with fade
get_char('c23') '[convertstrid(1171531)]' (**arg(23, 1171531))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc005_01 17', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1171532)]' (**arg(24, 1171532))
$ update_portrait('oc005_01 19', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1171533)]' (**arg(25, 1171533))
$ update_portrait('oc005_01 4', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1171534)]' (**arg(26, 1171534))
$ update_portrait('oc005_01 4', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 16', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1171535)]' (**arg(27, 1171535))
$ update_portrait('oc002_01 16', 'p2', [r(-3), dark], 5)
$ update_portrait('oc005_01 17', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1171536)]' (**arg(28, 1171536))
$ update_portrait('oc005_01 19', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1171537)]' (**arg(29, 1171537))
$ update_portrait('oc005_01 19', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1171538)]' (**arg(30, 1171538))
return "avg10723"