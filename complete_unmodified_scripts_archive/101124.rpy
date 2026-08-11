label avg101124(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc003_01 5', 'p11', [l(-4), light, flip], 6)
$ update_narrator('c111')
window show
with trans
get_char('c111') '[convertstrid(1220454)]' (**arg(1, 1220454))
return "avg101124"