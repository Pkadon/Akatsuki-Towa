label avg101902(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1218322)]' (**arg(1, 1218322))
hide p1
$ update_portrait('sc011_01 2', 'p19', [mid(-1), light], 6)
get_char('c193') '[convertstrid(1218323)]' (**arg(2, 1218323))
hide p19
$ update_portrait('oc001_01 22', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218324)]' (**arg(3, 1218324))
hide p1
$ update_portrait('sc011_01 1', 'p19', [mid(-1), light], 6)
get_char('c193') '[convertstrid(1218325)]' (**arg(4, 1218325))
return "avg101902"