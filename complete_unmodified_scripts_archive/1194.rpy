label avg1194:

$ play_music("ed7111.ogg")
scene avg_bg_019
$ update_portrait('occ04_01 21', 'p2627', [l(-5), light, flip], 6)
$ update_narrator('c26271')
window show
with fade_in
play sfx2 "other_7057.ogg"
get_char('c26271') '[convertstrid(2107455)]' (**arg(1, 2107455))
$ update_portrait('occ04_01 21', 'p2627', [l(-5), dark, flip], 5)
$ update_portrait('sca46_01 1', 'p2632', [r(-5), light], 6)
get_char('c26323') '[convertstrid(2107456)]' (**arg(2, 2107456))
$ update_portrait('sca46_01 5', 'p2632', [r(-5), light], 6)
get_char('c26323') '[convertstrid(2107457)]' (**arg(3, 2107457))
$ update_portrait('sca46_01 5', 'p2632', [r(-5), light], 6)
get_char('c26323') '[convertstrid(2107458)]' (**arg(4, 2107458))
$ update_portrait('sca46_01 5', 'p2632', [r(-5), light], 6)
get_char('c26323') '[convertstrid(2107459)]' (**arg(5, 2107459))
hide p2627
$ update_portrait('sca46_01 5', 'p2632', [r(-5), dark], 5)
$ update_portrait('uc002_03 2', 'p2647', [l(-23), light, flip], 6)
play sfx2 "other_7064.ogg"
get_char('c26471') '[convertstrid(2107460)]' (**arg(6, 2107460))
hide p2647
$ update_portrait('uc002_03 3', 'p2648', [l(-23), light, flip], 6)
play sfx2 "other_7064.ogg"
get_char('c26481') '[convertstrid(2107461)]' (**arg(7, 2107461))
hide p2648
$ update_portrait('occ04_01 1', 'p2627', [l(-5), light, flip], 6)
get_char('c26271') '[convertstrid(2107462)]' (**arg(8, 2107462))
$ update_portrait('occ04_01 16', 'p2627', [l(-5), l_shake, light, flip], 6)
get_char('c26271') '[convertstrid(2107463)]' (**arg(9, 2107463))
hide p2627
get_char('c6431') '[convertstrid(2107464)]' (**arg(10, 2107464, size=(1.2))) with shake
$ update_portrait('occ04_01 9', 'p2627', [l(-5), light, flip], 6)
get_char('c26271') '[convertstrid(2107465)]' (**arg(11, 2107465))
$ update_portrait('occ04_01 14', 'p2627', [l(-5), light, flip], 6)
get_char('c26271') '[convertstrid(2107466)]' (**arg(12, 2107466))
hide p2632
$ update_portrait('occ04_01 14', 'p2627', [l(-5), dark, flip], 5)
get_char('c6433') '[convertstrid(2107467)]' (**arg(13, 2107467, size=(1.2))) with shake
$ update_portrait('sca46_01 1', 'p2632', [r(-5), light], 6)
get_char('c26323') '[convertstrid(2107468)]' (**arg(14, 2107468))
$ play_music("ed7101.ogg")
scene avg_bg_020
$ update_narrator('c26293')
with fade
$ update_portrait('scb38_01 2', 'p2629', [r_entrance(-1), light], 6)
get_char('c26293') '[convertstrid(2107469)]' (**arg(15, 2107469))
$ update_portrait('scb38_01 4', 'p2629', [r(-1), light], 6)
get_char('c26293') '[convertstrid(2107470)]' (**arg(16, 2107470))
hide p2629
$ update_portrait('scb38_01 2', 'p2629', [r(-1), light], 6)
$ update_narrator('c26293')
with fade
get_char('c26293') '[convertstrid(2107471)]' (**arg(17, 2107471))
$ update_portrait('scb38_01 2', 'p2629', [r(-1), dark], 5)
$ update_portrait('uc002_01 1', 'p2638', [l(2), l_shake, light, flip], 6)
get_char('c26381') '[convertstrid(2107472)]' (**arg(18, 2107472))
$ update_portrait('uc002_01 1', 'p2638', [l(2), dark, flip], 5)
$ update_portrait('scb38_01 2', 'p2629', [r(-1), light], 6)
get_char('c26293') '[convertstrid(2107473)]' (**arg(19, 2107473))
hide p2638
$ update_portrait('scb38_01 2', 'p2629', [r(-1), dark], 5)
$ update_portrait('uc002_01 1', 'p2639', [l(2), light, flip], 6)
get_char('c26391') '[convertstrid(2107474)]' (**arg(20, 2107474))
$ update_portrait('uc002_01 1', 'p2639', [l(2), dark, flip], 5)
$ update_portrait('scb38_01 2', 'p2629', [r(-1), r_shake, light], 6)
get_char('c26293') '[convertstrid(2107475)]' (**arg(21, 2107475))
hide p2639
$ update_portrait('scb38_01 2', 'p2629', [r(-1), dark], 5)
$ update_portrait('ocb03_01 14', 'p2628', [l(-6), light, flip], 6)
get_char('c26281') '[convertstrid(2107476)]' (**arg(22, 2107476))
hide p2628
$ update_portrait('uc002_01 1', 'p2638', [l(2), light, flip], 6)
get_char('c26381') '[convertstrid(2107477)]' (**arg(23, 2107477))
$ update_portrait('uc002_01 1', 'p2638', [l(2), dark, flip], 5)
$ update_portrait('scb38_01 1', 'p2629', [r(-1), light], 6)
get_char('c26293') '[convertstrid(2107478)]' (**arg(24, 2107478))
$ update_portrait('scb38_01 1', 'p2629', [r(-1), light], 6)
get_char('c26293') '[convertstrid(2107479)]' (**arg(25, 2107479))
$ update_portrait('scb38_01 1', 'p2629', [r(-1), light], 6)
get_char('c26293') '[convertstrid(2107480)]' (**arg(26, 2107480))
hide p2638
$ update_portrait('scb38_01 1', 'p2629', [r(-1), dark], 5)
$ update_portrait('uc002_01 1', 'p2639', [l(2), light, flip], 6)
get_char('c26391') '[convertstrid(2107481)]' (**arg(27, 2107481))
$ update_portrait('uc002_01 1', 'p2639', [l(2), dark, flip], 5)
$ update_portrait('scb38_01 5', 'p2629', [r(-1), light], 6)
play sfx2 "other_7088.ogg"
get_char('c26293') '[convertstrid(2107482)]' (**arg(28, 2107482))
hide p2639
$ update_portrait('scb38_01 5', 'p2629', [r(-1), dark], 5)
$ update_portrait('ocb03_01 8', 'p2628', [l(-6), light, flip], 6)
get_char('c26281') '[convertstrid(2107483)]' (**arg(29, 2107483))
$ update_portrait('ocb03_01 8', 'p2628', [l(-6), dark, flip], 5)
$ update_portrait('scb38_01 1', 'p2629', [r(-1), light], 6)
get_char('c26293') '[convertstrid(2107484)]' (**arg(30, 2107484))
$ update_portrait('scb38_01 1', 'p2629', [r(-1), dark], 5)
$ update_portrait('ocb03_01 16', 'p2628', [l(-6), light, flip], 6)
get_char('c26281') '[convertstrid(2107485)]' (**arg(31, 2107485))
$ update_portrait('ocb03_01 16', 'p2628', [l(-6), dark, flip], 5)
$ update_portrait('scb38_01 2', 'p2629', [r(-1), light], 6)
get_char('c26293') '[convertstrid(2107486)]' (**arg(32, 2107486))
$ update_portrait('scb38_01 2', 'p2629', [r(-1), dark], 5)
$ update_portrait('ocb03_01 17', 'p2628', [l(-6), light, flip], 6)
get_char('c26281') '[convertstrid(2107487)]' (**arg(33, 2107487))
hide p2628
hide p2629
get_char('c0') '[convertstrid(2107488)]' (**arg(34, 2107488))
$ update_portrait('scb38_01 2', 'p2629', [r(-1), light], 6)
get_char('c26293') '[convertstrid(2107489)]' (**arg(35, 2107489))
$ update_portrait('scb38_01 2', 'p2629', [r(-1), dark], 5)
$ update_portrait('ocb03_01 1', 'p2628', [l(-6), light, flip], 6)
get_char('c26281') '[convertstrid(2107490)]' (**arg(36, 2107490))
$ update_portrait('ocb03_01 1', 'p2628', [l(-6), dark, flip], 5)
$ update_portrait('scb38_01 2', 'p2629', [r(-1), light], 6)
get_char('c26293') '[convertstrid(2107491)]' (**arg(37, 2107491))
$ update_portrait('scb38_01 2', 'p2629', [r(-1), dark], 5)
$ update_portrait('ocb03_01 17', 'p2628', [l(-6), light, flip], 6)
get_char('c26281') '[convertstrid(2107492)]' (**arg(38, 2107492))
hide p2629
$ update_portrait('ocb03_01 17', 'p2628', [l(-6), dark, flip], 5)
$ update_portrait('uc002_01 1', 'p2638', [r(2), light], 6)
get_char('c26383') '[convertstrid(2107493)]' (**arg(39, 2107493))
$ update_portrait('uc002_01 1', 'p2638', [r(2), dark], 5)
$ update_portrait('ocb03_01 1', 'p2628', [l(-6), light, flip], 6)
get_char('c26281') '[convertstrid(2107494)]' (**arg(40, 2107494))
hide p2638
$ update_portrait('ocb03_01 1', 'p2628', [l(-6), dark, flip], 5)
$ update_portrait('uc002_01 1', 'p2639', [r(2), light], 6)
get_char('c26393') '[convertstrid(2107495)]' (**arg(41, 2107495))
$ update_portrait('uc002_01 1', 'p2639', [r(2), dark], 5)
$ update_portrait('ocb03_01 16', 'p2628', [l(-6), light, flip], 6)
get_char('c26281') '[convertstrid(2107496)]' (**arg(42, 2107496))
hide p2639
$ update_portrait('ocb03_01 16', 'p2628', [l(-6), dark, flip], 5)
$ update_portrait('scb38_01 2', 'p2629', [r(-1), r_shake, light], 6)
get_char('c26293') '[convertstrid(2107497)]' (**arg(43, 2107497))
$ update_portrait('scb38_01 2', 'p2629', [r(-1), dark], 5)
$ update_portrait('ocb03_01 17', 'p2628', [l(-6), light, flip], 6)
get_char('c26281') '[convertstrid(2107498)]' (**arg(44, 2107498))
hide p2629
$ update_portrait('ocb03_01 17', 'p2628', [l(-6), dark, flip], 5)
$ update_portrait('uc002_01 1', 'p2640', [r(2), light], 6)
get_char('c26403') '[convertstrid(2107499)]' (**arg(45, 2107499))
hide p2640
$ update_portrait('uc002_01 1', 'p2641', [r(2), light], 6)
get_char('c26413') '[convertstrid(2107500)]' (**arg(46, 2107500))
$ update_portrait('uc002_01 1', 'p2641', [r(2), dark], 5)
$ update_portrait('ocb03_01 2', 'p2628', [l(-6), light, flip], 6)
get_char('c26281') '[convertstrid(2107501)]' (**arg(47, 2107501))
hide p2641
$ update_portrait('ocb03_01 2', 'p2628', [l(-6), dark, flip], 5)
$ update_portrait('scb38_01 2', 'p2629', [r(-1), r_shake, light], 6)
get_char('c26293') '[convertstrid(2107502)]' (**arg(48, 2107502))
$ update_portrait('scb38_01 4', 'p2629', [r(-1), light], 6)
get_char('c26293') '[convertstrid(2107503)]' (**arg(49, 2107503))
$ play_music("ed7116.ogg")
hide p2628
$ update_portrait('scb38_01 4', 'p2629', [r(-1), dark], 5)
get_char('c26421') '[convertstrid(2107504)]' (**arg(50, 2107504, size=(1.2))) with shake
get_char('c26431') '[convertstrid(2107505)]' (**arg(51, 2107505, size=(1.2)))
get_char('c26441') '[convertstrid(2107506)]' (**arg(52, 2107506))
hide p2629
$ update_portrait('uc002_01 1', 'p2638', [r(2), r_shake, light], 6)
get_char('c26383') '[convertstrid(2107507)]' (**arg(53, 2107507))
hide p2638
play sfx2 "other_7064.ogg"
get_char('c0') '[convertstrid(2107508)]' (**arg(54, 2107508))
$ update_portrait('sc066_01 1', 'p70', [l_entrance(-34), light, flip], 6)
get_char('c701') '[convertstrid(2107509)]' (**arg(55, 2107509))
$ update_portrait('sc066_01 1', 'p70', [l(-34), dark, flip], 5)
$ update_portrait('scb38_01 2', 'p2629', [r(-1), light], 6)
get_char('c26293') '[convertstrid(2107510)]' (**arg(56, 2107510))
hide p2629
get_char('c26423') '[convertstrid(2107511)]' (**arg(57, 2107511))
$ update_portrait('sc066_01 3', 'p70', [l(-34), light, flip], 6)
play sfx2 "other_7087.ogg"
get_char('c701') '[convertstrid(2107512)]' (**arg(58, 2107512, size=(1.2)))
$ update_portrait('sc066_01 3', 'p70', [l(-34), dark, flip], 5)
$ update_portrait('uc002_01 3', 'p2641', [r(2), light], 6)
get_char('c26413') '[convertstrid(2107513)]' (**arg(59, 2107513)) with shake
hide p70
hide p2641
play sfx2 "other_7045.ogg"
get_char('c0') '[convertstrid(2107514)]' (**arg(60, 2107514))
get_char('c26433') '[convertstrid(2107515)]' (**arg(61, 2107515))
$ play_music("ed7455.ogg")
get_char('c26461') '[convertstrid(2107516)]' (**arg(62, 2107516, size=(1.2))) with shake
$ update_portrait('ocb03_01 17', 'p2628', [l(-6), light, flip], 6)
get_char('c26281') '[convertstrid(2107517)]' (**arg(63, 2107517))
$ update_portrait('ocb03_01 17', 'p2628', [l(-6), dark, flip], 5)
$ update_portrait('scb38_01 4', 'p2629', [r(-1), light], 6)
get_char('c26293') '[convertstrid(2107518)]' (**arg(64, 2107518))
$ update_portrait('scb38_01 4', 'p2629', [r(-1), dark], 5)
$ update_portrait('ocb03_01 1', 'p2628', [l(-6), light, flip], 6)
get_char('c26281') '[convertstrid(2107519)]' (**arg(65, 2107519))
hide p2628
hide p2629
play sfx2 "fight_6010.ogg"
get_char('c0') '[convertstrid(2107520)]' (**arg(66, 2107520))
$ update_portrait('ocb03_01 20', 'p2628', [l_exit(-6), light, flip], 6)
play sfx2 "other_7057.ogg"
get_char('c26281') '[convertstrid(2107521)]' (**arg(67, 2107521))
hide p2628
$ update_portrait('uc002_01 1', 'p2639', [r(2), light], 6)
get_char('c26393') '[convertstrid(2107522)]' (**arg(68, 2107522))
hide p2639
$ update_portrait('scb38_01 2', 'p2629', [r_entrance(-1), light], 6)
get_char('c26293') '[convertstrid(2107523)]' (**arg(69, 2107523))
$ update_portrait('scb38_01 2', 'p2629', [r(-1), dark], 5)
$ update_portrait('ocb03_01 4', 'p2628', [l_entrance(-6), light, flip], 6)
play sfx2 "fight_6025.ogg"
get_char('c26281') '[convertstrid(2107524)]' (**arg(70, 2107524))
$ update_portrait('ocb03_01 4', 'p2628', [l(-6), dark, flip], 5)
$ update_portrait('scb38_01 4', 'p2629', [r(-1), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c26293') '[convertstrid(2107525)]' (**arg(71, 2107525))
hide p2628
$ update_portrait('scb38_01 4', 'p2629', [r(-1), dark], 5)
get_char('c26451') '[convertstrid(2107526)]' (**arg(72, 2107526))
get_char('c26451') '[convertstrid(2107527)]' (**arg(73, 2107527))
hide p2629
get_char('c0') '[convertstrid(2107528)]' (**arg(74, 2107528))
return