label avg20090(trans=fade_in):

$ play_music("ed7117.ogg")
scene avg_bg_021
$ update_narrator('c6781')
window show
with trans
get_char('c6781') '[convertstrid(1004506)]' (**arg(1, 1004506))
play sfx2 "other_7004.ogg"
get_char('c6793') '[convertstrid(1004507)]' (**arg(2, 1004507))
get_char('c6801') '[convertstrid(1004508)]' (**arg(3, 1004508))
get_char('c6793') '[convertstrid(1004509)]' (**arg(4, 1004509))
get_char('c6801') '[convertstrid(1004510)]' (**arg(5, 1004510))
get_char('c6783') '[convertstrid(1004511)]' (**arg(6, 1004511))
get_char('c6783') '[convertstrid(1004513)]' (**arg(7, 1004513))
get_char('c6801') '[convertstrid(1004514)]' (**arg(8, 1004514))
get_char('c6801') '[convertstrid(1004515)]' (**arg(9, 1004515))
$ update_portrait('oc001_01 2', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1004516)]' (**arg(10, 1004516))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c33') '[convertstrid(1004517)]' (**arg(11, 1004517))
hide p1
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c21') '[convertstrid(1004518)]' (**arg(12, 1004518))
hide p3
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1123027)]' (**arg(13, 1123027))
return "avg20090"