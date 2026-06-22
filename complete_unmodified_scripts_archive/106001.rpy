label avg106001:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1219035)]' (**arg(1, 1219035))
hide p1
$ update_portrait('sc053_01 1', 'p60', [mid(-32), light], 6)
get_char('c603') '[convertstrid(1219036)]' (**arg(2, 1219036))
hide p60
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219037)]' (**arg(3, 1219037))
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219038)]' (**arg(4, 1219038))
hide p1
$ update_portrait('sc053_01 5', 'p60', [mid(-32), light], 6)
get_char('c603') '[convertstrid(1219039)]' (**arg(5, 1219039))
hide p60
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219040)]' (**arg(6, 1219040))
return