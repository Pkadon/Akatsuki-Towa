label avg12352(trans=fade_in):

$ play_music("ed9999.ogg")
scene avg_bg_050
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7021.ogg"
get_char('c13') '[convertstrid(1133603)]' (**arg(1, 1133603))
$ update_portrait('oc001_01 6', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1133604)]' (**arg(2, 1133604))
hide p1
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1133605)]' (**arg(3, 1133605))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133606)]' (**arg(4, 1133606))
hide p3
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133607)]' (**arg(5, 1133607))
hide p1
$ update_portrait('oc002_01 9', 'p2', [r_exit(-3), light], 6)
get_char('c23') '[convertstrid(1133608)]' (**arg(6, 1133608))
hide p2
hide p4
$ update_narrator('c10931')
with fade
play sfx2 "other_7021.ogg"
get_char('c10931') '[convertstrid(1133609)]' (**arg(7, 1133609))
$ update_portrait('oc002_01 2', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1133610)]' (**arg(8, 1133610))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1133611)]' (**arg(9, 1133611))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
get_char('c10931') '[convertstrid(1133612)]' (**arg(10, 1133612))
hide p1
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133613)]' (**arg(11, 1133613))
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133614)]' (**arg(12, 1133614))
hide p1
get_char('c0') '[convertstrid(1133615)]' (**arg(13, 1133615))
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c21') '[convertstrid(1133616)]' (**arg(14, 1133616))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133617)]' (**arg(15, 1133617))
hide p2
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
get_char('c10941') '[convertstrid(1133618)]' (**arg(16, 1133618))
hide p4
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133619)]' (**arg(17, 1133619))
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133620)]' (**arg(18, 1133620))
$ update_portrait('oc001_01 6', 'p1', [r(-2), dark], 5)
get_char('c10941') '[convertstrid(1133621)]' (**arg(19, 1133621))
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133622)]' (**arg(20, 1133622))
hide p1
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133623)]' (**arg(21, 1133623))
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li30.ogg"
get_char('c43') '[convertstrid(1133624)]' (**arg(22, 1133624))
hide p4
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1133625)]' (**arg(23, 1133625))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
get_char('c10941') '[convertstrid(1133626)]' (**arg(24, 1133626))
get_char('c10941') '[convertstrid(1133627)]' (**arg(25, 1133627))
hide p1
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133628)]' (**arg(26, 1133628))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
get_char('c10941') '[convertstrid(1133629)]' (**arg(27, 1133629))
get_char('c10941') '[convertstrid(1133630)]' (**arg(28, 1133630))
get_char('c10941') '[convertstrid(1133631)]' (**arg(29, 1133631))
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch13.ogg"
get_char('c21') '[convertstrid(1133632)]' (**arg(30, 1133632))
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 6', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li22.ogg"
get_char('c43') '[convertstrid(1133633)]' (**arg(31, 1133633))
hide p2
$ update_portrait('oc004_01 6', 'p4', [r(-5), dark], 5)
get_char('c10941') '[convertstrid(1133634)]' (**arg(32, 1133634))
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1133635)]' (**arg(33, 1133635))
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133636)]' (**arg(34, 1133636))
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133637)]' (**arg(35, 1133637))
$ update_portrait('oc001_01 6', 'p1', [r(-2), dark], 5)
get_char('c10941') '[convertstrid(1133638)]' (**arg(36, 1133638))
get_char('c10941') '[convertstrid(1133639)]' (**arg(37, 1133639))
hide p1
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133640)]' (**arg(38, 1133640))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
get_char('c10941') '[convertstrid(1133641)]' (**arg(39, 1133641))
$ update_portrait('oc002_01 16', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch23.ogg"
get_char('c21') '[convertstrid(1133642)]' (**arg(40, 1133642))
hide p4
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
play sfx2 "other_7004.ogg"
get_char('c13') '[convertstrid(1133643)]' (**arg(41, 1133643))
hide p2
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
get_char('c10941') '[convertstrid(1133644)]' (**arg(42, 1133644))
$ play_music("ed9998.ogg")
scene avg_bg_001
$ update_portrait('oc005_01 2', 'p5', [r(-6), light], 6)
$ update_narrator('c53')
with fade
get_char('c53') '[convertstrid(1133645)]' (**arg(43, 1133645))
$ update_portrait('oc005_01 2', 'p5', [r(-6), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1133646)]' (**arg(44, 1133646))
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1133647)]' (**arg(45, 1133647))
hide p4
$ update_portrait('oc005_01 4', 'p5', [r(-6), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133648)]' (**arg(46, 1133648))
hide p5
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 6)
play sfx2 "other_7018.ogg"
get_char('c13') '[convertstrid(1133649)]' (**arg(47, 1133649))
return "avg12352"