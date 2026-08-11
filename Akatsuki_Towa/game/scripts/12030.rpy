label avg12030(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_015
$ update_narrator('c9721')
window show
with trans
play sfx2 "other_7047.ogg"
get_char('c9721') '[convertstrid(1120128)]' (**arg(1, 1120128))
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120129)]' (**arg(2, 1120129))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120130)]' (**arg(3, 1120130))
hide p1
get_char('c0') '[convertstrid(1120131)]' (**arg(4, 1120131))
get_char('c9721') '[convertstrid(1120132)]' (**arg(5, 1120132))
get_char('c9721') '[convertstrid(1120133)]' (**arg(6, 1120133))
$ update_portrait('oc002_01 5', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1120134)]' (**arg(7, 1120134))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
get_char('c9721') '[convertstrid(1120136)]' (**arg(8, 1120136))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120137)]' (**arg(9, 1120137))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120138)]' (**arg(10, 1120138))
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120139)]' (**arg(11, 1120139))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120140)]' (**arg(12, 1120140))
return "avg12030"