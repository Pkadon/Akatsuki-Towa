label avg12190(trans=fade_in):

$ play_music("ed7110.ogg")
scene avg_bg_023
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_cancel.ogg"
get_char('c13') '[convertstrid(1120720)]' (**arg(1, 1120720))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('st009_01 2', 'p209', [l(-22), light, flip], 6)
get_char('c2091') '[convertstrid(1120721)]' (**arg(2, 1120721))
return "avg12190"