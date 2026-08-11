label avg100106(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc001_01 2', 'p9', [l(-11), light, flip], 6)
$ update_narrator('c91')
window show
with trans
get_char('c91') '[convertstrid(1218029)]' (**arg(1, 1218029))
$ update_portrait('sc001_01 5', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218030)]' (**arg(2, 1218030))
return "avg100106"