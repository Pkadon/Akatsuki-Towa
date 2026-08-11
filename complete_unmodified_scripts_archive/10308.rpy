label avg10308(trans=fade_in):

$ play_music("ed7124.ogg")
scene avg_bg_059
$ update_narrator('c10063')
window show
with trans
play sfx2 "other_7021.ogg"
get_char('c10063') '[convertstrid(1130265)]' (**arg(1, 1130265))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1130266)]' (**arg(2, 1130266))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c10063') '[convertstrid(1130267)]' (**arg(3, 1130267))
get_char('c10063') '[convertstrid(1130268)]' (**arg(4, 1130268))
get_char('c10063') '[convertstrid(1130269)]' (**arg(5, 1130269))
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130270)]' (**arg(6, 1130270))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
get_char('c10063') '[convertstrid(1130271)]' (**arg(7, 1130271))
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130272)]' (**arg(8, 1130272))
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 5)
get_char('c10063') '[convertstrid(1130273)]' (**arg(9, 1130273))
get_char('c10063') '[convertstrid(1130274)]' (**arg(10, 1130274))
$ update_portrait('oc004_01 12', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1130275)]' (**arg(11, 1130275))
$ update_portrait('oc004_01 12', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130276)]' (**arg(12, 1130276))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130277)]' (**arg(13, 1130277))
hide p2
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro08.ogg"
get_char('c33') '[convertstrid(1130278)]' (**arg(14, 1130278))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1130279)]' (**arg(15, 1130279))
hide p3
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
get_char('c10063') '[convertstrid(1130280)]' (**arg(16, 1130280))
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li30.ogg"
get_char('c41') '[convertstrid(1130281)]' (**arg(17, 1130281))
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130282)]' (**arg(18, 1130282))
menu:
    extend ""
    '[convertstrid(1130283)]':
        call avg10309
    '[convertstrid(1130284)]':
        call avg10310
return _return