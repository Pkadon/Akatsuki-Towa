label avg107105(trans=fade_in):

$ play_music("ed7544.ogg")
scene avg_bg_211
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
play sfx2 "other_7018.ogg"
get_char('c21') '[convertstrid(1179769)]' (**arg(1, 1179769))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
play sfx2 "other_7018.ogg"
get_char('c13') '[convertstrid(1179770)]' (**arg(2, 1179770))
hide p2
hide p1
get_char('c0') '[convertstrid(1179771)]' (**arg(3, 1179771))
get_char('c0') '[convertstrid(1179772)]' (**arg(4, 1179772))
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1179773)]' (**arg(5, 1179773))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('sc010_01 4', 'p18', [r(-10), light], 6)
get_char('c183') '[convertstrid(1179774)]' (**arg(6, 1179774))
hide p4
$ update_portrait('sc010_01 4', 'p18', [r(-10), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1179775)]' (**arg(7, 1179775))
hide p18
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1179776)]' (**arg(8, 1179776))
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1179777)]' (**arg(9, 1179777))
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7073.ogg"
get_char('c31') '[convertstrid(1179778)]' (**arg(10, 1179778))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 13', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1179779)]' (**arg(11, 1179779))
hide p3
hide p4
get_char('c0') '[convertstrid(1179780)]' (**arg(12, 1179780))
$ update_portrait('oc004_01 21', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1179781)]' (**arg(13, 1179781))
$ update_portrait('oc004_01 21', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179782)]' (**arg(14, 1179782))
hide p4
hide p1
play sfx2 "other_7011.ogg"
get_char('c0') '[convertstrid(1179783)]' (**arg(15, 1179783))
$ update_portrait('oc004_01 3', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7011.ogg"
get_char('c41') '[convertstrid(1179784)]' (**arg(16, 1179784))
$ update_portrait('oc004_01 3', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 21', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1179785)]' (**arg(17, 1179785))
$ update_portrait('oc003_01 21', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 20', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1179786)]' (**arg(18, 1179786))
hide p3
$ update_portrait('oc004_01 20', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1179787)]' (**arg(19, 1179787))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1179788)]' (**arg(20, 1179788))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 18', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1179789)]' (**arg(21, 1179789))
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1179790)]' (**arg(22, 1179790))
$ update_portrait('oc004_01 11', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 10', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1179791)]' (**arg(23, 1179791))
$ update_portrait('oc003_01 10', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 21', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1179792)]' (**arg(24, 1179792))
hide p4
hide p3
play sfx2 "other_7023.ogg"
get_char('c0') '[convertstrid(1179793)]' (**arg(25, 1179793))
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7087.ogg"
get_char('c41') '[convertstrid(1179794)]' (**arg(26, 1179794)) with shake
scene avg_bg_506
$ update_narrator('c0')
with fade
play sfx2 "other_7017.ogg"
get_char('c0') '[convertstrid(1179795)]' (**arg(27, 1179795))
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1179796)]' (**arg(28, 1179796))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179797)]' (**arg(29, 1179797))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1179798)]' (**arg(30, 1179798))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179799)]' (**arg(31, 1179799))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179800)]' (**arg(32, 1179800))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179801)]' (**arg(33, 1179801))
hide p2
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 12', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1179802)]' (**arg(34, 1179802))
$ update_portrait('oc004_01 21', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1179803)]' (**arg(35, 1179803))
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1179804)]' (**arg(36, 1179804))
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179805)]' (**arg(37, 1179805))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l_exit(-5), light, flip], 6)
play sfx2 "other_7085.ogg"
get_char('c41') '[convertstrid(1179806)]' (**arg(38, 1179806))
hide p4
$ update_portrait('oc001_01 12', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1179807)]' (**arg(39, 1179807))
hide p1
get_char('c0') '[convertstrid(1179808)]' (**arg(40, 1179808))
$ update_portrait('sc010_01 4', 'p18', [l_entrance(-10), light, flip], 6)
get_char('c181') '[convertstrid(1179809)]' (**arg(41, 1179809))
hide p18
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1179810)]' (**arg(42, 1179810))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 14', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179811)]' (**arg(43, 1179811))
$ update_portrait('oc001_01 14', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1179812)]' (**arg(44, 1179812))
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179813)]' (**arg(45, 1179813))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179814)]' (**arg(46, 1179814))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1179815)]' (**arg(47, 1179815))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1179816)]' (**arg(48, 1179816))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179817)]' (**arg(49, 1179817))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179818)]' (**arg(50, 1179818))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1179819)]' (**arg(51, 1179819))
hide p18
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1179820)]' (**arg(52, 1179820))
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1179821)]' (**arg(53, 1179821))
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179822)]' (**arg(54, 1179822))
hide p1304
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1179823)]' (**arg(55, 1179823))
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1179824)]' (**arg(56, 1179824))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179825)]' (**arg(57, 1179825))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179826)]' (**arg(58, 1179826))
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1179827)]' (**arg(59, 1179827))
get_char('c0') '[convertstrid(1179828)]' (**arg(60, 1179828))
scene avg_bg_211
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
get_char('c21') '[convertstrid(1179829)]' (**arg(61, 1179829))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 21', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1179830)]' (**arg(62, 1179830))
hide p2
$ update_portrait('oc003_01 21', 'p3', [r(-6), dark], 5)
get_char('c14541') '[convertstrid(1179831)]' (**arg(63, 1179831))
get_char('c14551') '[convertstrid(1179832)]' (**arg(64, 1179832))
get_char('c14561') '[convertstrid(1179833)]' (**arg(65, 1179833))
$ update_portrait('st061_01 3', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1179834)]' (**arg(66, 1179834))
$ update_portrait('st061_01 3', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1179835)]' (**arg(67, 1179835))
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1179836)]' (**arg(68, 1179836))
hide p1304
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1179837)]' (**arg(69, 1179837))
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 9', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1179838)]' (**arg(70, 1179838))
$ update_portrait('oc003_01 9', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1179839)]' (**arg(71, 1179839))
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1179840)]' (**arg(72, 1179840))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 9', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1179841)]' (**arg(73, 1179841))
hide p2
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 2', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1179842)]' (**arg(74, 1179842))
hide p1304
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1179843)]' (**arg(75, 1179843))
hide p3
get_char('c0') '[convertstrid(1179844)]' (**arg(76, 1179844))
get_char('c14541') '[convertstrid(1179845)]' (**arg(77, 1179845))
get_char('c14551') '[convertstrid(1179846)]' (**arg(78, 1179846))
get_char('c14561') '[convertstrid(1179847)]' (**arg(79, 1179847))
get_char('c0') '[convertstrid(1179848)]' (**arg(80, 1179848))
$ update_portrait('oc002_01 16', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1179849)]' (**arg(81, 1179849))
$ update_portrait('oc002_01 16', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1179850)]' (**arg(82, 1179850))
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1179851)]' (**arg(83, 1179851))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1179852)]' (**arg(84, 1179852))
hide p3
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1179853)]' (**arg(85, 1179853))
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1179854)]' (**arg(86, 1179854))
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1179855)]' (**arg(87, 1179855))
hide p4
$ update_portrait('sc010_01 4', 'p18', [l(-10), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179856)]' (**arg(88, 1179856))
return "avg107105"