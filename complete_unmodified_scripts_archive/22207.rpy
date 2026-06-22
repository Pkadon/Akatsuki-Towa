label avg22207:

$ play_music("ed7102.ogg")
scene avg_bg_008
$ update_narrator('c7211')
window show
with fade_in
play sfx2 "other_7064.ogg"
get_char('c7211') '[convertstrid(1128623)]' (**arg(1, 1128623))
$ update_portrait('oc002_01 1', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1128624)]' (**arg(2, 1128624))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
get_char('c7211') '[convertstrid(1128625)]' (**arg(3, 1128625))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128626)]' (**arg(4, 1128626))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128627)]' (**arg(5, 1128627))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c7211') '[convertstrid(1128628)]' (**arg(6, 1128628))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128629)]' (**arg(7, 1128629))
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128630)]' (**arg(8, 1128630))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128631)]' (**arg(9, 1128631))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c7211') '[convertstrid(1128632)]' (**arg(10, 1128632))
get_char('c7211') '[convertstrid(1128633)]' (**arg(11, 1128633))
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1128634)]' (**arg(12, 1128634))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1128635)]' (**arg(13, 1128635))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1128636)]' (**arg(14, 1128636))
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
get_char('c7213') '[convertstrid(1128637)]' (**arg(15, 1128637))
get_char('c7213') '[convertstrid(1128638)]' (**arg(16, 1128638))
hide p4
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128639)]' (**arg(17, 1128639))
$ update_portrait('oc001_01 18', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128640)]' (**arg(18, 1128640))
hide p2
get_char('c7213') '[convertstrid(1128641)]' (**arg(19, 1128641))
get_char('c7213') '[convertstrid(1128642)]' (**arg(20, 1128642))
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128643)]' (**arg(21, 1128643))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na10_b.ogg"
get_char('c11') '[convertstrid(1128644)]' (**arg(22, 1128644))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1128645)]' (**arg(23, 1128645))
return