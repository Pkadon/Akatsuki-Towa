label avg102116(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc013_01 2', 'p21', [mid(-12), light], 6)
$ update_narrator('c213')
window show
with trans
get_char('c213') '[convertstrid(1218845)]' (**arg(1, 1218845))
return "avg102116"