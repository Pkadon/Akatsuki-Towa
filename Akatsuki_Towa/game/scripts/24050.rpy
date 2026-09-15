label avg24050(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_049
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1200215)]' (**arg(1, 1200215))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c7603') '[convertstrid(1200216)]' (**arg(2, 1200216))
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200217)]' (**arg(3, 1200217))
return "avg24050"