label avg12108(trans=fade_in):

$ play_music("ed7101.ogg")
scene avg_bg_073
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
play sfx2 "other_7020.ogg"
get_char('c11') '[convertstrid(1128038)]' (**arg(1, 1128038))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
get_char('c9513') '[convertstrid(1128039)]' (**arg(2, 1128039))
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128040)]' (**arg(3, 1128040))
hide p1
get_char('c0') '[convertstrid(1128041)]' (**arg(4, 1128041))
play sfx2 "other_7004.ogg"
get_char('c9513') '[convertstrid(1128042)]' (**arg(5, 1128042))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128043)]' (**arg(6, 1128043))
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
get_char('c9513') '[convertstrid(1128044)]' (**arg(7, 1128044))
hide p3
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c11') '[convertstrid(1128045)]' (**arg(8, 1128045))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1128046)]' (**arg(9, 1128046))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
get_char('c9513') '[convertstrid(1128047)]' (**arg(10, 1128047))
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1128048)]' (**arg(11, 1128048))
hide p2
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
play sfxvoice "bcv_oc001_c04_01.ogg"
get_char('c11') '[convertstrid(1128049)]' (**arg(12, 1128049, size=(1.2))) with shake
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 5)
get_char('c9513') '[convertstrid(1128050)]' (**arg(13, 1128050))
get_char('c9513') '[convertstrid(1128051)]' (**arg(14, 1128051))
get_char('c9513') '[convertstrid(1128052)]' (**arg(15, 1128052))
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1128053)]' (**arg(16, 1128053))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
get_char('c9513') '[convertstrid(1128054)]' (**arg(17, 1128054))
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c11') '[convertstrid(1128055)]' (**arg(18, 1128055))
return "avg12108"