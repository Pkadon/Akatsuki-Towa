label avg101113(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc003_01 6', 'p11', [mid(-4), light], 6)
$ update_narrator('c113')
window show
with trans
get_char('c113') '[convertstrid(1220420)]' (**arg(1, 1220420))
return "avg101113"