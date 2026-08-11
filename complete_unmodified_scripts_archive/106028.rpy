label avg106028(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc053_01 2', 'p60', [l(-32), light, flip], 6)
$ update_narrator('c601')
window show
with trans
get_char('c601') '[convertstrid(1219129)]' (**arg(1, 1219129))
$ update_portrait('sc053_01 6', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1219130)]' (**arg(2, 1219130))
return "avg106028"