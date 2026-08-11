label avg101532(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc007_01 3', 'p15', [mid(-17), light], 6)
$ update_narrator('c153')
window show
with trans
get_char('c153') '[convertstrid(1221346)]' (**arg(1, 1221346))
return "avg101532"