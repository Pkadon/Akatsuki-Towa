label avg106020(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 22', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1219101)]' (**arg(1, 1219101))
hide p1
$ update_portrait('sc053_01 1', 'p60', [mid(-32), light], 6)
get_char('c603') '[convertstrid(1219102)]' (**arg(2, 1219102))
$ update_portrait('sc053_01 2', 'p60', [mid(-32), light], 6)
get_char('c603') '[convertstrid(1219103)]' (**arg(3, 1219103))
hide p60
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219104)]' (**arg(4, 1219104))
hide p1
$ update_portrait('sc053_01 5', 'p60', [mid(-32), light], 6)
get_char('c603') '[convertstrid(1219105)]' (**arg(5, 1219105))
hide p60
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219106)]' (**arg(6, 1219106))
return "avg106020"