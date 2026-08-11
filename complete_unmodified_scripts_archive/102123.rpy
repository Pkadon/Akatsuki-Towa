label avg102123(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc013_01 3', 'p21', [l(-12), light, flip], 6)
$ update_narrator('c211')
window show
with trans
get_char('c211') '[convertstrid(1218876)]' (**arg(1, 1218876))
return "avg102123"