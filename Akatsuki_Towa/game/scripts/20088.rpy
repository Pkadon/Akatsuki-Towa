label avg20088(trans=fade_in):

$ play_music("ed7106.ogg")
scene avg_bg_019
$ update_narrator('c6521')
window show
with trans
get_char('c6521') '[convertstrid(1004487)]' (**arg(1, 1004487))
get_char('c6521') '[convertstrid(1004488)]' (**arg(2, 1004488))
get_char('c6521') '[convertstrid(1004489)]' (**arg(3, 1004489))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1004490)]' (**arg(4, 1004490))
return "avg20088"