label avg101319(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1220997)]' (**arg(1, 1220997))
hide p1
$ update_portrait('sc005_01 1', 'p13', [mid(-17), light], 6)
get_char('c133') '[convertstrid(1220998)]' (**arg(2, 1220998))
$ update_portrait('sc005_01 5', 'p13', [mid(-17), light], 6)
get_char('c133') '[convertstrid(1220999)]' (**arg(3, 1220999))
hide p13
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221000)]' (**arg(4, 1221000))
hide p1
$ update_portrait('sc005_01 5', 'p13', [mid(-17), light], 6)
get_char('c133') '[convertstrid(1221001)]' (**arg(5, 1221001))
hide p13
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221002)]' (**arg(6, 1221002))
return "avg101319"