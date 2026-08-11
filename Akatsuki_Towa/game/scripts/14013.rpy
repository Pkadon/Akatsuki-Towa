label avg14013(trans=fade_in):

$ play_music("ED6200.ogg")
scene avg_bg_010
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1202311)]' (**arg(1, 1202311))
$ update_portrait('sc020_01 4', 'p28', [l(-10), light, flip], 6)
get_char('c281') '[convertstrid(1202312)]' (**arg(2, 1202312))
$ update_portrait('sc020_01 4', 'p28', [l(-10), light, flip], 6)
get_char('c281') '[convertstrid(1202313)]' (**arg(3, 1202313))
$ update_portrait('sc020_01 4', 'p28', [l(-10), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202314)]' (**arg(4, 1202314))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202315)]' (**arg(5, 1202315))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
get_char('c281') '[convertstrid(1202316)]' (**arg(6, 1202316))
$ update_portrait('sc020_01 1', 'p28', [l(-10), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202317)]' (**arg(7, 1202317))
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202318)]' (**arg(8, 1202318))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202319)]' (**arg(9, 1202319))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202320)]' (**arg(10, 1202320))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
get_char('c281') '[convertstrid(1202321)]' (**arg(11, 1202321))
$ update_portrait('sc020_01 4', 'p28', [l(-10), light, flip], 6)
get_char('c281') '[convertstrid(1202322)]' (**arg(12, 1202322))
return "avg14013"