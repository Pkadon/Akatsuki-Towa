label avg24054:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1200227)]' (**arg(1, 1200227))
hide p2
get_char('c7613') '[convertstrid(1200228)]' (**arg(2, 1200228))
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200229)]' (**arg(3, 1200229))
return