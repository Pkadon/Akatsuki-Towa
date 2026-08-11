label avg101533(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc007_01 4', 'p15', [mid(-17), light], 6)
$ update_narrator('c153')
window show
with trans
get_char('c153') '[convertstrid(1221347)]' (**arg(1, 1221347))
return "avg101533"