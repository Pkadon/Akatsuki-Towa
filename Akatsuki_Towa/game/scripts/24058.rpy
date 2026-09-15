label avg24058(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_050
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1200240)]' (**arg(1, 1200240))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c7583') '[convertstrid(1200241)]' (**arg(2, 1200241))
hide p1
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1200242)]' (**arg(3, 1200242))
return "avg24058"