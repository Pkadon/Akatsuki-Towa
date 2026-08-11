label avg12646(trans=fade_in):

$ play_music("ED6202.ogg")
scene avg_bg_070
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1163231)]' (**arg(1, 1163231))
scene avg_bg_201
$ update_narrator('c13271')
with fade
get_char('c13271') '[convertstrid(1163232)]' (**arg(2, 1163232))
get_char('c13281') '[convertstrid(1163233)]' (**arg(3, 1163233))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1163234)]' (**arg(4, 1163234))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1163235)]' (**arg(5, 1163235))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c13281') '[convertstrid(1163236)]' (**arg(6, 1163236))
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1163237)]' (**arg(7, 1163237))
hide p2
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1163238)]' (**arg(8, 1163238))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c13271') '[convertstrid(1163239)]' (**arg(9, 1163239))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1163240)]' (**arg(10, 1163240))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c13271') '[convertstrid(1163241)]' (**arg(11, 1163241))
get_char('c13281') '[convertstrid(1163242)]' (**arg(12, 1163242))
get_char('c13271') '[convertstrid(1163243)]' (**arg(13, 1163243))
hide p1
$ update_portrait('oc002_01 22', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1163244)]' (**arg(14, 1163244))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1163245)]' (**arg(15, 1163245))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c13281') '[convertstrid(1163246)]' (**arg(16, 1163246))
get_char('c13271') '[convertstrid(1163247)]' (**arg(17, 1163247))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1163248)]' (**arg(18, 1163248))
hide p1
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1163249)]' (**arg(19, 1163249))
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
get_char('c13281') '[convertstrid(1163250)]' (**arg(20, 1163250))
get_char('c13271') '[convertstrid(1163251)]' (**arg(21, 1163251))
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1163252)]' (**arg(22, 1163252))
$ update_portrait('st061_01 5', 'p1304', [r(-2), dark], 5)
get_char('c13271') '[convertstrid(1163253)]' (**arg(23, 1163253))
get_char('c13281') '[convertstrid(1163254)]' (**arg(24, 1163254))
hide p1304
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1163255)]' (**arg(25, 1163255))
return "avg12646"