label avg101816(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc010_01 2', 'p18', [mid(-10), light], 6)
$ update_narrator('c183')
window show
with trans
get_char('c183') '[convertstrid(1222191)]' (**arg(1, 1222191))
return "avg101816"