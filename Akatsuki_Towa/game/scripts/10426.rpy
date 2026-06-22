label avg10426:

$ play_music("ed7151.ogg")
scene avg_bg_212
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1141246)]' (**arg(1, 1141246))
get_char('c0') '[convertstrid(1141247)]' (**arg(2, 1141247))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1141248)]' (**arg(3, 1141248))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1141249)]' (**arg(4, 1141249))
hide p1
play sfx2 "elc_5007.ogg"
get_char('c0') '[convertstrid(1141250)]' (**arg(5, 1141250))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1141251)]' (**arg(6, 1141251))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1141252)]' (**arg(7, 1141252))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
get_char('c11091') '[convertstrid(1141253)]' (**arg(8, 1141253))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_02.ogg"
get_char('c13') '[convertstrid(1141254)]' (**arg(9, 1141254, size=(1.1)))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
get_char('c11091') '[convertstrid(1141255)]' (**arg(10, 1141255, size=(1.2))) with shake
get_char('c11091') '[convertstrid(1141256)]' (**arg(11, 1141256, size=(1.3))) with shake
get_char('c11091') '[convertstrid(1141257)]' (**arg(12, 1141257, size=(1.4))) with shake
$ play_music("ED6516.ogg")
$ update_portrait('oc001_01 19', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1141258)]' (**arg(13, 1141258))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
play sfx2 "other_7072.ogg"
get_char('c10831') '[convertstrid(1141259)]' (**arg(14, 1141259))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1141260)]' (**arg(15, 1141260))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
get_char('c10831') '[convertstrid(1141261)]' (**arg(16, 1141261))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1141262)]' (**arg(17, 1141262))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
get_char('c10831') '[convertstrid(1141263)]' (**arg(18, 1141263))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfx2 "other_7007.ogg"
get_char('c13') '[convertstrid(1141264)]' (**arg(19, 1141264, size=(1.2))) with shake
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
get_char('c10831') '[convertstrid(1141265)]' (**arg(20, 1141265))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "other_7073.ogg"
get_char('c13') '[convertstrid(1141266)]' (**arg(21, 1141266))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c11091') '[convertstrid(1141267)]' (**arg(22, 1141267, size=(1.1))) with shake
get_char('c11091') '[convertstrid(1141268)]' (**arg(23, 1141268, size=(1.2))) with shake
$ update_portrait('oc001_01 3', 'p1', [r_midback(-2), light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na11.ogg"
get_char('c13') '[convertstrid(1141269)]' (**arg(24, 1141269, size=(1.1)))
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
play sfx2 "other_7007.ogg"
get_char('c11091') '[convertstrid(1141270)]' (**arg(25, 1141270, size=(1.1))) with shake
return