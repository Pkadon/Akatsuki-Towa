label avg101217(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc004_01 1', 'p12', [mid(-12), light], 6)
$ update_narrator('c123')
window show
with trans
get_char('c123') '[convertstrid(1220696)]' (**arg(1, 1220696))
return "avg101217"