label avg106027(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc053_01 2', 'p60', [l(-32), light, flip], 6)
$ update_narrator('c601')
window show
with trans
get_char('c601') '[convertstrid(1219128)]' (**arg(1, 1219128))
return "avg106027"