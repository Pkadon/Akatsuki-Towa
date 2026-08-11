label avg101123(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc003_01 1', 'p11', [l(-4), light, flip], 6)
$ update_narrator('c111')
window show
with trans
get_char('c111') '[convertstrid(1220453)]' (**arg(1, 1220453))
return "avg101123"