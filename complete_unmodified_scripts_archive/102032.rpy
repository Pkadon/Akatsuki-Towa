label avg102032(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc012_01 2', 'p20', [mid(-16), light], 6)
$ update_narrator('c203')
window show
with trans
get_char('c203') '[convertstrid(1218709)]' (**arg(1, 1218709))
return "avg102032"