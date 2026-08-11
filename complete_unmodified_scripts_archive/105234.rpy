label avg105234(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc052_01 5', 'p59', [mid(-25), light], 6)
$ update_narrator('c593')
window show
with trans
get_char('c593') '[convertstrid(1219337)]' (**arg(1, 1219337))
return "avg105234"