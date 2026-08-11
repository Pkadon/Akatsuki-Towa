label avg102031(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc012_01 5', 'p20', [mid(-16), light], 6)
$ update_narrator('c203')
window show
with trans
get_char('c203') '[convertstrid(1218707)]' (**arg(1, 1218707))
return "avg102031"