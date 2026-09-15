label avg24078(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_027
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200297)]' (**arg(1, 1200297))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
get_char('c9851') '[convertstrid(1200298)]' (**arg(2, 1200298))
get_char('c9851') '[convertstrid(1200299)]' (**arg(3, 1200299))
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200300)]' (**arg(4, 1200300))
return "avg24078"