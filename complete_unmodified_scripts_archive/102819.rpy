label avg102819:

stop music
scene placeholderbackground
$ update_portrait('sc020_01 1', 'p28', [mid(-10), light], 6)
$ update_narrator('c283')
window show
with fade_in
get_char('c283') '[convertstrid(1219762)]' (**arg(1, 1219762))
hide p28
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219763)]' (**arg(2, 1219763))
hide p1
$ update_portrait('sc020_01 4', 'p28', [mid(-10), light], 6)
get_char('c283') '[convertstrid(1219764)]' (**arg(3, 1219764))
$ update_portrait('sc020_01 4', 'p28', [mid(-10), light], 6)
get_char('c283') '[convertstrid(1219765)]' (**arg(4, 1219765))
hide p28
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219766)]' (**arg(5, 1219766))
hide p1
$ update_portrait('sc020_01 1', 'p28', [mid(-10), light], 6)
get_char('c283') '[convertstrid(1219767)]' (**arg(6, 1219767))
hide p28
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219768)]' (**arg(7, 1219768))
return