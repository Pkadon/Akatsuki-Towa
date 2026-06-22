label avg102803:

stop music
scene placeholderbackground
$ update_portrait('sc020_01 1', 'p28', [mid(-10), light], 6)
$ update_narrator('c283')
window show
with fade_in
get_char('c283') '[convertstrid(1219716)]' (**arg(1, 1219716))
hide p28
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219717)]' (**arg(2, 1219717))
hide p1
$ update_portrait('sc020_01 1', 'p28', [mid(-10), light], 6)
get_char('c283') '[convertstrid(1219718)]' (**arg(3, 1219718))
hide p28
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219719)]' (**arg(4, 1219719))
hide p1
$ update_portrait('sc020_01 5', 'p28', [mid(-10), light], 6)
get_char('c283') '[convertstrid(1219720)]' (**arg(5, 1219720))
$ update_portrait('sc020_01 1', 'p28', [mid(-10), light], 6)
get_char('c283') '[convertstrid(1219721)]' (**arg(6, 1219721))
hide p28
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219722)]' (**arg(7, 1219722))
return