label avg10427(trans=fade_in):

$ play_music("ed7511.ogg")
scene placeholderbackground
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1141272)]' (**arg(1, 1141272))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1141273)]' (**arg(2, 1141273))
$ update_portrait('oc001_01 3', 'p1', [r(-2), l_shake, light], 6)
play sfxvoice "avg_vocal_na07.ogg"
get_char('c13') '[convertstrid(1141274)]' (**arg(3, 1141274))
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
get_char('c11091') '[convertstrid(1141275)]' (**arg(4, 1141275))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_02.ogg"
get_char('c13') '[convertstrid(1141276)]' (**arg(5, 1141276))
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1141277)]' (**arg(6, 1141277))
hide p2
$ update_portrait('oc004_01 12', 'p4', [l_entrance(-5), light, flip], 6)
play sfxvoice "avg_vocal_li11.ogg"
get_char('c41') '[convertstrid(1141278)]' (**arg(7, 1141278))
$ update_portrait('oc004_01 12', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1141279)]' (**arg(8, 1141279))
hide p4
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c31') '[convertstrid(1141280)]' (**arg(9, 1141280))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1141281)]' (**arg(10, 1141281))
hide p3
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
play sfx2 "other_7007.ogg"
get_char('c11091') '[convertstrid(1141282)]' (**arg(11, 1141282)) with shake
return "avg10427"