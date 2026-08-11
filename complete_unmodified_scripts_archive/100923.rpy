label avg100923(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc001_01 5', 'p9', [l(-11), light, flip], 6)
$ update_narrator('c91')
window show
with trans
get_char('c91') '[convertstrid(1218084)]' (**arg(1, 1218084))
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218085)]' (**arg(2, 1218085))
return "avg100923"