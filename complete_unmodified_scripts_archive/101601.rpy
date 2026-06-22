label avg101601:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1221519)]' (**arg(1, 1221519))
hide p1
$ update_portrait('sc008_01 1', 'p16', [mid(-18), light], 6)
get_char('c163') '[convertstrid(1221520)]' (**arg(2, 1221520))
hide p16
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221521)]' (**arg(3, 1221521))
hide p1
$ update_portrait('sc008_01 5', 'p16', [mid(-18), light], 6)
get_char('c163') '[convertstrid(1221522)]' (**arg(4, 1221522))
$ update_portrait('sc008_01 4', 'p16', [mid(-18), light], 6)
get_char('c163') '[convertstrid(1221523)]' (**arg(5, 1221523))
hide p16
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221524)]' (**arg(6, 1221524))
return