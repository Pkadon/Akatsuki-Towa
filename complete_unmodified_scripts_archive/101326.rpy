label avg101326(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc005_01 4', 'p13', [l(-17), light, flip], 6)
$ update_narrator('c131')
window show
with trans
get_char('c131') '[convertstrid(1221031)]' (**arg(1, 1221031))
return "avg101326"