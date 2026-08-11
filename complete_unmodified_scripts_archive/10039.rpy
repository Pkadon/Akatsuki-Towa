label avg10039(trans=fade_in):

$ play_music("ed7511.ogg")
scene avg_bg_034
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
play sfx2 "fight_6022.ogg"
play sfxvoice "bcv_oc001_c03_01.ogg"
get_char('c11') '[convertstrid(1003378)]' (**arg(1, 1003378))
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st012_01 2', 'p211', [r(-6), r_shake, light], 6)
get_char('c2113') '[convertstrid(1003379)]' (**arg(2, 1003379))
hide p1
$ update_portrait('st012_01 2', 'p211', [r(-6), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l_midback(-3), light, flip], 6)
play sfx2 "fight_6019.ogg"
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c21') '[convertstrid(1003380)]' (**arg(3, 1003380))
hide p211
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r_midback(-6), light], 6)
play sfx2 "fight_6010.ogg"
play sfxvoice "avg_vocal_ro06.ogg"
get_char('c33') '[convertstrid(1003381)]' (**arg(4, 1003381))
hide p2
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1003382)]' (**arg(5, 1003382))
hide p3
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003383)]' (**arg(6, 1003383))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st012_01 1', 'p211', [l(-6), l_shake, light, flip], 6)
get_char('c2111') '[convertstrid(1003384)]' (**arg(7, 1003384))
$ update_portrait('st012_01 1', 'p211', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003385)]' (**arg(8, 1003385))
hide p211
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
get_char('c6161') '[convertstrid(1003386)]' (**arg(9, 1003386))
$ update_portrait('oc003_01 6', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1003387)]' (**arg(10, 1003387))
hide p1
$ update_portrait('oc003_01 6', 'p3', [l(-6), dark, flip], 5)
get_char('c6173') '[convertstrid(1003388)]' (**arg(11, 1003388))
hide p3
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003389)]' (**arg(12, 1003389))
hide p2
get_char('c6181') '[convertstrid(1003390)]' (**arg(13, 1003390))
$ update_portrait('oc004_01 16', 'p4', [r(-5), r_shake, light], 6)
get_char('c43') '[convertstrid(1003391)]' (**arg(14, 1003391))
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
get_char('c6191') '[convertstrid(1003392)]' (**arg(15, 1003392))
hide p4
get_char('c6203') '[convertstrid(1003393)]' (**arg(16, 1003393))
$ update_portrait('oc003_01 3', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro16.ogg"
get_char('c31') '[convertstrid(1003394)]' (**arg(17, 1003394))
$ update_portrait('oc003_01 3', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003395)]' (**arg(18, 1003395))
hide p3
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('st012_01 1', 'p211', [l(-6), light, flip], 6)
get_char('c2111') '[convertstrid(1003396)]' (**arg(19, 1003396))
$ update_portrait('st012_01 1', 'p211', [l(-6), light, flip], 6)
get_char('c2111') '[convertstrid(1003397)]' (**arg(20, 1003397))
$ update_portrait('st012_01 1', 'p211', [l(-6), light, flip], 6)
get_char('c2111') '[convertstrid(1003398)]' (**arg(21, 1003398))
$ update_portrait('st012_01 1', 'p211', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003399)]' (**arg(22, 1003399))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('st012_01 1', 'p211', [l(-6), light, flip], 6)
get_char('c2111') '[convertstrid(1003400)]' (**arg(23, 1003400))
$ update_portrait('st012_01 1', 'p211', [l(-6), light, flip], 6)
get_char('c2111') '[convertstrid(1003401)]' (**arg(24, 1003401))
$ update_portrait('st012_01 5', 'p211', [l(-6), light, flip], 6)
get_char('c2111') '[convertstrid(1003402)]' (**arg(25, 1003402)) with shake
hide p1
$ update_portrait('st012_01 5', 'p211', [l(-6), dark, flip], 5)
$ update_portrait('uc003_01 4', 'p506', [r(-26), light], 6)
get_char('c5063') '[convertstrid(1003403)]' (**arg(26, 1003403))
hide p506
$ update_portrait('uc003_01 4', 'p507', [r(-26), light], 6)
get_char('c5073') '[convertstrid(1003404)]' (**arg(27, 1003404))
hide p211
$ update_portrait('uc003_01 4', 'p507', [r(-26), dark], 5)
$ update_portrait('oc003_01 3', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro18.ogg"
get_char('c31') '[convertstrid(1003405)]' (**arg(28, 1003405))
hide p507
$ update_portrait('oc003_01 3', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li26.ogg"
get_char('c43') '[convertstrid(1003406)]' (**arg(29, 1003406))
hide p4
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003407)]' (**arg(30, 1003407))
hide p1
$ update_portrait('st012_01 5', 'p211', [r(-6), r_shake, light], 6)
get_char('c2113') '[convertstrid(1003408)]' (**arg(31, 1003408))
stop music
hide p211
get_char('c6213') '[convertstrid(1003409)]' (**arg(32, 1003409))
hide p3
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c11') '[convertstrid(1003410)]' (**arg(33, 1003410))
hide p1
play sfx2 "other_7064.ogg"
get_char('c0') '[convertstrid(1003411)]' (**arg(34, 1003411))
$ update_portrait('st012_01 2', 'p211', [r(-6), light], 6)
get_char('c2113') '[convertstrid(1003412)]' (**arg(35, 1003412))
$ update_portrait('st012_01 2', 'p211', [r(-6), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003413)]' (**arg(36, 1003413))
hide p211
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003414)]' (**arg(37, 1003414))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c6071') '[convertstrid(1003415)]' (**arg(38, 1003415))
$ play_music("ED6523.ogg")
$ update_portrait('sc025_01 4', 'p622', [l(-1), light, flip], 6)
get_char('c6221') '[convertstrid(1003416)]' (**arg(39, 1003416))
hide p1
$ update_portrait('sc025_01 4', 'p622', [l(-1), dark, flip], 5)
$ update_portrait('uc004_02 4', 'p623', [r(-9), light], 6)
play sfx2 "common_wheel.ogg"
get_char('c6233') '[convertstrid(1003417)]' (**arg(40, 1003417)) with shake
hide p623
$ update_portrait('st012_01 2', 'p211', [r(-6), r_shake, light], 6)
get_char('c2113') '[convertstrid(1003418)]' (**arg(41, 1003418))
hide p622
$ update_portrait('st012_01 2', 'p211', [r(-6), dark], 5)
get_char('c6091') '[convertstrid(1003419)]' (**arg(42, 1003419))
$ update_portrait('sc017_01 4', 'p571', [l(-7), light, flip], 6)
get_char('c5711') '[convertstrid(1003420)]' (**arg(43, 1003420))
hide p211
$ update_portrait('sc017_01 4', 'p571', [l(-7), dark, flip], 5)
play sfx2 "fight_6024.ogg"
get_char('c6243') '[convertstrid(1003421)]' (**arg(44, 1003421)) with shake
$ update_portrait('uc004_02 2', 'p625', [r(-9), light], 6)
get_char('c6253') '[convertstrid(1003422)]' (**arg(45, 1003422))
hide p571
$ update_portrait('uc004_02 2', 'p625', [r(-9), dark], 5)
$ update_portrait('uc003_01 1', 'p583', [l(-26), light, flip], 6)
get_char('c5831') '[convertstrid(1003423)]' (**arg(46, 1003423))
hide p583
$ update_portrait('uc003_01 1', 'p584', [l(-26), light, flip], 6)
get_char('c5841') '[convertstrid(1003424)]' (**arg(47, 1003424))
hide p584
$ update_portrait('uc003_01 4', 'p585', [l(-26), light, flip], 6)
get_char('c5851') '[convertstrid(1003425)]' (**arg(48, 1003425))
hide p585
$ update_portrait('uc003_01 1', 'p627', [l(-26), light, flip], 6)
get_char('c6271') '[convertstrid(1003426)]' (**arg(49, 1003426))
hide p625
$ update_portrait('uc003_01 1', 'p627', [l(-26), dark, flip], 5)
$ update_portrait('st013_01 4', 'p212', [r(-16), light], 6)
play sfx2 "fight_6025.ogg"
get_char('c2123') '[convertstrid(1003427)]' (**arg(50, 1003427))
$ update_portrait('st013_01 4', 'p212', [r(-16), dark], 5)
$ update_portrait('uc003_01 1', 'p627', [l(-26), light, flip], 6)
get_char('c6271') '[convertstrid(1003428)]' (**arg(51, 1003428))
hide p627
$ update_portrait('uc003_01 1', 'p628', [l(-26), light, flip], 6)
get_char('c6281') '[convertstrid(1003429)]' (**arg(52, 1003429))
hide p628
$ update_portrait('sc025_01 4', 'p622', [l(-1), light, flip], 6)
get_char('c6221') '[convertstrid(1003430)]' (**arg(53, 1003430))
hide p212
$ update_portrait('sc025_01 4', 'p622', [l(-1), dark, flip], 5)
$ update_portrait('uc004_02 4', 'p570', [r(-9), light], 6)
get_char('c5703') '[convertstrid(1003431)]' (**arg(54, 1003431)) with shake
hide p622
hide p570
$ update_portrait('sc071_01 2', 'p611', [l(-20), light, flip], 6)
$ update_narrator('c6111')
with fade
get_char('c6111') '[convertstrid(1003432)]' (**arg(55, 1003432))
$ update_portrait('sc071_01 2', 'p611', [l(-20), dark, flip], 5)
$ update_portrait('st029_01 4', 'p610', [r(-28), light], 6)
get_char('c6103') '[convertstrid(1003433)]' (**arg(56, 1003433))
$ update_portrait('st029_01 2', 'p610', [r(-28), light], 6)
get_char('c6103') '[convertstrid(1003434)]' (**arg(57, 1003434))
$ update_portrait('st029_01 2', 'p610', [r(-28), dark], 5)
$ update_portrait('sc071_01 2', 'p611', [l(-20), light, flip], 6)
play sfx2 "other_7085.ogg"
get_char('c6111') '[convertstrid(1003435)]' (**arg(58, 1003435))
hide p611
hide p610
$ update_narrator('c2113')
$ update_portrait('st012_01 3', 'p211', [r(-6), light], 6)
with fade
$ update_portrait('st012_01 3', 'p211', [r(-6), r_shake, light], 6)
get_char('c2113') '[convertstrid(1003436)]' (**arg(59, 1003436))
$ update_portrait('st012_01 3', 'p211', [r(-6), light], 6)
get_char('c2113') '[convertstrid(1003437)]' (**arg(60, 1003437))
$ update_portrait('st012_01 3', 'p211', [r(-6), dark], 5)
$ update_portrait('sc017_01 4', 'p571', [l(-7), light, flip], 6)
get_char('c5711') '[convertstrid(1003438)]' (**arg(61, 1003438))
hide p211
$ update_portrait('sc017_01 4', 'p571', [l(-7), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1003439)]' (**arg(62, 1003439))
hide p2
$ update_portrait('st012_01 3', 'p211', [r_midback(-6), light], 6)
get_char('c2113') '[convertstrid(1003440)]' (**arg(63, 1003440))
$ update_portrait('st012_01 3', 'p211', [r(-6), dark], 5)
$ update_portrait('sc017_01 4', 'p571', [l_midback(-7), light, flip], 6)
play sfx2 "fight_6022.ogg"
get_char('c5711') '[convertstrid(1003441)]' (**arg(64, 1003441))
$ update_portrait('sc017_01 4', 'p571', [l(-7), dark, flip], 5)
$ update_portrait('st012_01 3', 'p211', [r(-6), r_shake, light], 6)
play sfx2 "other_7057.ogg"
get_char('c2113') '[convertstrid(1003442)]' (**arg(65, 1003442))
hide p211
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003443)]' (**arg(66, 1003443))
hide p571
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 12', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1003444)]' (**arg(67, 1003444))
hide p1
$ update_portrait('oc004_01 12', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1003445)]' (**arg(68, 1003445))
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('sc025_01 4', 'p622', [l(-1), light, flip], 6)
get_char('c6221') '[convertstrid(1003446)]' (**arg(69, 1003446))
hide p3
$ update_portrait('sc025_01 4', 'p622', [l(-1), dark, flip], 5)
$ update_portrait('st012_01 3', 'p211', [r(-6), light], 6)
get_char('c2113') '[convertstrid(1003447)]' (**arg(70, 1003447))
$ update_portrait('st012_01 3', 'p211', [r(-6), light], 6)
get_char('c2113') '[convertstrid(1003448)]' (**arg(71, 1003448))
$ update_portrait('st012_01 3', 'p211', [r(-6), dark], 5)
$ update_portrait('sc025_01 4', 'p622', [l(-1), light, flip], 6)
get_char('c6221') '[convertstrid(1003449)]' (**arg(72, 1003449))
$ update_portrait('sc025_01 4', 'p622', [l(-1), dark, flip], 5)
$ update_portrait('st012_01 3', 'p211', [r(-6), r_shake, light], 6)
get_char('c2113') '[convertstrid(1003450)]' (**arg(73, 1003450, size=(1.1)))
$ update_portrait('st012_01 3', 'p211', [r(-6), light], 6)
get_char('c2113') '[convertstrid(1003451)]' (**arg(74, 1003451, size=(1.2))) with shake
return "avg10039"