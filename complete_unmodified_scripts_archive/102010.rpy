label avg102010(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc012_01 3', 'p20', [l(-16), light, flip], 6)
$ update_narrator('c201')
window show
with trans
get_char('c201') '[convertstrid(1218656)]' (**arg(1, 1218656))
return "avg102010"