label avg102115(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc013_01 2', 'p21', [mid(-12), light], 6)
$ update_narrator('c213')
window show
with trans
get_char('c213') '[convertstrid(1218844)]' (**arg(1, 1218844))
return "avg102115"