label avg19010(trans=fade_in):

stop music
scene avg_bg_023
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
$ update_narrator('c561')
window show
with trans
get_char('c561') '[convertstrid(1216070)]' (**arg(1, 1216070, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1216071)]' (**arg(2, 1216071, size=(0.9)))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216072)]' (**arg(3, 1216072, size=(0.9)))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216073)]' (**arg(4, 1216073, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216074)]' (**arg(5, 1216074, size=(0.9)))
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1216075)]' (**arg(6, 1216075, size=(0.9)))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216076)]' (**arg(7, 1216076, size=(0.9)))
hide p1
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1216077)]' (**arg(8, 1216077, size=(0.9)))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216078)]' (**arg(9, 1216078, size=(0.9)))
hide p2
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216079)]' (**arg(10, 1216079, size=(0.9)))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216080)]' (**arg(11, 1216080, size=(0.9)))
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216081)]' (**arg(12, 1216081, size=(0.9)))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216082)]' (**arg(13, 1216082, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216083)]' (**arg(14, 1216083, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216084)]' (**arg(15, 1216084, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216085)]' (**arg(16, 1216085, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216086)]' (**arg(17, 1216086, size=(0.9)))
menu:
    extend ""
    '[convertstrid(1216087)]':
        call avg19011
    '[convertstrid(1216088)]':
        call avg19022
return _return