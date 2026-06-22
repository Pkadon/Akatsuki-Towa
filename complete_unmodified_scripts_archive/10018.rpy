label avg10018:

$ play_music("ed7111.ogg")
scene avg_bg_012
$ update_portrait('st051_01 1', 'p552', [l(-9), light, flip], 6)
$ update_narrator('c5521')
window show
with fade_in
play sfx2 "other_7046.ogg"
get_char('c5521') '[convertstrid(1001706)]' (**arg(1, 1001706))
$ update_portrait('st051_01 1', 'p552', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1001707)]' (**arg(2, 1001707))
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001708)]' (**arg(3, 1001708))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('st051_01 1', 'p552', [l(-9), light, flip], 6)
get_char('c5521') '[convertstrid(1001709)]' (**arg(4, 1001709))
hide p2
$ update_portrait('st051_01 1', 'p552', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001710)]' (**arg(5, 1001710))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001711)]' (**arg(6, 1001711))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('st051_01 1', 'p552', [l(-9), light, flip], 6)
get_char('c5521') '[convertstrid(1001712)]' (**arg(7, 1001712))
$ update_portrait('st051_01 1', 'p552', [l(-9), light, flip], 6)
get_char('c5521') '[convertstrid(1001713)]' (**arg(8, 1001713))
hide p2
$ update_portrait('st051_01 1', 'p552', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001714)]' (**arg(9, 1001714))
hide p552
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
get_char('c5531') '[convertstrid(1001715)]' (**arg(10, 1001715))
$ update_portrait('st051_01 1', 'p552', [l(-9), light, flip], 6)
get_char('c5521') '[convertstrid(1001716)]' (**arg(11, 1001716))
hide p552
$ update_portrait('oc003_01 5', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001717)]' (**arg(12, 1001717))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001718)]' (**arg(13, 1001718))
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001719)]' (**arg(14, 1001719))
hide p1
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001720)]' (**arg(15, 1001720))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001721)]' (**arg(16, 1001721))
hide p3
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st051_01 1', 'p709', [l(-9), light, flip], 6)
get_char('c7091') '[convertstrid(1001722)]' (**arg(17, 1001722))
$ update_portrait('st051_01 1', 'p709', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001723)]' (**arg(18, 1001723))
scene avg_bg_047
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
play sfx2 "other_7044.ogg"
get_char('c31') '[convertstrid(1001724)]' (**arg(19, 1001724))
hide p3
$ update_portrait('oc005_01 1', 'p554', [l(-6), light, flip], 6)
play sfx2 "other_7047.ogg"
play sfxvoice "avg_vocal_ji10.ogg"
get_char('c5541') '[convertstrid(1001725)]' (**arg(20, 1001725))
$ update_portrait('oc005_01 1', 'p554', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001726)]' (**arg(21, 1001726))
hide p554
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 16', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji01.ogg"
get_char('c51') '[convertstrid(1001727)]' (**arg(22, 1001727))
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001728)]' (**arg(23, 1001728))
$ update_portrait('oc005_01 1', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1001729)]' (**arg(24, 1001729))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 2', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001730)]' (**arg(25, 1001730))
hide p1
$ update_portrait('oc005_01 2', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001731)]' (**arg(26, 1001731))
hide p5
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001732)]' (**arg(27, 1001732))
hide p3
$ update_portrait('oc005_01 8', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji16.ogg"
get_char('c51') '[convertstrid(1001733)]' (**arg(28, 1001733))
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001734)]' (**arg(29, 1001734))
hide p2
$ update_portrait('oc005_01 1', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001735)]' (**arg(30, 1001735))
hide p1
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001736)]' (**arg(31, 1001736))
hide p5
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001737)]' (**arg(32, 1001737))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001738)]' (**arg(33, 1001738))
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001739)]' (**arg(34, 1001739))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001740)]' (**arg(35, 1001740))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001741)]' (**arg(36, 1001741))
hide p3
$ update_portrait('oc005_01 8', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001742)]' (**arg(37, 1001742))
$ update_portrait('oc005_01 4', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001743)]' (**arg(38, 1001743))
$ update_portrait('oc005_01 16', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001744)]' (**arg(39, 1001744))
$ update_portrait('oc005_01 16', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001745)]' (**arg(40, 1001745))
hide p1
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001746)]' (**arg(41, 1001746))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001747)]' (**arg(42, 1001747))
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001748)]' (**arg(43, 1001748))
hide p5
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001749)]' (**arg(44, 1001749))
hide p3
$ update_portrait('oc005_01 5', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001750)]' (**arg(45, 1001750))
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001751)]' (**arg(46, 1001751))
hide p2
$ update_portrait('oc005_01 1', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001752)]' (**arg(47, 1001752))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001753)]' (**arg(48, 1001753))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc005_01 8', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001754)]' (**arg(49, 1001754))
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001755)]' (**arg(50, 1001755))
hide p5
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001756)]' (**arg(51, 1001756))
hide p2
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001757)]' (**arg(52, 1001757))
hide p1
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001758)]' (**arg(53, 1001758))
hide p3
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001759)]' (**arg(54, 1001759))
$ update_portrait('oc005_01 5', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001760)]' (**arg(55, 1001760))
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001761)]' (**arg(56, 1001761))
hide p5
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001762)]' (**arg(57, 1001762))
hide p3
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001763)]' (**arg(58, 1001763))
$ update_portrait('oc005_01 8', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001764)]' (**arg(59, 1001764))
$ update_portrait('oc005_01 8', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001765)]' (**arg(60, 1001765))
hide p2
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001766)]' (**arg(61, 1001766))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 8', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001767)]' (**arg(62, 1001767))
$ update_portrait('oc005_01 5', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001768)]' (**arg(63, 1001768))
$ update_portrait('oc005_01 5', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1001769)]' (**arg(64, 1001769))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001770)]' (**arg(65, 1001770))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001771)]' (**arg(66, 1001771))
hide p1
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch09.ogg"
get_char('c23') '[convertstrid(1001772)]' (**arg(67, 1001772))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c13') '[convertstrid(1001773)]' (**arg(68, 1001773))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 5', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001774)]' (**arg(69, 1001774))
$ update_portrait('oc005_01 16', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001775)]' (**arg(70, 1001775))
hide p5
hide p1
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1001776)]' (**arg(71, 1001776))
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1001777)]' (**arg(72, 1001777))
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001778)]' (**arg(73, 1001778))
$ update_portrait('oc005_01 5', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1001779)]' (**arg(74, 1001779))
$ update_portrait('oc005_01 5', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1001780)]' (**arg(75, 1001780))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 4', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji05.ogg"
get_char('c51') '[convertstrid(1001781)]' (**arg(76, 1001781))
$ update_portrait('oc005_01 4', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c33') '[convertstrid(1001782)]' (**arg(77, 1001782))
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1001783)]' (**arg(78, 1001783))
hide p5
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001784)]' (**arg(79, 1001784))
hide p3
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001785)]' (**arg(80, 1001785))
return