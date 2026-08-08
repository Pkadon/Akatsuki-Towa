label avg10405:

$ play_music("ED6518.ogg")
scene avg_bg_001
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_select.ogg"
get_char('c13') '[convertstrid(1140288)]' (**arg(1, 1140288))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1140289)]' (**arg(2, 1140289))
hide p2
$ update_portrait('sc048_01 1', 'p55', [l_entrance(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140290)]' (**arg(3, 1140290))
$ update_portrait('sc048_01 1', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140291)]' (**arg(4, 1140291))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140292)]' (**arg(5, 1140292))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140293)]' (**arg(6, 1140293))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140294)]' (**arg(7, 1140294))
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1140295)]' (**arg(8, 1140295))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140296)]' (**arg(9, 1140296))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140297)]' (**arg(10, 1140297))
hide p1
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc004_01 22', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1140298)]' (**arg(11, 1140298))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1140299)]' (**arg(12, 1140299))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1140300)]' (**arg(13, 1140300))
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1140301)]' (**arg(14, 1140301))
$ update_portrait('oc004_01 10', 'p4', [r(-5), dark], 5)
$ update_portrait('sc048_01 2', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140302)]' (**arg(15, 1140302))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140303)]' (**arg(16, 1140303))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140304)]' (**arg(17, 1140304))
hide p55
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro14.ogg"
get_char('c31') '[convertstrid(1140305)]' (**arg(18, 1140305))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1140306)]' (**arg(19, 1140306))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140307)]' (**arg(20, 1140307))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1140308)]' (**arg(21, 1140308))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1140309)]' (**arg(22, 1140309))
hide p3
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140310)]' (**arg(23, 1140310))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140311)]' (**arg(24, 1140311))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140312)]' (**arg(25, 1140312))
hide p2
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1140313)]' (**arg(26, 1140313))
hide p3
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch19.ogg"
get_char('c23') '[convertstrid(1140314)]' (**arg(27, 1140314))
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140315)]' (**arg(28, 1140315))
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140316)]' (**arg(29, 1140316))
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1140317)]' (**arg(30, 1140317))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1140318)]' (**arg(31, 1140318))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140319)]' (**arg(32, 1140319))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140320)]' (**arg(33, 1140320))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140321)]' (**arg(34, 1140321))
hide p1
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1140322)]' (**arg(35, 1140322))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140323)]' (**arg(36, 1140323))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140324)]' (**arg(37, 1140324))
hide p1
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc003_01 10', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro16.ogg"
get_char('c33') '[convertstrid(1140325)]' (**arg(38, 1140325))
$ update_portrait('oc003_01 21', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1140326)]' (**arg(39, 1140326))
hide p3
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140327)]' (**arg(40, 1140327))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140328)]' (**arg(41, 1140328))
hide p55
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1140329)]' (**arg(42, 1140329))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140330)]' (**arg(43, 1140330))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140331)]' (**arg(44, 1140331))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140332)]' (**arg(45, 1140332))
return