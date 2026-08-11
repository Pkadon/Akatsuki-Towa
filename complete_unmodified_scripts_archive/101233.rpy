label avg101233(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc004_01 1', 'p12', [mid(-12), light], 6)
$ update_narrator('c123')
window show
with trans
get_char('c123') '[convertstrid(1220745)]' (**arg(1, 1220745))
return "avg101233"