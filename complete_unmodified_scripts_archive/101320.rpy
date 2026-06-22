label avg101320:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1221004)]' (**arg(1, 1221004))
hide p1
$ update_portrait('sc005_01 1', 'p13', [mid(-17), light], 6)
get_char('c133') '[convertstrid(1221005)]' (**arg(2, 1221005))
hide p13
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221006)]' (**arg(3, 1221006))
hide p1
$ update_portrait('sc005_01 4', 'p13', [mid(-17), light], 6)
get_char('c133') '[convertstrid(1221007)]' (**arg(4, 1221007))
hide p13
$ update_portrait('oc001_01 16', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221008)]' (**arg(5, 1221008))
hide p1
$ update_portrait('sc005_01 1', 'p13', [mid(-17), light], 6)
get_char('c133') '[convertstrid(1221009)]' (**arg(6, 1221009))
hide p13
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221010)]' (**arg(7, 1221010))
return