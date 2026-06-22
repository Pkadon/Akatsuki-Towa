label avg101720:

stop music
scene placeholderbackground
$ update_portrait('sc009_01 4', 'p17', [mid(-13), light], 6)
$ update_narrator('c173')
window show
with fade_in
get_char('c173') '[convertstrid(1221926)]' (**arg(1, 1221926))
hide p17
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221927)]' (**arg(2, 1221927))
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221928)]' (**arg(3, 1221928))
hide p1
$ update_portrait('sc009_01 1', 'p17', [mid(-13), light], 6)
get_char('c173') '[convertstrid(1221929)]' (**arg(4, 1221929))
hide p17
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221930)]' (**arg(5, 1221930))
return