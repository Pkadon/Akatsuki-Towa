label avg101512(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc007_01 1', 'p15', [mid(-17), light], 6)
$ update_narrator('c153')
window show
with trans
get_char('c153') '[convertstrid(1221292)]' (**arg(1, 1221292))
return "avg101512"