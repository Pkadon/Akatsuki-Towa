label avg24067(trans=fade_in):

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
get_char('c21') '[convertstrid(1200267)]' (**arg(1, 1200267))
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
get_char('c7553') '[convertstrid(1200268)]' (**arg(2, 1200268))
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1200269)]' (**arg(3, 1200269))
return "avg24067"