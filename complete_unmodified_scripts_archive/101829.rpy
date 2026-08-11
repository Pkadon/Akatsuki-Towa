label avg101829(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc010_01 1', 'p18', [mid(-10), light], 6)
$ update_narrator('c183')
window show
with trans
get_char('c183') '[convertstrid(1222236)]' (**arg(1, 1222236))
return "avg101829"