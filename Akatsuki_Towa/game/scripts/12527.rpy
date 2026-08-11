label avg12527(trans=fade_in):

$ play_music("ED6301.ogg")
scene placeholderbackground
$ update_narrator('c33')
window show
with trans
$ update_portrait('oc003_01 8', 'p3', [r_entrance(-6), light], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c33') '[convertstrid(1151515)]' (**arg(1, 1151515))
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1151516)]' (**arg(2, 1151516))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1151517)]' (**arg(3, 1151517))
hide p3
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1151518)]' (**arg(4, 1151518))
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1151519)]' (**arg(5, 1151519))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1151520)]' (**arg(6, 1151520))
return "avg12527"