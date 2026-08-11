label avg10444(trans=fade_in):

$ play_music("ed7551.ogg")
scene avg_bg_062
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1141856)]' (**arg(1, 1141856))
$ update_portrait('uc003_04 4', 'p1116', [r(-14), light], 6)
get_char('c11163') '[convertstrid(1141857)]' (**arg(2, 1141857))
hide p1116
$ update_portrait('uc003_04 3', 'p1117', [r_entrance(-14), light], 6)
get_char('c11173') '[convertstrid(1141858)]' (**arg(3, 1141858))
hide p1117
$ update_portrait('uc003_04 4', 'p1118', [r_entrance(-14), light], 6)
get_char('c11183') '[convertstrid(1141859)]' (**arg(4, 1141859))
hide p1118
get_char('c10563') '[convertstrid(1141860)]' (**arg(5, 1141860))
$ update_portrait('st039_01 4', 'p238', [l(-6), l_shake, light, flip], 6)
get_char('c2381') '[convertstrid(1141861)]' (**arg(6, 1141861))
$ update_portrait('st039_01 4', 'p238', [l(-6), dark, flip], 5)
get_char('c10563') '[convertstrid(1141862)]' (**arg(7, 1141862))
$ update_portrait('st039_01 2', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1141863)]' (**arg(8, 1141863))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1141864)]' (**arg(9, 1141864))
hide p238
$ update_portrait('uc003_04 2', 'p1118', [r(-14), light], 6)
$ update_narrator('c11183')
with fade
play sfx2 "other_7018.ogg"
get_char('c11183') '[convertstrid(1141865)]' (**arg(10, 1141865))
hide p1118
$ update_portrait('uc003_04 3', 'p1116', [r_entrance(-14), light], 6)
get_char('c11163') '[convertstrid(1141866)]' (**arg(11, 1141866))
hide p1116
$ update_portrait('uc003_04 3', 'p1117', [r_entrance(-14), light], 6)
get_char('c11173') '[convertstrid(1141867)]' (**arg(12, 1141867))
hide p1117
get_char('c10563') '[convertstrid(1141868)]' (**arg(13, 1141868))
$ update_portrait('st039_01 1', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1141869)]' (**arg(14, 1141869))
scene avg_bg_003
$ update_narrator('c41')
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
with fade
$ update_portrait('oc004_01 16', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1141870)]' (**arg(15, 1141870))
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1141871)]' (**arg(16, 1141871))
hide p4
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 10', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro16.ogg"
get_char('c31') '[convertstrid(1141872)]' (**arg(17, 1141872))
hide p2
$ update_portrait('oc003_01 10', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1141873)]' (**arg(18, 1141873))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1141874)]' (**arg(19, 1141874))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1141875)]' (**arg(20, 1141875))
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1141876)]' (**arg(21, 1141876))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 16', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1141877)]' (**arg(22, 1141877))
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1141878)]' (**arg(23, 1141878))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1141879)]' (**arg(24, 1141879))
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1141880)]' (**arg(25, 1141880))
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1141881)]' (**arg(26, 1141881))
hide p4
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1141882)]' (**arg(27, 1141882))
hide p2
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1141883)]' (**arg(28, 1141883))
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc005_01 7', 'p5', [r(-6), r_shake, light], 6)
get_char('c53') '[convertstrid(1141884)]' (**arg(29, 1141884))
hide p3
$ update_portrait('oc005_01 7', 'p5', [r(-6), dark], 5)
$ update_portrait('oc004_01 16', 'p4', [l(-5), l_shake, light, flip], 6)
play sfx2 "other_7049.ogg"
get_char('c41') '[convertstrid(1141885)]' (**arg(30, 1141885))
scene avg_bg_062
$ update_narrator('c11213')
with fade
play sfx2 "other_7033.ogg"
get_char('c11213') '[convertstrid(1141886)]' (**arg(31, 1141886)) with shake
$ update_portrait('uc003_04 3', 'p1116', [r(-14), r_shake, light], 6)
get_char('c11163') '[convertstrid(1141887)]' (**arg(32, 1141887))
hide p1116
get_char('c10563') '[convertstrid(1141888)]' (**arg(33, 1141888))
$ update_portrait('st039_01 1', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1141889)]' (**arg(34, 1141889))
$ update_portrait('st039_01 1', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1141890)]' (**arg(35, 1141890))
$ update_portrait('st039_01 1', 'p238', [l(-6), dark, flip], 5)
get_char('c10563') '[convertstrid(1141891)]' (**arg(36, 1141891))
$ update_portrait('oc004_01 16', 'p4', [r(-5), r_shake, light], 6)
get_char('c43') '[convertstrid(1141892)]' (**arg(37, 1141892))
hide p4
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1141893)]' (**arg(38, 1141893))
hide p238
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro19.ogg"
get_char('c31') '[convertstrid(1141894)]' (**arg(39, 1141894))
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1141895)]' (**arg(40, 1141895))
hide p3
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('st039_01 4', 'p238', [l_exit(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1141896)]' (**arg(41, 1141896))
hide p238
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
get_char('c13') '[convertstrid(1141897)]' (**arg(42, 1141897))
return "avg10444"