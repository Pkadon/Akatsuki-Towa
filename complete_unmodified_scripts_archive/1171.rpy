label avg1171(trans=fade_in):

$ play_music("ED6103.ogg")
scene avg_bg_035
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(2105308)]' (**arg(1, 2105308))
$ update_portrait('oc001_01 12', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7047.ogg"
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(2105309)]' (**arg(2, 2105309))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), l_shake, light, flip], 6)
get_char('c151') '[convertstrid(2105310)]' (**arg(3, 2105310))
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105311)]' (**arg(4, 2105311))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 3', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105312)]' (**arg(5, 2105312))
$ update_portrait('sc007_01 3', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105313)]' (**arg(6, 2105313))
hide p15
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st025_01 1', 'p224', [l(-17), light, flip], 6)
get_char('c2241') '[convertstrid(2105314)]' (**arg(7, 2105314))
$ update_portrait('st025_01 1', 'p224', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105315)]' (**arg(8, 2105315))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st025_01 1', 'p224', [l(-17), light, flip], 6)
get_char('c2241') '[convertstrid(2105316)]' (**arg(9, 2105316))
hide p224
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105317)]' (**arg(10, 2105317))
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105318)]' (**arg(11, 2105318))
hide p15
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st044_01 5', 'p692', [l(10), light, flip], 6)
get_char('c6921') '[convertstrid(2105319)]' (**arg(12, 2105319))
$ update_portrait('st044_01 1', 'p692', [l(10), light, flip], 6)
get_char('c6921') '[convertstrid(2105320)]' (**arg(13, 2105320))
hide p1
$ update_portrait('st044_01 1', 'p692', [l(10), dark, flip], 5)
$ update_portrait('st025_01 4', 'p224', [r(-17), r_shake, light], 6)
get_char('c2243') '[convertstrid(2105321)]' (**arg(14, 2105321))
hide p224
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(2105322)]' (**arg(15, 2105322))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfx2 "fight_6008.ogg"
get_char('c13') '[convertstrid(2105323)]' (**arg(16, 2105323)) with shake
hide p692
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 3', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105324)]' (**arg(17, 2105324))
hide p15
$ update_portrait('st025_01 4', 'p224', [l(-17), light, flip], 6)
get_char('c2241') '[convertstrid(2105325)]' (**arg(18, 2105325))
$ update_portrait('st025_01 4', 'p224', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105326)]' (**arg(19, 2105326))
hide p224
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 2', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105327)]' (**arg(20, 2105327))
$ update_portrait('sc007_01 2', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04.ogg"
get_char('c13') '[convertstrid(2105328)]' (**arg(21, 2105328))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "fight_6008.ogg"
get_char('c13') '[convertstrid(2105329)]' (**arg(22, 2105329)) with shake
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105330)]' (**arg(23, 2105330))
hide p15
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st044_01 4', 'p692', [l(10), light, flip], 6)
get_char('c6921') '[convertstrid(2105331)]' (**arg(24, 2105331))
hide p1
$ update_portrait('st044_01 4', 'p692', [l(10), dark, flip], 5)
$ update_portrait('st025_01 4', 'p224', [r(-17), light], 6)
get_char('c2243') '[convertstrid(2105332)]' (**arg(25, 2105332))
hide p692
$ update_portrait('st025_01 4', 'p224', [r(-17), dark], 5)
$ update_portrait('sc007_01 3', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105333)]' (**arg(26, 2105333))
$ play_music("ed7516.ogg")
hide p224
$ update_portrait('sc007_01 3', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105334)]' (**arg(27, 2105334))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105335)]' (**arg(28, 2105335))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(2105336)]' (**arg(29, 2105336))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 2', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105337)]' (**arg(30, 2105337))
$ update_portrait('sc007_01 2', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105338)]' (**arg(31, 2105338))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfx2 "other_7052.ogg"
get_char('c13') '[convertstrid(2105339)]' (**arg(32, 2105339)) with shake
hide p15
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('st044_01 1', 'p692', [l(10), light, flip], 6)
get_char('c6921') '[convertstrid(2105340)]' (**arg(33, 2105340))
hide p1
$ update_portrait('st044_01 1', 'p692', [l(10), dark, flip], 5)
$ update_portrait('sc007_01 3', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(2105341)]' (**arg(34, 2105341))
$ update_portrait('sc007_01 2', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(2105342)]' (**arg(35, 2105342))
$ update_portrait('sc007_01 4', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(2105343)]' (**arg(36, 2105343))
hide p15
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(2105344)]' (**arg(37, 2105344))
hide p692
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 3', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105345)]' (**arg(38, 2105345))
$ update_portrait('sc007_01 3', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105346)]' (**arg(39, 2105346))
$ update_portrait('sc007_01 3', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105347)]' (**arg(40, 2105347))
$ update_portrait('sc007_01 3', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105348)]' (**arg(41, 2105348))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105349)]' (**arg(42, 2105349))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105350)]' (**arg(43, 2105350))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105351)]' (**arg(44, 2105351))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 2', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105352)]' (**arg(45, 2105352))
$ update_portrait('sc007_01 2', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105353)]' (**arg(46, 2105353))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105354)]' (**arg(47, 2105354))
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c13') '[convertstrid(2105355)]' (**arg(48, 2105355))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 2', 'p15', [l(-17), l_shake, light, flip], 6)
get_char('c151') '[convertstrid(2105356)]' (**arg(49, 2105356))
$ update_portrait('sc007_01 2', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105357)]' (**arg(50, 2105357))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 2', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105358)]' (**arg(51, 2105358))
$ update_portrait('sc007_01 2', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105359)]' (**arg(52, 2105359))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 5', 'p15', [l(-17), l_shake, light, flip], 6)
get_char('c151') '[convertstrid(2105360)]' (**arg(53, 2105360))
hide p15
$ update_portrait('st044_01 2', 'p692', [l(10), light, flip], 6)
get_char('c6921') '[convertstrid(2105361)]' (**arg(54, 2105361))
$ update_portrait('st044_01 2', 'p692', [l(10), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105362)]' (**arg(55, 2105362))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st044_01 1', 'p692', [l(10), light, flip], 6)
get_char('c6921') '[convertstrid(2105363)]' (**arg(56, 2105363))
hide p1
$ update_portrait('st044_01 1', 'p692', [l(10), dark, flip], 5)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(2105364)]' (**arg(57, 2105364))
hide p15
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105365)]' (**arg(58, 2105365))
hide p692
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st025_01 5', 'p224', [l(-17), light, flip], 6)
get_char('c2241') '[convertstrid(2105366)]' (**arg(59, 2105366))
scene avg_bg_070
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(2105367)]' (**arg(60, 2105367))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105368)]' (**arg(61, 2105368))
$ play_music("ED6103.ogg")
scene avg_bg_035
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
$ update_narrator('c151')
with fade
get_char('c151') '[convertstrid(2105369)]' (**arg(62, 2105369))
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105370)]' (**arg(63, 2105370))
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105371)]' (**arg(64, 2105371))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105372)]' (**arg(65, 2105372))
hide p15
play sfx2 "other_7034.ogg"
get_char('c25331') '[convertstrid(2105373)]' (**arg(66, 2105373))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(2105374)]' (**arg(67, 2105374))
scene avg_bg_070
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(2105375)]' (**arg(68, 2105375))
scene avg_bg_037
$ update_portrait('st025_01 1', 'p224', [l(-17), light, flip], 6)
$ update_narrator('c2241')
with fade
get_char('c2241') '[convertstrid(2105376)]' (**arg(69, 2105376))
$ play_music("ed7511.ogg")
hide p224
play sfx2 "other_7034.ogg"
get_char('c25331') '[convertstrid(2105377)]' (**arg(70, 2105377))
$ update_portrait('oc001_01 4', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(2105378)]' (**arg(71, 2105378))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 4', 'p15', [l(-17), l_shake, light, flip], 6)
get_char('c151') '[convertstrid(2105379)]' (**arg(72, 2105379))
$ play_music("ED6103.ogg")
scene avg_bg_070
$ update_narrator('c0')
with fade
play sfx2 "fight_6009.ogg"
get_char('c0') '[convertstrid(2105380)]' (**arg(73, 2105380))
scene avg_bg_037
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
play sfx2 "fight_6027.ogg"
play sfxvoice "avg_vocal_na03_b.ogg"
get_char('c13') '[convertstrid(2105381)]' (**arg(74, 2105381))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105382)]' (**arg(75, 2105382))
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105383)]' (**arg(76, 2105383))
hide p15
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st044_01 1', 'p692', [l(10), light, flip], 6)
get_char('c6921') '[convertstrid(2105384)]' (**arg(77, 2105384))
scene avg_bg_035
$ update_portrait('st025_01 1', 'p224', [r(-17), light], 6)
$ update_narrator('c2243')
with fade
get_char('c2243') '[convertstrid(2105385)]' (**arg(78, 2105385))
$ update_portrait('st025_01 1', 'p224', [r(-17), dark], 5)
$ update_portrait('st044_01 1', 'p692', [l(10), light, flip], 6)
get_char('c6921') '[convertstrid(2105386)]' (**arg(79, 2105386))
$ update_portrait('st044_01 1', 'p692', [l(10), dark, flip], 5)
$ update_portrait('st025_01 1', 'p224', [r(-17), light], 6)
get_char('c2243') '[convertstrid(2105387)]' (**arg(80, 2105387))
hide p692
$ update_portrait('st025_01 1', 'p224', [r(-17), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105388)]' (**arg(81, 2105388))
$ play_music("ed7514.ogg")
scene avg_bg_037
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
$ update_narrator('c151')
with fade
get_char('c151') '[convertstrid(2105389)]' (**arg(82, 2105389))
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2105390)]' (**arg(83, 2105390))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105391)]' (**arg(84, 2105391))
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105392)]' (**arg(85, 2105392))
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na16.ogg"
get_char('c13') '[convertstrid(2105393)]' (**arg(86, 2105393))
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 5', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(2105394)]' (**arg(87, 2105394))
return "avg1171"