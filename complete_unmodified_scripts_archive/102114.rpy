label avg102114(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc013_01 5', 'p21', [mid(-12), light], 6)
$ update_narrator('c213')
window show
with trans
get_char('c213') '[convertstrid(1218842)]' (**arg(1, 1218842))
return "avg102114"