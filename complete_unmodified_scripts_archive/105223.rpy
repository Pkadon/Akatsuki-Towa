label avg105223(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc052_01 5', 'p59', [l(-25), light, flip], 6)
$ update_narrator('c591')
window show
with trans
get_char('c591') '[convertstrid(1219316)]' (**arg(1, 1219316))
return "avg105223"