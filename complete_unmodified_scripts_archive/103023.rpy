label avg103023(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc022_01 1', 'p30', [l(-9), light, flip], 6)
$ update_narrator('c301')
window show
with trans
get_char('c301') '[convertstrid(1222481)]' (**arg(1, 1222481))
return "avg103023"