label avg101930(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc011_01 6', 'p19', [mid(-1), light], 6)
$ update_narrator('c193')
window show
with trans
get_char('c193') '[convertstrid(1218404)]' (**arg(1, 1218404))
return "avg101930"