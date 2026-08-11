label avg24015(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c7423')
window show
with trans
get_char('c7423') '[convertstrid(1200064)]' (**arg(1, 1200064))
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200065)]' (**arg(2, 1200065))
return "avg24015"