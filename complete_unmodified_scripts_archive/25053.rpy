label avg25053(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('uc001_02 2', 'p2006', [mid(6), light], 6)
$ update_narrator('c20063')
window show
with trans
get_char('c20063') '[convertstrid(1210146)]' (**arg(1, 1210146))
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 6)
get_char('c20063') '[convertstrid(1210147)]' (**arg(2, 1210147))
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 6)
get_char('c20063') '[convertstrid(1210148)]' (**arg(3, 1210148))
return "avg25053"