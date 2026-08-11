label avg101129(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc003_01 1', 'p11', [mid(-4), light], 6)
$ update_narrator('c113')
window show
with trans
get_char('c113') '[convertstrid(1220466)]' (**arg(1, 1220466))
return "avg101129"