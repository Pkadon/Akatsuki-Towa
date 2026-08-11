label avg10081(trans=fade_in):

$ play_music("ED6103.ogg")
scene avg_bg_023
$ update_narrator('c11')
window show
with trans
$ update_portrait('oc001_01 1', 'p1', [l_entrance(-2), light, flip], 6)
play sfx2 "other_7047.ogg"
get_char('c11') '[convertstrid(1005262)]' (**arg(1, 1005262))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c6993') '[convertstrid(1005263)]' (**arg(2, 1005263))
get_char('c6993') '[convertstrid(1005264)]' (**arg(3, 1005264))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005265)]' (**arg(4, 1005265))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
get_char('c6993') '[convertstrid(1005266)]' (**arg(5, 1005266))
get_char('c6993') '[convertstrid(1005267)]' (**arg(6, 1005267))
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005268)]' (**arg(7, 1005268))
hide p2
$ update_portrait('sc039_01 4', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1005269)]' (**arg(8, 1005269))
$ update_portrait('sc039_01 4', 'p46', [l(-13), dark, flip], 5)
get_char('c6993') '[convertstrid(1005273)]' (**arg(9, 1005273))
hide p46
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005274)]' (**arg(10, 1005274))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
get_char('c6993') '[convertstrid(1005275)]' (**arg(11, 1005275))
get_char('c6993') '[convertstrid(1005276)]' (**arg(12, 1005276))
hide p1
$ update_portrait('sc040_01 4', 'p47', [l(-9), light, flip], 6)
get_char('c471') '[convertstrid(1005277)]' (**arg(13, 1005277))
$ update_portrait('sc040_01 4', 'p47', [l(-9), dark, flip], 5)
get_char('c6993') '[convertstrid(1005279)]' (**arg(14, 1005279))
get_char('c6993') '[convertstrid(1005280)]' (**arg(15, 1005280))
hide p47
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005281)]' (**arg(16, 1005281))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
get_char('c6993') '[convertstrid(1005282)]' (**arg(17, 1005282))
get_char('c6993') '[convertstrid(1005283)]' (**arg(18, 1005283))
hide p2
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005284)]' (**arg(19, 1005284))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c6993') '[convertstrid(1005285)]' (**arg(20, 1005285))
get_char('c6993') '[convertstrid(1005286)]' (**arg(21, 1005286))
return "avg10081"