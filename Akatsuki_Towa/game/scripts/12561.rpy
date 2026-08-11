label avg12561(trans=fade_in):

$ play_music("ED6200.ogg")
scene avg_bg_080
$ update_portrait('oc004_01 6', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with trans
get_char('c41') '[convertstrid(1153132)]' (**arg(1, 1153132))
$ update_portrait('oc004_01 6', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1153133)]' (**arg(2, 1153133))
hide p4
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1153134)]' (**arg(3, 1153134))
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1153135)]' (**arg(4, 1153135))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1153136)]' (**arg(5, 1153136))
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1153137)]' (**arg(6, 1153137))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1153138)]' (**arg(7, 1153138))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c21') '[convertstrid(1153139)]' (**arg(8, 1153139))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1153140)]' (**arg(9, 1153140))
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1153141)]' (**arg(10, 1153141))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1153142)]' (**arg(11, 1153142))
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1153143)]' (**arg(12, 1153143))
hide p4
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1153144)]' (**arg(13, 1153144))
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1153145)]' (**arg(14, 1153145))
return "avg12561"