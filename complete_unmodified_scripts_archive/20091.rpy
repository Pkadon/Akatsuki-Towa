label avg20091(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_022
$ update_narrator('c5411')
window show
with trans
get_char('c5411') '[convertstrid(1004519)]' (**arg(1, 1004519))
get_char('c5411') '[convertstrid(1004520)]' (**arg(2, 1004520))
get_char('c5411') '[convertstrid(1004521)]' (**arg(3, 1004521))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1004522)]' (**arg(4, 1004522))
return "avg20091"