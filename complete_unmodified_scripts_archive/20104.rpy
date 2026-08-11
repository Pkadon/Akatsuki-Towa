label avg20104(trans=fade_in):

$ play_music("ED6103.ogg")
scene avg_bg_037
$ update_narrator('c6941')
window show
with trans
get_char('c6941') '[convertstrid(1005074)]' (**arg(1, 1005074))
get_char('c6953') '[convertstrid(1005075)]' (**arg(2, 1005075))
get_char('c6941') '[convertstrid(1005076)]' (**arg(3, 1005076))
get_char('c6953') '[convertstrid(1005077)]' (**arg(4, 1005077))
get_char('c6953') '[convertstrid(1005078)]' (**arg(5, 1005078))
get_char('c6941') '[convertstrid(1005079)]' (**arg(6, 1005079))
get_char('c6953') '[convertstrid(1005080)]' (**arg(7, 1005080))
get_char('c6941') '[convertstrid(1005081)]' (**arg(8, 1005081))
get_char('c6941') '[convertstrid(1005082)]' (**arg(9, 1005082))
$ update_portrait('oc002_01 4', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005083)]' (**arg(10, 1005083))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005084)]' (**arg(11, 1005084))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c6951') '[convertstrid(1005085)]' (**arg(12, 1005085))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005086)]' (**arg(13, 1005086))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c6941') '[convertstrid(1005087)]' (**arg(14, 1005087))
get_char('c6951') '[convertstrid(1005091)]' (**arg(15, 1005091))
hide p1
$ update_portrait('sc040_01 2', 'p47', [r(-9), light], 6)
get_char('c473') '[convertstrid(1005092)]' (**arg(16, 1005092))
$ update_portrait('sc040_01 2', 'p47', [r(-9), dark], 5)
get_char('c6951') '[convertstrid(1005093)]' (**arg(17, 1005093))
$ update_portrait('sc040_01 1', 'p47', [r(-9), light], 6)
get_char('c473') '[convertstrid(1005094)]' (**arg(18, 1005094))
$ update_portrait('sc040_01 1', 'p47', [r(-9), dark], 5)
get_char('c6951') '[convertstrid(1005095)]' (**arg(19, 1005095))
get_char('c6941') '[convertstrid(1005096)]' (**arg(20, 1005096))
hide p47
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1005097)]' (**arg(21, 1005097))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
get_char('c6951') '[convertstrid(1005098)]' (**arg(22, 1005098))
get_char('c6941') '[convertstrid(1005099)]' (**arg(23, 1005099))
hide p1
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005100)]' (**arg(24, 1005100))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005101)]' (**arg(25, 1005101))
return "avg20104"