label avg10677(trans=fade_in):

$ play_music("ed7564.ogg")
scene avg_bg_050
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1166333)]' (**arg(1, 1166333))
get_char('c0') '[convertstrid(1166334)]' (**arg(2, 1166334))
get_char('c0') '[convertstrid(1166335)]' (**arg(3, 1166335))
get_char('c0') '[convertstrid(1166336)]' (**arg(4, 1166336))
scene avg_bg_070
$ update_portrait('oc008_01 1', 'p8', [l(-5), light, flip], 6)
$ update_narrator('c81')
with fade
get_char('c81') '[convertstrid(1166337)]' (**arg(5, 1166337))
$ update_portrait('oc008_01 1', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1166338)]' (**arg(6, 1166338))
$ update_portrait('oc008_01 1', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1166339)]' (**arg(7, 1166339))
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_ai02b.ogg"
get_char('c81') '[convertstrid(1166340)]' (**arg(8, 1166340))
$ update_portrait('oc008_01 6', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1166341)]' (**arg(9, 1166341))
hide p8
play sfxvoice "avg_vocal_ai07.ogg"
get_char('c0') '[convertstrid(1166342)]' (**arg(10, 1166342))
return "avg10677"