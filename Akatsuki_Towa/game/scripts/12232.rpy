label avg12232(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_023
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_cancel.ogg"
get_char('c13') '[convertstrid(1121117)]' (**arg(1, 1121117))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
get_char('c6891') '[convertstrid(1121118)]' (**arg(2, 1121118))
return "avg12232"