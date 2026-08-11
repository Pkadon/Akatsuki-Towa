label avg20034(trans=fade_in):

$ play_music("ed7104.ogg")
scene placeholderbackground
$ update_narrator('c5623')
window show
with trans
get_char('c5623') '[convertstrid(1002255)]' (**arg(1, 1002255))
get_char('c5633') '[convertstrid(1002256)]' (**arg(2, 1002256))
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1002257)]' (**arg(3, 1002257))
hide p2
get_char('c5623') '[convertstrid(1002258)]' (**arg(4, 1002258))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1002259)]' (**arg(5, 1002259))
hide p2
get_char('c5623') '[convertstrid(1002260)]' (**arg(6, 1002260))
get_char('c5623') '[convertstrid(1002261)]' (**arg(7, 1002261))
get_char('c5623') '[convertstrid(1002262)]' (**arg(8, 1002262))
get_char('c5633') '[convertstrid(1002263)]' (**arg(9, 1002263))
get_char('c5623') '[convertstrid(1002264)]' (**arg(10, 1002264))
get_char('c5633') '[convertstrid(1002265)]' (**arg(11, 1002265))
get_char('c5633') '[convertstrid(1002266)]' (**arg(12, 1002266))
get_char('c5623') '[convertstrid(1002267)]' (**arg(13, 1002267))
get_char('c5633') '[convertstrid(1002268)]' (**arg(14, 1002268))
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch02.ogg"
get_char('c23') '[convertstrid(1002269)]' (**arg(15, 1002269))
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1002270)]' (**arg(16, 1002270))
hide p2
get_char('c5623') '[convertstrid(1002271)]' (**arg(17, 1002271))
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1002272)]' (**arg(18, 1002272))
return "avg20034"