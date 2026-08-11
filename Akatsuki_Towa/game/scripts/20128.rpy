label avg20128(trans=fade_in):

$ play_music("ed7103.ogg")
scene avg_bg_019
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1006630)]' (**arg(1, 1006630))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c21') '[convertstrid(1006631)]' (**arg(2, 1006631))
return "avg20128"