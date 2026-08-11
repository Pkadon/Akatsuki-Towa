label avg106024(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
$ update_narrator('c601')
window show
with trans
get_char('c601') '[convertstrid(1219118)]' (**arg(1, 1219118))
return "avg106024"