label avg103027(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc022_01 2', 'p30', [l(-9), light, flip], 6)
$ update_narrator('c301')
window show
with trans
get_char('c301') '[convertstrid(1222491)]' (**arg(1, 1222491))
return "avg103027"