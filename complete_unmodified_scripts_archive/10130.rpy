label avg10130(trans=fade_in):

$ play_music("ed7110.ogg")
scene avg_bg_018
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1007298)]' (**arg(1, 1007298))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007299)]' (**arg(2, 1007299))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1007300)]' (**arg(3, 1007300))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007301)]' (**arg(4, 1007301))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 13', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1007302)]' (**arg(5, 1007302))
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007303)]' (**arg(6, 1007303))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1007304)]' (**arg(7, 1007304))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfx2 "fight_6024.ogg"
get_char('c11') '[convertstrid(1007305)]' (**arg(8, 1007305))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007306)]' (**arg(9, 1007306))
$ update_portrait('oc002_01 7', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007307)]' (**arg(10, 1007307))
$ play_music("ed7106.ogg")
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfx2 "other_7020.ogg"
get_char('c23') '[convertstrid(1007308)]' (**arg(11, 1007308))
hide p1
hide p2
$ update_narrator('c9673')
with fade
play sfx2 "other_7088.ogg"
get_char('c9673') '[convertstrid(1007309)]' (**arg(12, 1007309))
$ update_portrait('oc002_01 18', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1007310)]' (**arg(13, 1007310))
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
get_char('c9673') '[convertstrid(1007311)]' (**arg(14, 1007311))
hide p2
$ update_portrait('oc001_01 22', 'p1', [l(-2), light, flip], 6)
play sfx2 "fight_6024.ogg"
get_char('c11') '[convertstrid(1007312)]' (**arg(15, 1007312))
$ update_portrait('oc001_01 22', 'p1', [l(-2), dark, flip], 5)
get_char('c9673') '[convertstrid(1007313)]' (**arg(16, 1007313))
get_char('c9673') '[convertstrid(1007314)]' (**arg(17, 1007314))
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch04_b.ogg"
get_char('c23') '[convertstrid(1007315)]' (**arg(18, 1007315))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007316)]' (**arg(19, 1007316))
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c11') '[convertstrid(1007317)]' (**arg(20, 1007317))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1007318)]' (**arg(21, 1007318))
return "avg10130"