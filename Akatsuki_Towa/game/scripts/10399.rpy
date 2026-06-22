label avg10399:

$ play_music("ed7526.ogg")
scene avg_bg_052
$ update_narrator('c10511')
window show
with fade_in
$ update_portrait('uc003_04 1', 'p1051', [l_entrance(-14), light, flip], 6)
play sfx2 "fight_6024.ogg"
get_char('c10511') '[convertstrid(1132746)]' (**arg(1, 1132746))
$ update_portrait('uc003_04 2', 'p1051', [l(-14), light, flip], 6)
get_char('c10511') '[convertstrid(1132747)]' (**arg(2, 1132747))
hide p1051
$ update_portrait('uc003_04 4', 'p1045', [l(-14), light, flip], 6)
get_char('c10451') '[convertstrid(1132748)]' (**arg(3, 1132748))
$ update_portrait('uc003_04 4', 'p1045', [l(-14), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p4', [r_midback(-5), light], 6)
get_char('c43') '[convertstrid(1132749)]' (**arg(4, 1132749))
hide p4
$ update_portrait('oc001_01 15', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1132750)]' (**arg(5, 1132750))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132751)]' (**arg(6, 1132751))
hide p1045
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 3', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132752)]' (**arg(7, 1132752))
$ update_portrait('sc048_01 3', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1132753)]' (**arg(8, 1132753))
hide p55
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('uc003_04 2', 'p1051', [l(-14), light, flip], 6)
get_char('c10511') '[convertstrid(1132754)]' (**arg(9, 1132754))
$ update_portrait('uc003_04 3', 'p1051', [l(-14), light, flip], 6)
play sfx2 "other_7007.ogg"
get_char('c10511') '[convertstrid(1132755)]' (**arg(10, 1132755)) with shake
hide p1
$ update_portrait('uc003_04 3', 'p1051', [l(-14), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1132756)]' (**arg(11, 1132756))
hide p1051
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 12', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132757)]' (**arg(12, 1132757))
hide p3
$ update_portrait('uc003_04 2', 'p1045', [l_midback(-14), light, flip], 6)
get_char('c10451') '[convertstrid(1132758)]' (**arg(13, 1132758))
hide p1045
$ update_portrait('uc003_04 3', 'p1051', [l(-14), l_shake, light, flip], 6)
get_char('c10511') '[convertstrid(1132759)]' (**arg(14, 1132759))
$ update_portrait('uc003_04 3', 'p1051', [l(-14), light, flip], 6)
get_char('c10511') '[convertstrid(1132760)]' (**arg(15, 1132760))
$ update_portrait('uc003_04 3', 'p1051', [l_exit(-14), light, flip], 6)
play sfx2 "other_7057.ogg"
get_char('c10511') '[convertstrid(1132761)]' (**arg(16, 1132761)) with shake
hide p1051
hide p2
$ update_portrait('oc003_01 21', 'p3', [r_midback(-6), light], 6)
play sfxvoice "avg_vocal_ro22.ogg"
get_char('c33') '[convertstrid(1132762)]' (**arg(17, 1132762))
$ update_portrait('oc003_01 21', 'p3', [r(-6), dark], 5)
$ update_portrait('sc048_01 3', 'p55', [l_entrance(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132763)]' (**arg(18, 1132763))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132764)]' (**arg(19, 1132764))
hide p3
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r_midback(-3), light], 6)
get_char('c23') '[convertstrid(1132765)]' (**arg(20, 1132765))
hide p2
$ update_portrait('oc001_01 3', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1132766)]' (**arg(21, 1132766))
hide p55
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
play sfx2 "other_7007.ogg"
get_char('c10521') '[convertstrid(1132767)]' (**arg(22, 1132767)) with shake
hide p1
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1132768)]' (**arg(23, 1132768))
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1132769)]' (**arg(24, 1132769))
$ update_portrait('oc003_01 9', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1132770)]' (**arg(25, 1132770))
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
get_char('c10521') '[convertstrid(1132771)]' (**arg(26, 1132771))
get_char('c10521') '[convertstrid(1132772)]' (**arg(27, 1132772))
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1132773)]' (**arg(28, 1132773))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
get_char('c10521') '[convertstrid(1132774)]' (**arg(29, 1132774))
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1132775)]' (**arg(30, 1132775))
hide p3
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132776)]' (**arg(31, 1132776))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c10521') '[convertstrid(1132777)]' (**arg(32, 1132777))
get_char('c10521') '[convertstrid(1132778)]' (**arg(33, 1132778))
hide p1
play sfx2 "other_7088.ogg"
get_char('c0') '[convertstrid(1132779)]' (**arg(34, 1132779))
get_char('c10521') '[convertstrid(1132780)]' (**arg(35, 1132780))
$ update_portrait('oc003_01 9', 'p3', [r_midback(-6), light], 6)
play sfxvoice "avg_vocal_ro15.ogg"
get_char('c33') '[convertstrid(1132781)]' (**arg(36, 1132781))
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
$ update_portrait('uc003_04 3', 'p1045', [l(-14), light, flip], 6)
get_char('c10451') '[convertstrid(1132782)]' (**arg(37, 1132782))
hide p3
$ update_portrait('uc003_04 3', 'p1045', [l(-14), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na09_b.ogg"
get_char('c13') '[convertstrid(1132783)]' (**arg(38, 1132783)) with shake
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('uc003_04 3', 'p1045', [l(-14), light, flip], 6)
get_char('c10451') '[convertstrid(1132784)]' (**arg(39, 1132784))
hide p1045
$ update_portrait('uc003_04 3', 'p1046', [l(-14), light, flip], 6)
get_char('c10461') '[convertstrid(1132785)]' (**arg(40, 1132785))
hide p1
$ update_portrait('uc003_04 3', 'p1046', [l(-14), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r_midback(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1132786)]' (**arg(41, 1132786))
hide p1046
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
get_char('c10521') '[convertstrid(1132787)]' (**arg(42, 1132787))
stop music
hide p2
$ update_portrait('oc004_01 14', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1132788)]' (**arg(43, 1132788))
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
play sfx2 "other_7007.ogg"
get_char('c43') '[convertstrid(1132789)]' (**arg(44, 1132789, size=(1.2))) with shake
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
get_char('c10521') '[convertstrid(1132790)]' (**arg(45, 1132790))
$ play_music("ed7514.ogg")
$ update_portrait('oc004_01 21', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li19.ogg"
get_char('c43') '[convertstrid(1132791)]' (**arg(46, 1132791))
$ update_portrait('oc004_01 20', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1132792)]' (**arg(47, 1132792))
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1132793)]' (**arg(48, 1132793))
$ update_portrait('oc004_01 15', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1132794)]' (**arg(49, 1132794))
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1132795)]' (**arg(50, 1132795))
$ update_portrait('oc004_01 21', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1132796)]' (**arg(51, 1132796))
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1132797)]' (**arg(52, 1132797))
$ update_portrait('oc004_01 9', 'p4', [r_midback(-5), light], 6)
play sfxvoice "avg_vocal_li07.ogg"
get_char('c43') '[convertstrid(1132798)]' (**arg(53, 1132798))
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
get_char('c10521') '[convertstrid(1132799)]' (**arg(54, 1132799))
get_char('c10521') '[convertstrid(1132800)]' (**arg(55, 1132800))
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1132801)]' (**arg(56, 1132801))
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
get_char('c10521') '[convertstrid(1132802)]' (**arg(57, 1132802))
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li18.ogg"
get_char('c43') '[convertstrid(1132803)]' (**arg(58, 1132803))
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1132804)]' (**arg(59, 1132804))
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
get_char('c10521') '[convertstrid(1132805)]' (**arg(60, 1132805))
get_char('c10521') '[convertstrid(1132806)]' (**arg(61, 1132806))
get_char('c10521') '[convertstrid(1132807)]' (**arg(62, 1132807))
hide p4
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1132808)]' (**arg(63, 1132808))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1132809)]' (**arg(64, 1132809))
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro10.ogg"
get_char('c33') '[convertstrid(1132810)]' (**arg(65, 1132810))
hide p2
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
play sfx2 "other_7085.ogg"
get_char('c10481') '[convertstrid(1132811)]' (**arg(66, 1132811))
hide p3
play sfx2 "other_7085.ogg"
get_char('c10553') '[convertstrid(1132812)]' (**arg(67, 1132812))
play sfx2 "other_7085.ogg"
get_char('c10561') '[convertstrid(1132813)]' (**arg(68, 1132813))
$ update_portrait('uc003_04 3', 'p1045', [l(-14), light, flip], 6)
get_char('c10451') '[convertstrid(1132814)]' (**arg(69, 1132814))
hide p1045
$ update_portrait('uc003_04 2', 'p1046', [l(-14), light, flip], 6)
get_char('c10461') '[convertstrid(1132815)]' (**arg(70, 1132815))
hide p1046
$ update_portrait('uc003_04 3', 'p1045', [l(-14), light, flip], 6)
get_char('c10451') '[convertstrid(1132816)]' (**arg(71, 1132816))
$ update_portrait('uc003_04 3', 'p1045', [l(-14), dark, flip], 5)
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1132817)]' (**arg(72, 1132817))
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1132818)]' (**arg(73, 1132818))
$ update_portrait('oc004_01 5', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1132819)]' (**arg(74, 1132819))
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li07.ogg"
get_char('c43') '[convertstrid(1132820)]' (**arg(75, 1132820))
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('uc003_04 3', 'p1045', [l(-14), light, flip], 6)
get_char('c10451') '[convertstrid(1132821)]' (**arg(76, 1132821))
hide p1045
$ update_portrait('uc003_04 1', 'p1046', [l(-14), light, flip], 6)
get_char('c10461') '[convertstrid(1132822)]' (**arg(77, 1132822))
hide p1046
$ update_portrait('uc003_04 3', 'p1045', [l(-14), light, flip], 6)
get_char('c10451') '[convertstrid(1132823)]' (**arg(78, 1132823))
hide p1045
$ update_portrait('uc003_04 1', 'p1046', [l(-14), light, flip], 6)
get_char('c10461') '[convertstrid(1132824)]' (**arg(79, 1132824))
hide p4
$ update_portrait('uc003_04 1', 'p1046', [l(-14), dark, flip], 5)
get_char('c10573') '[convertstrid(1132825)]' (**arg(80, 1132825))
$ update_portrait('st040_01 5', 'p239', [r_entrance(-19), light], 6)
get_char('c2393') '[convertstrid(1132826)]' (**arg(81, 1132826))
$ update_portrait('st040_01 3', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1132827)]' (**arg(82, 1132827))
$ update_portrait('st040_01 6', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1132828)]' (**arg(83, 1132828))
hide p1046
$ update_portrait('st040_01 6', 'p239', [r(-19), dark], 5)
$ update_portrait('sc048_01 3', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132829)]' (**arg(84, 1132829))
hide p239
$ update_portrait('sc048_01 3', 'p55', [l(-7), dark, flip], 5)
get_char('c10573') '[convertstrid(1132830)]' (**arg(85, 1132830))
$ update_portrait('st040_01 5', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1132831)]' (**arg(86, 1132831))
$ update_portrait('st040_01 5', 'p239', [r(-19), dark], 5)
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132832)]' (**arg(87, 1132832))
hide p239
$ update_portrait('sc048_01 1', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro03.ogg"
get_char('c33') '[convertstrid(1132833)]' (**arg(88, 1132833))
hide p3
get_char('c10573') '[convertstrid(1132834)]' (**arg(89, 1132834))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132835)]' (**arg(90, 1132835))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1132836)]' (**arg(91, 1132836))
hide p2
get_char('c10573') '[convertstrid(1132837)]' (**arg(92, 1132837, size=(1.5))) with shake
return