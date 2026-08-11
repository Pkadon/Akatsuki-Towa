label avg10003(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_043
$ update_narrator('c13')
window show
with trans
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7020.ogg"
get_char('c13') '[convertstrid(1000100)]' (**arg(1, 1000100))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000101)]' (**arg(2, 1000101))
hide p2
$ update_portrait('sc049_01 1', 'p56', [l_entrance(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000102)]' (**arg(3, 1000102))
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000103)]' (**arg(4, 1000103))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000104)]' (**arg(5, 1000104))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na22.ogg"
get_char('c13') '[convertstrid(1000105)]' (**arg(6, 1000105))
hide p1
$ update_portrait('oc002_01 18', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1000106)]' (**arg(7, 1000106))
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000107)]' (**arg(8, 1000107))
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000108)]' (**arg(9, 1000108))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000109)]' (**arg(10, 1000109))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1000110)]' (**arg(11, 1000110))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1000111)]' (**arg(12, 1000111))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000112)]' (**arg(13, 1000112))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000113)]' (**arg(14, 1000113))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000114)]' (**arg(15, 1000114))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000115)]' (**arg(16, 1000115))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000116)]' (**arg(17, 1000116))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000117)]' (**arg(18, 1000117))
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
play sfx2 "common_core.ogg"
get_char('c561') '[convertstrid(1000118)]' (**arg(19, 1000118))
hide p56
hide p1
show Image1 zorder 4
play sfx2 "common_correct.ogg"
get_char('c0') '[convertstrid(1007252)]' (**arg(20, 1007252))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000119)]' (**arg(21, 1000119))
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1000120)]' (**arg(22, 1000120))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000121)]' (**arg(23, 1000121))
hide Image1
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1007485)]' (**arg(24, 1007485))
hide p56
hide p2
play sfx2 "common_correct.ogg"
get_char('c0') '[convertstrid(1007486)]' (**arg(25, 1007486))
play sfx2 "common_correct.ogg"
get_char('c0') '[convertstrid(1007487)]' (**arg(26, 1007487))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1007488)]' (**arg(27, 1007488))
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1007489)]' (**arg(28, 1007489))
$ update_portrait('sc049_01 8', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1007490)]' (**arg(29, 1007490))
$ update_portrait('sc049_01 8', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000126)]' (**arg(30, 1000126))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1000127)]' (**arg(31, 1000127))
hide p1
$ update_portrait('oc002_01 13', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch09.ogg"
get_char('c23') '[convertstrid(1000128)]' (**arg(32, 1000128))
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 6', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000129)]' (**arg(33, 1000129))
$ update_portrait('sc049_01 6', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1000130)]' (**arg(34, 1000130))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 6', 'p56', [l(-8), light, flip], 6)
play sfx2 "other_7091.ogg"
get_char('c561') '[convertstrid(1007491)]' (**arg(35, 1007491))
show Image1 zorder 4
hide p2
$ update_portrait('sc049_01 6', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007492)]' (**arg(36, 1007492))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007493)]' (**arg(37, 1007493))
hide p1
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007494)]' (**arg(38, 1007494))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007495)]' (**arg(39, 1007495))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007496)]' (**arg(40, 1007496))
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007497)]' (**arg(41, 1007497))
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 6', 'p56', [l(-8), light, flip], 6)
play sfx2 "other_7091.ogg"
get_char('c561') '[convertstrid(1007498)]' (**arg(42, 1007498))
hide p1
$ update_portrait('sc049_01 6', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
play sfxvoice "bcv_oc002_com_01.ogg"
get_char('c23') '[convertstrid(1007499)]' (**arg(43, 1007499))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007500)]' (**arg(44, 1007500))
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007501)]' (**arg(45, 1007501))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1007502)]' (**arg(46, 1007502))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1007503)]' (**arg(47, 1007503))
hide Image1
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1007504)]' (**arg(48, 1007504))
hide p56
hide p2
$ update_narrator('c21')
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
with fade
$ update_portrait('oc002_01 6', 'p2', [l(-3), l_shake, light, flip], 6)
play sfx2 "common_wheel.ogg"
get_char('c21') '[convertstrid(1007505)]' (**arg(49, 1007505))
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04.ogg"
get_char('c13') '[convertstrid(1007506)]' (**arg(50, 1007506))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "common_wheel.ogg"
get_char('c13') '[convertstrid(1007507)]' (**arg(51, 1007507))
hide p2
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
$ update_narrator('c561')
with fade
get_char('c561') '[convertstrid(1007508)]' (**arg(52, 1007508))
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1007509)]' (**arg(53, 1007509))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1007510)]' (**arg(54, 1007510))
$ update_portrait('sc049_01 6', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1007511)]' (**arg(55, 1007511))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1007512)]' (**arg(56, 1007512))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1007513)]' (**arg(57, 1007513))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007514)]' (**arg(58, 1007514))
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1000130)]' (**arg(59, 1000130))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000131)]' (**arg(60, 1000131))
hide p56
hide p2
play sfx2 "common_correct.ogg"
get_char('c0') '[convertstrid(1000132)]' (**arg(61, 1000132))
play sfx2 "common_correct.ogg"
get_char('c0') '[convertstrid(1007515)]' (**arg(62, 1007515))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1007516)]' (**arg(63, 1007516))
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1007517)]' (**arg(64, 1007517))
$ update_portrait('sc049_01 4', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007518)]' (**arg(65, 1007518))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000133)]' (**arg(66, 1000133))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000134)]' (**arg(67, 1000134))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000135)]' (**arg(68, 1000135))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 6', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000136)]' (**arg(69, 1000136))
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000137)]' (**arg(70, 1000137))
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000138)]' (**arg(71, 1000138))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000139)]' (**arg(72, 1000139))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000140)]' (**arg(73, 1000140))
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1000141)]' (**arg(74, 1000141))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000142)]' (**arg(75, 1000142))
hide p56
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1000143)]' (**arg(76, 1000143))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c21') '[convertstrid(1000144)]' (**arg(77, 1000144))
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1000145)]' (**arg(78, 1000145, size=(1.1)))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na03_b.ogg"
get_char('c13') '[convertstrid(1000146)]' (**arg(79, 1000146))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000147)]' (**arg(80, 1000147))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000148)]' (**arg(81, 1000148))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000149)]' (**arg(82, 1000149))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000150)]' (**arg(83, 1000150))
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1000151)]' (**arg(84, 1000151))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000152)]' (**arg(85, 1000152))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000153)]' (**arg(86, 1000153))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1000154)]' (**arg(87, 1000154))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 23', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000155)]' (**arg(88, 1000155))
$ update_portrait('oc002_01 23', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000156)]' (**arg(89, 1000156))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000157)]' (**arg(90, 1000157))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1000158)]' (**arg(91, 1000158))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000159)]' (**arg(92, 1000159))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na19.ogg"
get_char('c13') '[convertstrid(1000160)]' (**arg(93, 1000160))
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000161)]' (**arg(94, 1000161))
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000162)]' (**arg(95, 1000162))
$ update_portrait('oc001_01 6', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), l_shake, light, flip], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_ch04_b.ogg"
get_char('c21') '[convertstrid(1000163)]' (**arg(96, 1000163))
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000164)]' (**arg(97, 1000164))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000165)]' (**arg(98, 1000165))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000166)]' (**arg(99, 1000166))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000167)]' (**arg(100, 1000167))
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1000168)]' (**arg(101, 1000168))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000169)]' (**arg(102, 1000169))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000170)]' (**arg(103, 1000170))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfx2 "other_7047.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1000174)]' (**arg(104, 1000174))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c13') '[convertstrid(1000175)]' (**arg(105, 1000175))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000176)]' (**arg(106, 1000176))
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000177)]' (**arg(107, 1000177))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1000178)]' (**arg(108, 1000178))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000179)]' (**arg(109, 1000179))
return "avg10003"