label avg12354(trans=fade_in):

$ play_music("ed7123.ogg")
scene avg_bg_046
$ update_narrator('c10951')
window show
with trans
play sfx2 "other_7048.ogg"
get_char('c10951') '[convertstrid(1133650)]' (**arg(1, 1133650))
get_char('c10951') '[convertstrid(1133651)]' (**arg(2, 1133651))
get_char('c10951') '[convertstrid(1133652)]' (**arg(3, 1133652))
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 6)
play sfx2 "other_7004.ogg"
get_char('c13') '[convertstrid(1133653)]' (**arg(4, 1133653))
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133654)]' (**arg(5, 1133654))
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
get_char('c10951') '[convertstrid(1133655)]' (**arg(6, 1133655))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133657)]' (**arg(7, 1133657))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133658)]' (**arg(8, 1133658))
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch10.ogg"
get_char('c21') '[convertstrid(1133656)]' (**arg(9, 1133656))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133659)]' (**arg(10, 1133659))
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133660)]' (**arg(11, 1133660))
hide p3
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133661)]' (**arg(12, 1133661))
return "avg12354"