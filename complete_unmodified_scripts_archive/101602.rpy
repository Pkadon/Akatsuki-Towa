label avg101602:

stop music
scene placeholderbackground
$ update_portrait('sc008_01 1', 'p16', [mid(-18), light], 6)
$ update_narrator('c163')
window show
with fade_in
get_char('c163') '[convertstrid(1221526)]' (**arg(1, 1221526))
hide p16
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221527)]' (**arg(2, 1221527))
hide p1
$ update_portrait('sc008_01 1', 'p16', [mid(-18), light], 6)
get_char('c163') '[convertstrid(1221528)]' (**arg(3, 1221528))
$ update_portrait('sc008_01 4', 'p16', [mid(-18), light], 6)
get_char('c163') '[convertstrid(1221529)]' (**arg(4, 1221529))
hide p16
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221530)]' (**arg(5, 1221530))
return