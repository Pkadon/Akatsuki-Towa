label avg20057(trans=fade_in):

$ play_music("ed7151.ogg")
scene avg_bg_027
$ update_narrator('c4971')
window show
with trans
play sfx2 "other_7071.ogg"
get_char('c4971') '[convertstrid(1002976)]' (**arg(1, 1002976))
get_char('c4971') '[convertstrid(1002977)]' (**arg(2, 1002977))
get_char('c4971') '[convertstrid(1002978)]' (**arg(3, 1002978))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002979)]' (**arg(4, 1002979))
$ update_portrait('oc001_01 3', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "other_7073.ogg"
get_char('c13') '[convertstrid(1002980)]' (**arg(5, 1002980))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002981)]' (**arg(6, 1002981))
return "avg20057"