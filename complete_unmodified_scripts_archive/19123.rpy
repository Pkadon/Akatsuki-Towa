label avg19123(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_071
$ update_portrait('sc001_01 5', 'p9', [l(-11), light, flip], 6)
$ update_narrator('c91')
window show
with trans
get_char('c91') '[convertstrid(1218083)]' (**arg(1, 1218083, size=(0.9)))
return "avg19123"