label avg12036:

$ play_music("ed7150.ogg")
scene avg_bg_023
$ update_portrait('sc049_01 2', 'p56', [r(-8), light], 6)
$ update_narrator('c563')
window show
with fade_in
get_char('c563') '[convertstrid(1120233)]' (**arg(1, 1120233))
$ update_portrait('sc049_01 7', 'p56', [r(-8), light], 6)
get_char('c563') '[convertstrid(1120234)]' (**arg(2, 1120234))
$ update_portrait('sc049_01 7', 'p56', [r(-8), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120235)]' (**arg(3, 1120235))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc049_01 1', 'p56', [r(-8), light], 6)
get_char('c563') '[convertstrid(1120236)]' (**arg(4, 1120236))
hide p2
$ update_portrait('sc049_01 1', 'p56', [r(-8), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120237)]' (**arg(5, 1120237))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc049_01 1', 'p56', [r(-8), light], 6)
get_char('c563') '[convertstrid(1120238)]' (**arg(6, 1120238))
$ update_portrait('sc049_01 1', 'p56', [r(-8), light], 6)
get_char('c563') '[convertstrid(1120239)]' (**arg(7, 1120239))
$ update_portrait('sc049_01 1', 'p56', [r(-8), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121551)]' (**arg(8, 1121551))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc049_01 5', 'p56', [r(-8), light], 6)
get_char('c563') '[convertstrid(1120240)]' (**arg(9, 1120240))
hide p1
$ update_portrait('sc049_01 5', 'p56', [r(-8), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1120241)]' (**arg(10, 1120241))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc049_01 4', 'p56', [r(-8), light], 6)
get_char('c563') '[convertstrid(1121552)]' (**arg(11, 1121552))
$ update_portrait('sc049_01 4', 'p56', [r(-8), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121553)]' (**arg(12, 1121553))
return