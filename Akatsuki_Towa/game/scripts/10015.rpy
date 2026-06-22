label avg10015:

$ play_music("ED6200.ogg")
scene avg_bg_010
$ update_narrator('c5301')
$ update_portrait('uc002_03 2', 'p530', [l(-23), light, flip], 6)
window show
with fade_in
$ update_portrait('uc002_03 2', 'p530', [l(-23), l_shake, light, flip], 6)
play sfx2 "other_7057.ogg"
get_char('c5301') '[convertstrid(1001367)]' (**arg(1, 1001367))
hide p530
$ update_portrait('uc002_03 2', 'p531', [l(-23), light, flip], 6)
play sfx2 "fight_6024.ogg"
get_char('c5311') '[convertstrid(1001368)]' (**arg(2, 1001368))
hide p531
$ update_portrait('uc002_03 2', 'p532', [l(-23), light, flip], 6)
play sfx2 "other_7057.ogg"
get_char('c5321') '[convertstrid(1001369)]' (**arg(3, 1001369))
$ update_portrait('uc002_03 2', 'p532', [l(-23), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "bcv_oc002_win_02.ogg"
get_char('c23') '[convertstrid(1001370)]' (**arg(4, 1001370))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001371)]' (**arg(5, 1001371))
hide p1
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1001372)]' (**arg(6, 1001372))
hide p532
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('uc002_03 2', 'p530', [l(-23), l_shake, light, flip], 6)
get_char('c5301') '[convertstrid(1001373)]' (**arg(7, 1001373))
$ update_portrait('uc002_03 2', 'p530', [l(-23), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c33') '[convertstrid(1001374)]' (**arg(8, 1001374))
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('uc002_03 3', 'p530', [l(-23), light, flip], 6)
get_char('c5301') '[convertstrid(1001375)]' (**arg(9, 1001375))
hide p530
$ update_portrait('uc002_03 2', 'p531', [l(-23), light, flip], 6)
get_char('c5311') '[convertstrid(1001376)]' (**arg(10, 1001376))
hide p531
$ update_portrait('uc002_03 4', 'p532', [l(-23), light, flip], 6)
get_char('c5321') '[convertstrid(1001377)]' (**arg(11, 1001377))
hide p3
$ update_portrait('uc002_03 4', 'p532', [l(-23), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001378)]' (**arg(12, 1001378))
hide p532
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001379)]' (**arg(13, 1001379))
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001380)]' (**arg(14, 1001380))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001381)]' (**arg(15, 1001381))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001382)]' (**arg(16, 1001382))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001383)]' (**arg(17, 1001383))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001384)]' (**arg(18, 1001384))
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001385)]' (**arg(19, 1001385))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001386)]' (**arg(20, 1001386))
$ update_portrait('oc003_01 13', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001387)]' (**arg(21, 1001387))
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1001388)]' (**arg(22, 1001388))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001389)]' (**arg(23, 1001389))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('uc002_03 2', 'p530', [l(-23), light, flip], 6)
get_char('c5301') '[convertstrid(1001390)]' (**arg(24, 1001390))
hide p530
$ update_portrait('uc002_03 4', 'p531', [l(-23), light, flip], 6)
get_char('c5311') '[convertstrid(1001391)]' (**arg(25, 1001391))
hide p531
$ update_portrait('uc002_03 2', 'p532', [l(-23), light, flip], 6)
get_char('c5321') '[convertstrid(1001392)]' (**arg(26, 1001392))
$ update_portrait('uc002_03 2', 'p532', [l(-23), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001393)]' (**arg(27, 1001393))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001394)]' (**arg(28, 1001394))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001395)]' (**arg(29, 1001395))
hide p532
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1001396)]' (**arg(30, 1001396))
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001397)]' (**arg(31, 1001397))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001398)]' (**arg(32, 1001398))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001399)]' (**arg(33, 1001399))
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001400)]' (**arg(34, 1001400))
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1001401)]' (**arg(35, 1001401))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfx2 "other_7058.ogg"
get_char('c13') '[convertstrid(1001402)]' (**arg(36, 1001402))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfx2 "other_7017.ogg"
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1001403)]' (**arg(37, 1001403))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001404)]' (**arg(38, 1001404))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001405)]' (**arg(39, 1001405))
hide p3
hide p1
play sfx2 "other_7018.ogg"
get_char('c0') '[convertstrid(1001406)]' (**arg(40, 1001406))
$ update_portrait('sc013_01 1', 'p21', [r_entrance(-12), light], 6)
play sfx2 "other_7046.ogg"
get_char('c213') '[convertstrid(1001407)]' (**arg(41, 1001407))
$ update_portrait('sc013_01 1', 'p21', [r(-12), dark], 5)
$ update_portrait('sc012_01 1', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1001408)]' (**arg(42, 1001408))
hide p21
$ update_portrait('sc012_01 1', 'p20', [l(-16), dark, flip], 5)
$ update_portrait('sc011_01 2', 'p19', [r(-1), light], 6)
get_char('c193') '[convertstrid(1001409)]' (**arg(43, 1001409))
$ update_portrait('sc011_01 4', 'p19', [r(-1), r_shake, light], 6)
get_char('c193') '[convertstrid(1001410)]' (**arg(44, 1001410))
hide p20
$ update_portrait('sc011_01 4', 'p19', [r(-1), dark], 5)
$ update_portrait('sc013_01 2', 'p21', [l(-12), light, flip], 6)
get_char('c211') '[convertstrid(1001411)]' (**arg(45, 1001411))
hide p19
$ update_portrait('sc013_01 2', 'p21', [l(-12), dark, flip], 5)
$ update_portrait('sc012_01 1', 'p20', [r(-16), light], 6)
play sfx2 "other_7058.ogg"
get_char('c203') '[convertstrid(1001412)]' (**arg(46, 1001412))
hide p21
hide p20
play sfx2 "other_7018.ogg"
get_char('c0') '[convertstrid(1001413)]' (**arg(47, 1001413))
$ update_portrait('st007_01 2', 'p207', [l_entrance(-6), light, flip], 6)
play sfx2 "other_7046.ogg"
get_char('c2071') '[convertstrid(1001414)]' (**arg(48, 1001414))
$ update_portrait('st007_01 2', 'p207', [l(-6), dark, flip], 5)
$ update_portrait('st003_01 2', 'p203', [r(-7), light], 6)
get_char('c2033') '[convertstrid(1001415)]' (**arg(49, 1001415))
hide p207
$ update_portrait('st003_01 2', 'p203', [r(-7), dark], 5)
$ update_portrait('st008_01 2', 'p208', [l(-19), light, flip], 6)
get_char('c2081') '[convertstrid(1001416)]' (**arg(50, 1001416))
hide p203
$ update_portrait('st008_01 2', 'p208', [l(-19), dark, flip], 5)
$ update_portrait('oc006_01 2', 'p6', [r(-5), light], 6)
get_char('c63') '[convertstrid(1001417)]' (**arg(51, 1001417))
hide p6
$ update_portrait('sc011_01 2', 'p19', [r(-1), light], 6)
get_char('c193') '[convertstrid(1001418)]' (**arg(52, 1001418))
hide p208
$ update_portrait('sc011_01 2', 'p19', [r(-1), dark], 5)
$ update_portrait('st003_01 2', 'p203', [l(-7), light, flip], 6)
get_char('c2031') '[convertstrid(1001419)]' (**arg(53, 1001419))
hide p19
$ update_portrait('st003_01 2', 'p203', [l(-7), dark, flip], 5)
$ update_portrait('st007_01 2', 'p207', [r(-6), r_shake, light], 6)
get_char('c2073') '[convertstrid(1001420)]' (**arg(54, 1001420))
hide p207
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001421)]' (**arg(55, 1001421))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001422)]' (**arg(56, 1001422))
hide p203
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l_entrance(-5), light, flip], 6)
play sfxvoice "avg_vocal_li03.ogg"
get_char('c41') '[convertstrid(1001423)]' (**arg(57, 1001423))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1001424)]' (**arg(58, 1001424))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1001425)]' (**arg(59, 1001425))
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001426)]' (**arg(60, 1001426))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1001427)]' (**arg(61, 1001427))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1001428)]' (**arg(62, 1001428))
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c33') '[convertstrid(1001429)]' (**arg(63, 1001429))
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1001430)]' (**arg(64, 1001430))
hide p3
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001431)]' (**arg(65, 1001431))
hide p4
hide p2
play sfx2 "other_7060.ogg"
get_char('c0') '[convertstrid(1001432)]' (**arg(66, 1001432))
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1001433)]' (**arg(67, 1001433))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1001434)]' (**arg(68, 1001434))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001435)]' (**arg(69, 1001435))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1001436)]' (**arg(70, 1001436))
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc006_01 1', 'p6', [r(-5), light], 6)
get_char('c63') '[convertstrid(1001437)]' (**arg(71, 1001437))
hide p6
$ update_portrait('sc011_01 2', 'p19', [r(-1), light], 6)
get_char('c193') '[convertstrid(1001438)]' (**arg(72, 1001438))
hide p4
$ update_portrait('sc011_01 2', 'p19', [r(-1), dark], 5)
$ update_portrait('st003_01 2', 'p203', [l(-7), light, flip], 6)
get_char('c2031') '[convertstrid(1001439)]' (**arg(73, 1001439))
hide p203
$ update_portrait('uc002_03 2', 'p530', [l(-23), light, flip], 6)
get_char('c5301') '[convertstrid(1001440)]' (**arg(74, 1001440))
hide p530
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1001441)]' (**arg(75, 1001441))
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1001442)]' (**arg(76, 1001442))
hide p19
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('uc002_03 2', 'p530', [r(-23), r_shake, light], 6)
get_char('c5303') '[convertstrid(1001443)]' (**arg(77, 1001443))
$ update_portrait('uc002_03 2', 'p530', [r(-23), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1001444)]' (**arg(78, 1001444))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1001445)]' (**arg(79, 1001445))
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1001446)]' (**arg(80, 1001446))
hide p530
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('uc002_03 4', 'p531', [r(-23), light], 6)
get_char('c5313') '[convertstrid(1001447)]' (**arg(81, 1001447))
$ update_portrait('uc002_03 4', 'p531', [r(-23), dark], 5)
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li28.ogg"
get_char('c41') '[convertstrid(1001448)]' (**arg(82, 1001448))
hide p531
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('uc002_03 4', 'p532', [r(-23), light], 6)
get_char('c5323') '[convertstrid(1001449)]' (**arg(83, 1001449))
$ update_portrait('uc002_03 4', 'p532', [r(-23), dark], 5)
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1001450)]' (**arg(84, 1001450))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1001451)]' (**arg(85, 1001451))
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1001452)]' (**arg(86, 1001452))
hide p532
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('uc002_03 4', 'p530', [r(-23), light], 6)
get_char('c5303') '[convertstrid(1001453)]' (**arg(87, 1001453))
hide p4
$ update_portrait('uc002_03 4', 'p530', [r(-23), dark], 5)
$ update_portrait('sc011_01 2', 'p19', [l_entrance(-1), light, flip], 6)
get_char('c191') '[convertstrid(1001454)]' (**arg(88, 1001454))
$ update_portrait('sc011_01 4', 'p19', [l(-1), l_shake, light, flip], 6)
get_char('c191') '[convertstrid(1001455)]' (**arg(89, 1001455))
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
get_char('c191') '[convertstrid(1001456)]' (**arg(90, 1001456))
hide p530
$ update_portrait('sc011_01 4', 'p19', [l(-1), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001457)]' (**arg(91, 1001457))
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001458)]' (**arg(92, 1001458))
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('sc011_01 2', 'p19', [l(-1), light, flip], 6)
get_char('c191') '[convertstrid(1001459)]' (**arg(93, 1001459))
$ update_portrait('sc011_01 2', 'p19', [l(-1), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001460)]' (**arg(94, 1001460))
hide p19
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('sc013_01 2', 'p21', [l(-12), light, flip], 6)
get_char('c211') '[convertstrid(1001461)]' (**arg(95, 1001461))
$ update_portrait('sc013_01 2', 'p21', [l(-12), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001462)]' (**arg(96, 1001462))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001463)]' (**arg(97, 1001463))
hide p21
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001464)]' (**arg(98, 1001464))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001465)]' (**arg(99, 1001465))
hide p2
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c11') '[convertstrid(1001466)]' (**arg(100, 1001466))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 5', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li06.ogg"
get_char('c43') '[convertstrid(1001467)]' (**arg(101, 1001467))
hide p1
$ update_portrait('oc004_01 5', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001468)]' (**arg(102, 1001468, size=(1.2))) with shake
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001469)]' (**arg(103, 1001469))
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001470)]' (**arg(104, 1001470))
hide p2
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('st007_01 5', 'p207', [l(-6), light, flip], 6)
get_char('c2071') '[convertstrid(1001471)]' (**arg(105, 1001471))
hide p4
$ update_portrait('st007_01 5', 'p207', [l(-6), dark, flip], 5)
$ update_portrait('st003_01 1', 'p203', [r(-7), light], 6)
get_char('c2033') '[convertstrid(1001472)]' (**arg(106, 1001472))
hide p207
$ update_portrait('st003_01 1', 'p203', [r(-7), dark], 5)
$ update_portrait('st008_01 1', 'p208', [l(-19), l_shake, light, flip], 6)
get_char('c2081') '[convertstrid(1001473)]' (**arg(107, 1001473))
hide p208
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001474)]' (**arg(108, 1001474))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001475)]' (**arg(109, 1001475))
hide p203
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001476)]' (**arg(110, 1001476))
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001477)]' (**arg(111, 1001477))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001478)]' (**arg(112, 1001478))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 10', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001479)]' (**arg(113, 1001479))
$ update_portrait('oc003_01 10', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001480)]' (**arg(114, 1001480))
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li07.ogg"
get_char('c43') '[convertstrid(1001481)]' (**arg(115, 1001481))
hide p3
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1001482)]' (**arg(116, 1001482))
hide p4
$ update_portrait('oc006_01 4', 'p6', [l(-5), dark, flip], 5)
$ update_portrait('sc013_01 2', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001483)]' (**arg(117, 1001483))
hide p6
$ update_portrait('sc013_01 2', 'p21', [r(-12), dark], 5)
$ update_portrait('st008_01 4', 'p208', [l(-19), light, flip], 6)
get_char('c2081') '[convertstrid(1001484)]' (**arg(118, 1001484))
hide p208
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1001485)]' (**arg(119, 1001485))
hide p21
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001486)]' (**arg(120, 1001486))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001487)]' (**arg(121, 1001487))
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001488)]' (**arg(122, 1001488))
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001489)]' (**arg(123, 1001489))
hide p2
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('sc011_01 2', 'p19', [l(-1), light, flip], 6)
get_char('c191') '[convertstrid(1001490)]' (**arg(124, 1001490))
$ update_portrait('sc011_01 2', 'p19', [l(-1), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001491)]' (**arg(125, 1001491))
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001492)]' (**arg(126, 1001492))
$ update_portrait('oc004_01 18', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001493)]' (**arg(127, 1001493))
$ update_portrait('oc004_01 14', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001494)]' (**arg(128, 1001494))
hide p19
$ update_portrait('oc004_01 14', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch14.ogg"
get_char('c21') '[convertstrid(1001495)]' (**arg(129, 1001495))
hide p4
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001496)]' (**arg(130, 1001496))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc012_01 4', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1001497)]' (**arg(131, 1001497))
hide p1
$ update_portrait('sc012_01 4', 'p20', [l(-16), dark, flip], 5)
$ update_portrait('sc011_01 2', 'p19', [r(-1), r_shake, light], 6)
get_char('c193') '[convertstrid(1001498)]' (**arg(132, 1001498))
hide p20
$ update_portrait('sc011_01 2', 'p19', [r(-1), dark], 5)
$ update_portrait('st008_01 2', 'p208', [l_entrance(-19), light, flip], 6)
get_char('c2081') '[convertstrid(1001499)]' (**arg(133, 1001499))
hide p19
$ update_portrait('st008_01 2', 'p208', [l(-19), dark, flip], 5)
$ update_portrait('st003_01 1', 'p203', [r(-7), light], 6)
get_char('c2033') '[convertstrid(1001500)]' (**arg(134, 1001500))
hide p203
$ update_portrait('uc002_03 4', 'p530', [r(-23), light], 6)
get_char('c5303') '[convertstrid(1001501)]' (**arg(135, 1001501))
hide p530
$ update_portrait('uc002_03 2', 'p531', [r(-23), r_shake, light], 6)
get_char('c5313') '[convertstrid(1001502)]' (**arg(136, 1001502))
hide p531
$ update_portrait('uc002_03 4', 'p532', [r(-23), light], 6)
get_char('c5323') '[convertstrid(1001503)]' (**arg(137, 1001503))
hide p208
$ update_portrait('uc002_03 4', 'p532', [r(-23), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001504)]' (**arg(138, 1001504))
hide p532
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001505)]' (**arg(139, 1001505))
hide p1
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1001506)]' (**arg(140, 1001506))
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001507)]' (**arg(141, 1001507))
$ update_portrait('oc004_01 22', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001508)]' (**arg(142, 1001508))
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001509)]' (**arg(143, 1001509))
hide p3
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001510)]' (**arg(144, 1001510))
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001511)]' (**arg(145, 1001511))
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c21') '[convertstrid(1001512)]' (**arg(146, 1001512))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001513)]' (**arg(147, 1001513))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001514)]' (**arg(148, 1001514))
$ update_portrait('oc003_01 8', 'p3', [l(-6), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1001515)]' (**arg(149, 1001515))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001516)]' (**arg(150, 1001516))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001517)]' (**arg(151, 1001517))
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li03.ogg"
get_char('c43') '[convertstrid(1001518)]' (**arg(152, 1001518))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001519)]' (**arg(153, 1001519))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 5', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001520)]' (**arg(154, 1001520))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1001521)]' (**arg(155, 1001521))
return