label avg10507:

$ play_music("ED6100.ogg")
scene avg_bg_023
$ update_narrator('c12021')
window show
with fade_in
get_char('c12021') '[convertstrid(1150376)]' (**arg(1, 1150376))
get_char('c12021') '[convertstrid(1150377)]' (**arg(2, 1150377))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1150378)]' (**arg(3, 1150378))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c12021') '[convertstrid(1150379)]' (**arg(4, 1150379))
hide p1
$ update_portrait('st041_01 5', 'p240', [r_entrance(-1), light], 6)
get_char('c2403') '[convertstrid(1150380)]' (**arg(5, 1150380))
hide p240
get_char('c0') '[convertstrid(1150381)]' (**arg(6, 1150381))
$ update_portrait('oc003_01 4', 'p3', [r_exit(-6), light], 6)
get_char('c33') '[convertstrid(1150382)]' (**arg(7, 1150382))
hide p3
get_char('c12021') '[convertstrid(1150383)]' (**arg(8, 1150383))
$ update_portrait('st041_01 5', 'p240', [r_entrance(-1), light], 6)
get_char('c2403') '[convertstrid(1150384)]' (**arg(9, 1150384))
$ update_portrait('st041_01 5', 'p240', [r(-1), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150385)]' (**arg(10, 1150385))
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1150386)]' (**arg(11, 1150386))
hide p2
hide p240
$ update_narrator('c2391')
with fade
$ update_portrait('st040_01 1', 'p239', [l_entrance(-19), light, flip], 6)
play sfx2 "other_7020.ogg"
get_char('c2391') '[convertstrid(1150387)]' (**arg(12, 1150387))
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1150388)]' (**arg(13, 1150388))
hide p15
$ update_portrait('sc005_01 1', 'p13', [r_entrance(-17), light], 6)
get_char('c133') '[convertstrid(1150389)]' (**arg(14, 1150389))
$ update_portrait('sc005_01 1', 'p13', [r(-17), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1150390)]' (**arg(15, 1150390))
hide p13
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('sc007_01 5', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1150391)]' (**arg(16, 1150391))
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1150392)]' (**arg(17, 1150392))
$ update_portrait('sc007_01 1', 'p15', [r(-17), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1150393)]' (**arg(18, 1150393))
hide p15
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1150394)]' (**arg(19, 1150394))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1150395)]' (**arg(20, 1150395))
hide p3
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150396)]' (**arg(21, 1150396))
hide p239
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch04_b.ogg"
get_char('c21') '[convertstrid(1150397)]' (**arg(22, 1150397))
hide p2
$ update_portrait('st040_01 4', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1150398)]' (**arg(23, 1150398))
hide p1
$ update_portrait('st040_01 4', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch09.ogg"
get_char('c23') '[convertstrid(1150399)]' (**arg(24, 1150399))
hide p239
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('sc005_01 2', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1150400)]' (**arg(25, 1150400))
$ update_portrait('sc005_01 4', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1150401)]' (**arg(26, 1150401))
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1150402)]' (**arg(27, 1150402))
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1150403)]' (**arg(28, 1150403))
hide p2
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150404)]' (**arg(29, 1150404))
hide p13
hide p1
$ update_portrait('st041_01 1', 'p240', [r(-1), light], 6)
$ update_narrator('c2403')
with fade
get_char('c2403') '[convertstrid(1150405)]' (**arg(30, 1150405))
$ update_portrait('st041_01 1', 'p240', [r(-1), dark], 5)
$ update_portrait('st050_01 5', 'p257', [l(-11), l_shake, light, flip], 6)
get_char('c2571') '[convertstrid(1150406)]' (**arg(31, 1150406))
hide p257
$ update_portrait('st040_01 3', 'p239', [l_entrance(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1150407)]' (**arg(32, 1150407))
$ update_portrait('st040_01 3', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1150408)]' (**arg(33, 1150408))
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1150409)]' (**arg(34, 1150409))
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('st041_01 2', 'p240', [r(-1), r_shake, light], 6)
get_char('c2403') '[convertstrid(1150410)]' (**arg(35, 1150410))
hide p239
$ update_portrait('st041_01 2', 'p240', [r(-1), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150411)]' (**arg(36, 1150411))
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150412)]' (**arg(37, 1150412))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st041_01 3', 'p240', [r(-1), r_shake, light], 6)
get_char('c2403') '[convertstrid(1150413)]' (**arg(38, 1150413))
$ update_portrait('st041_01 1', 'p240', [r(-1), light], 6)
get_char('c2403') '[convertstrid(1150414)]' (**arg(39, 1150414))
hide p3
$ update_portrait('st041_01 1', 'p240', [r(-1), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li03.ogg"
get_char('c41') '[convertstrid(1150415)]' (**arg(40, 1150415))
hide p240
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150416)]' (**arg(41, 1150416))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150417)]' (**arg(42, 1150417))
return