label avg103011(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc022_01 5', 'p30', [l(-9), light, flip], 6)
$ update_narrator('c301')
window show
with trans
get_char('c301') '[convertstrid(1222441)]' (**arg(1, 1222441))
return "avg103011"