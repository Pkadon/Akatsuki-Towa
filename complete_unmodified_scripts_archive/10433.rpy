label avg10433:

$ play_music("ed7526.ogg")
scene avg_bg_036
$ update_narrator('c43')
window show
with fade_in
$ update_portrait('oc004_01 4', 'p4', [r_entrance(-5), light], 6)
get_char('c43') '[convertstrid(1141497)]' (**arg(1, 1141497))
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1141498)]' (**arg(2, 1141498))
$ update_portrait('oc004_01 11', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1141499)]' (**arg(3, 1141499))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc005_01 4', 'p5', [r_exit(-6), light], 6)
play sfxvoice "avg_vocal_ji11.ogg"
get_char('c53') '[convertstrid(1141500)]' (**arg(4, 1141500))
hide p5
$ update_portrait('oc002_01 4', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch13.ogg"
get_char('c23') '[convertstrid(1141501)]' (**arg(5, 1141501))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1141502)]' (**arg(6, 1141502))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1141503)]' (**arg(7, 1141503))
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1141504)]' (**arg(8, 1141504))
hide p3
hide p2
get_char('c0') '[convertstrid(1141505)]' (**arg(9, 1141505))
return