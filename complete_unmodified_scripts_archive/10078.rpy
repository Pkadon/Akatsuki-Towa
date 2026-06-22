label avg10078:

$ play_music("ED6103.ogg")
scene avg_bg_023
$ update_narrator('c11')
window show
with fade_in
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
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch17.ogg"
get_char('c21') '[convertstrid(1005268)]' (**arg(7, 1005268))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005269)]' (**arg(8, 1005269))
hide p2
$ update_portrait('sc039_01 1', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005270)]' (**arg(9, 1005270))
hide p46
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005271)]' (**arg(10, 1005271))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c11') '[convertstrid(1005272)]' (**arg(11, 1005272))
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
get_char('c6993') '[convertstrid(1005273)]' (**arg(12, 1005273))
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005274)]' (**arg(13, 1005274))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
get_char('c6993') '[convertstrid(1005275)]' (**arg(14, 1005275))
get_char('c6993') '[convertstrid(1005276)]' (**arg(15, 1005276))
hide p1
$ update_portrait('sc040_01 4', 'p47', [l(-9), light, flip], 6)
get_char('c471') '[convertstrid(1005277)]' (**arg(16, 1005277))
$ update_portrait('sc040_01 4', 'p47', [l(-9), dark, flip], 5)
get_char('c6993') '[convertstrid(1005279)]' (**arg(17, 1005279))
get_char('c6993') '[convertstrid(1005280)]' (**arg(18, 1005280))
hide p47
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005281)]' (**arg(19, 1005281))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
get_char('c6993') '[convertstrid(1005282)]' (**arg(20, 1005282))
get_char('c6993') '[convertstrid(1005283)]' (**arg(21, 1005283))
hide p2
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005284)]' (**arg(22, 1005284))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c6993') '[convertstrid(1005285)]' (**arg(23, 1005285))
get_char('c6993') '[convertstrid(1005286)]' (**arg(24, 1005286))
return