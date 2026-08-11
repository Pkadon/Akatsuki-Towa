label avg105928(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc052_01 6', 'p59', [l(-25), light, flip], 6)
$ update_narrator('c591')
window show
with trans
get_char('c591') '[convertstrid(1219328)]' (**arg(1, 1219328))
$ update_portrait('sc052_01 6', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc001_01 24', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1219329)]' (**arg(2, 1219329))
return "avg105928"