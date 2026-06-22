label avg10366:

$ play_music("ed9999.ogg")
scene avg_bg_049
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1132030)]' (**arg(1, 1132030))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1132031)]' (**arg(2, 1132031))
hide p2
$ update_portrait('oc003_01 5', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132032)]' (**arg(3, 1132032))
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1132033)]' (**arg(4, 1132033))
hide p3
hide p4
play sfx2 "other_7047.ogg"
get_char('c0') '[convertstrid(1132034)]' (**arg(5, 1132034))
$ update_portrait('st040_01 1', 'p1042', [l_entrance(-19), light, flip], 6)
get_char('c10421') '[convertstrid(1132035)]' (**arg(6, 1132035))
$ update_portrait('st040_01 1', 'p1042', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132036)]' (**arg(7, 1132036))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('st040_01 1', 'p1042', [l(-19), light, flip], 6)
get_char('c10421') '[convertstrid(1132037)]' (**arg(8, 1132037))
$ update_portrait('st040_01 1', 'p1042', [l(-19), light, flip], 6)
get_char('c10421') '[convertstrid(1132038)]' (**arg(9, 1132038))
hide p1
$ update_portrait('st040_01 1', 'p1042', [l(-19), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro02.ogg"
get_char('c33') '[convertstrid(1132039)]' (**arg(10, 1132039))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('st040_01 1', 'p1042', [l(-19), light, flip], 6)
get_char('c10421') '[convertstrid(1132040)]' (**arg(11, 1132040))
hide p3
$ update_portrait('st040_01 1', 'p1042', [l(-19), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li03.ogg"
get_char('c43') '[convertstrid(1132041)]' (**arg(12, 1132041))
hide p1042
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('st040_01 6', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1132042)]' (**arg(13, 1132042))
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1132043)]' (**arg(14, 1132043))
hide p4
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1132044)]' (**arg(15, 1132044))
hide p2
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132045)]' (**arg(16, 1132045))
return