label avg101931(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc011_01 6', 'p19', [mid(-1), light], 6)
$ update_narrator('c193')
window show
with trans
get_char('c193') '[convertstrid(1218405)]' (**arg(1, 1218405))
return "avg101931"