label avg101132(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc003_01 4', 'p11', [mid(-4), light], 6)
$ update_narrator('c113')
window show
with trans
get_char('c113') '[convertstrid(1220470)]' (**arg(1, 1220470))
return "avg101132"