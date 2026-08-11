label avg101301(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc005_01 1', 'p13', [mid(-17), light], 6)
$ update_narrator('c133')
window show
with trans
get_char('c133') '[convertstrid(1220938)]' (**arg(1, 1220938))
hide p13
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220939)]' (**arg(2, 1220939))
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220940)]' (**arg(3, 1220940))
hide p1
$ update_portrait('sc005_01 1', 'p13', [mid(-17), light], 6)
get_char('c133') '[convertstrid(1220941)]' (**arg(4, 1220941))
$ update_portrait('sc005_01 5', 'p13', [mid(-17), light], 6)
get_char('c133') '[convertstrid(1220942)]' (**arg(5, 1220942))
hide p13
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220943)]' (**arg(6, 1220943))
return "avg101301"