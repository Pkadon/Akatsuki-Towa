label avg20016(trans=fade_in):

$ play_music("ED6518.ogg")
scene avg_bg_008
$ update_narrator('c21')
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
window show
with trans
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
play sfx2 "common_cancel.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c21') '[convertstrid(1000950)]' (**arg(1, 1000950))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1000951)]' (**arg(2, 1000951))
return "avg20016"