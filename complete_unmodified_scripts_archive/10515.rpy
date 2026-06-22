label avg10515:

$ play_music("ED6200.ogg")
scene avg_bg_010
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with fade_in
get_char('c31') '[convertstrid(1150607)]' (**arg(1, 1150607))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150608)]' (**arg(2, 1150608))
hide p3
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1150609)]' (**arg(3, 1150609))
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150610)]' (**arg(4, 1150610))
return