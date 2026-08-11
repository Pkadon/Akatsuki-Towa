label avg101329(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc005_01 6', 'p13', [mid(-17), light], 6)
$ update_narrator('c133')
window show
with trans
get_char('c133') '[convertstrid(1221035)]' (**arg(1, 1221035))
return "avg101329"