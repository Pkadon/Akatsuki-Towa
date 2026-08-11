label avg20025(trans=fade_in):

$ play_music("ed7150.ogg")
scene placeholderbackground
$ update_portrait('st002_01 1', 'p202', [mid(-9), light], 6)
$ update_narrator('c2023')
window show
with trans
get_char('c2023') '[convertstrid(1001654)]' (**arg(1, 1001654))
hide p202
$ update_portrait('sc058_01 1', 'p63', [mid(-20), light], 6)
get_char('c633') '[convertstrid(1001655)]' (**arg(2, 1001655))
$ update_portrait('sc058_01 4', 'p63', [mid(-20), light], 6)
get_char('c633') '[convertstrid(1001656)]' (**arg(3, 1001656))
hide p63
$ update_portrait('st005_01 1', 'p205', [mid(4), light], 6)
get_char('c2053') '[convertstrid(1001657)]' (**arg(4, 1001657))
$ update_portrait('st005_01 4', 'p205', [mid(4), light], 6)
get_char('c2053') '[convertstrid(1001658)]' (**arg(5, 1001658))
hide p205
$ update_portrait('st002_01 1', 'p202', [mid(-9), light], 6)
get_char('c2023') '[convertstrid(1001659)]' (**arg(6, 1001659))
$ update_portrait('st002_01 4', 'p202', [mid(-9), light], 6)
get_char('c2023') '[convertstrid(1001660)]' (**arg(7, 1001660))
$ update_portrait('st002_01 2', 'p202', [mid(-9), light], 6)
get_char('c2023') '[convertstrid(1001661)]' (**arg(8, 1001661))
return "avg20025"