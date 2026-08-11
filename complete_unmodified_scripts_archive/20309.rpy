label avg20309(trans=fade_in):

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1130285)]' (**arg(1, 1130285))
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1130286)]' (**arg(2, 1130286))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1130287)]' (**arg(3, 1130287))
hide p1
$ update_portrait('oc004_01 1', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1130288)]' (**arg(4, 1130288))
hide p4
get_char('c10063') '[convertstrid(1130289)]' (**arg(5, 1130289))
$ update_portrait('oc004_01 9', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1130290)]' (**arg(6, 1130290))
return "avg20309"