label avg101619:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1221574)]' (**arg(1, 1221574))
hide p1
$ update_portrait('sc008_01 1', 'p16', [mid(-18), light], 6)
get_char('c163') '[convertstrid(1221575)]' (**arg(2, 1221575))
hide p16
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221576)]' (**arg(3, 1221576))
hide p1
$ update_portrait('sc008_01 2', 'p16', [mid(-18), light], 6)
get_char('c163') '[convertstrid(1221577)]' (**arg(4, 1221577))
hide p16
$ update_portrait('oc001_01 16', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221578)]' (**arg(5, 1221578))
return