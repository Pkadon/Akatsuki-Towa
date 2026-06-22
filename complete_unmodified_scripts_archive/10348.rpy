label avg10348:

$ play_music("ed7567.ogg")
scene avg_bg_031
$ update_narrator('c43')
window show
with fade_in
$ update_portrait('oc004_01 8', 'p4', [r_entrance(-5), light], 6)
play sfxvoice "avg_vocal_li18.ogg"
get_char('c43') '[convertstrid(1131284)]' (**arg(1, 1131284))
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1131285)]' (**arg(2, 1131285))
hide p3
hide p4
$ update_portrait('sc046_01 3', 'p1004', [l(-5), light, flip], 6)
$ update_narrator('c10041')
with fade
get_char('c10041') '[convertstrid(1131286)]' (**arg(3, 1131286))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1131287)]' (**arg(4, 1131287))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1131288)]' (**arg(5, 1131288))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131289)]' (**arg(6, 1131289))
hide p1
$ update_portrait('oc004_01 3', 'p4', [r(-5), r_shake, light], 6)
play sfxvoice "avg_vocal_li26.ogg"
get_char('c43') '[convertstrid(1131290)]' (**arg(7, 1131290, size=(1.2)))
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
$ update_portrait('sc046_01 3', 'p1004', [l(-5), l_shake, light, flip], 6)
get_char('c10041') '[convertstrid(1131291)]' (**arg(8, 1131291))
hide p4
$ update_portrait('sc046_01 3', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1131292)]' (**arg(9, 1131292))
hide p2
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1131293)]' (**arg(10, 1131293))
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('sc046_01 3', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1131294)]' (**arg(11, 1131294))
$ update_portrait('sc046_01 3', 'p1004', [l_exit(-5), light, flip], 6)
play sfx2 "other_7057.ogg"
get_char('c10041') '[convertstrid(1131295)]' (**arg(12, 1131295)) with shake
hide p1004
hide p3
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131296)]' (**arg(13, 1131296, size=(1.4)))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
get_char('c10201') '[convertstrid(1131297)]' (**arg(14, 1131297, size=(1.4)))
$ update_portrait('st037_01 2', 'p236', [l_entrance(-10), l_shake, light, flip], 6)
get_char('c2361') '[convertstrid(1131298)]' (**arg(15, 1131298))
hide p1
$ update_portrait('st037_01 2', 'p236', [l(-10), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1131299)]' (**arg(16, 1131299))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('st037_01 4', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(1131300)]' (**arg(17, 1131300))
hide p2
$ update_portrait('st037_01 4', 'p236', [l(-10), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1131301)]' (**arg(18, 1131301))
$ update_portrait('oc003_01 3', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1131302)]' (**arg(19, 1131302))
hide p236
hide p3
$ update_narrator('c43')
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
with fade
$ update_portrait('oc004_01 3', 'p4', [r_midback(-5), light], 6)
play sfxvoice "avg_vocal_li26.ogg"
get_char('c43') '[convertstrid(1131303)]' (**arg(20, 1131303))
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l_exit(-2), light, flip], 6)
get_char('c11') '[convertstrid(1131304)]' (**arg(21, 1131304))
hide p1
hide p4
$ update_narrator('c43')
with fade
$ update_portrait('oc004_01 16', 'p4', [r_entrance(-5), light], 6)
get_char('c43') '[convertstrid(1131305)]' (**arg(22, 1131305))
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
$ update_portrait('sc046_01 4', 'p1004', [l_entrance(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1131306)]' (**arg(23, 1131306))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1131307)]' (**arg(24, 1131307))
hide p1004
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
get_char('c10211') '[convertstrid(1131308)]' (**arg(25, 1131308, size=(1.2)))
hide p4
play sfx2 "other_7088.ogg"
get_char('c0') '[convertstrid(1131309)]' (**arg(26, 1131309, size=(1.4)))
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1131310)]' (**arg(27, 1131310))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131311)]' (**arg(28, 1131311))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131312)]' (**arg(29, 1131312))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1131313)]' (**arg(30, 1131313))
hide p2
hide p1
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
$ update_narrator('c43')
with fade
get_char('c43') '[convertstrid(1131314)]' (**arg(31, 1131314))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1131315)]' (**arg(32, 1131315))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
get_char('c10211') '[convertstrid(1131316)]' (**arg(33, 1131316))
hide p4
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
get_char('c21') '[convertstrid(1131317)]' (**arg(34, 1131317, size=(1.4)))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131318)]' (**arg(35, 1131318))
hide p2
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1131319)]' (**arg(36, 1131319))
hide p1
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r_entrance(-6), light], 6)
get_char('c33') '[convertstrid(1131320)]' (**arg(37, 1131320))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 3', 'p4', [l_midback(-5), light, flip], 6)
get_char('c41') '[convertstrid(1131321)]' (**arg(38, 1131321, size=(1.2)))
$ update_portrait('oc004_01 3', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 12', 'p3', [r_exit(-6), light], 6)
get_char('c33') '[convertstrid(1131322)]' (**arg(39, 1131322))
hide p3
$ update_portrait('oc001_01 12', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1131323)]' (**arg(40, 1131323))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1131324)]' (**arg(41, 1131324))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131325)]' (**arg(42, 1131325))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1131326)]' (**arg(43, 1131326))
hide p4
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1131327)]' (**arg(44, 1131327))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131328)]' (**arg(45, 1131328))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131329)]' (**arg(46, 1131329))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131330)]' (**arg(47, 1131330))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st037_01 4', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(1131331)]' (**arg(48, 1131331))
$ update_portrait('st037_01 1', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(1131332)]' (**arg(49, 1131332))
hide p1
$ update_portrait('st037_01 1', 'p236', [l(-10), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1131333)]' (**arg(50, 1131333))
hide p236
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
with fade
get_char('c33') '[convertstrid(1131334)]' (**arg(51, 1131334))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1131335)]' (**arg(52, 1131335))
hide p3
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1131336)]' (**arg(53, 1131336, size=(1.2)))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131337)]' (**arg(54, 1131337, size=(1.4)))
hide p4
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7007.ogg"
get_char('c31') '[convertstrid(1131338)]' (**arg(55, 1131338, size=(1.8))) with shake
return