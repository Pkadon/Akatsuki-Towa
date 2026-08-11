label avg101127(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc003_01 6', 'p11', [l(-4), light, flip], 6)
$ update_narrator('c111')
window show
with trans
get_char('c111') '[convertstrid(1220463)]' (**arg(1, 1220463))
return "avg101127"