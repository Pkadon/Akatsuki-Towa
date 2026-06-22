label avg101203:

stop music
scene placeholderbackground
$ update_portrait('sc004_01 1', 'p12', [mid(-12), light], 6)
$ update_narrator('c123')
window show
with fade_in
get_char('c123') '[convertstrid(1220662)]' (**arg(1, 1220662))
hide p12
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220663)]' (**arg(2, 1220663))
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220664)]' (**arg(3, 1220664))
hide p1
$ update_portrait('sc004_01 2', 'p12', [mid(-12), light], 6)
get_char('c123') '[convertstrid(1220665)]' (**arg(4, 1220665))
hide p12
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220666)]' (**arg(5, 1220666))
hide p1
$ update_portrait('sc004_01 4', 'p12', [mid(-12), light], 6)
get_char('c123') '[convertstrid(1220667)]' (**arg(6, 1220667))
hide p12
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220668)]' (**arg(7, 1220668))
return