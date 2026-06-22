label avg12668:

$ play_music("ed7150.ogg")
scene avg_bg_015
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1166661)]' (**arg(1, 1166661))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166662)]' (**arg(2, 1166662))
hide p2
get_char('c13661') '[convertstrid(1166663)]' (**arg(3, 1166663))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166664)]' (**arg(4, 1166664))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc051_01 4', 'p58', [l_entrance(-32), light, flip], 6)
get_char('c581') '[convertstrid(1166665)]' (**arg(5, 1166665))
hide p1
$ update_portrait('sc051_01 4', 'p58', [l(-32), dark, flip], 5)
$ update_portrait('sc053_01 4', 'p60', [r_entrance(-32), light], 6)
get_char('c603') '[convertstrid(1166666)]' (**arg(6, 1166666))
hide p58
hide p60
play sfx2 "other_7085.ogg"
get_char('c0') '[convertstrid(1166667)]' (**arg(7, 1166667))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166668)]' (**arg(8, 1166668))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1166669)]' (**arg(9, 1166669))
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1166670)]' (**arg(10, 1166670))
return