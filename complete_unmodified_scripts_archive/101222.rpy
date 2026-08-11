label avg101222(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc004_01 4', 'p12', [l(-12), light, flip], 6)
$ update_narrator('c121')
window show
with trans
get_char('c121') '[convertstrid(1220726)]' (**arg(1, 1220726))
return "avg101222"