label avg102022(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc012_01 1', 'p20', [l(-16), light, flip], 6)
$ update_narrator('c201')
window show
with trans
get_char('c201') '[convertstrid(1218691)]' (**arg(1, 1218691))
return "avg102022"