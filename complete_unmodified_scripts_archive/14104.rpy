label avg14104(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_023
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1202130)]' (**arg(1, 1202130))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1202131)]' (**arg(2, 1202131))
hide p2
$ update_portrait('sc053_01 1', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202132)]' (**arg(3, 1202132))
hide p1
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch04.ogg"
get_char('c23') '[convertstrid(1202133)]' (**arg(4, 1202133))
hide p60
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1202134)]' (**arg(5, 1202134))
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1202135)]' (**arg(6, 1202135))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202136)]' (**arg(7, 1202136))
hide p56
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1202137)]' (**arg(8, 1202137))
$ update_portrait('sc053_01 5', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1202138)]' (**arg(9, 1202138))
$ update_portrait('sc053_01 5', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202139)]' (**arg(10, 1202139))
return "avg14104"