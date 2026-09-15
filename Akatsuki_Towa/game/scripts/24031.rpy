label avg24031(trans=fade_in):

$ play_music("ed7123.ogg")
scene avg_bg_046
$ update_narrator('c13')
window show
with trans
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1200125)]' (**arg(1, 1200125))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c10151') '[convertstrid(1200126)]' (**arg(2, 1200126))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200127)]' (**arg(3, 1200127))
return "avg24031"