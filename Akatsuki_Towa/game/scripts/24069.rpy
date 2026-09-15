label avg24069(trans=fade_in):

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
get_char('c21') '[convertstrid(1200273)]' (**arg(1, 1200273))
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
get_char('c7553') '[convertstrid(1200274)]' (**arg(2, 1200274))
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1200275)]' (**arg(3, 1200275))
return "avg24069"