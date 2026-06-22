label avg12180:

$ play_music("ed7110.ogg")
scene avg_bg_003
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
$ update_narrator('c51')
window show
with fade_in
get_char('c51') '[convertstrid(1120580)]' (**arg(1, 1120580))
$ update_portrait('oc005_01 2', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji09.ogg"
get_char('c51') '[convertstrid(1120581)]' (**arg(2, 1120581))
$ update_portrait('oc005_01 16', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji07.ogg"
get_char('c51') '[convertstrid(1120582)]' (**arg(3, 1120582))
$ update_portrait('oc005_01 16', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120583)]' (**arg(4, 1120583))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc005_01 9', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1120584)]' (**arg(5, 1120584))
hide p2
$ update_portrait('oc005_01 9', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120585)]' (**arg(6, 1120585))
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1120586)]' (**arg(7, 1120586))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc005_01 11', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji05.ogg"
get_char('c51') '[convertstrid(1120587)]' (**arg(8, 1120587))
hide p2
$ update_portrait('oc005_01 11', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1120588)]' (**arg(9, 1120588))
return