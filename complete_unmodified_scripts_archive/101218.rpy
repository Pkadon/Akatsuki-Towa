label avg101218(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1220698)]' (**arg(1, 1220698))
hide p1
$ update_portrait('sc004_01 4', 'p12', [mid(-12), light], 6)
get_char('c123') '[convertstrid(1220699)]' (**arg(2, 1220699))
hide p12
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220700)]' (**arg(3, 1220700))
hide p1
$ update_portrait('sc004_01 2', 'p12', [mid(-12), light], 6)
get_char('c123') '[convertstrid(1220701)]' (**arg(4, 1220701))
hide p12
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220702)]' (**arg(5, 1220702))
return "avg101218"