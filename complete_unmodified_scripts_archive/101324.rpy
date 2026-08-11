label avg101324(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
$ update_narrator('c131')
window show
with trans
get_char('c131') '[convertstrid(1221022)]' (**arg(1, 1221022))
return "avg101324"