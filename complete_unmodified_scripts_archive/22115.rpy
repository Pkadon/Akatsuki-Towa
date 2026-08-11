label avg22115(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1128202)]' (**arg(1, 1128202))
return "avg22115"