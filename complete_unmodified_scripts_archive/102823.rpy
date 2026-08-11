label avg102823(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
$ update_narrator('c281')
window show
with trans
get_char('c281') '[convertstrid(1219785)]' (**arg(1, 1219785))
return "avg102823"