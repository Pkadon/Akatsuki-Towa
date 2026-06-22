label avg10126:

$ play_music("ed7511.ogg")
scene avg_bg_071
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "fight_6011.ogg"
play sfxvoice "avg_vocal_na11.ogg"
get_char('c13') '[convertstrid(1000348)]' (**arg(1, 1000348))
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('uc003_01 4', 'p506', [l(-26), light, flip], 6)
get_char('c5061') '[convertstrid(1000349)]' (**arg(2, 1000349))
hide p506
$ update_portrait('uc003_01 4', 'p507', [l(-26), light, flip], 6)
get_char('c5071') '[convertstrid(1000350)]' (**arg(3, 1000350))
hide p507
$ update_portrait('oc002_01 3', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch22.ogg"
get_char('c21') '[convertstrid(1000351)]' (**arg(4, 1000351))
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000352)]' (**arg(5, 1000352))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000353)]' (**arg(6, 1000353))
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000354)]' (**arg(7, 1000354))
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000355)]' (**arg(8, 1000355))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 20', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1000356)]' (**arg(9, 1000356))
$ update_portrait('oc002_01 20', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 15', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1000357)]' (**arg(10, 1000357))
$ update_portrait('oc001_01 15', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000358)]' (**arg(11, 1000358))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000359)]' (**arg(12, 1000359))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1000360)]' (**arg(13, 1000360))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 3', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000361)]' (**arg(14, 1000361))
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000362)]' (**arg(15, 1000362))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1000363)]' (**arg(16, 1000363))
hide p2
$ update_portrait('st000_01 5', 'p504', [l(-9), light, flip], 6)
get_char('c5041') '[convertstrid(1000364)]' (**arg(17, 1000364))
hide p1
$ update_portrait('st000_01 5', 'p504', [l(-9), dark, flip], 5)
$ update_portrait('st001_01 5', 'p201', [r(-15), light], 6)
get_char('c2013') '[convertstrid(1000365)]' (**arg(18, 1000365))
hide p504
$ update_portrait('st001_01 5', 'p201', [r(-15), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1000366)]' (**arg(19, 1000366))
hide p201
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('uc003_01 1', 'p506', [r(-26), light], 6)
get_char('c5063') '[convertstrid(1000367)]' (**arg(20, 1000367))
hide p506
$ update_portrait('uc003_01 1', 'p507', [r(-26), light], 6)
get_char('c5073') '[convertstrid(1000368)]' (**arg(21, 1000368))
hide p507
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1000369)]' (**arg(22, 1000369))
$ play_music("ed7565.ogg")
hide p2
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l_entrance(-8), light, flip], 6)
play sfx2 "other_7021.ogg"
get_char('c561') '[convertstrid(1000370)]' (**arg(23, 1000370))
hide p1
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1000371)]' (**arg(24, 1000371))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000372)]' (**arg(25, 1000372))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
play sfx2 "other_7091.ogg"
get_char('c561') '[convertstrid(1000373)]' (**arg(26, 1000373))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000374)]' (**arg(27, 1000374))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na22.ogg"
get_char('c13') '[convertstrid(1000375)]' (**arg(28, 1000375))
hide p56
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('st000_01 4', 'p504', [l(-9), light, flip], 6)
get_char('c5041') '[convertstrid(1000376)]' (**arg(29, 1000376))
$ update_portrait('st000_01 1', 'p504', [l(-9), light, flip], 6)
play sfx2 "other_7037.ogg"
get_char('c5041') '[convertstrid(1000377)]' (**arg(30, 1000377))
hide p1
$ update_portrait('st000_01 1', 'p504', [l(-9), dark, flip], 5)
$ update_portrait('st001_01 2', 'p201', [r(-15), light], 6)
get_char('c2013') '[convertstrid(1000378)]' (**arg(31, 1000378))
$ update_portrait('st001_01 4', 'p201', [r(-15), light], 6)
play sfx2 "other_7036.ogg"
get_char('c2013') '[convertstrid(1000379)]' (**arg(32, 1000379))
hide p504
$ update_portrait('st001_01 4', 'p201', [r(-15), dark], 5)
$ update_portrait('uc003_01 1', 'p506', [l(-26), light, flip], 6)
get_char('c5061') '[convertstrid(1000380)]' (**arg(33, 1000380))
$ update_portrait('uc003_01 1', 'p506', [l(-26), light, flip], 6)
play sfx2 "other_7037.ogg"
get_char('c5061') '[convertstrid(1000381)]' (**arg(34, 1000381))
hide p506
$ update_portrait('uc003_01 1', 'p507', [l(-26), light, flip], 6)
get_char('c5071') '[convertstrid(1000382)]' (**arg(35, 1000382))
$ update_portrait('uc003_01 1', 'p507', [l(-26), light, flip], 6)
play sfx2 "other_7036.ogg"
get_char('c5071') '[convertstrid(1000383)]' (**arg(36, 1000383))
hide p201
$ update_portrait('uc003_01 1', 'p507', [l(-26), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1000384)]' (**arg(37, 1000384))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000385)]' (**arg(38, 1000385))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1000386)]' (**arg(39, 1000386))
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1000387)]' (**arg(40, 1000387))
hide p507
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000388)]' (**arg(41, 1000388))
$ update_portrait('sc049_01 6', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000389)]' (**arg(42, 1000389))
hide p2
$ update_portrait('sc049_01 6', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('st000_01 1', 'p504', [r(-9), light], 6)
get_char('c5043') '[convertstrid(1000390)]' (**arg(43, 1000390))
hide p504
$ update_portrait('sc052_01 1', 'p59', [r(-25), light], 6)
play sfx2 "other_7088.ogg"
get_char('c593') '[convertstrid(1000391)]' (**arg(44, 1000391))
hide p56
$ update_portrait('sc052_01 1', 'p59', [r(-25), dark], 5)
$ update_portrait('st001_01 4', 'p201', [l(-15), light, flip], 6)
get_char('c2011') '[convertstrid(1000392)]' (**arg(45, 1000392))
hide p201
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
play sfx2 "other_7088.ogg"
get_char('c601') '[convertstrid(1000393)]' (**arg(46, 1000393))
hide p59
$ update_portrait('sc053_01 1', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('uc003_01 1', 'p506', [r(-26), light], 6)
get_char('c5063') '[convertstrid(1000394)]' (**arg(47, 1000394))
hide p506
$ update_portrait('sc050_01 1', 'p57', [r(-19), light], 6)
play sfx2 "fight_6025.ogg"
get_char('c573') '[convertstrid(1000395)]' (**arg(48, 1000395))
hide p60
$ update_portrait('sc050_01 1', 'p57', [r(-19), dark], 5)
$ update_portrait('uc003_01 1', 'p507', [l(-26), light, flip], 6)
get_char('c5071') '[convertstrid(1000396)]' (**arg(49, 1000396))
hide p507
$ update_portrait('sc051_01 1', 'p58', [l(-32), light, flip], 6)
play sfx2 "fight_6025.ogg"
get_char('c581') '[convertstrid(1000397)]' (**arg(50, 1000397))
hide p57
$ update_portrait('sc051_01 1', 'p58', [l(-32), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000398)]' (**arg(51, 1000398))
hide p1
$ update_portrait('oc002_01 6', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1000399)]' (**arg(52, 1000399))
hide p58
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000400)]' (**arg(53, 1000400))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1000401)]' (**arg(54, 1000401))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1000402)]' (**arg(55, 1000402))
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1000403)]' (**arg(56, 1000403))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000404)]' (**arg(57, 1000404))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1000405)]' (**arg(58, 1000405))
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
play sfx2 "other_7020.ogg"
get_char('c561') '[convertstrid(1000406)]' (**arg(59, 1000406))
return