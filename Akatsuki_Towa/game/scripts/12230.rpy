label avg12230(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_023
$ update_narrator('c6891')
window show
with trans
get_char('c6891') '[convertstrid(1121103)]' (**arg(1, 1121103))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1121104)]' (**arg(2, 1121104))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c6891') '[convertstrid(1121105)]' (**arg(3, 1121105))
$ update_portrait('sc030_01 4', 'p38', [l(-12), light, flip], 6)
get_char('c381') '[convertstrid(1121106)]' (**arg(4, 1121106))
hide p38
$ update_portrait('sc031_01 2', 'p39', [l(-14), light, flip], 6)
get_char('c391') '[convertstrid(1121107)]' (**arg(5, 1121107))
hide p39
$ update_portrait('sc032_01 5', 'p40', [l(-17), light, flip], 6)
get_char('c401') '[convertstrid(1121108)]' (**arg(6, 1121108))
hide p1
$ update_portrait('sc032_01 5', 'p40', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121109)]' (**arg(7, 1121109))
hide p40
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c6891') '[convertstrid(1121110)]' (**arg(8, 1121110))
hide p2
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121111)]' (**arg(9, 1121111))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('sc030_01 2', 'p38', [l(-12), light, flip], 6)
get_char('c381') '[convertstrid(1121112)]' (**arg(10, 1121112))
menu:
    extend ""
    '[convertstrid(1121113)]':
        call avg12231
    '[convertstrid(1121114)]':
        call avg12232
return _return