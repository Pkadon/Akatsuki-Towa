label avg10033(trans=fade_in):

$ play_music("ed7151.ogg")
scene avg_bg_027
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1003050)]' (**arg(1, 1003050))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003051)]' (**arg(2, 1003051))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003052)]' (**arg(3, 1003052))
hide p1
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1003053)]' (**arg(4, 1003053))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1003054)]' (**arg(5, 1003054))
hide p4
$ update_portrait('st017_01 2', 'p216', [l_entrance(-18), light, flip], 6)
get_char('c2161') '[convertstrid(1003055)]' (**arg(6, 1003055))
hide p3
$ update_portrait('st017_01 2', 'p216', [l(-18), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1003056)]' (**arg(7, 1003056))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('st017_01 1', 'p216', [l(-18), light, flip], 6)
get_char('c2161') '[convertstrid(1003057)]' (**arg(8, 1003057))
hide p2
$ update_portrait('st017_01 1', 'p216', [l(-18), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1003058)]' (**arg(9, 1003058))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('st017_01 5', 'p216', [l(-18), light, flip], 6)
get_char('c2161') '[convertstrid(1003059)]' (**arg(10, 1003059))
$ update_portrait('st017_01 5', 'p216', [l(-18), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003060)]' (**arg(11, 1003060))
hide p1
$ update_portrait('st018_01 2', 'p217', [r(-16), light], 6)
get_char('c2173') '[convertstrid(1003061)]' (**arg(12, 1003061))
hide p216
$ update_portrait('st018_01 2', 'p217', [r(-16), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1003062)]' (**arg(13, 1003062))
hide p4
$ update_portrait('st016_01 2', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1003063)]' (**arg(14, 1003063))
$ update_portrait('st016_01 5', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1003064)]' (**arg(15, 1003064))
hide p217
$ update_portrait('st016_01 5', 'p215', [l(-8), dark, flip], 5)
$ update_portrait('st019_01 5', 'p218', [r(-17), light], 6)
get_char('c2183') '[convertstrid(1003065)]' (**arg(16, 1003065))
$ update_portrait('st019_01 5', 'p218', [r(-17), dark], 5)
$ update_portrait('st016_01 1', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1003066)]' (**arg(17, 1003066))
$ update_portrait('st016_01 1', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1003067)]' (**arg(18, 1003067))
hide p215
$ update_portrait('oc001_01 9', 'p1', [l(-2), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c11') '[convertstrid(1003068)]' (**arg(19, 1003068))
hide p218
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1003069)]' (**arg(20, 1003069))
hide p1
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('st014_01 4', 'p213', [l(-18), light, flip], 6)
get_char('c2131') '[convertstrid(1003070)]' (**arg(21, 1003070))
$ update_portrait('st014_01 1', 'p213', [l(-18), light, flip], 6)
get_char('c2131') '[convertstrid(1003071)]' (**arg(22, 1003071))
hide p2
$ update_portrait('st014_01 1', 'p213', [l(-18), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1003072)]' (**arg(23, 1003072))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('st014_01 4', 'p213', [l(-18), light, flip], 6)
get_char('c2131') '[convertstrid(1003073)]' (**arg(24, 1003073))
hide p4
$ update_portrait('st014_01 4', 'p213', [l(-18), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1003074)]' (**arg(25, 1003074))
hide p213
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('st016_01 2', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1003075)]' (**arg(26, 1003075))
$ play_music("ed7511.ogg")
$ update_portrait('st016_01 2', 'p215', [l(-8), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
play sfx2 "other_7075.ogg"
get_char('c33') '[convertstrid(1003076)]' (**arg(27, 1003076))
$ update_portrait('oc003_01 3', 'p3', [r(-6), r_shake, light], 6)
play sfx2 "elc_5005.ogg"
play sfxvoice "avg_vocal_ro16.ogg"
get_char('c33') '[convertstrid(1003077)]' (**arg(28, 1003077))
$ update_portrait('oc003_01 10', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1003078)]' (**arg(29, 1003078))
hide p215
$ update_portrait('oc003_01 10', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003079)]' (**arg(30, 1003079))
hide p3
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st016_01 2', 'p215', [r(-8), light], 6)
get_char('c2153') '[convertstrid(1003080)]' (**arg(31, 1003080))
$ update_portrait('st016_01 2', 'p215', [r(-8), dark], 5)
$ update_portrait('oc002_01 19', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1003081)]' (**arg(32, 1003081))
hide p215
$ update_portrait('oc002_01 19', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1003082)]' (**arg(33, 1003082))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003083)]' (**arg(34, 1003083))
hide p2
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('st018_01 2', 'p217', [l(-16), light, flip], 6)
get_char('c2171') '[convertstrid(1003084)]' (**arg(35, 1003084, size=(1.2))) with shake
hide p1
$ update_portrait('st018_01 2', 'p217', [l(-16), dark, flip], 5)
$ update_portrait('st016_01 2', 'p215', [r(-8), light], 6)
get_char('c2153') '[convertstrid(1003085)]' (**arg(36, 1003085))
hide p215
$ update_portrait('oc001_01 3', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "other_7071.ogg"
get_char('c13') '[convertstrid(1003086)]' (**arg(37, 1003086))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "other_7072.ogg"
get_char('c13') '[convertstrid(1003087)]' (**arg(38, 1003087))
hide p217
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c4971') '[convertstrid(1003088)]' (**arg(39, 1003088))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003089)]' (**arg(40, 1003089))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
get_char('c4971') '[convertstrid(1003090)]' (**arg(41, 1003090))
get_char('c4971') '[convertstrid(1003091)]' (**arg(42, 1003091))
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1003092)]' (**arg(43, 1003092))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003093)]' (**arg(44, 1003093, size=(1.2))) with shake
hide p1
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1003094)]' (**arg(45, 1003094))
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
get_char('c4971') '[convertstrid(1003095)]' (**arg(46, 1003095))
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1003096)]' (**arg(47, 1003096))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003097)]' (**arg(48, 1003097))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003098)]' (**arg(49, 1003098))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
play sfx2 "other_7073.ogg"
get_char('c4971') '[convertstrid(1003099)]' (**arg(50, 1003099))
hide p1
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1003100)]' (**arg(51, 1003100))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003101)]' (**arg(52, 1003101))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003102)]' (**arg(53, 1003102))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfx2 "other_7074.ogg"
get_char('c13') '[convertstrid(1003103)]' (**arg(54, 1003103))
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
play sfx2 "other_7072.ogg"
get_char('c13') '[convertstrid(1003104)]' (**arg(55, 1003104))
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
get_char('c6051') '[convertstrid(1003105)]' (**arg(56, 1003105))
hide p1
get_char('c0') '[convertstrid(1003106)]' (**arg(57, 1003106))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003107)]' (**arg(58, 1003107))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c6051') '[convertstrid(1003108)]' (**arg(59, 1003108))
get_char('c6051') '[convertstrid(1003109)]' (**arg(60, 1003109))
hide p1
$ update_portrait('oc002_01 9', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1003110)]' (**arg(61, 1003110))
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
get_char('c6051') '[convertstrid(1003111)]' (**arg(62, 1003111))
get_char('c6051') '[convertstrid(1003112)]' (**arg(63, 1003112))
hide p2
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfx2 "other_7073.ogg"
get_char('c13') '[convertstrid(1003113)]' (**arg(64, 1003113))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1003114)]' (**arg(65, 1003114))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003115)]' (**arg(66, 1003115))
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 3', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro18.ogg"
get_char('c31') '[convertstrid(1003116)]' (**arg(67, 1003116))
hide p1
$ update_portrait('oc003_01 3', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1003117)]' (**arg(68, 1003117))
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('st019_01 2', 'p218', [l(-17), l_shake, light, flip], 6)
get_char('c2181') '[convertstrid(1003118)]' (**arg(69, 1003118))
hide p4
$ update_portrait('st019_01 2', 'p218', [l(-17), dark, flip], 5)
$ update_portrait('st014_01 4', 'p213', [r(-18), light], 6)
get_char('c2133') '[convertstrid(1003119)]' (**arg(70, 1003119))
hide p218
$ update_portrait('st014_01 4', 'p213', [r(-18), dark], 5)
$ update_portrait('st018_01 4', 'p217', [l(-16), light, flip], 6)
get_char('c2171') '[convertstrid(1003120)]' (**arg(71, 1003120))
hide p217
$ update_portrait('st019_01 3', 'p218', [l_exit(-17), light, flip], 6)
get_char('c2181') '[convertstrid(1003121)]' (**arg(72, 1003121))
hide p218
hide p213
$ update_portrait('oc004_01 16', 'p4', [r(-5), r_shake, light], 6)
get_char('c43') '[convertstrid(1003122)]' (**arg(73, 1003122))
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1003123)]' (**arg(74, 1003123))
hide p4
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st014_01 4', 'p213', [r(-18), light], 6)
get_char('c2133') '[convertstrid(1003124)]' (**arg(75, 1003124))
hide p2
$ update_portrait('st014_01 4', 'p213', [r(-18), dark], 5)
$ update_portrait('st016_01 2', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1003125)]' (**arg(76, 1003125))
hide p215
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1003126)]' (**arg(77, 1003126))
hide p213
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1003127)]' (**arg(78, 1003127))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1003128)]' (**arg(79, 1003128))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1003129)]' (**arg(80, 1003129))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1003130)]' (**arg(81, 1003130))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 10', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1003131)]' (**arg(82, 1003131))
hide p2
$ update_portrait('oc003_01 10', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003132)]' (**arg(83, 1003132))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003133)]' (**arg(84, 1003133))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003134)]' (**arg(85, 1003134))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003135)]' (**arg(86, 1003135))
hide p3
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('st016_01 2', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1003136)]' (**arg(87, 1003136))
hide p1
$ update_portrait('st016_01 2', 'p215', [l(-8), dark, flip], 5)
$ update_portrait('st014_01 1', 'p213', [r(-18), light], 6)
get_char('c2133') '[convertstrid(1003137)]' (**arg(88, 1003137))
$ update_portrait('st014_01 1', 'p213', [r(-18), dark], 5)
$ update_portrait('st016_01 2', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1003138)]' (**arg(89, 1003138))
$ update_portrait('st016_01 2', 'p215', [l(-8), dark, flip], 5)
$ update_portrait('st014_01 2', 'p213', [r(-18), r_shake, light], 6)
get_char('c2133') '[convertstrid(1003139)]' (**arg(90, 1003139))
hide p213
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003140)]' (**arg(91, 1003140))
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('st016_01 2', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1003141)]' (**arg(92, 1003141)) with shake
$ update_portrait('st016_01 2', 'p215', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1003142)]' (**arg(93, 1003142))
hide p215
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 3', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1003143)]' (**arg(94, 1003143))
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003144)]' (**arg(95, 1003144))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch03.ogg"
get_char('c21') '[convertstrid(1003145)]' (**arg(96, 1003145))
hide p2
hide p1
play sfx2 "other_7088.ogg"
get_char('c0') '[convertstrid(1003146)]' (**arg(97, 1003146))
$ update_portrait('st016_01 2', 'p215', [r(-8), light], 6)
get_char('c2153') '[convertstrid(1003147)]' (**arg(98, 1003147))
$ update_portrait('st016_01 2', 'p215', [r(-8), dark], 5)
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003148)]' (**arg(99, 1003148))
hide p215
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003149)]' (**arg(100, 1003149))
$ update_portrait('oc001_01 14', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1003150)]' (**arg(101, 1003150))
$ update_portrait('oc001_01 14', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003151)]' (**arg(102, 1003151))
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st014_01 2', 'p213', [r(-18), light], 6)
get_char('c2133') '[convertstrid(1003152)]' (**arg(103, 1003152))
hide p213
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003153)]' (**arg(104, 1003153))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003154)]' (**arg(105, 1003154))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1003155)]' (**arg(106, 1003155))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1003156)]' (**arg(107, 1003156))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1003157)]' (**arg(108, 1003157))
hide p3
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003158)]' (**arg(109, 1003158))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1003159)]' (**arg(110, 1003159))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 19', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003160)]' (**arg(111, 1003160))
$ update_portrait('oc002_01 19', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
play sfx2 "other_7075.ogg"
play sfxvoice "avg_vocal_na09_b.ogg"
get_char('c13') '[convertstrid(1003161)]' (**arg(112, 1003161))
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003162)]' (**arg(113, 1003162))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 13', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1003163)]' (**arg(114, 1003163))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003164)]' (**arg(115, 1003164))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003165)]' (**arg(116, 1003165))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003166)]' (**arg(117, 1003166))
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
play sfx2 "elc_5005.ogg"
get_char('c21') '[convertstrid(1003003)]' (**arg(118, 1003003))
menu:
    extend ""
    '[convertstrid(1003004)]':
        call avg10035
    '[convertstrid(1003005)]':
        call avg10036
    '[convertstrid(1003006)]':
        call avg10034
return _return