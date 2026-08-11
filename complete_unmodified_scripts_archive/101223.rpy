label avg101223(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc004_01 3', 'p12', [l(-12), light, flip], 6)
$ update_narrator('c121')
window show
with trans
get_char('c121') '[convertstrid(1220727)]' (**arg(1, 1220727))
return "avg101223"