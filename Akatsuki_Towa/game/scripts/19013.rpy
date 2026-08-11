label avg19013(trans=fade_in):

stop music
scene avg_bg_023
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1216114)]' (**arg(1, 1216114, size=(0.9)))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216115)]' (**arg(2, 1216115, size=(0.9)))
hide p2
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216116)]' (**arg(3, 1216116, size=(0.9)))
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1216117)]' (**arg(4, 1216117, size=(0.9)))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216118)]' (**arg(5, 1216118, size=(0.9)))
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216134)]' (**arg(6, 1216134, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216135)]' (**arg(7, 1216135, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216136)]' (**arg(8, 1216136, size=(0.9)))
hide p2
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216137)]' (**arg(9, 1216137, size=(0.9)))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216138)]' (**arg(10, 1216138, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216139)]' (**arg(11, 1216139, size=(0.9)))
hide p56
hide p1
get_char('c0') '[convertstrid(1216140)]' (**arg(12, 1216140, size=(0.9)))
menu:
    extend ""
    '[convertstrid(1216141)]':
        call avg19015
    '[convertstrid(1216142)]':
        call avg19016
    '[convertstrid(1216143)]':
        call avg19017
return _return