label avg101220(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1220712)]' (**arg(1, 1220712))
hide p1
$ update_portrait('sc004_01 1', 'p12', [mid(-12), light], 6)
get_char('c123') '[convertstrid(1220713)]' (**arg(2, 1220713))
$ update_portrait('sc004_01 5', 'p12', [mid(-12), light], 6)
get_char('c123') '[convertstrid(1220714)]' (**arg(3, 1220714))
hide p12
$ update_portrait('oc001_01 16', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220715)]' (**arg(4, 1220715))
hide p1
$ update_portrait('sc004_01 4', 'p12', [mid(-12), light], 6)
get_char('c123') '[convertstrid(1220716)]' (**arg(5, 1220716))
hide p12
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220717)]' (**arg(6, 1220717))
return "avg101220"