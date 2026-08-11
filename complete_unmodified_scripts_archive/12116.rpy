label avg12116(trans=fade_in):

$ play_music("ed7111.ogg")
scene avg_bg_047
$ update_portrait('oc005_01 1', 'p5', [r(-6), light], 6)
$ update_narrator('c53')
window show
with trans
play sfxvoice "avg_vocal_ji02.ogg"
get_char('c53') '[convertstrid(1128203)]' (**arg(1, 1128203))
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
play sfx2 "other_7004.ogg"
get_char('c53') '[convertstrid(1128204)]' (**arg(2, 1128204))
$ update_portrait('oc005_01 4', 'p5', [r(-6), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128205)]' (**arg(3, 1128205))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128206)]' (**arg(4, 1128206))
hide p5
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1128207)]' (**arg(5, 1128207))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128208)]' (**arg(6, 1128208))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128209)]' (**arg(7, 1128209))
hide p3
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
play sfxvoice "bcv_oc002_c02_01.ogg"
get_char('c21') '[convertstrid(1128210)]' (**arg(8, 1128210))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_c04_01.ogg"
get_char('c13') '[convertstrid(1128211)]' (**arg(9, 1128211)) with shake
return "avg12116"