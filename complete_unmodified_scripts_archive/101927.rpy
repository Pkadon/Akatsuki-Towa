label avg101927(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc011_01 1', 'p19', [l(-1), light, flip], 6)
$ update_narrator('c191')
window show
with trans
get_char('c191') '[convertstrid(1218400)]' (**arg(1, 1218400))
return "avg101927"