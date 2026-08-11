label avg10394(trans=fade_in):

$ play_music("ed7526.ogg")
scene avg_bg_052
$ update_narrator('c13')
window show
with trans
$ update_portrait('oc001_01 19', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1132617)]' (**arg(1, 1132617))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 3', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1132618)]' (**arg(2, 1132618))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132619)]' (**arg(3, 1132619))
$ update_portrait('oc003_01 10', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro18.ogg"
get_char('c31') '[convertstrid(1132620)]' (**arg(4, 1132620))
hide p1
$ update_portrait('oc003_01 10', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1132621)]' (**arg(5, 1132621))
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132622)]' (**arg(6, 1132622))
hide p2
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132623)]' (**arg(7, 1132623))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132624)]' (**arg(8, 1132624))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132625)]' (**arg(9, 1132625))
hide p1
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1132626)]' (**arg(10, 1132626))
hide p2
$ update_portrait('oc001_01 13', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1132627)]' (**arg(11, 1132627))
hide p55
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132628)]' (**arg(12, 1132628))
$ update_portrait('oc003_01 10', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132629)]' (**arg(13, 1132629))
$ update_portrait('oc003_01 10', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na07.ogg"
get_char('c13') '[convertstrid(1132630)]' (**arg(14, 1132630))
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132631)]' (**arg(15, 1132631))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132632)]' (**arg(16, 1132632))
hide p1
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 21', 'p4', [r(-5), r_shake, light], 6)
get_char('c43') '[convertstrid(1132633)]' (**arg(17, 1132633))
$ update_portrait('oc004_01 21', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132634)]' (**arg(18, 1132634))
$ update_portrait('oc003_01 10', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132635)]' (**arg(19, 1132635))
$ update_portrait('oc003_01 21', 'p3', [l(-6), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ro16.ogg"
get_char('c31') '[convertstrid(1132636)]' (**arg(20, 1132636))
$ update_portrait('oc003_01 10', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132637)]' (**arg(21, 1132637))
$ update_portrait('oc003_01 18', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132638)]' (**arg(22, 1132638))
hide p4
$ update_portrait('oc003_01 18', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 3', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1132639)]' (**arg(23, 1132639))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1132640)]' (**arg(24, 1132640))
stop music
scene avg_bg_070
$ update_portrait('oc002_01 20', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
play sfx2 "other_7089.ogg"
get_char('c21') '[convertstrid(1132641)]' (**arg(25, 1132641))
$ play_music("ed7510.ogg")
scene avg_bg_051
show memoryoverlay zorder 2
$ update_narrator('c10493')
with fade
get_char('c10493') '[convertstrid(1132642)]' (**arg(26, 1132642))
get_char('c10493') '[convertstrid(1132643)]' (**arg(27, 1132643))
get_char('c10501') '[convertstrid(1132644)]' (**arg(28, 1132644))
get_char('c10501') '[convertstrid(1132645)]' (**arg(29, 1132645))
get_char('c10493') '[convertstrid(1132646)]' (**arg(30, 1132646))
get_char('c10493') '[convertstrid(1132647)]' (**arg(31, 1132647))
get_char('c10501') '[convertstrid(1132648)]' (**arg(32, 1132648))
get_char('c10501') '[convertstrid(1132649)]' (**arg(33, 1132649))
get_char('c10493') '[convertstrid(1132650)]' (**arg(34, 1132650))
get_char('c10501') '[convertstrid(1132651)]' (**arg(35, 1132651))
get_char('c10493') '[convertstrid(1132652)]' (**arg(36, 1132652))
get_char('c10501') '[convertstrid(1132653)]' (**arg(37, 1132653))
scene avg_bg_070
$ update_portrait('oc002_01 3', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
play sfx2 "other_7089.ogg"
play sfxvoice "avg_vocal_ch14.ogg"
get_char('c21') '[convertstrid(1132654)]' (**arg(38, 1132654)) with shake
scene avg_bg_052
$ update_narrator('c13')
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
with fade
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1132655)]' (**arg(39, 1132655))
$ play_music("ed7526.ogg")
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 3', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch13.ogg"
get_char('c21') '[convertstrid(1132656)]' (**arg(40, 1132656))
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r_midback(-2), light], 6)
get_char('c13') '[convertstrid(1132657)]' (**arg(41, 1132657))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch10.ogg"
get_char('c21') '[convertstrid(1132658)]' (**arg(42, 1132658))
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1132659)]' (**arg(43, 1132659))
$ update_portrait('oc002_01 15', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132660)]' (**arg(44, 1132660))
return "avg10394"