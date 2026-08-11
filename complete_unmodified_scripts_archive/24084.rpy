label avg24084(trans=fade_in):

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_narrator('c7423')
window show
with trans
get_char('c7423') '[convertstrid(1200312)]' (**arg(1, 1200312))
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200313)]' (**arg(2, 1200313))
return "avg24084"