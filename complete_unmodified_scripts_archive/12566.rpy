label avg12566:

$ play_music("ED6200.ogg")
scene avg_bg_080
$ update_portrait('st019_01 3', 'p218', [l(-17), light, flip], 6)
$ update_narrator('c2181')
window show
with fade_in
get_char('c2181') '[convertstrid(1153267)]' (**arg(1, 1153267))
$ update_portrait('st019_01 3', 'p218', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1153268)]' (**arg(2, 1153268))
hide p218
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('st018_01 2', 'p217', [l(-16), light, flip], 6)
get_char('c2171') '[convertstrid(1153269)]' (**arg(3, 1153269))
hide p217
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
with fade
get_char('c41') '[convertstrid(1153270)]' (**arg(4, 1153270))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1153271)]' (**arg(5, 1153271))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1153272)]' (**arg(6, 1153272))
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1153273)]' (**arg(7, 1153273))
hide p3
hide p1
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
with fade
get_char('c33') '[convertstrid(1153274)]' (**arg(8, 1153274))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('st019_01 3', 'p218', [l(-17), light, flip], 6)
get_char('c2181') '[convertstrid(1153275)]' (**arg(9, 1153275))
$ update_portrait('st019_01 3', 'p218', [l(-17), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1153276)]' (**arg(10, 1153276))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('st019_01 5', 'p218', [l(-17), l_shake, light, flip], 6)
get_char('c2181') '[convertstrid(1153277)]' (**arg(11, 1153277))
hide p218
$ update_portrait('st018_01 2', 'p217', [l(-16), light, flip], 6)
get_char('c2171') '[convertstrid(1153278)]' (**arg(12, 1153278))
$ update_portrait('st018_01 2', 'p217', [l(-16), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro02.ogg"
get_char('c33') '[convertstrid(1153279)]' (**arg(13, 1153279))
hide p217
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1153280)]' (**arg(14, 1153280))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1153281)]' (**arg(15, 1153281))
hide p4
hide p1
get_char('c0') '[convertstrid(1153282)]' (**arg(16, 1153282))
get_char('c0') '[convertstrid(1153283)]' (**arg(17, 1153283))
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1153284)]' (**arg(18, 1153284))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1153285)]' (**arg(19, 1153285))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1153286)]' (**arg(20, 1153286))
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1153287)]' (**arg(21, 1153287))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1153288)]' (**arg(22, 1153288))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1153289)]' (**arg(23, 1153289))
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1153290)]' (**arg(24, 1153290))
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1153291)]' (**arg(25, 1153291))
return