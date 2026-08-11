label avg20024(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_020
$ update_portrait('st033_01 2', 'p232', [r(-7), light], 6)
$ update_narrator('c2323')
window show
with trans
get_char('c2323') '[convertstrid(1001649)]' (**arg(1, 1001649))
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
get_char('c5381') '[convertstrid(1001650)]' (**arg(2, 1001650))
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1001651)]' (**arg(3, 1001651))
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1001652)]' (**arg(4, 1001652))
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
get_char('c5381') '[convertstrid(1001653)]' (**arg(5, 1001653))
return "avg20024"