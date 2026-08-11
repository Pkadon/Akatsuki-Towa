label avg102023(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc012_01 5', 'p20', [l(-16), light, flip], 6)
$ update_narrator('c201')
window show
with trans
get_char('c201') '[convertstrid(1218692)]' (**arg(1, 1218692))
return "avg102023"