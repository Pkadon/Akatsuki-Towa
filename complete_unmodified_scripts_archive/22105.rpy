label avg22105(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('st051_01 5', 'p709', [mid(-9), light], 6)
$ update_narrator('c7093')
window show
with trans
get_char('c7093') '[convertstrid(1128025)]' (**arg(1, 1128025))
$ update_portrait('st051_01 6', 'p709', [mid(-9), light], 6)
get_char('c7093') '[convertstrid(1128026)]' (**arg(2, 1128026))
return "avg22105"