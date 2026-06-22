label avg20056:

$ play_music("ed7151.ogg")
scene placeholderbackground
$ update_portrait('oc003_01 4', 'p3', [mid(-6), light], 6)
$ update_narrator('c33')
window show
with fade_in
get_char('c33') '[convertstrid(1002968)]' (**arg(1, 1002968))
hide p3
play sfx2 "other_7071.ogg"
get_char('c4973') '[convertstrid(1002969)]' (**arg(2, 1002969))
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1002970)]' (**arg(3, 1002970))
hide p2
get_char('c4973') '[convertstrid(1002971)]' (**arg(4, 1002971))
get_char('c4973') '[convertstrid(1002972)]' (**arg(5, 1002972))
$ update_portrait('oc003_01 10', 'p3', [mid(-6), light], 6)
play sfx2 "other_7073.ogg"
get_char('c33') '[convertstrid(1002973)]' (**arg(6, 1002973))
hide p3
$ update_portrait('oc004_01 20', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1002974)]' (**arg(7, 1002974))
$ update_portrait('oc004_01 3', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1002975)]' (**arg(8, 1002975))
return