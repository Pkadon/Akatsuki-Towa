label avg19012:

stop music
scene avg_bg_023
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1216111)]' (**arg(1, 1216111, size=(0.9)))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216112)]' (**arg(2, 1216112, size=(0.9)))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216113)]' (**arg(3, 1216113, size=(0.9)))
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216134)]' (**arg(4, 1216134, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216135)]' (**arg(5, 1216135, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216136)]' (**arg(6, 1216136, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216137)]' (**arg(7, 1216137, size=(0.9)))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216138)]' (**arg(8, 1216138, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216139)]' (**arg(9, 1216139, size=(0.9)))
hide p56
hide p1
get_char('c0') '[convertstrid(1216140)]' (**arg(10, 1216140, size=(0.9)))
menu:
    extend ""
    '[convertstrid(1216141)]':
        call avg19015
    '[convertstrid(1216142)]':
        call avg19016
    '[convertstrid(1216143)]':
        call avg19017
return