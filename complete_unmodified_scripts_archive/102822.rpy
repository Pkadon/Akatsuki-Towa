label avg102822(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
$ update_narrator('c281')
window show
with trans
get_char('c281') '[convertstrid(1219784)]' (**arg(1, 1219784))
return "avg102822"