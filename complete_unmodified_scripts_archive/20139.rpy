label avg20139(trans=fade_in):

$ play_music("ed7150.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1003722)]' (**arg(1, 1003722))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1003723)]' (**arg(2, 1003723))
$ update_portrait('oc002_01 7', 'p2', [r(-3), dark], 5)
get_char('c5533') '[convertstrid(1003724)]' (**arg(3, 1003724))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfx2 "other_7020.ogg"
get_char('c23') '[convertstrid(1003725)]' (**arg(4, 1003725))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc042_01 1', 'p641', [l_entrance(-19), light, flip], 6)
get_char('c6411') '[convertstrid(1003726)]' (**arg(5, 1003726))
$ update_portrait('sc042_01 1', 'p641', [l(-19), light, flip], 6)
get_char('c6411') '[convertstrid(1003727)]' (**arg(6, 1003727))
$ update_portrait('sc042_01 1', 'p641', [l_exit(-19), light, flip], 6)
get_char('c6411') '[convertstrid(1003728)]' (**arg(7, 1003728))
hide p641
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch19.ogg"
get_char('c23') '[convertstrid(1003729)]' (**arg(8, 1003729))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l_entrance(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c11') '[convertstrid(1003730)]' (**arg(9, 1003730))
return "avg20139"