label avg10396:

$ play_music("ed7526.ogg")
scene avg_bg_052
$ update_narrator('c5003')
window show
with fade_in
get_char('c5003') '[convertstrid(1132679)]' (**arg(1, 1132679))
play sfx2 "other_7007.ogg"
get_char('c10521') '[convertstrid(1132680)]' (**arg(2, 1132680)) with shake
$ update_portrait('oc001_01 20', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1132681)]' (**arg(3, 1132681))
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1132682)]' (**arg(4, 1132682))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132683)]' (**arg(5, 1132683))
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1132684)]' (**arg(6, 1132684))
hide p3
hide p4
$ update_portrait('sc048_01 4', 'p55', [r(-7), light], 6)
$ update_narrator('c553')
with fade
get_char('c553') '[convertstrid(1132685)]' (**arg(7, 1132685))
$ update_portrait('sc048_01 4', 'p55', [r(-7), light], 6)
get_char('c553') '[convertstrid(1132686)]' (**arg(8, 1132686))
$ update_portrait('sc048_01 4', 'p55', [r(-7), dark], 5)
get_char('c10521') '[convertstrid(1132687)]' (**arg(9, 1132687, size=(1.3))) with shake
get_char('c10521') '[convertstrid(1132688)]' (**arg(10, 1132688))
hide p55
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1132689)]' (**arg(11, 1132689))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch17.ogg"
get_char('c21') '[convertstrid(1132690)]' (**arg(12, 1132690))
hide p2
get_char('c10521') '[convertstrid(1132691)]' (**arg(13, 1132691))
stop music
hide p1
$ update_portrait('oc004_01 13', 'p4', [r_midback(-5), light], 6)
play sfxvoice "avg_vocal_li10.ogg"
get_char('c43') '[convertstrid(1132692)]' (**arg(14, 1132692))
$ update_portrait('oc004_01 13', 'p4', [r(-5), dark], 5)
$ update_portrait('uc003_04 1', 'p1051', [l(-14), light, flip], 6)
get_char('c10511') '[convertstrid(1132693)]' (**arg(15, 1132693))
$ play_music("ed7510.ogg")
hide p1051
hide p4
play sfx2 "other_7031.ogg"
get_char('c0') '[convertstrid(1132694)]' (**arg(16, 1132694))
play sfx2 "other_7079.ogg"
get_char('c10531') '[convertstrid(1132695)]' (**arg(17, 1132695, size=(1.3)))
play sfx2 "other_7080.ogg"
get_char('c10531') '[convertstrid(1132696)]' (**arg(18, 1132696, size=(1.3)))
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro16.ogg"
get_char('c31') '[convertstrid(1132697)]' (**arg(19, 1132697))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1132698)]' (**arg(20, 1132698))
hide p3
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
get_char('c10521') '[convertstrid(1132699)]' (**arg(21, 1132699))
get_char('c10521') '[convertstrid(1132700)]' (**arg(22, 1132700))
hide p1
$ update_portrait('oc003_01 3', 'p3', [r(-6), r_shake, light], 6)
get_char('c33') '[convertstrid(1132701)]' (**arg(23, 1132701))
$ update_portrait('oc003_01 3', 'p3', [r(-6), dark], 5)
get_char('c10521') '[convertstrid(1132702)]' (**arg(24, 1132702))
hide p3
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li26.ogg"
get_char('c43') '[convertstrid(1132703)]' (**arg(25, 1132703))
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
$ update_portrait('uc003_04 2', 'p1051', [l(-14), light, flip], 6)
get_char('c10511') '[convertstrid(1132704)]' (**arg(26, 1132704))
hide p4
$ update_portrait('uc003_04 2', 'p1051', [l(-14), dark, flip], 5)
$ update_portrait('uc003_04 2', 'p1045', [r(-14), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c10453') '[convertstrid(1132705)]' (**arg(27, 1132705))
hide p1045
get_char('c10543') '[convertstrid(1132706)]' (**arg(28, 1132706))
$ update_portrait('uc003_04 3', 'p1051', [l(-14), light, flip], 6)
get_char('c10511') '[convertstrid(1132707)]' (**arg(29, 1132707))
hide p1051
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132708)]' (**arg(30, 1132708))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132709)]' (**arg(31, 1132709))
hide p3
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 19', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch22.ogg"
get_char('c21') '[convertstrid(1132710)]' (**arg(32, 1132710))
hide p2
$ update_portrait('sc048_01 4', 'p55', [l_midback(-7), light, flip], 6)
get_char('c551') '[convertstrid(1132711)]' (**arg(33, 1132711))
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
play sfx2 "fight_6025.ogg"
get_char('c13') '[convertstrid(1132712)]' (**arg(34, 1132712))
hide p55
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
play sfx2 "fight_6003.ogg"
get_char('c21') '[convertstrid(1132713)]' (**arg(35, 1132713))
hide p1
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 9', 'p3', [r(-6), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c33') '[convertstrid(1132714)]' (**arg(36, 1132714))
hide p2
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7093.ogg"
play sfxvoice "avg_vocal_li23.ogg"
get_char('c41') '[convertstrid(1132715)]' (**arg(37, 1132715))
return