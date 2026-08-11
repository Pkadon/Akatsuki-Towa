label avg105905(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc052_01 2', 'p59', [l(-25), light, flip], 6)
$ update_narrator('c591')
window show
with trans
get_char('c591') '[convertstrid(1219264)]' (**arg(1, 1219264))
return "avg105905"