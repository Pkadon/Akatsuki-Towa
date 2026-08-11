label avg10736(trans=fade_in):

$ play_music("ed7511.ogg")
scene avg_bg_038
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with trans
get_char('c31') '[convertstrid(1172583)]' (**arg(1, 1172583))
$ update_portrait('oc003_01 9', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172584)]' (**arg(2, 1172584))
hide p3
hide p1
get_char('c0') '[convertstrid(1172585)]' (**arg(3, 1172585))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172586)]' (**arg(4, 1172586))
hide p1
get_char('c0') '[convertstrid(1172587)]' (**arg(5, 1172587))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172588)]' (**arg(6, 1172588))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 21', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172589)]' (**arg(7, 1172589))
hide p3
hide p1
get_char('c0') '[convertstrid(1172590)]' (**arg(8, 1172590))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172591)]' (**arg(9, 1172591))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172592)]' (**arg(10, 1172592))
$ update_portrait('oc003_01 9', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172593)]' (**arg(11, 1172593))
hide p3
hide p1
play sfx2 "other_7085.ogg"
get_char('c0') '[convertstrid(1172594)]' (**arg(12, 1172594))
return "avg10736"