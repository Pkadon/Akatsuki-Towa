label avg105903:

stop music
scene placeholderbackground
$ update_portrait('sc052_01 5', 'p59', [mid(-25), light], 6)
$ update_narrator('c593')
window show
with fade_in
get_char('c593') '[convertstrid(1219250)]' (**arg(1, 1219250))
hide p59
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219251)]' (**arg(2, 1219251))
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219252)]' (**arg(3, 1219252))
hide p1
$ update_portrait('sc052_01 1', 'p59', [mid(-25), light], 6)
get_char('c593') '[convertstrid(1219253)]' (**arg(4, 1219253))
$ update_portrait('sc052_01 5', 'p59', [mid(-25), light], 6)
get_char('c593') '[convertstrid(1219254)]' (**arg(5, 1219254))
hide p59
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219255)]' (**arg(6, 1219255))
return