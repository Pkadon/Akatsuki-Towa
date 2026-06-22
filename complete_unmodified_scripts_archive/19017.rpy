label avg19017:

stop music
scene avg_bg_023
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1216150)]' (**arg(1, 1216150, size=(0.9)))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216151)]' (**arg(2, 1216151, size=(0.9)))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216152)]' (**arg(3, 1216152, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216153)]' (**arg(4, 1216153, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216154)]' (**arg(5, 1216154, size=(0.9)))
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216155)]' (**arg(6, 1216155, size=(0.9)))
$ update_portrait('sc049_01 2', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216156)]' (**arg(7, 1216156, size=(0.9)))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216157)]' (**arg(8, 1216157, size=(0.9)))
hide p1
$ update_portrait('sc049_01 10', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1216165)]' (**arg(9, 1216165, size=(0.9)))
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1216166)]' (**arg(10, 1216166, size=(0.9)))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216167)]' (**arg(11, 1216167, size=(0.9)))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216168)]' (**arg(12, 1216168, size=(0.9)))
hide p1
$ update_portrait('sc049_01 10', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1216169)]' (**arg(13, 1216169, size=(0.9)))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216170)]' (**arg(14, 1216170, size=(0.9)))
hide p1
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1216171)]' (**arg(15, 1216171, size=(0.9)))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216172)]' (**arg(16, 1216172, size=(0.9)))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216158)]' (**arg(17, 1216158, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216159)]' (**arg(18, 1216159, size=(0.9)))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216160)]' (**arg(19, 1216160, size=(0.9)))
hide p56
hide p1
get_char('c0') '[convertstrid(1216161)]' (**arg(20, 1216161, size=(0.9)))
menu:
    extend ""
    '[convertstrid(1216162)]':
        call avg19017
    '[convertstrid(1216163)]':
        call avg19018
    '[convertstrid(1216164)]':
        call avg19019
return