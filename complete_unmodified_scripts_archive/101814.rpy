label avg101814(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc010_01 5', 'p18', [mid(-10), light], 6)
$ update_narrator('c183')
window show
with trans
get_char('c183') '[convertstrid(1222188)]' (**arg(1, 1222188))
return "avg101814"