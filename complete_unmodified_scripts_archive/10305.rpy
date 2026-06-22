label avg10305:

stop music
scene avg_bg_070
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7020.ogg"
get_char('c0') '[convertstrid(1130176)]' (**arg(1, 1130176))
$ play_music("ed7151.ogg")
scene avg_bg_032
$ update_narrator('c13')
with fade
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1130177)]' (**arg(2, 1130177))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st034_01 1', 'p233', [l(12), light, flip], 6)
get_char('c2331') '[convertstrid(1130178)]' (**arg(3, 1130178))
$ update_portrait('st034_01 4', 'p233', [l(12), light, flip], 6)
get_char('c2331') '[convertstrid(1130179)]' (**arg(4, 1130179))
$ update_portrait('st034_01 4', 'p233', [l(12), light, flip], 6)
get_char('c2331') '[convertstrid(1130180)]' (**arg(5, 1130180))
$ update_portrait('st034_01 4', 'p233', [l(12), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130181)]' (**arg(6, 1130181))
hide p1
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro12.ogg"
get_char('c33') '[convertstrid(1130182)]' (**arg(7, 1130182))
hide p3
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130183)]' (**arg(8, 1130183))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130184)]' (**arg(9, 1130184))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('st034_01 5', 'p233', [l(12), light, flip], 6)
get_char('c2331') '[convertstrid(1130185)]' (**arg(10, 1130185))
$ update_portrait('st034_01 1', 'p233', [l(12), light, flip], 6)
get_char('c2331') '[convertstrid(1130186)]' (**arg(11, 1130186))
$ update_portrait('st034_01 1', 'p233', [l(12), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li06.ogg"
get_char('c43') '[convertstrid(1130187)]' (**arg(12, 1130187))
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130188)]' (**arg(13, 1130188))
hide p233
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130189)]' (**arg(14, 1130189))
$ update_portrait('oc004_01 6', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130190)]' (**arg(15, 1130190))
hide p1
$ update_portrait('oc004_01 6', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1130191)]' (**arg(16, 1130191))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130192)]' (**arg(17, 1130192))
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130193)]' (**arg(18, 1130193))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130194)]' (**arg(19, 1130194))
hide p4
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st034_01 5', 'p233', [l_entrance(12), light, flip], 6)
get_char('c2331') '[convertstrid(1130195)]' (**arg(20, 1130195))
hide p1
$ update_portrait('st034_01 5', 'p233', [l(12), dark, flip], 5)
$ update_portrait('oc004_01 6', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130196)]' (**arg(21, 1130196))
hide p4
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130197)]' (**arg(22, 1130197))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('st034_01 1', 'p233', [l(12), light, flip], 6)
get_char('c2331') '[convertstrid(1130198)]' (**arg(23, 1130198))
return