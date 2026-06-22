label avg102801:

stop music
scene placeholderbackground
$ update_portrait('sc020_01 1', 'p28', [mid(-10), light], 6)
$ update_narrator('c283')
window show
with fade_in
get_char('c283') '[convertstrid(1219700)]' (**arg(1, 1219700))
hide p28
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219701)]' (**arg(2, 1219701))
hide p1
$ update_portrait('sc020_01 1', 'p28', [mid(-10), light], 6)
get_char('c283') '[convertstrid(1219702)]' (**arg(3, 1219702))
hide p28
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219703)]' (**arg(4, 1219703))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219704)]' (**arg(5, 1219704))
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219705)]' (**arg(6, 1219705))
return