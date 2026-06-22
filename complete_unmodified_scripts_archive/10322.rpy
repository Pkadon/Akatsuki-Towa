label avg10322:

$ play_music("ed7123.ogg")
scene avg_bg_040
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
$ update_narrator('c551')
window show
with fade_in
get_char('c551') '[convertstrid(1130700)]' (**arg(1, 1130700))
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130701)]' (**arg(2, 1130701))
$ update_portrait('sc048_01 1', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('st036_01 5', 'p1017', [r(-17), light], 6)
get_char('c10173') '[convertstrid(1130702)]' (**arg(3, 1130702))
$ update_portrait('st036_01 5', 'p1017', [r(-17), dark], 5)
$ update_portrait('sc048_01 5', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130703)]' (**arg(4, 1130703))
$ update_portrait('sc048_01 5', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('st036_01 2', 'p1017', [r(-17), light], 6)
play sfx2 "other_7020.ogg"
get_char('c10173') '[convertstrid(1130704)]' (**arg(5, 1130704))
$ update_portrait('st036_01 2', 'p1017', [r(-17), dark], 5)
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
play sfx2 "other_7044.ogg"
get_char('c551') '[convertstrid(1130705)]' (**arg(6, 1130705))
hide p55
$ update_portrait('oc001_01 4', 'p1', [l_entrance(-2), light, flip], 6)
play sfx2 "other_7047.ogg"
get_char('c11') '[convertstrid(1130706)]' (**arg(7, 1130706))
hide p1017
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc048_01 1', 'p55', [r(-7), light], 6)
get_char('c553') '[convertstrid(1130707)]' (**arg(8, 1130707))
$ update_portrait('sc048_01 5', 'p55', [r(-7), light], 6)
get_char('c553') '[convertstrid(1130708)]' (**arg(9, 1130708))
hide p1
$ update_portrait('sc048_01 5', 'p55', [r(-7), dark], 5)
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li02.ogg"
get_char('c41') '[convertstrid(1130709)]' (**arg(10, 1130709))
hide p55
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st036_01 2', 'p235', [r(-17), light], 6)
get_char('c2353') '[convertstrid(1130710)]' (**arg(11, 1130710))
hide p4
$ update_portrait('st036_01 2', 'p235', [r(-17), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1130711)]' (**arg(12, 1130711))
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130712)]' (**arg(13, 1130712))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st036_01 5', 'p235', [r(-17), light], 6)
get_char('c2353') '[convertstrid(1130713)]' (**arg(14, 1130713))
hide p4
$ update_portrait('st036_01 5', 'p235', [r(-17), dark], 5)
$ update_portrait('sc048_01 5', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130714)]' (**arg(15, 1130714))
hide p55
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1130715)]' (**arg(16, 1130715))
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1130716)]' (**arg(17, 1130716))
hide p235
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130717)]' (**arg(18, 1130717))
hide p2
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130718)]' (**arg(19, 1130718))
$ update_portrait('oc004_01 10', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c11') '[convertstrid(1130719)]' (**arg(20, 1130719))
hide p1
$ update_portrait('oc003_01 6', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130720)]' (**arg(21, 1130720))
hide p4
$ update_portrait('oc003_01 6', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st036_01 3', 'p235', [r(-17), light], 6)
get_char('c2353') '[convertstrid(1130721)]' (**arg(22, 1130721))
$ update_portrait('st036_01 3', 'p235', [r(-17), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro15.ogg"
get_char('c31') '[convertstrid(1130722)]' (**arg(23, 1130722))
hide p3
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130723)]' (**arg(24, 1130723))
hide p235
$ update_portrait('sc048_01 1', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130724)]' (**arg(25, 1130724))
hide p55
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130725)]' (**arg(26, 1130725))
hide p4
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 24', 'p1', [r_midback(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1130726)]' (**arg(27, 1130726))
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1130727)]' (**arg(28, 1130727))
get_char('c0') '[convertstrid(1130728)]' (**arg(29, 1130728))
scene avg_bg_040
$ update_portrait('st036_01 5', 'p235', [r(-17), light], 6)
$ update_narrator('c2353')
with fade
get_char('c2353') '[convertstrid(1130729)]' (**arg(30, 1130729))
$ update_portrait('st036_01 5', 'p235', [r(-17), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130730)]' (**arg(31, 1130730))
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch03.ogg"
get_char('c21') '[convertstrid(1130731)]' (**arg(32, 1130731))
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st036_01 5', 'p235', [r(-17), light], 6)
get_char('c2353') '[convertstrid(1130732)]' (**arg(33, 1130732))
hide p2
$ update_portrait('st036_01 5', 'p235', [r(-17), dark], 5)
$ update_portrait('sc048_01 5', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130733)]' (**arg(34, 1130733))
hide p55
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130734)]' (**arg(35, 1130734))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130735)]' (**arg(36, 1130735))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st036_01 1', 'p235', [r(-17), light], 6)
get_char('c2353') '[convertstrid(1130736)]' (**arg(37, 1130736))
hide p4
$ update_portrait('st036_01 1', 'p235', [r(-17), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130737)]' (**arg(38, 1130737))
hide p235
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130738)]' (**arg(39, 1130738))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130739)]' (**arg(40, 1130739))
$ update_portrait('sc048_01 5', 'p55', [l_exit(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130740)]' (**arg(41, 1130740))
hide p55
hide p1
$ update_portrait('st036_01 5', 'p235', [r(-17), light], 6)
play sfx2 "other_7047.ogg"
get_char('c2353') '[convertstrid(1130741)]' (**arg(42, 1130741))
$ play_music("ed7151.ogg")
scene avg_bg_046
$ update_narrator('c551')
with fade
$ update_portrait('sc048_01 1', 'p55', [l_entrance(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130742)]' (**arg(43, 1130742))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130743)]' (**arg(44, 1130743))
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130744)]' (**arg(45, 1130744))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130745)]' (**arg(46, 1130745))
hide p1
$ update_portrait('sc048_01 1', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130746)]' (**arg(47, 1130746))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130747)]' (**arg(48, 1130747))
hide p2
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130748)]' (**arg(49, 1130748))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130749)]' (**arg(50, 1130749))
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1130750)]' (**arg(51, 1130750)) with shake
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130751)]' (**arg(52, 1130751))
$ update_portrait('sc048_01 1', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130752)]' (**arg(53, 1130752))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130753)]' (**arg(54, 1130753))
hide p1
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130754)]' (**arg(55, 1130754))
$ update_portrait('oc004_01 10', 'p4', [r(-5), dark], 5)
$ update_portrait('sc048_01 2', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130755)]' (**arg(56, 1130755))
$ update_portrait('sc048_01 2', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130756)]' (**arg(57, 1130756))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130757)]' (**arg(58, 1130757))
hide p4
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1130758)]' (**arg(59, 1130758))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130759)]' (**arg(60, 1130759))
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1130760)]' (**arg(61, 1130760))
hide p1
$ update_portrait('sc048_01 1', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130761)]' (**arg(62, 1130761))
scene avg_bg_070
$ update_narrator('c0')
with fade
play sfx2 "other_7020.ogg"
get_char('c0') '[convertstrid(1130762)]' (**arg(63, 1130762))
scene avg_bg_046
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1130763)]' (**arg(64, 1130763))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130764)]' (**arg(65, 1130764))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 22', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130765)]' (**arg(66, 1130765))
$ update_portrait('oc002_01 22', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130766)]' (**arg(67, 1130766))
hide p1
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130767)]' (**arg(68, 1130767))
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130768)]' (**arg(69, 1130768))
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1130769)]' (**arg(70, 1130769))
hide p3
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130770)]' (**arg(71, 1130770))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130771)]' (**arg(72, 1130771))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130772)]' (**arg(73, 1130772))
hide p4
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130773)]' (**arg(74, 1130773))
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130774)]' (**arg(75, 1130774))
hide p1
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130775)]' (**arg(76, 1130775))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130776)]' (**arg(77, 1130776))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130777)]' (**arg(78, 1130777))
return