label avg101522(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc007_01 2', 'p15', [l(-17), light, flip], 6)
$ update_narrator('c151')
window show
with trans
get_char('c151') '[convertstrid(1221327)]' (**arg(1, 1221327))
return "avg101522"