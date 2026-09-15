label avg24097(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_050
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1200341)]' (**arg(1, 1200341))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c50123') '[convertstrid(1200342)]' (**arg(2, 1200342))
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200343)]' (**arg(3, 1200343))
return "avg24097"