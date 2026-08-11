label avg12151(trans=fade_in):

$ play_music("ED6505.ogg")
scene avg_bg_027
$ update_portrait('uc004_02 1', 'p960', [l(-9), light, flip], 6)
$ update_narrator('c9601')
window show
with trans
play sfx2 "other_7060.ogg"
get_char('c9601') '[convertstrid(1128367)]' (**arg(1, 1128367))
$ update_portrait('uc004_02 1', 'p960', [l(-9), dark, flip], 5)
$ update_portrait('uc004_02 2', 'p961', [r(-9), light], 6)
get_char('c9613') '[convertstrid(1128368)]' (**arg(2, 1128368))
hide p961
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1128369)]' (**arg(3, 1128369))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128370)]' (**arg(4, 1128370))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('uc004_02 1', 'p960', [l(-9), light, flip], 6)
get_char('c9601') '[convertstrid(1128371)]' (**arg(5, 1128371))
$ play_music("ED6107.ogg")
scene avg_bg_070
$ update_narrator('c0')
with fade
play sfx2 "other_7021.ogg"
get_char('c0') '[convertstrid(1128373)]' (**arg(6, 1128373))
scene avg_bg_038
$ update_narrator('c9621')
with fade
get_char('c9621') '[convertstrid(1128374)]' (**arg(7, 1128374))
get_char('c9621') '[convertstrid(1128375)]' (**arg(8, 1128375))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128376)]' (**arg(9, 1128376))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c9621') '[convertstrid(1128377)]' (**arg(10, 1128377))
get_char('c9621') '[convertstrid(1128378)]' (**arg(11, 1128378))
menu:
    extend ""
    '[convertstrid(1100001)]':
        call avg12154
    '[convertstrid(1100002)]':
        call avg12153
return _return