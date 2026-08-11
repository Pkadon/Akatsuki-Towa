label avg101117(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc003_01 4', 'p11', [mid(-4), light], 6)
$ update_narrator('c113')
window show
with trans
get_char('c113') '[convertstrid(1220425)]' (**arg(1, 1220425))
return "avg101117"