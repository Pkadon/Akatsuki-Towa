label avg20005(trans=fade_in):

$ play_music("ed9997.ogg")
scene avg_bg_071
$ update_narrator('c13')
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
window show
with trans
$ update_portrait('oc001_01 19', 'p1', [r(-2), l_shake, light], 6)
play sfxvoice "bcv_oc001_hurt_02.ogg"
get_char('c13') '[convertstrid(1000224)]' (**arg(1, 1000224))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000225)]' (**arg(2, 1000225))
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1000226)]' (**arg(3, 1000226))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000227)]' (**arg(4, 1000227))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 20', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch31.ogg"
get_char('c21') '[convertstrid(1000228)]' (**arg(5, 1000228))
hide p2
hide p1
play sfx2 "common_remind.ogg"
get_char('c0') '[convertstrid(1000229)]' (**arg(6, 1000229))
get_char('c0') '[convertstrid(1000230)]' (**arg(7, 1000230))
return "avg20005"