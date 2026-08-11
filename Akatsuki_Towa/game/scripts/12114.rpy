label avg12114(trans=fade_in):

$ play_music("ed7117.ogg")
scene avg_bg_017
$ update_narrator('c9573')
window show
with trans
play sfx2 "other_7048.ogg"
get_char('c9573') '[convertstrid(1128181)]' (**arg(1, 1128181))
play sfx2 "other_7091.ogg"
get_char('c9573') '[convertstrid(1128182)]' (**arg(2, 1128182))
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c11') '[convertstrid(1128183)]' (**arg(3, 1128183))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1128184)]' (**arg(4, 1128184))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
get_char('c9573') '[convertstrid(1128185)]' (**arg(5, 1128185))
hide p2
$ update_portrait('oc003_01 14', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128186)]' (**arg(6, 1128186))
hide p3
get_char('c0') '[convertstrid(1128187)]' (**arg(7, 1128187))
$ update_portrait('oc001_01 11', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128188)]' (**arg(8, 1128188))
$ update_portrait('oc001_01 11', 'p1', [l(-2), dark, flip], 5)
get_char('c9573') '[convertstrid(1128189)]' (**arg(9, 1128189))
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128190)]' (**arg(10, 1128190))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
get_char('c9573') '[convertstrid(1128191)]' (**arg(11, 1128191))
hide p1
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
play sfx2 "other_7004.ogg"
get_char('c21') '[convertstrid(1128192)]' (**arg(12, 1128192))
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c21') '[convertstrid(1128193)]' (**arg(13, 1128193, size=(1.2))) with shake
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
get_char('c9573') '[convertstrid(1128194)]' (**arg(14, 1128194))
hide p2
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro08.ogg"
get_char('c31') '[convertstrid(1128195)]' (**arg(15, 1128195))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
get_char('c9573') '[convertstrid(1128196)]' (**arg(16, 1128196))
get_char('c9573') '[convertstrid(1128197)]' (**arg(17, 1128197))
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128198)]' (**arg(18, 1128198))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128199)]' (**arg(19, 1128199))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 14', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128200)]' (**arg(20, 1128200))
hide p2
$ update_portrait('oc003_01 14', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128201)]' (**arg(21, 1128201))
return "avg12114"