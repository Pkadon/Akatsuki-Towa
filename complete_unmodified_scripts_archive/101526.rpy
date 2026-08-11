label avg101526(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc007_01 5', 'p15', [l(-17), light, flip], 6)
$ update_narrator('c151')
window show
with trans
get_char('c151') '[convertstrid(1221338)]' (**arg(1, 1221338))
return "avg101526"