label avg103020:

stop music
scene placeholderbackground
$ update_portrait('sc022_01 1', 'p30', [mid(-9), light], 6)
$ update_narrator('c303')
window show
with fade_in
get_char('c303') '[convertstrid(1222464)]' (**arg(1, 1222464))
hide p30
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222465)]' (**arg(2, 1222465))
hide p1
$ update_portrait('sc022_01 1', 'p30', [mid(-9), light], 6)
get_char('c303') '[convertstrid(1222466)]' (**arg(3, 1222466))
$ update_portrait('sc022_01 4', 'p30', [mid(-9), light], 6)
get_char('c303') '[convertstrid(1222467)]' (**arg(4, 1222467))
hide p30
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222468)]' (**arg(5, 1222468))
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222469)]' (**arg(6, 1222469))
return