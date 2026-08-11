label avg101331(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc005_01 5', 'p13', [mid(-17), light], 6)
$ update_narrator('c133')
window show
with trans
get_char('c133') '[convertstrid(1221037)]' (**arg(1, 1221037))
return "avg101331"