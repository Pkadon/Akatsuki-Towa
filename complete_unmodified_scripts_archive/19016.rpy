label avg19016:

stop music
scene avg_bg_023
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1216147)]' (**arg(1, 1216147, size=(0.9)))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216148)]' (**arg(2, 1216148, size=(0.9)))
hide p2
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216149)]' (**arg(3, 1216149, size=(0.9)))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216158)]' (**arg(4, 1216158, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216159)]' (**arg(5, 1216159, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216160)]' (**arg(6, 1216160, size=(0.9)))
hide p56
hide p1
get_char('c0') '[convertstrid(1216161)]' (**arg(7, 1216161, size=(0.9)))
menu:
    extend ""
    '[convertstrid(1216162)]':
        call avg19017
    '[convertstrid(1216163)]':
        call avg19018
    '[convertstrid(1216164)]':
        call avg19019
return