label avg101231(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc004_01 6', 'p12', [mid(-12), light], 6)
$ update_narrator('c123')
window show
with trans
get_char('c123') '[convertstrid(1220742)]' (**arg(1, 1220742))
return "avg101231"