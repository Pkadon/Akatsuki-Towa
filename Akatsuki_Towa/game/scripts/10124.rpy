label avg10124:

$ play_music("ed7561.ogg")
scene avg_bg_071
$ update_narrator('c21')
window show
with fade_in
$ update_portrait('oc002_01 12', 'p2', [l_entrance(-3), light, flip], 6)
play sfx2 "other_7057.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1000236)]' (**arg(1, 1000236))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7088.ogg"
get_char('c13') '[convertstrid(1000237)]' (**arg(2, 1000237))
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000238)]' (**arg(3, 1000238))
$ update_portrait('oc002_01 15', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000239)]' (**arg(4, 1000239))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1000240)]' (**arg(5, 1000240))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000241)]' (**arg(6, 1000241))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st000_01 3', 'p200', [l(-9), light, flip], 6)
play sfx2 "other_7088.ogg"
get_char('c2001') '[convertstrid(1000242)]' (**arg(7, 1000242))
hide p1
$ update_portrait('st000_01 3', 'p200', [l(-9), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1000243)]' (**arg(8, 1000243))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c13') '[convertstrid(1000244)]' (**arg(9, 1000244))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('st000_01 2', 'p200', [l(-9), light, flip], 6)
get_char('c2001') '[convertstrid(1000245)]' (**arg(10, 1000245))
hide p1
$ update_portrait('st000_01 2', 'p200', [l(-9), dark, flip], 5)
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1000246)]' (**arg(11, 1000246))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1000247)]' (**arg(12, 1000247))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000248)]' (**arg(13, 1000248))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na01.ogg"
get_char('c13') '[convertstrid(1000249)]' (**arg(14, 1000249))
hide p200
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st000_01 1', 'p504', [l(-9), light, flip], 6)
get_char('c5041') '[convertstrid(1000250)]' (**arg(15, 1000250))
$ update_portrait('st000_01 3', 'p504', [l(-9), light, flip], 6)
get_char('c5041') '[convertstrid(1000251)]' (**arg(16, 1000251, size=(1.4))) with shake
hide p1
$ update_portrait('st000_01 3', 'p504', [l(-9), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1000252)]' (**arg(17, 1000252))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000253)]' (**arg(18, 1000253))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('st000_01 4', 'p504', [l(-9), l_shake, light, flip], 6)
get_char('c5041') '[convertstrid(1000254)]' (**arg(19, 1000254))
$ update_portrait('st000_01 3', 'p504', [l(-9), l_shake, light, flip], 6)
get_char('c5041') '[convertstrid(1000255)]' (**arg(20, 1000255))
$ update_portrait('st000_01 3', 'p504', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1000256)]' (**arg(21, 1000256))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1000257)]' (**arg(22, 1000257))
hide p2
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000258)]' (**arg(23, 1000258))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000259)]' (**arg(24, 1000259))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000260)]' (**arg(25, 1000260))
hide p1
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch03.ogg"
get_char('c23') '[convertstrid(1000261)]' (**arg(26, 1000261))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('st000_01 1', 'p504', [l(-9), light, flip], 6)
get_char('c5041') '[convertstrid(1000262)]' (**arg(27, 1000262))
$ update_portrait('st000_01 4', 'p504', [l(-9), light, flip], 6)
get_char('c5041') '[convertstrid(1000263)]' (**arg(28, 1000263))
hide p2
$ update_portrait('st000_01 4', 'p504', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000264)]' (**arg(29, 1000264))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000265)]' (**arg(30, 1000265))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('st000_01 3', 'p504', [l(-9), l_shake, light, flip], 6)
get_char('c5041') '[convertstrid(1000266)]' (**arg(31, 1000266))
$ update_portrait('st000_01 3', 'p504', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000267)]' (**arg(32, 1000267))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000268)]' (**arg(33, 1000268))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st000_01 4', 'p504', [l(-9), light, flip], 6)
get_char('c5041') '[convertstrid(1000269)]' (**arg(34, 1000269))
hide p504
$ update_portrait('oc002_01 15', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1000270)]' (**arg(35, 1000270))
$ update_portrait('oc002_01 15', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000271)]' (**arg(36, 1000271))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1000272)]' (**arg(37, 1000272))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000273)]' (**arg(38, 1000273))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000274)]' (**arg(39, 1000274))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1000275)]' (**arg(40, 1000275))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000276)]' (**arg(41, 1000276))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000277)]' (**arg(42, 1000277))
hide p2
hide p1
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
play sfx2 "other_7074.ogg"
get_char('c13') '[convertstrid(1000278)]' (**arg(43, 1000278))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "other_7072.ogg"
get_char('c13') '[convertstrid(1000279)]' (**arg(44, 1000279))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c4991') '[convertstrid(1000280)]' (**arg(45, 1000280))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000281)]' (**arg(46, 1000281))
hide p1
get_char('c0') '[convertstrid(1000282)]' (**arg(47, 1000282))
get_char('c4991') '[convertstrid(1000283)]' (**arg(48, 1000283))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000284)]' (**arg(49, 1000284))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c4991') '[convertstrid(1000285)]' (**arg(50, 1000285))
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1000286)]' (**arg(51, 1000286))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
get_char('c4991') '[convertstrid(1000287)]' (**arg(52, 1000287))
get_char('c4991') '[convertstrid(1000288)]' (**arg(53, 1000288))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000289)]' (**arg(54, 1000289))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
get_char('c4991') '[convertstrid(1000290)]' (**arg(55, 1000290))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000291)]' (**arg(56, 1000291))
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1000292)]' (**arg(57, 1000292))
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000293)]' (**arg(58, 1000293))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1000294)]' (**arg(59, 1000294))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
get_char('c4991') '[convertstrid(1000295)]' (**arg(60, 1000295))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
play sfx2 "other_7073.ogg"
get_char('c13') '[convertstrid(1000296)]' (**arg(61, 1000296))
hide p1
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
with fade
play sfx2 "other_7088.ogg"
get_char('c23') '[convertstrid(1000297)]' (**arg(62, 1000297))
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1000298)]' (**arg(63, 1000298))
$ update_portrait('oc002_01 23', 'p2', [r(-3), dark], 5)
$ update_portrait('st000_01 5', 'p504', [l(-9), light, flip], 6)
get_char('c5041') '[convertstrid(1000299)]' (**arg(64, 1000299))
hide p2
$ update_portrait('st000_01 5', 'p504', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1000300)]' (**arg(65, 1000300))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
get_char('c13') '[convertstrid(1000301)]' (**arg(66, 1000301))
return