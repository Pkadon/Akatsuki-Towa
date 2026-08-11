label avg12442(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_019
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1143255)]' (**arg(1, 1143255))
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch31.ogg"
get_char('c21') '[convertstrid(1143256)]' (**arg(2, 1143256))
$ update_portrait('oc002_01 21', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch21.ogg"
get_char('c21') '[convertstrid(1143257)]' (**arg(3, 1143257))
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1143258)]' (**arg(4, 1143258))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1143259)]' (**arg(5, 1143259))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1143260)]' (**arg(6, 1143260))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1143261)]' (**arg(7, 1143261))
hide p3
hide p1
$ update_narrator('c11513')
with fade
get_char('c11513') '[convertstrid(1143262)]' (**arg(8, 1143262))
get_char('c11513') '[convertstrid(1143263)]' (**arg(9, 1143263))
get_char('c11521') '[convertstrid(1143264)]' (**arg(10, 1143264))
$ update_portrait('oc002_01 2', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1143265)]' (**arg(11, 1143265))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c11521') '[convertstrid(1143266)]' (**arg(12, 1143266)) with shake
get_char('c11511') '[convertstrid(1143267)]' (**arg(13, 1143267))
get_char('c11511') '[convertstrid(1143268)]' (**arg(14, 1143268))
get_char('c11511') '[convertstrid(1143269)]' (**arg(15, 1143269))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143270)]' (**arg(16, 1143270))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c11511') '[convertstrid(1143271)]' (**arg(17, 1143271))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1143272)]' (**arg(18, 1143272))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1143273)]' (**arg(19, 1143273))
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1143274)]' (**arg(20, 1143274))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c13') '[convertstrid(1143275)]' (**arg(21, 1143275))
hide p2
hide p1
get_char('c0') '[convertstrid(1143276)]' (**arg(22, 1143276))
play sfx2 "other_7033.ogg"
get_char('c0') '[convertstrid(1143277)]' (**arg(23, 1143277))
$ update_portrait('oc003_01 12', 'p3', [l(-6), l_shake, light, flip], 6)
get_char('c31') '[convertstrid(1143278)]' (**arg(24, 1143278))
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1143279)]' (**arg(25, 1143279))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1143280)]' (**arg(26, 1143280))
hide p3
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
get_char('c11511') '[convertstrid(1143281)]' (**arg(27, 1143281))
get_char('c11511') '[convertstrid(1143282)]' (**arg(28, 1143282))
$ update_portrait('oc003_01 17', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(1143283)]' (**arg(29, 1143283))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1143284)]' (**arg(30, 1143284))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1143285)]' (**arg(31, 1143285))
hide p3
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1143286)]' (**arg(32, 1143286))
return "avg12442"