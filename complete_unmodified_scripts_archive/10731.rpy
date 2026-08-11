label avg10731(trans=fade_in):

$ play_music("ED6105.ogg")
scene avg_bg_070
$ update_narrator('c0')
window show
with trans
play sfx2 "other_7060.ogg"
get_char('c0') '[convertstrid(1172484)]' (**arg(1, 1172484))
get_char('c0') '[convertstrid(1172485)]' (**arg(2, 1172485))
scene avg_bg_203
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
get_char('c31') '[convertstrid(1172486)]' (**arg(3, 1172486))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172487)]' (**arg(4, 1172487))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172488)]' (**arg(5, 1172488))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172489)]' (**arg(6, 1172489))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172490)]' (**arg(7, 1172490))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172491)]' (**arg(8, 1172491))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172492)]' (**arg(9, 1172492))
hide p3
hide p1
get_char('c0') '[convertstrid(1172493)]' (**arg(10, 1172493))
$ update_portrait('st063_01 1', 'p1346', [l_entrance(-16), light, flip], 6)
get_char('c13461') '[convertstrid(1172494)]' (**arg(11, 1172494))
$ update_portrait('st063_01 1', 'p1346', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172495)]' (**arg(12, 1172495))
return "avg10731"