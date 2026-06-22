label avg10315:

$ play_music("ed7150.ogg")
scene avg_bg_022
$ update_narrator('c23')
window show
with fade_in
$ update_portrait('oc002_01 2', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1130321)]' (**arg(1, 1130321))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc053_01 2', 'p60', [l(-32), light, flip], 6)
play sfx2 "other_7064.ogg"
get_char('c601') '[convertstrid(1130322)]' (**arg(2, 1130322))
hide p60
hide p2
$ update_narrator('c10081')
with fade
play sfx2 "fight_6010.ogg"
get_char('c10081') '[convertstrid(1130323)]' (**arg(3, 1130323))
$ update_portrait('sc052_01 4', 'p59', [r(-25), light], 6)
get_char('c593') '[convertstrid(1130324)]' (**arg(4, 1130324))
$ update_portrait('sc052_01 4', 'p59', [r(-25), dark], 5)
get_char('c10091') '[convertstrid(1130325)]' (**arg(5, 1130325))
get_char('c10101') '[convertstrid(1130326)]' (**arg(6, 1130326))
hide p59
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130327)]' (**arg(7, 1130327))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130328)]' (**arg(8, 1130328))
hide p3
$ update_portrait('sc053_01 4', 'p60', [l_entrance(-32), light, flip], 6)
get_char('c601') '[convertstrid(1130329)]' (**arg(9, 1130329))
hide p1
$ update_portrait('sc053_01 4', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130330)]' (**arg(10, 1130330))
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1130331)]' (**arg(11, 1130331))
$ update_portrait('sc053_01 4', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130332)]' (**arg(12, 1130332))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130333)]' (**arg(13, 1130333))
hide p60
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130334)]' (**arg(14, 1130334))
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 12', 'p4', [r(-5), r_shake, light], 6)
play sfxvoice "avg_vocal_li31.ogg"
get_char('c43') '[convertstrid(1130335)]' (**arg(15, 1130335))
$ update_portrait('oc004_01 5', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130336)]' (**arg(16, 1130336))
hide p3
$ update_portrait('oc004_01 5', 'p4', [r(-5), dark], 5)
get_char('c10101') '[convertstrid(1130337)]' (**arg(17, 1130337))
get_char('c10081') '[convertstrid(1130338)]' (**arg(18, 1130338))
get_char('c10091') '[convertstrid(1130339)]' (**arg(19, 1130339))
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130340)]' (**arg(20, 1130340))
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li28.ogg"
get_char('c43') '[convertstrid(1130341)]' (**arg(21, 1130341))
$ update_portrait('oc004_01 10', 'p4', [r(-5), dark], 5)
get_char('c10101') '[convertstrid(1130342)]' (**arg(22, 1130342))
get_char('c10081') '[convertstrid(1130343)]' (**arg(23, 1130343))
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130344)]' (**arg(24, 1130344))
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
get_char('c10081') '[convertstrid(1130345)]' (**arg(25, 1130345))
get_char('c10091') '[convertstrid(1130346)]' (**arg(26, 1130346))
get_char('c10101') '[convertstrid(1130347)]' (**arg(27, 1130347))
get_char('c10081') '[convertstrid(1130348)]' (**arg(28, 1130348))
get_char('c10091') '[convertstrid(1130349)]' (**arg(29, 1130349))
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130350)]' (**arg(30, 1130350))
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130351)]' (**arg(31, 1130351, size=(1.6))) with shake
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
get_char('c10091') '[convertstrid(1130352)]' (**arg(32, 1130352))
$ update_portrait('oc004_01 14', 'p4', [r(-5), r_shake, light], 6)
get_char('c43') '[convertstrid(1130353)]' (**arg(33, 1130353))
$ update_portrait('oc004_01 14', 'p4', [r(-5), dark], 5)
get_char('c10101') '[convertstrid(1130354)]' (**arg(34, 1130354))
get_char('c10081') '[convertstrid(1130355)]' (**arg(35, 1130355))
hide p4
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130356)]' (**arg(36, 1130356))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130357)]' (**arg(37, 1130357))
hide p2
hide p1
$ update_narrator('c10091')
with fade
get_char('c10091') '[convertstrid(1130358)]' (**arg(38, 1130358))
$ update_portrait('oc002_01 22', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1130359)]' (**arg(39, 1130359))
$ update_portrait('oc002_01 22', 'p2', [r(-3), dark], 5)
get_char('c10091') '[convertstrid(1130360)]' (**arg(40, 1130360))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130361)]' (**arg(41, 1130361))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c10091') '[convertstrid(1130362)]' (**arg(42, 1130362))
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch04.ogg"
get_char('c23') '[convertstrid(1130363)]' (**arg(43, 1130363))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130364)]' (**arg(44, 1130364))
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1130365)]' (**arg(45, 1130365))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
get_char('c10091') '[convertstrid(1130366)]' (**arg(46, 1130366))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130367)]' (**arg(47, 1130367))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c10091') '[convertstrid(1130368)]' (**arg(48, 1130368))
hide p2
$ update_portrait('sc052_01 5', 'p59', [r(-25), light], 6)
play sfx2 "common_35rewardholy.ogg"
get_char('c593') '[convertstrid(1130369)]' (**arg(49, 1130369))
hide p59
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1130370)]' (**arg(50, 1130370))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130371)]' (**arg(51, 1130371))
hide p3
$ update_portrait('sc053_01 5', 'p60', [l_entrance(-32), light, flip], 6)
get_char('c601') '[convertstrid(1130372)]' (**arg(52, 1130372))
hide p60
$ update_portrait('sc052_01 5', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(1130373)]' (**arg(53, 1130373))
$ update_portrait('sc052_01 5', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130374)]' (**arg(54, 1130374))
hide p59
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc053_01 1', 'p60', [l_entrance(-32), light, flip], 6)
get_char('c601') '[convertstrid(1130375)]' (**arg(55, 1130375))
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1130376)]' (**arg(56, 1130376))
hide p60
$ update_portrait('sc052_01 2', 'p59', [l(-25), l_shake, light, flip], 6)
get_char('c591') '[convertstrid(1130377)]' (**arg(57, 1130377, size=(1.2)))
hide p1
$ update_portrait('sc052_01 2', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc004_01 23', 'p4', [r(-5), r_shake, light], 6)
get_char('c43') '[convertstrid(1130378)]' (**arg(58, 1130378))
$ update_portrait('oc004_01 24', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li09.ogg"
get_char('c43') '[convertstrid(1130379)]' (**arg(59, 1130379))
$ update_portrait('oc004_01 24', 'p4', [r(-5), dark], 5)
$ update_portrait('sc052_01 5', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(1130380)]' (**arg(60, 1130380))
$ update_portrait('sc052_01 6', 'p59', [l_midback(-25), light, flip], 6)
get_char('c591') '[convertstrid(1130381)]' (**arg(61, 1130381))
hide p59
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1130382)]' (**arg(62, 1130382))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130383)]' (**arg(63, 1130383))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1130384)]' (**arg(64, 1130384))
$ update_portrait('sc053_01 1', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130385)]' (**arg(65, 1130385))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1130386)]' (**arg(66, 1130386))
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1130387)]' (**arg(67, 1130387))
hide p1
$ update_portrait('sc053_01 1', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130388)]' (**arg(68, 1130388))
hide p60
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc052_01 5', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(1130389)]' (**arg(69, 1130389))
hide p59
hide p2
$ update_portrait('oc004_01 13', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
with fade
get_char('c41') '[convertstrid(1130390)]' (**arg(70, 1130390))
$ update_portrait('oc004_01 13', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130391)]' (**arg(71, 1130391))
hide p4
hide p1
$ update_narrator('c591')
$ update_portrait('sc052_01 5', 'p59', [l(-25), light, flip], 6)
with fade
$ update_portrait('sc052_01 5', 'p59', [l_midback(-25), light, flip], 6)
get_char('c591') '[convertstrid(1130392)]' (**arg(72, 1130392))
$ update_portrait('sc052_01 5', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc004_01 23', 'p4', [r(-5), r_shake, light], 6)
play sfxvoice "avg_vocal_li08.ogg"
get_char('c43') '[convertstrid(1130393)]' (**arg(73, 1130393))
$ update_portrait('oc004_01 15', 'p4', [r_exit(-5), light], 6)
get_char('c43') '[convertstrid(1130394)]' (**arg(74, 1130394))
hide p4
$ update_portrait('oc003_01 6', 'p3', [r_entrance(-6), light], 6)
play sfx2 "other_7086.ogg"
get_char('c33') '[convertstrid(1130395)]' (**arg(75, 1130395))
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130396)]' (**arg(76, 1130396))
hide p1
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130397)]' (**arg(77, 1130397))
hide p59
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1130398)]' (**arg(78, 1130398))
hide p60
$ update_portrait('sc052_01 2', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(1130399)]' (**arg(79, 1130399))
return