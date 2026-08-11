label avg102033(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc012_01 1', 'p20', [mid(-16), light], 6)
$ update_narrator('c203')
window show
with trans
get_char('c203') '[convertstrid(1218710)]' (**arg(1, 1218710))
return "avg102033"