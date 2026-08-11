label avg12761(trans=fade_in):

stop music
scene avg_bg_070
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1174546)]' (**arg(1, 1174546))
get_char('c0') '[convertstrid(1174547)]' (**arg(2, 1174547))
$ play_music("ed7111.ogg")
scene avg_bg_003
$ update_narrator('c23')
with fade
$ update_portrait('oc002_01 14', 'p2', [r_entrance(-3), light], 6)
play sfx2 "other_7046.ogg"
get_char('c23') '[convertstrid(1174548)]' (**arg(3, 1174548))
$ update_portrait('oc002_01 16', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1174549)]' (**arg(4, 1174549))
$ update_portrait('oc002_01 16', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1174550)]' (**arg(5, 1174550))
hide p2
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174551)]' (**arg(6, 1174551))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174552)]' (**arg(7, 1174552))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1174553)]' (**arg(8, 1174553))
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1174554)]' (**arg(9, 1174554))
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1174555)]' (**arg(10, 1174555))
$ update_portrait('oc004_01 18', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1174556)]' (**arg(11, 1174556))
hide p1
$ update_portrait('oc004_01 18', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1174557)]' (**arg(12, 1174557))
$ update_portrait('oc002_01 22', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1174558)]' (**arg(13, 1174558))
hide p2
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1174559)]' (**arg(14, 1174559))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1174560)]' (**arg(15, 1174560))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1174561)]' (**arg(16, 1174561))
hide p3
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174562)]' (**arg(17, 1174562))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 12', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1174563)]' (**arg(18, 1174563))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1174564)]' (**arg(19, 1174564))
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st044_01 1', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1174565)]' (**arg(20, 1174565))
$ update_portrait('st044_01 1', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1174566)]' (**arg(21, 1174566))
$ update_portrait('st044_01 1', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1174567)]' (**arg(22, 1174567))
hide p4
$ update_portrait('st044_01 1', 'p692', [r(10), dark], 5)
$ update_portrait('st061_01 2', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1174568)]' (**arg(23, 1174568))
hide p692
$ update_portrait('st061_01 2', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174569)]' (**arg(24, 1174569))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1174570)]' (**arg(25, 1174570))
hide p1
$ update_portrait('st061_01 5', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1174571)]' (**arg(26, 1174571))
hide p1304
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1174572)]' (**arg(27, 1174572))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1174573)]' (**arg(28, 1174573))
hide p3
$ update_portrait('st044_01 4', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1174574)]' (**arg(29, 1174574))
hide p2
$ update_portrait('st044_01 4', 'p692', [r(10), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1174575)]' (**arg(30, 1174575))
hide p4
$ update_portrait('oc005_01 4', 'p5', [l(-6), light, flip], 6)
play sfx2 "other_7071.ogg"
get_char('c51') '[convertstrid(1174576)]' (**arg(31, 1174576))
hide p692
$ update_portrait('oc005_01 4', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174577)]' (**arg(32, 1174577))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 4', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1174578)]' (**arg(33, 1174578))
$ update_portrait('oc005_01 4', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1174579)]' (**arg(34, 1174579))
hide p1
$ update_portrait('oc005_01 4', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1174580)]' (**arg(35, 1174580))
hide p5
$ update_portrait('st061_01 4', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1174581)]' (**arg(36, 1174581))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1174582)]' (**arg(37, 1174582))
hide p3
$ update_portrait('st061_01 4', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1174583)]' (**arg(38, 1174583))
hide p1304
$ update_portrait('oc004_01 11', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st044_01 1', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1174584)]' (**arg(39, 1174584))
hide p692
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174585)]' (**arg(40, 1174585))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1174586)]' (**arg(41, 1174586))
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1174587)]' (**arg(42, 1174587))
hide p3
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1174588)]' (**arg(43, 1174588))
hide p1304
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174589)]' (**arg(44, 1174589))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1174590)]' (**arg(45, 1174590))
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174591)]' (**arg(46, 1174591))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1174592)]' (**arg(47, 1174592))
$ update_portrait('oc005_01 5', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1174593)]' (**arg(48, 1174593))
hide p5
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1174594)]' (**arg(49, 1174594))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174595)]' (**arg(50, 1174595))
hide p1
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1174596)]' (**arg(51, 1174596))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1174597)]' (**arg(52, 1174597))
hide p3
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174598)]' (**arg(53, 1174598))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174599)]' (**arg(54, 1174599))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1174600)]' (**arg(55, 1174600))
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
play sfx2 "other_7017.ogg"
get_char('c53') '[convertstrid(1174601)]' (**arg(56, 1174601))
return "avg12761"