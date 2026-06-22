label avg10410:

$ play_music("ed7151.ogg")
scene avg_bg_003
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
window show
with fade_in
play sfx2 "other_7046.ogg"
get_char('c33') '[convertstrid(1140624)]' (**arg(1, 1140624))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 8', 'p5', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji16.ogg"
get_char('c51') '[convertstrid(1140625)]' (**arg(2, 1140625))
$ update_portrait('oc005_01 8', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1140626)]' (**arg(3, 1140626))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 2', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1140627)]' (**arg(4, 1140627))
hide p3
$ update_portrait('oc005_01 2', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140628)]' (**arg(5, 1140628))
hide p5
hide p2
get_char('c0') '[convertstrid(1140629)]' (**arg(6, 1140629))
$ update_portrait('oc005_01 19', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji20.ogg"
get_char('c51') '[convertstrid(1140630)]' (**arg(7, 1140630))
$ update_portrait('oc005_01 7', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1140631)]' (**arg(8, 1140631)) with shake
$ update_portrait('oc005_01 7', 'p5', [l(-6), l_shake, light, flip], 6)
get_char('c51') '[convertstrid(1140632)]' (**arg(9, 1140632))
$ update_portrait('oc005_01 7', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1140633)]' (**arg(10, 1140633, size=(0.9)))
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140634)]' (**arg(11, 1140634, size=(0.9)))
hide p2
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1140635)]' (**arg(12, 1140635))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 19', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1140636)]' (**arg(13, 1140636))
$ update_portrait('oc005_01 12', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1140637)]' (**arg(14, 1140637))
$ update_portrait('oc005_01 12', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1140638)]' (**arg(15, 1140638))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 4', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1140639)]' (**arg(16, 1140639))
hide p3
$ update_portrait('oc005_01 4', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1140640)]' (**arg(17, 1140640))
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc005_01 5', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1140641)]' (**arg(18, 1140641))
hide p2
$ update_portrait('oc005_01 5', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1140642)]' (**arg(19, 1140642))
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1140643)]' (**arg(20, 1140643))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 4', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1140644)]' (**arg(21, 1140644))
$ update_portrait('oc005_01 4', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1140645)]' (**arg(22, 1140645))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140646)]' (**arg(23, 1140646))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 10', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji11.ogg"
get_char('c51') '[convertstrid(1140647)]' (**arg(24, 1140647))
return