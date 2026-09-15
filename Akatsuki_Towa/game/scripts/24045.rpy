label avg24045(trans=fade_in):

$ play_music("ed7113.ogg")
scene avg_bg_021
$ update_narrator('c13')
window show
with trans
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1200178)]' (**arg(1, 1200178))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c6541') '[convertstrid(1200179)]' (**arg(2, 1200179))
get_char('c6541') '[convertstrid(1200180)]' (**arg(3, 1200180))
get_char('c6541') '[convertstrid(1200181)]' (**arg(4, 1200181))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200182)]' (**arg(5, 1200182))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c6541') '[convertstrid(1200183)]' (**arg(6, 1200183))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200184)]' (**arg(7, 1200184))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c6541') '[convertstrid(1200185)]' (**arg(8, 1200185))
return "avg24045"