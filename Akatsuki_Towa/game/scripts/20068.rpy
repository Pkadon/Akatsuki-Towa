label avg20068(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_043
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
play sfx2 "other_7043.ogg"
get_char('c11') '[convertstrid(1003875)]' (**arg(1, 1003875))
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1003876)]' (**arg(2, 1003876))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1003877)]' (**arg(3, 1003877))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1001582)]' (**arg(4, 1001582))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c11') '[convertstrid(1003879)]' (**arg(5, 1003879))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1003880)]' (**arg(6, 1003880))
return "avg20068"