label avg101226(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc004_01 4', 'p12', [l(-12), light, flip], 6)
$ update_narrator('c121')
window show
with trans
get_char('c121') '[convertstrid(1220736)]' (**arg(1, 1220736))
return "avg101226"