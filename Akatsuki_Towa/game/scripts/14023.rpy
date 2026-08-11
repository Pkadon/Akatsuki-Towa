label avg14023(trans=fade_in):

$ play_music("ed7300.ogg")
scene avg_bg_071
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1202446)]' (**arg(1, 1202446))
$ update_portrait('oc002_01 20', 'p2', [l_entrance(-3), light, flip], 6)
play sfx2 "fight_6010.ogg"
get_char('c21') '[convertstrid(1202447)]' (**arg(2, 1202447))
$ update_portrait('oc002_01 20', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r_entrance(-2), light], 6)
play sfx2 "elc_5005.ogg"
get_char('c13') '[convertstrid(1202448)]' (**arg(3, 1202448))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202459)]' (**arg(4, 1202459))
$ play_music("ed7150.ogg")
scene avg_bg_022
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1202474)]' (**arg(5, 1202474))
get_char('c9771') '[convertstrid(1202477)]' (**arg(6, 1202477))
$ update_portrait('oc002_01 18', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1202478)]' (**arg(7, 1202478))
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
get_char('c11041') '[convertstrid(1202479)]' (**arg(8, 1202479))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202480)]' (**arg(9, 1202480))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202481)]' (**arg(10, 1202481))
hide p1
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202482)]' (**arg(11, 1202482))
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
get_char('c11041') '[convertstrid(1202484)]' (**arg(12, 1202484))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202485)]' (**arg(13, 1202485))
$ play_music("ed7300.ogg")
scene avg_bg_071
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1202486)]' (**arg(14, 1202486))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202487)]' (**arg(15, 1202487))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202488)]' (**arg(16, 1202488))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202489)]' (**arg(17, 1202489))
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202490)]' (**arg(18, 1202490))
hide p1
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 5)
get_char('c20163') '[convertstrid(1202491)]' (**arg(19, 1202491))
return "avg14023"