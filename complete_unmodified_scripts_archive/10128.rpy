label avg10128(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_013
$ update_narrator('c50053')
window show
with trans
get_char('c50053') '[convertstrid(1007277)]' (**arg(1, 1007277))
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007278)]' (**arg(2, 1007278))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c50053') '[convertstrid(1007279)]' (**arg(3, 1007279))
$ update_portrait('oc001_01 7', 'p1', [l(-2), l_shake, light, flip], 6)
get_char('c11') '[convertstrid(1007280)]' (**arg(4, 1007280))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
get_char('c50053') '[convertstrid(1007281)]' (**arg(5, 1007281))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007282)]' (**arg(6, 1007282))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
get_char('c50053') '[convertstrid(1007283)]' (**arg(7, 1007283))
$ update_portrait('oc001_01 18', 'p1', [l(-2), l_shake, light, flip], 6)
get_char('c11') '[convertstrid(1007284)]' (**arg(8, 1007284))
$ update_portrait('oc001_01 18', 'p1', [l(-2), dark, flip], 5)
get_char('c50053') '[convertstrid(1007285)]' (**arg(9, 1007285))
scene avg_bg_019
$ update_narrator('c11')
with fade
$ update_portrait('oc001_01 22', 'p1', [l_entrance(-2), light, flip], 6)
play sfx2 "other_7060.ogg"
get_char('c11') '[convertstrid(1007287)]' (**arg(10, 1007287))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7020.ogg"
get_char('c11') '[convertstrid(1007288)]' (**arg(11, 1007288))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1007289)]' (**arg(12, 1007289))
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 19', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007290)]' (**arg(13, 1007290))
$ update_portrait('oc001_01 19', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 19', 'p2', [r_exit(-3), light], 6)
play sfx2 "other_7085.ogg"
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1007291)]' (**arg(14, 1007291))
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), l_shake, light, flip], 6)
play sfx2 "fight_6021.ogg"
get_char('c11') '[convertstrid(1007292)]' (**arg(15, 1007292))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1007293)]' (**arg(16, 1007293))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c11') '[convertstrid(1007294)]' (**arg(17, 1007294))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007295)]' (**arg(18, 1007295))
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na18.ogg"
get_char('c11') '[convertstrid(1007296)]' (**arg(19, 1007296))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1007297)]' (**arg(20, 1007297))
$ play_music("ed7110.ogg")
scene avg_bg_018
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
with fade
get_char('c11') '[convertstrid(1007299)]' (**arg(21, 1007299))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1007300)]' (**arg(22, 1007300))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007301)]' (**arg(23, 1007301))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1007302)]' (**arg(24, 1007302))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007303)]' (**arg(25, 1007303))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1007304)]' (**arg(26, 1007304))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfx2 "common_core.ogg"
play sfxvoice "avg_vocal_na20.ogg"
get_char('c11') '[convertstrid(1007305)]' (**arg(27, 1007305))
hide p1
hide p2
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
with fade
get_char('c23') '[convertstrid(1007306)]' (**arg(28, 1007306))
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c11') '[convertstrid(1007307)]' (**arg(29, 1007307))
$ play_music("ed7106.ogg")
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
play sfx2 "other_7020.ogg"
get_char('c23') '[convertstrid(1007308)]' (**arg(30, 1007308))
hide p1
hide p2
$ update_narrator('c9673')
with fade
play sfx2 "other_7088.ogg"
get_char('c9673') '[convertstrid(1007309)]' (**arg(31, 1007309))
$ update_portrait('oc002_01 2', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1007310)]' (**arg(32, 1007310))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
get_char('c9673') '[convertstrid(1007311)]' (**arg(33, 1007311))
hide p2
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
play sfx2 "common_core.ogg"
get_char('c11') '[convertstrid(1007312)]' (**arg(34, 1007312))
hide p1
get_char('c0') '[convertstrid(1007660)]' (**arg(35, 1007660))
get_char('c9673') '[convertstrid(1007313)]' (**arg(36, 1007313))
get_char('c9673') '[convertstrid(1007314)]' (**arg(37, 1007314))
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007315)]' (**arg(38, 1007315))
$ update_portrait('oc002_01 7', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007316)]' (**arg(39, 1007316))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007661)]' (**arg(40, 1007661))
hide p1
hide p2
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
with fade
get_char('c23') '[convertstrid(1007662)]' (**arg(41, 1007662))
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007317)]' (**arg(42, 1007317))
hide p1
hide p2
get_char('c0') '[convertstrid(1007663)]' (**arg(43, 1007663))
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch09.ogg"
get_char('c23') '[convertstrid(1007318)]' (**arg(44, 1007318))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na19.ogg"
get_char('c11') '[convertstrid(1007664)]' (**arg(45, 1007664))
hide p2
$ update_portrait('oc001_01 5', 'p1', [l(-2), dark, flip], 5)
get_char('c9673') '[convertstrid(1007665)]' (**arg(46, 1007665))
$ update_portrait('oc001_01 6', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007666)]' (**arg(47, 1007666))
$ play_music("ed7113.ogg")
scene avg_bg_021
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
with fade
play sfx2 "other_7064.ogg"
get_char('c11') '[convertstrid(1007320)]' (**arg(48, 1007320))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1007321)]' (**arg(49, 1007321))
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007322)]' (**arg(50, 1007322))
hide p1
hide p2
$ update_narrator('c6543')
with fade
play sfx2 "other_7020.ogg"
get_char('c6543') '[convertstrid(1007323)]' (**arg(51, 1007323))
$ update_portrait('oc002_01 18', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1007324)]' (**arg(52, 1007324))
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
get_char('c6543') '[convertstrid(1007325)]' (**arg(53, 1007325))
hide p2
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007326)]' (**arg(54, 1007326))
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
get_char('c6543') '[convertstrid(1007327)]' (**arg(55, 1007327))
hide p1
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch03_b.ogg"
get_char('c21') '[convertstrid(1007328)]' (**arg(56, 1007328))
hide p2
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c11') '[convertstrid(1007329)]' (**arg(57, 1007329))
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
get_char('c6543') '[convertstrid(1007330)]' (**arg(58, 1007330))
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007331)]' (**arg(59, 1007331))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
get_char('c6543') '[convertstrid(1007333)]' (**arg(60, 1007333))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007334)]' (**arg(61, 1007334))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007335)]' (**arg(62, 1007335))
return "avg10128"