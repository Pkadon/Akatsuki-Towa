label avg19014(trans=fade_in):

stop music
scene avg_bg_023
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1216119)]' (**arg(1, 1216119, size=(0.9)))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 8', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216120)]' (**arg(2, 1216120, size=(0.9)))
hide p2
$ update_portrait('sc049_01 8', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216121)]' (**arg(3, 1216121, size=(0.9)))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1216122)]' (**arg(4, 1216122, size=(0.9)))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216123)]' (**arg(5, 1216123, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216124)]' (**arg(6, 1216124, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216125)]' (**arg(7, 1216125, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1216126)]' (**arg(8, 1216126, size=(0.9)))
hide p2
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216127)]' (**arg(9, 1216127, size=(0.9)))
hide p1
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1216128)]' (**arg(10, 1216128, size=(0.9)))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216129)]' (**arg(11, 1216129, size=(0.9)))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216130)]' (**arg(12, 1216130, size=(0.9)))
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216131)]' (**arg(13, 1216131, size=(0.9)))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216132)]' (**arg(14, 1216132, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216133)]' (**arg(15, 1216133, size=(0.9)))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216134)]' (**arg(16, 1216134, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216135)]' (**arg(17, 1216135, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216136)]' (**arg(18, 1216136, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216137)]' (**arg(19, 1216137, size=(0.9)))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216138)]' (**arg(20, 1216138, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216139)]' (**arg(21, 1216139, size=(0.9)))
hide p56
hide p1
get_char('c0') '[convertstrid(1216140)]' (**arg(22, 1216140, size=(0.9)))
menu:
    extend ""
    '[convertstrid(1216141)]':
        call avg19015
    '[convertstrid(1216142)]':
        call avg19016
    '[convertstrid(1216143)]':
        call avg19017
return _return