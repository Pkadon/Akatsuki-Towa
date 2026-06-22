label avg101201:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1220648)]' (**arg(1, 1220648))
hide p1
$ update_portrait('sc004_01 1', 'p12', [mid(-12), light], 6)
get_char('c123') '[convertstrid(1220649)]' (**arg(2, 1220649))
hide p12
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220650)]' (**arg(3, 1220650))
hide p1
$ update_portrait('sc004_01 2', 'p12', [mid(-12), light], 6)
get_char('c123') '[convertstrid(1220651)]' (**arg(4, 1220651))
hide p12
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220652)]' (**arg(5, 1220652))
return