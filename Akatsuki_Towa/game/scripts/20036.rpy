label avg20036(trans=fade_in):

$ play_music("ed7104.ogg")
scene avg_bg_011
$ update_narrator('c21')
window show
with trans
$ update_portrait('oc002_01 2', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1002290)]' (**arg(1, 1002290))
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002291)]' (**arg(2, 1002291))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1002292)]' (**arg(3, 1002292))
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002293)]' (**arg(4, 1002293))
hide p2
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
$ update_portrait('st015_01 1', 'p214', [l_entrance(-9), light, flip], 6)
get_char('c2141') '[convertstrid(1002294)]' (**arg(5, 1002294))
$ update_portrait('st015_01 1', 'p214', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), l_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1002295)]' (**arg(6, 1002295))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('st015_01 5', 'p214', [l(-9), light, flip], 6)
get_char('c2141') '[convertstrid(1002296)]' (**arg(7, 1002296))
$ update_portrait('st015_01 1', 'p214', [l(-9), light, flip], 6)
get_char('c2141') '[convertstrid(1002297)]' (**arg(8, 1002297))
$ update_portrait('st015_01 4', 'p214', [l(-9), light, flip], 6)
get_char('c2141') '[convertstrid(1002298)]' (**arg(9, 1002298))
$ update_portrait('st015_01 1', 'p214', [l(-9), light, flip], 6)
get_char('c2141') '[convertstrid(1002299)]' (**arg(10, 1002299))
$ update_portrait('st015_01 1', 'p214', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1002300)]' (**arg(11, 1002300))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st015_01 2', 'p214', [l(-9), r_shake, light, flip], 6)
get_char('c2141') '[convertstrid(1002301)]' (**arg(12, 1002301))
$ update_portrait('st015_01 5', 'p214', [l(-9), light, flip], 6)
get_char('c2141') '[convertstrid(1002302)]' (**arg(13, 1002302))
$ update_portrait('st015_01 1', 'p214', [l(-9), light, flip], 6)
get_char('c2141') '[convertstrid(1002303)]' (**arg(14, 1002303))
$ update_portrait('st015_01 1', 'p214', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1002304)]' (**arg(15, 1002304))
return "avg20036"