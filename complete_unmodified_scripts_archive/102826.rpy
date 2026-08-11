label avg102826(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc020_01 4', 'p28', [l(-10), light, flip], 6)
$ update_narrator('c281')
window show
with trans
get_char('c281') '[convertstrid(1219794)]' (**arg(1, 1219794))
return "avg102826"