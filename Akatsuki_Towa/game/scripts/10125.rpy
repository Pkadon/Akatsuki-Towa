label avg10125(trans=fade_in):

$ play_music("ED6516.ogg")
scene avg_bg_071
$ update_narrator('c5051')
window show
with trans
play sfx2 "other_7007.ogg"
get_char('c5051') '[convertstrid(1000305)]' (**arg(1, 1000305)) with shake
$ update_portrait('oc001_01 19', 'p1', [r_entrance(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1000306)]' (**arg(2, 1000306))
hide p1
$ update_portrait('uc003_01 4', 'p506', [r(-26), light], 6)
$ update_narrator('c5063')
with fade
get_char('c5063') '[convertstrid(1000307)]' (**arg(3, 1000307))
hide p506
$ update_portrait('uc003_01 4', 'p507', [r(-26), light], 6)
get_char('c5073') '[convertstrid(1000308)]' (**arg(4, 1000308))
hide p507
$ update_narrator('c21')
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
with fade
$ update_portrait('oc002_01 16', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch13.ogg"
get_char('c21') '[convertstrid(1000309)]' (**arg(5, 1000309))
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000310)]' (**arg(6, 1000310))
hide p2
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('st000_01 4', 'p504', [l(-9), l_shake, light, flip], 6)
get_char('c5041') '[convertstrid(1000311)]' (**arg(7, 1000311, size=(1.1)))
$ update_portrait('st000_01 4', 'p504', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000312)]' (**arg(8, 1000312))
hide p504
hide p1
$ update_portrait('st001_01 3', 'p201', [l(-15), light, flip], 6)
$ update_narrator('c2011')
with fade
get_char('c2011') '[convertstrid(1000313)]' (**arg(9, 1000313))
$ update_portrait('st001_01 4', 'p201', [l(-15), l_shake, light, flip], 6)
get_char('c2011') '[convertstrid(1000314)]' (**arg(10, 1000314))
$ update_portrait('st001_01 4', 'p201', [l(-15), dark, flip], 5)
$ update_portrait('uc003_01 4', 'p506', [r(-26), light], 6)
get_char('c5063') '[convertstrid(1000315)]' (**arg(11, 1000315))
hide p506
$ update_portrait('uc003_01 4', 'p507', [r(-26), light], 6)
get_char('c5073') '[convertstrid(1000316)]' (**arg(12, 1000316))
hide p201
hide p507
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
get_char('c21') '[convertstrid(1000317)]' (**arg(13, 1000317))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000318)]' (**arg(14, 1000318))
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1000319)]' (**arg(15, 1000319))
$ update_portrait('oc002_01 15', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000320)]' (**arg(16, 1000320))
hide p2
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('st000_01 3', 'p504', [l(-9), l_shake, light, flip], 6)
get_char('c5041') '[convertstrid(1000321)]' (**arg(17, 1000321))
hide p504
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000322)]' (**arg(18, 1000322))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000323)]' (**arg(19, 1000323))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1000324)]' (**arg(20, 1000324))
hide p2
hide p1
$ update_portrait('uc003_01 4', 'p506', [r(-26), light], 6)
$ update_narrator('c5063')
with fade
play sfx2 "other_7007.ogg"
get_char('c5063') '[convertstrid(1000325)]' (**arg(21, 1000325))
hide p506
$ update_portrait('uc003_01 4', 'p507', [r(-26), r_shake, light], 6)
play sfx2 "fight_6024.ogg"
get_char('c5073') '[convertstrid(1000326)]' (**arg(22, 1000326))
$ update_portrait('uc003_01 4', 'p507', [r(-26), dark], 5)
$ update_portrait('st001_01 3', 'p201', [l(-15), light, flip], 6)
get_char('c2011') '[convertstrid(1000327)]' (**arg(23, 1000327, size=(1.2))) with shake
hide p201
hide p507
$ update_portrait('st000_01 3', 'p504', [l(-9), light, flip], 6)
$ update_narrator('c5041')
with fade
get_char('c5041') '[convertstrid(1000328)]' (**arg(24, 1000328, size=(1.2)))
$ update_portrait('st000_01 3', 'p504', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 15', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na07.ogg"
get_char('c13') '[convertstrid(1000329)]' (**arg(25, 1000329))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000330)]' (**arg(26, 1000330))
hide p504
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000331)]' (**arg(27, 1000331))
hide p2
hide p1
play sfx2 "common_sephi2.ogg"
get_char('c0') '[convertstrid(1000332)]' (**arg(28, 1000332))
$ play_music("ed9997.ogg")
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na24.ogg"
get_char('c13') '[convertstrid(1000333)]' (**arg(29, 1000333))
hide p1
play sfx2 "fight_6017.ogg"
get_char('c0') '[convertstrid(1000334)]' (**arg(30, 1000334))
$ update_portrait('uc003_01 2', 'p506', [l(-26), l_shake, light, flip], 6)
get_char('c5061') '[convertstrid(1000335)]' (**arg(31, 1000335))
hide p506
$ update_portrait('uc003_01 2', 'p507', [l(-26), l_shake, light, flip], 6)
get_char('c5071') '[convertstrid(1000336)]' (**arg(32, 1000336))
$ update_portrait('uc003_01 2', 'p507', [l(-26), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfx2 "other_7085.ogg"
play sfxvoice "bcv_oc001_atk_01.ogg"
get_char('c13') '[convertstrid(1000337)]' (**arg(33, 1000337))
hide p1
$ update_portrait('oc002_01 9', 'p2', [r_midback(-3), light], 6)
play sfx2 "fight_6003.ogg"
play sfxvoice "bcv_oc002_com_01.ogg"
get_char('c23') '[convertstrid(1000338)]' (**arg(34, 1000338, size=(1.2)))
hide p2
$ update_portrait('oc001_01 20', 'p1', [r_midback(-2), light], 6)
play sfx2 "fight_6019.ogg"
play sfxvoice "bcv_oc001_atk_02.ogg"
get_char('c13') '[convertstrid(1000339)]' (**arg(35, 1000339))
hide p507
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('uc003_01 4', 'p506', [l(-26), r_shake, light, flip], 6)
play sfx2 "other_7057.ogg"
get_char('c5061') '[convertstrid(1000340)]' (**arg(36, 1000340))
hide p506
$ update_portrait('st001_01 2', 'p201', [l(-15), light, flip], 6)
get_char('c2011') '[convertstrid(1000341)]' (**arg(37, 1000341))
hide p1
$ update_portrait('st001_01 2', 'p201', [l(-15), dark, flip], 5)
$ update_portrait('st000_01 2', 'p504', [r(-9), light], 6)
get_char('c5043') '[convertstrid(1000342)]' (**arg(38, 1000342))
hide p504
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1000343)]' (**arg(39, 1000343))
hide p201
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('uc003_01 3', 'p507', [l(-26), light, flip], 6)
get_char('c5071') '[convertstrid(1000344)]' (**arg(40, 1000344))
hide p2
$ update_portrait('uc003_01 3', 'p507', [l(-26), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000345)]' (**arg(41, 1000345))
hide p507
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('uc003_01 4', 'p506', [l(-26), light, flip], 6)
play sfx2 "fight_6024.ogg"
get_char('c5061') '[convertstrid(1000346)]' (**arg(42, 1000346))
hide p1
$ update_portrait('uc003_01 4', 'p506', [l(-26), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1000347)]' (**arg(43, 1000347))
return "avg10125"