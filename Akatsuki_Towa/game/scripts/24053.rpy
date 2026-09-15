label avg24053(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_050
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1200224)]' (**arg(1, 1200224))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
get_char('c7613') '[convertstrid(1200225)]' (**arg(2, 1200225))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200226)]' (**arg(3, 1200226))
return "avg24053"