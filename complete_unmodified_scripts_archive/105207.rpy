label avg105207(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc052_01 6', 'p59', [l(-25), light, flip], 6)
$ update_narrator('c591')
window show
with trans
get_char('c591') '[convertstrid(1219266)]' (**arg(1, 1219266))
return "avg105207"