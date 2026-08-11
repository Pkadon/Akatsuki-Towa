label avg101832(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc010_01 2', 'p18', [mid(-10), light], 6)
$ update_narrator('c183')
window show
with trans
get_char('c183') '[convertstrid(1222240)]' (**arg(1, 1222240))
return "avg101832"