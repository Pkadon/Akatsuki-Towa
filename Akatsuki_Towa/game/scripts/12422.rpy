label avg12422(trans=fade_in):

$ play_music("ed7103.ogg")
scene avg_bg_023
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1140266)]' (**arg(1, 1140266))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140267)]' (**arg(2, 1140267))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro02.ogg"
get_char('c31') '[convertstrid(1140268)]' (**arg(3, 1140268))
hide p3
$ update_portrait('oc004_01 1', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(1140269)]' (**arg(4, 1140269))
$ update_portrait('oc004_01 4', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1140270)]' (**arg(5, 1140270))
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch10.ogg"
get_char('c23') '[convertstrid(1140271)]' (**arg(6, 1140271))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140272)]' (**arg(7, 1140272))
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1140273)]' (**arg(8, 1140273))
hide p3
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1140274)]' (**arg(9, 1140274))
$ update_portrait('oc002_01 15', 'p2', [l_exit(-3), light, flip], 6)
get_char('c21') '[convertstrid(1140275)]' (**arg(10, 1140275))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1140276)]' (**arg(11, 1140276))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140277)]' (**arg(12, 1140277))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140278)]' (**arg(13, 1140278))
return "avg12422"