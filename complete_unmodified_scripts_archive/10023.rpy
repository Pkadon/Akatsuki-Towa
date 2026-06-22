label avg10023:

$ play_music("ED6518.ogg")
scene avg_bg_008
$ update_narrator('c21')
window show
with fade_in
$ update_portrait('oc002_01 14', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c21') '[convertstrid(1002042)]' (**arg(1, 1002042))
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002043)]' (**arg(2, 1002043))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002044)]' (**arg(3, 1002044))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfx2 "other_7064.ogg"
get_char('c13') '[convertstrid(1002045)]' (**arg(4, 1002045))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l_exit(-6), light, flip], 6)
get_char('c31') '[convertstrid(1002046)]' (**arg(5, 1002046))
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002047)]' (**arg(6, 1002047))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1002048)]' (**arg(7, 1002048))
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002049)]' (**arg(8, 1002049))
hide p2
$ update_portrait('oc003_01 7', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(1002050)]' (**arg(9, 1002050))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1002051)]' (**arg(10, 1002051))
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1002052)]' (**arg(11, 1002052))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002053)]' (**arg(12, 1002053))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002054)]' (**arg(13, 1002054))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002055)]' (**arg(14, 1002055))
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1002056)]' (**arg(15, 1002056))
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1002057)]' (**arg(16, 1002057))
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1002058)]' (**arg(17, 1002058))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002059)]' (**arg(18, 1002059))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7071.ogg"
get_char('c31') '[convertstrid(1002060)]' (**arg(19, 1002060))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1002061)]' (**arg(20, 1002061))
hide p1
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
get_char('c7013') '[convertstrid(1002062)]' (**arg(21, 1002062, size=(1.2))) with shake
$ update_portrait('oc003_01 12', 'p3', [l(-6), l_shake, light, flip], 6)
get_char('c31') '[convertstrid(1002063)]' (**arg(22, 1002063))
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 5)
get_char('c7013') '[convertstrid(1002064)]' (**arg(23, 1002064))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1002065)]' (**arg(24, 1002065))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1002066)]' (**arg(25, 1002066))
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
get_char('c7013') '[convertstrid(1002067)]' (**arg(26, 1002067))
get_char('c7013') '[convertstrid(1002068)]' (**arg(27, 1002068))
play sfx2 "other_7073.ogg"
get_char('c7013') '[convertstrid(1002069)]' (**arg(28, 1002069))
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1002070)]' (**arg(29, 1002070))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002071)]' (**arg(30, 1002071))
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002072)]' (**arg(31, 1002072))
return