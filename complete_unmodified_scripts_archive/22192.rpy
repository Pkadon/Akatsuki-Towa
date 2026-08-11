label avg22192(trans=fade_in):

$ play_music("ed7110.ogg")
scene avg_bg_013
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1120751)]' (**arg(1, 1120751))
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1120752)]' (**arg(2, 1120752))
return "avg22192"