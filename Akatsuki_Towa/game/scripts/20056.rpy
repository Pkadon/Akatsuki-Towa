label avg20056:

$ play_music("ed7151.ogg")
scene avg_bg_027
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
window show
with fade_in
get_char('c33') '[convertstrid(1002968)]' (**arg(1, 1002968))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
play sfx2 "other_7071.ogg"
get_char('c4971') '[convertstrid(1002969)]' (**arg(2, 1002969))
hide p3
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1002970)]' (**arg(3, 1002970))
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
get_char('c4971') '[convertstrid(1002971)]' (**arg(4, 1002971))
get_char('c4971') '[convertstrid(1002972)]' (**arg(5, 1002972))
$ update_portrait('oc003_01 10', 'p3', [l(-6), l_shake, light, flip], 6)
play sfx2 "other_7073.ogg"
get_char('c31') '[convertstrid(1002973)]' (**arg(6, 1002973))
hide p2
$ update_portrait('oc003_01 10', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 20', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1002974)]' (**arg(7, 1002974))
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1002975)]' (**arg(8, 1002975))
return