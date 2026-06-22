label avg10438:

$ play_music("ed7516.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_select.ogg"
get_char('c13') '[convertstrid(1141540)]' (**arg(1, 1141540))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1141541)]' (**arg(2, 1141541, size=(1.2))) with shake
hide p2
$ update_portrait('oc004_01 15', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1141542)]' (**arg(3, 1141542))
$ update_portrait('oc004_01 19', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li16.ogg"
get_char('c41') '[convertstrid(1141543)]' (**arg(4, 1141543))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1141544)]' (**arg(5, 1141544))
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1141545)]' (**arg(6, 1141545))
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1141546)]' (**arg(7, 1141546))
$ update_portrait('oc004_01 18', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1141547)]' (**arg(8, 1141547))
$ update_portrait('oc004_01 19', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1141548)]' (**arg(9, 1141548))
hide p4
$ update_portrait('oc002_01 16', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch14.ogg"
get_char('c23') '[convertstrid(1141549)]' (**arg(10, 1141549))
hide p3
$ update_portrait('oc002_01 16', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1141550)]' (**arg(11, 1141550))
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1141551)]' (**arg(12, 1141551))
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1141552)]' (**arg(13, 1141552))
hide p4
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro02.ogg"
get_char('c31') '[convertstrid(1141553)]' (**arg(14, 1141553))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1141554)]' (**arg(15, 1141554))
hide p3
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1141555)]' (**arg(16, 1141555))
hide p2
$ update_portrait('oc004_01 11', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na19.ogg"
get_char('c13') '[convertstrid(1141556)]' (**arg(17, 1141556))
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li23.ogg"
get_char('c41') '[convertstrid(1141557)]' (**arg(18, 1141557))
return