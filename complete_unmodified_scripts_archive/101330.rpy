label avg101330(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc005_01 4', 'p13', [mid(-17), light], 6)
$ update_narrator('c133')
window show
with trans
get_char('c133') '[convertstrid(1221036)]' (**arg(1, 1221036))
return "avg101330"