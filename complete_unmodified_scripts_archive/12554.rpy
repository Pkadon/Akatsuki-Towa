label avg12554:

$ play_music("ED6523.ogg")
scene avg_bg_081
$ update_narrator('c12411')
window show
with fade_in
get_char('c12411') '[convertstrid(1153047)]' (**arg(1, 1153047))
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1153048)]' (**arg(2, 1153048))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1153049)]' (**arg(3, 1153049))
hide p3
get_char('c12411') '[convertstrid(1153050)]' (**arg(4, 1153050))
hide p1
get_char('c12463') '[convertstrid(1153051)]' (**arg(5, 1153051))
get_char('c12471') '[convertstrid(1153052)]' (**arg(6, 1153052))
get_char('c12483') '[convertstrid(1153053)]' (**arg(7, 1153053))
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro04.ogg"
get_char('c33') '[convertstrid(1153054)]' (**arg(8, 1153054))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
get_char('c12491') '[convertstrid(1153055)]' (**arg(9, 1153055))
hide p3
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch24.ogg"
get_char('c23') '[convertstrid(1153056)]' (**arg(10, 1153056))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1153057)]' (**arg(11, 1153057))
return