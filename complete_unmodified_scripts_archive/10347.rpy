label avg10347:

$ play_music("ed7302.ogg")
scene avg_bg_031
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1131282)]' (**arg(1, 1131282))
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 3', 'p2', [l(-3), light, flip], 6)
play sfxvoice "bcv_oc002_hurt_01.ogg"
get_char('c21') '[convertstrid(1131283)]' (**arg(2, 1131283))
hide p1
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 19', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li20.ogg"
get_char('c43') '[convertstrid(1131284)]' (**arg(3, 1131284))
hide p2
$ update_portrait('oc004_01 19', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 3', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro16.ogg"
get_char('c31') '[convertstrid(1131285)]' (**arg(4, 1131285))
hide p3
$ update_portrait('sc046_01 3', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1131286)]' (**arg(5, 1131286))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1131287)]' (**arg(6, 1131287))
hide p4
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 15', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_02.ogg"
get_char('c13') '[convertstrid(1131288)]' (**arg(7, 1131288))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1131289)]' (**arg(8, 1131289))
hide p1
$ update_portrait('oc004_01 19', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li20.ogg"
get_char('c43') '[convertstrid(1131290)]' (**arg(9, 1131290, size=(1.2)))
$ update_portrait('oc004_01 19', 'p4', [r(-5), dark], 5)
$ update_portrait('sc046_01 3', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1131291)]' (**arg(10, 1131291))
hide p4
$ update_portrait('sc046_01 3', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1131292)]' (**arg(11, 1131292))
hide p2
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c33') '[convertstrid(1131293)]' (**arg(12, 1131293))
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('sc046_01 3', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1131294)]' (**arg(13, 1131294))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1131295)]' (**arg(14, 1131295))
hide p3
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na12.ogg"
get_char('c13') '[convertstrid(1131296)]' (**arg(15, 1131296, size=(1.4))) with shake
hide p1004
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
get_char('c10201') '[convertstrid(1131297)]' (**arg(16, 1131297, size=(1.4)))
$ update_portrait('st037_01 2', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(1131298)]' (**arg(17, 1131298))
hide p1
$ update_portrait('st037_01 2', 'p236', [l(-10), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1131299)]' (**arg(18, 1131299))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('st037_01 4', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(1131300)]' (**arg(19, 1131300))
hide p2
$ update_portrait('st037_01 4', 'p236', [l(-10), dark, flip], 5)
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c33') '[convertstrid(1131301)]' (**arg(20, 1131301))
$ update_portrait('oc003_01 21', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro22.ogg"
get_char('c33') '[convertstrid(1131302)]' (**arg(21, 1131302))
hide p3
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li26.ogg"
get_char('c43') '[convertstrid(1131303)]' (**arg(22, 1131303))
hide p236
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na18.ogg"
get_char('c11') '[convertstrid(1131304)]' (**arg(23, 1131304))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 12', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li10.ogg"
get_char('c43') '[convertstrid(1131305)]' (**arg(24, 1131305))
hide p1
$ update_portrait('oc004_01 12', 'p4', [r(-5), dark], 5)
$ update_portrait('sc046_01 3', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1131306)]' (**arg(25, 1131306))
$ update_portrait('sc046_01 3', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li26.ogg"
get_char('c43') '[convertstrid(1131307)]' (**arg(26, 1131307))
hide p1004
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
get_char('c10211') '[convertstrid(1131308)]' (**arg(27, 1131308, size=(1.2)))
hide p4
get_char('c0') '[convertstrid(1131309)]' (**arg(28, 1131309, size=(1.4)))
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1131310)]' (**arg(29, 1131310))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1131311)]' (**arg(30, 1131311))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1131312)]' (**arg(31, 1131312))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1131313)]' (**arg(32, 1131313))
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li03.ogg"
get_char('c43') '[convertstrid(1131314)]' (**arg(33, 1131314))
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li26.ogg"
get_char('c43') '[convertstrid(1131315)]' (**arg(34, 1131315))
hide p2
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
get_char('c10211') '[convertstrid(1131316)]' (**arg(35, 1131316))
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
play sfxvoice "bcv_oc002_die_01.ogg"
get_char('c21') '[convertstrid(1131317)]' (**arg(36, 1131317, size=(1.4)))
hide p4
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_02.ogg"
get_char('c13') '[convertstrid(1131318)]' (**arg(37, 1131318))
hide p2
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li26.ogg"
get_char('c41') '[convertstrid(1131319)]' (**arg(38, 1131319))
hide p1
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro10.ogg"
get_char('c33') '[convertstrid(1131320)]' (**arg(39, 1131320))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 20', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
get_char('c41') '[convertstrid(1131321)]' (**arg(40, 1131321, size=(1.2)))
$ update_portrait('oc004_01 20', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro18.ogg"
get_char('c33') '[convertstrid(1131322)]' (**arg(41, 1131322))
hide p3
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1131323)]' (**arg(42, 1131323))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
get_char('c41') '[convertstrid(1131324)]' (**arg(43, 1131324))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na10.ogg"
get_char('c13') '[convertstrid(1131325)]' (**arg(44, 1131325))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li18.ogg"
get_char('c41') '[convertstrid(1131326)]' (**arg(45, 1131326))
hide p4
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch23.ogg"
get_char('c21') '[convertstrid(1131327)]' (**arg(46, 1131327))
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1131328)]' (**arg(47, 1131328))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1131329)]' (**arg(48, 1131329))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1131330)]' (**arg(49, 1131330))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st037_01 2', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(1131331)]' (**arg(50, 1131331))
$ update_portrait('st037_01 1', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(1131332)]' (**arg(51, 1131332))
hide p236
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li03.ogg"
get_char('c41') '[convertstrid(1131333)]' (**arg(52, 1131333))
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 9', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro16.ogg"
get_char('c33') '[convertstrid(1131334)]' (**arg(53, 1131334))
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li23.ogg"
get_char('c41') '[convertstrid(1131335)]' (**arg(54, 1131335))
hide p4
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch14.ogg"
get_char('c21') '[convertstrid(1131336)]' (**arg(55, 1131336, size=(1.2)))
hide p3
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1131337)]' (**arg(56, 1131337, size=(1.4)))
hide p1
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro19.ogg"
get_char('c33') '[convertstrid(1131338)]' (**arg(57, 1131338, size=(1.8)))
return