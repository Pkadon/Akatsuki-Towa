label avg101929(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc011_01 6', 'p19', [mid(-1), light], 6)
$ update_narrator('c193')
window show
with trans
get_char('c193') '[convertstrid(1218403)]' (**arg(1, 1218403))
return "avg101929"