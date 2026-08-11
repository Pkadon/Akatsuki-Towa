label avg20010(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_023
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1000493)]' (**arg(1, 1000493))
get_char('c0') '[convertstrid(1000494)]' (**arg(2, 1000494))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000495)]' (**arg(3, 1000495))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000496)]' (**arg(4, 1000496))
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000497)]' (**arg(5, 1000497))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000498)]' (**arg(6, 1000498))
return "avg20010"