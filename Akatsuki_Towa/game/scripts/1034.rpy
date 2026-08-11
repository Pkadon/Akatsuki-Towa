label avg1034(trans=fade_in):

$ play_music("ed7201.ogg")
scene avg_bg_010
$ update_narrator('c23')
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
window show
with trans
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(2100577)]' (**arg(1, 2100577))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc053_01 4', 'p60', [l_entrance(-32), light, flip], 6)
get_char('c601') '[convertstrid(2100578)]' (**arg(2, 2100578))
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(2100579)]' (**arg(3, 2100579))
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(2100580)]' (**arg(4, 2100580))
$ update_portrait('sc053_01 4', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(2100581)]' (**arg(5, 2100581))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100582)]' (**arg(6, 2100582))
return "avg1034"