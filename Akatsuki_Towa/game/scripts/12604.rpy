label avg12604(trans=fade_in):

$ play_music("ED6105.ogg")
scene avg_bg_077
$ update_narrator('c0')
window show
with trans
play sfx2 "other_7060.ogg"
get_char('c0') '[convertstrid(1161149)]' (**arg(1, 1161149))
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1161150)]' (**arg(2, 1161150))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 23', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161151)]' (**arg(3, 1161151))
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161152)]' (**arg(4, 1161152))
hide p1
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st014_01 2', 'p213', [r(-18), light], 6)
get_char('c2133') '[convertstrid(1161153)]' (**arg(5, 1161153))
hide p2
$ update_portrait('st014_01 2', 'p213', [r(-18), dark], 5)
$ update_portrait('sc030_01 2', 'p38', [l(-12), light, flip], 6)
get_char('c381') '[convertstrid(1161154)]' (**arg(6, 1161154))
hide p213
$ update_portrait('sc030_01 2', 'p38', [l(-12), dark, flip], 5)
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1161155)]' (**arg(7, 1161155))
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1161156)]' (**arg(8, 1161156))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc030_01 1', 'p38', [l(-12), light, flip], 6)
get_char('c381') '[convertstrid(1161157)]' (**arg(9, 1161157))
hide p3
$ update_portrait('sc030_01 1', 'p38', [l(-12), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li03.ogg"
get_char('c43') '[convertstrid(1161158)]' (**arg(10, 1161158))
hide p38
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('st014_01 1', 'p213', [l(-18), light, flip], 6)
get_char('c2131') '[convertstrid(1161159)]' (**arg(11, 1161159))
hide p4
$ update_portrait('st014_01 1', 'p213', [l(-18), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1161160)]' (**arg(12, 1161160))
hide p213
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('sc030_01 1', 'p38', [l(-12), light, flip], 6)
get_char('c381') '[convertstrid(1161161)]' (**arg(13, 1161161))
hide p38
$ update_portrait('sc031_01 5', 'p39', [l(-14), light, flip], 6)
get_char('c391') '[convertstrid(1161162)]' (**arg(14, 1161162))
$ update_portrait('sc031_01 5', 'p39', [l(-14), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161163)]' (**arg(15, 1161163))
hide p39
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc030_01 4', 'p38', [l(-12), light, flip], 6)
get_char('c381') '[convertstrid(1161164)]' (**arg(16, 1161164))
hide p38
$ update_portrait('sc031_01 3', 'p39', [l(-14), light, flip], 6)
get_char('c391') '[convertstrid(1161165)]' (**arg(17, 1161165))
hide p39
$ update_portrait('sc030_01 4', 'p38', [l(-12), light, flip], 6)
get_char('c381') '[convertstrid(1161166)]' (**arg(18, 1161166))
$ update_portrait('sc030_01 4', 'p38', [l(-12), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161167)]' (**arg(19, 1161167))
hide p38
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('sc032_01 2', 'p40', [l_entrance(-17), light, flip], 6)
get_char('c401') '[convertstrid(1161168)]' (**arg(20, 1161168))
$ update_portrait('sc032_01 2', 'p40', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1161169)]' (**arg(21, 1161169))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('sc032_01 5', 'p40', [l(-17), light, flip], 6)
get_char('c401') '[convertstrid(1161170)]' (**arg(22, 1161170))
$ update_portrait('sc032_01 1', 'p40', [l(-17), light, flip], 6)
get_char('c401') '[convertstrid(1161171)]' (**arg(23, 1161171))
hide p2
$ update_portrait('sc032_01 1', 'p40', [l(-17), dark, flip], 5)
$ update_portrait('sc030_01 4', 'p38', [r(-12), light], 6)
get_char('c383') '[convertstrid(1161172)]' (**arg(24, 1161172))
$ update_portrait('sc030_01 4', 'p38', [r(-12), dark], 5)
$ update_portrait('sc032_01 1', 'p40', [l(-17), l_shake, light, flip], 6)
get_char('c401') '[convertstrid(1161173)]' (**arg(25, 1161173))
hide p38
$ update_portrait('sc032_01 1', 'p40', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161174)]' (**arg(26, 1161174))
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1161175)]' (**arg(27, 1161175))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('sc032_01 1', 'p40', [l(-17), light, flip], 6)
get_char('c401') '[convertstrid(1161176)]' (**arg(28, 1161176))
hide p4
$ update_portrait('sc032_01 1', 'p40', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161177)]' (**arg(29, 1161177))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('sc032_01 1', 'p40', [l(-17), light, flip], 6)
get_char('c401') '[convertstrid(1161178)]' (**arg(30, 1161178))
$ update_portrait('sc032_01 1', 'p40', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161179)]' (**arg(31, 1161179))
hide p2
$ update_portrait('oc004_01 22', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1161180)]' (**arg(32, 1161180))
hide p4
$ update_portrait('st018_01 1', 'p217', [r_entrance(-16), light], 6)
play sfx2 "other_7085.ogg"
get_char('c2173') '[convertstrid(1161181)]' (**arg(33, 1161181))
hide p40
$ update_portrait('st018_01 1', 'p217', [r(-16), dark], 5)
$ update_portrait('st019_01 1', 'p218', [l_entrance(-17), light, flip], 6)
play sfx2 "other_7085.ogg"
get_char('c2181') '[convertstrid(1161182)]' (**arg(34, 1161182))
hide p217
$ update_portrait('st019_01 1', 'p218', [l(-17), dark, flip], 5)
$ update_portrait('st017_01 5', 'p216', [r_entrance(-18), light], 6)
play sfx2 "other_7085.ogg"
get_char('c2163') '[convertstrid(1161183)]' (**arg(35, 1161183))
hide p218
$ update_portrait('st017_01 5', 'p216', [r(-18), dark], 5)
$ update_portrait('st016_01 4', 'p215', [l_entrance(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1161184)]' (**arg(36, 1161184))
hide p215
$ update_portrait('sc032_01 2', 'p40', [l(-17), l_shake, light, flip], 6)
get_char('c401') '[convertstrid(1161185)]' (**arg(37, 1161185))
$ update_portrait('sc032_01 1', 'p40', [l(-17), light, flip], 6)
get_char('c401') '[convertstrid(1161186)]' (**arg(38, 1161186))
hide p216
$ update_portrait('sc032_01 1', 'p40', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch02.ogg"
get_char('c23') '[convertstrid(1161187)]' (**arg(39, 1161187))
hide p40
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
$ update_portrait('st017_01 5', 'p216', [l(-18), l_shake, light, flip], 6)
get_char('c2161') '[convertstrid(1161188)]' (**arg(40, 1161188))
hide p2
$ update_portrait('st017_01 5', 'p216', [l(-18), dark, flip], 5)
$ update_portrait('st018_01 1', 'p217', [r(-16), light], 6)
get_char('c2173') '[convertstrid(1161189)]' (**arg(41, 1161189))
hide p216
$ update_portrait('st018_01 1', 'p217', [r(-16), dark], 5)
$ update_portrait('st019_01 2', 'p218', [l(-17), light, flip], 6)
get_char('c2181') '[convertstrid(1161190)]' (**arg(42, 1161190))
hide p218
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch29.ogg"
get_char('c21') '[convertstrid(1161191)]' (**arg(43, 1161191))
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st018_01 5', 'p217', [r(-16), light], 6)
get_char('c2173') '[convertstrid(1161192)]' (**arg(44, 1161192))
$ update_portrait('st018_01 5', 'p217', [r(-16), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161193)]' (**arg(45, 1161193))
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161194)]' (**arg(46, 1161194))
hide p217
$ update_portrait('oc002_01 15', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st019_01 3', 'p218', [r(-17), light], 6)
get_char('c2183') '[convertstrid(1161195)]' (**arg(47, 1161195))
hide p2
$ update_portrait('st019_01 3', 'p218', [r(-17), dark], 5)
$ update_portrait('st017_01 1', 'p216', [l(-18), light, flip], 6)
get_char('c2161') '[convertstrid(1161196)]' (**arg(48, 1161196))
hide p218
$ update_portrait('st017_01 1', 'p216', [l(-18), dark, flip], 5)
$ update_portrait('st018_01 1', 'p217', [r(-16), light], 6)
get_char('c2173') '[convertstrid(1161197)]' (**arg(49, 1161197))
hide p216
$ update_portrait('st018_01 1', 'p217', [r(-16), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161198)]' (**arg(50, 1161198))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st018_01 2', 'p217', [r(-16), light], 6)
get_char('c2173') '[convertstrid(1161199)]' (**arg(51, 1161199))
$ update_portrait('st018_01 2', 'p217', [r(-16), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161200)]' (**arg(52, 1161200))
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161201)]' (**arg(53, 1161201))
hide p217
$ update_portrait('oc002_01 7', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1161202)]' (**arg(54, 1161202))
hide p4
$ update_portrait('st018_01 4', 'p217', [r(-16), light], 6)
get_char('c2173') '[convertstrid(1161203)]' (**arg(55, 1161203))
$ update_portrait('st018_01 4', 'p217', [r(-16), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161204)]' (**arg(56, 1161204))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch23.ogg"
get_char('c21') '[convertstrid(1161205)]' (**arg(57, 1161205))
hide p217
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li17.ogg"
get_char('c43') '[convertstrid(1161206)]' (**arg(58, 1161206))
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161207)]' (**arg(59, 1161207))
$ update_portrait('oc002_01 13', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161208)]' (**arg(60, 1161208))
hide p4
$ update_portrait('oc002_01 13', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st018_01 4', 'p217', [r(-16), light], 6)
get_char('c2173') '[convertstrid(1161209)]' (**arg(61, 1161209))
$ update_portrait('st018_01 4', 'p217', [r(-16), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161210)]' (**arg(62, 1161210))
hide p217
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 18', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1161211)]' (**arg(63, 1161211))
hide p4
$ update_portrait('st018_01 1', 'p217', [r(-16), light], 6)
get_char('c2173') '[convertstrid(1161212)]' (**arg(64, 1161212))
$ update_portrait('st018_01 1', 'p217', [r(-16), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161213)]' (**arg(65, 1161213)) with shake
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st018_01 1', 'p217', [r(-16), light], 6)
get_char('c2173') '[convertstrid(1161214)]' (**arg(66, 1161214))
hide p2
$ update_portrait('st018_01 1', 'p217', [r(-16), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1161215)]' (**arg(67, 1161215))
hide p4
$ update_portrait('st016_01 4', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1161216)]' (**arg(68, 1161216))
$ update_portrait('st016_01 4', 'p215', [l(-8), dark, flip], 5)
$ update_portrait('st018_01 4', 'p217', [r(-16), light], 6)
get_char('c2173') '[convertstrid(1161217)]' (**arg(69, 1161217))
hide p215
$ update_portrait('st018_01 4', 'p217', [r(-16), dark], 5)
$ update_portrait('oc004_01 14', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1161218)]' (**arg(70, 1161218))
$ update_portrait('oc004_01 14', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st018_01 2', 'p217', [r(-16), light], 6)
get_char('c2173') '[convertstrid(1161219)]' (**arg(71, 1161219))
hide p217
$ update_portrait('st016_01 2', 'p215', [r(-8), light], 6)
get_char('c2153') '[convertstrid(1161220)]' (**arg(72, 1161220))
$ update_portrait('st016_01 2', 'p215', [r(-8), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1161221)]' (**arg(73, 1161221))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1161222)]' (**arg(74, 1161222))
hide p215
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st018_01 1', 'p217', [r(-16), light], 6)
get_char('c2173') '[convertstrid(1161223)]' (**arg(75, 1161223))
$ update_portrait('st018_01 1', 'p217', [r(-16), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1161224)]' (**arg(76, 1161224))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1161225)]' (**arg(77, 1161225))
hide p217
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1161226)]' (**arg(78, 1161226))
hide p2
$ update_portrait('st018_01 2', 'p217', [r(-16), light], 6)
get_char('c2173') '[convertstrid(1161227)]' (**arg(79, 1161227))
hide p4
$ update_portrait('st018_01 2', 'p217', [r(-16), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161228)]' (**arg(80, 1161228))
hide p2
$ update_portrait('st017_01 5', 'p216', [l(-18), light, flip], 6)
get_char('c2161') '[convertstrid(1161229)]' (**arg(81, 1161229))
$ update_portrait('st017_01 5', 'p216', [l(-18), dark, flip], 5)
$ update_portrait('st018_01 3', 'p217', [r_exit(-16), light], 6)
get_char('c2173') '[convertstrid(1161230)]' (**arg(82, 1161230)) with shake
hide p217
hide p216
$ update_portrait('st016_01 1', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1161231)]' (**arg(83, 1161231))
hide p215
get_char('c0') '[convertstrid(1161232)]' (**arg(84, 1161232))
get_char('c0') '[convertstrid(1161233)]' (**arg(85, 1161233))
return "avg12604"