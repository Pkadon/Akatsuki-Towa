label avg24060(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_063
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1200248)]' (**arg(1, 1200248))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c7543') '[convertstrid(1200249)]' (**arg(2, 1200249))
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200250)]' (**arg(3, 1200250))
return "avg24060"