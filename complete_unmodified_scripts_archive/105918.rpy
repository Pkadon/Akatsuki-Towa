label avg105918:

stop music
scene placeholderbackground
$ update_portrait('sc052_01 2', 'p59', [mid(-25), light], 6)
$ update_narrator('c593')
window show
with fade_in
get_char('c593') '[convertstrid(1219287)]' (**arg(1, 1219287))
hide p59
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219288)]' (**arg(2, 1219288))
hide p1
$ update_portrait('sc052_01 1', 'p59', [mid(-25), light], 6)
get_char('c593') '[convertstrid(1219289)]' (**arg(3, 1219289))
hide p59
get_char('c0') '[convertstrid(1219290)]' (**arg(4, 1219290))
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219291)]' (**arg(5, 1219291))
return