label avg102117(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc013_01 4', 'p21', [mid(-12), light], 6)
$ update_narrator('c213')
window show
with trans
get_char('c213') '[convertstrid(1218846)]' (**arg(1, 1218846))
return "avg102117"