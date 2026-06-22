label avg10441:

$ play_music("ed7162.ogg")
scene avg_bg_078
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1141749)]' (**arg(1, 1141749))
get_char('c0') '[convertstrid(1141750)]' (**arg(2, 1141750))
get_char('c0') '[convertstrid(1141751)]' (**arg(3, 1141751))
$ update_portrait('sc071_01 1', 'p611', [r(-20), light], 6)
get_char('c6113') '[convertstrid(1141752)]' (**arg(4, 1141752))
$ update_portrait('sc071_01 4', 'p611', [r(-20), light], 6)
get_char('c6113') '[convertstrid(1141753)]' (**arg(5, 1141753))
stop music
hide p611
$ update_portrait('uc004_01 4', 'p1022', [r(-25), light], 6)
get_char('c10223') '[convertstrid(1141754)]' (**arg(6, 1141754))
$ play_music("ed7544.ogg")
$ update_portrait('uc004_01 4', 'p1022', [r(-25), dark], 5)
$ update_portrait('st037_01 1', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(1141755)]' (**arg(7, 1141755))
$ update_portrait('st037_01 1', 'p236', [l(-10), dark, flip], 5)
$ update_portrait('uc004_01 4', 'p1022', [r(-25), light], 6)
get_char('c10223') '[convertstrid(1141756)]' (**arg(8, 1141756))
$ update_portrait('uc004_01 4', 'p1022', [r(-25), dark], 5)
$ update_portrait('st037_01 4', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(1141757)]' (**arg(9, 1141757))
return