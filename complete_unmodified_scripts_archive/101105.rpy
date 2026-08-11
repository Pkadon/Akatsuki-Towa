label avg101105(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc003_01 2', 'p11', [l(-4), light, flip], 6)
$ update_narrator('c111')
window show
with trans
get_char('c111') '[convertstrid(1220405)]' (**arg(1, 1220405))
return "avg101105"