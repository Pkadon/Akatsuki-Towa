label avg24095(trans=fade_in):

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
get_char('c21') '[convertstrid(1200337)]' (**arg(1, 1200337))
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
get_char('c50133') '[convertstrid(1200338)]' (**arg(2, 1200338))
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1200339)]' (**arg(3, 1200339))
return "avg24095"