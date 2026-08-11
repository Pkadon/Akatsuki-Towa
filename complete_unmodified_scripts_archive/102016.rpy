label avg102016(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc012_01 3', 'p20', [mid(-16), light], 6)
$ update_narrator('c203')
window show
with trans
get_char('c203') '[convertstrid(1218664)]' (**arg(1, 1218664))
return "avg102016"