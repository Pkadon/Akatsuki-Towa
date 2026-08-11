label avg102029(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc012_01 1', 'p20', [mid(-16), light], 6)
$ update_narrator('c203')
window show
with trans
get_char('c203') '[convertstrid(1218705)]' (**arg(1, 1218705))
return "avg102029"