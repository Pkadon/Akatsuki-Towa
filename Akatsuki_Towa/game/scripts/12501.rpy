label avg12501(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_008
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1150626)]' (**arg(1, 1150626))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), l_shake, light, flip], 6)
play sfx2 "other_7064.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1150627)]' (**arg(2, 1150627))
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150628)]' (**arg(3, 1150628))
hide p3
hide p1
$ update_narrator('c13')
with fade
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1150629)]' (**arg(4, 1150629))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c12071') '[convertstrid(1150630)]' (**arg(5, 1150630))
$ update_portrait('sc011_01 1', 'p19', [l_entrance(-1), light, flip], 6)
get_char('c191') '[convertstrid(1150631)]' (**arg(6, 1150631))
hide p1
$ update_portrait('sc011_01 1', 'p19', [l(-1), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1150632)]' (**arg(7, 1150632))
hide p19
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('sc012_01 4', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1150633)]' (**arg(8, 1150633))
hide p2
$ update_portrait('sc012_01 4', 'p20', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150634)]' (**arg(9, 1150634))
hide p20
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c12071') '[convertstrid(1150635)]' (**arg(10, 1150635))
get_char('c12081') '[convertstrid(1150636)]' (**arg(11, 1150636))
get_char('c12071') '[convertstrid(1150637)]' (**arg(12, 1150637))
hide p1
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1150638)]' (**arg(13, 1150638))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc011_01 2', 'p19', [l(-1), light, flip], 6)
play sfx2 "other_7004.ogg"
get_char('c191') '[convertstrid(1150639)]' (**arg(14, 1150639))
hide p19
play sfx2 "other_7004.ogg"
get_char('c12081') '[convertstrid(1150640)]' (**arg(15, 1150640))
get_char('c12071') '[convertstrid(1150641)]' (**arg(16, 1150641))
hide p3
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1150642)]' (**arg(17, 1150642))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150643)]' (**arg(18, 1150643))
hide p3
get_char('c12081') '[convertstrid(1150644)]' (**arg(19, 1150644))
$ update_portrait('sc012_01 1', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1150645)]' (**arg(20, 1150645))
hide p20
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
get_char('c191') '[convertstrid(1150646)]' (**arg(21, 1150646))
hide p19
get_char('c12081') '[convertstrid(1150647)]' (**arg(22, 1150647))
get_char('c12081') '[convertstrid(1150648)]' (**arg(23, 1150648))
hide p1
$ update_portrait('sc011_01 4', 'p19', [r(-1), light], 6)
get_char('c193') '[convertstrid(1150649)]' (**arg(24, 1150649)) with shake
$ update_portrait('sc011_01 4', 'p19', [r(-1), dark], 5)
get_char('c12081') '[convertstrid(1150650)]' (**arg(25, 1150650))
get_char('c12081') '[convertstrid(1150651)]' (**arg(26, 1150651))
get_char('c12081') '[convertstrid(1150652)]' (**arg(27, 1150652))
hide p19
$ update_portrait('oc003_01 17', 'p3', [r_entrance(-6), light], 6)
get_char('c33') '[convertstrid(1150653)]' (**arg(28, 1150653))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
get_char('c12071') '[convertstrid(1150654)]' (**arg(29, 1150654))
get_char('c12071') '[convertstrid(1150655)]' (**arg(30, 1150655))
get_char('c12071') '[convertstrid(1150656)]' (**arg(31, 1150656))
hide p3
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch20.ogg"
get_char('c23') '[convertstrid(1150657)]' (**arg(32, 1150657))
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
get_char('c191') '[convertstrid(1150658)]' (**arg(33, 1150658))
hide p19
$ update_portrait('sc012_01 3', 'p20', [l(-16), light, flip], 6)
get_char('c201') '[convertstrid(1150659)]' (**arg(34, 1150659))
hide p20
get_char('c12081') '[convertstrid(1150660)]' (**arg(35, 1150660))
get_char('c12081') '[convertstrid(1150661)]' (**arg(36, 1150661))
hide p2
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1150662)]' (**arg(37, 1150662))
hide p3
$ update_narrator('c21')
with fade
$ update_portrait('oc002_01 12', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150663)]' (**arg(38, 1150663))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1150664)]' (**arg(39, 1150664))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150665)]' (**arg(40, 1150665))
hide p2
hide p1
$ update_narrator('c5791')
with fade
play sfxvoice "avg_vocal_li03.ogg"
get_char('c5791') '[convertstrid(1150666)]' (**arg(41, 1150666))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150667)]' (**arg(42, 1150667))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150668)]' (**arg(43, 1150668))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(1150669)]' (**arg(44, 1150669))
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1150670)]' (**arg(45, 1150670))
hide p4
hide p1
get_char('c0') '[convertstrid(1150671)]' (**arg(46, 1150671))
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li28.ogg"
get_char('c41') '[convertstrid(1150672)]' (**arg(47, 1150672))
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1150673)]' (**arg(48, 1150673))
hide p4
$ update_narrator('c43')
with fade
$ update_portrait('oc004_01 4', 'p4', [r_entrance(-5), light], 6)
get_char('c43') '[convertstrid(1150674)]' (**arg(49, 1150674))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
get_char('c12071') '[convertstrid(1150675)]' (**arg(50, 1150675))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1150676)]' (**arg(51, 1150676))
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1150677)]' (**arg(52, 1150677))
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
get_char('c12071') '[convertstrid(1150678)]' (**arg(53, 1150678))
hide p4
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1150679)]' (**arg(54, 1150679))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li12.ogg"
get_char('c41') '[convertstrid(1150680)]' (**arg(55, 1150680))
hide p1
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150681)]' (**arg(56, 1150681))
hide p4
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro12.ogg"
get_char('c31') '[convertstrid(1150682)]' (**arg(57, 1150682))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1150683)]' (**arg(58, 1150683))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150684)]' (**arg(59, 1150684))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150685)]' (**arg(60, 1150685))
hide p3
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1150686)]' (**arg(61, 1150686))
hide p1
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150687)]' (**arg(62, 1150687))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1150688)]' (**arg(63, 1150688))
hide p4
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150689)]' (**arg(64, 1150689))
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150690)]' (**arg(65, 1150690))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1150691)]' (**arg(66, 1150691))
hide p3
hide p2
$ update_narrator('c43')
with fade
$ update_portrait('oc004_01 4', 'p4', [r_entrance(-5), light], 6)
get_char('c43') '[convertstrid(1150692)]' (**arg(67, 1150692))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
play sfx2 "other_7004.ogg"
get_char('c191') '[convertstrid(1150693)]' (**arg(68, 1150693))
hide p19
play sfx2 "other_7004.ogg"
get_char('c12081') '[convertstrid(1150694)]' (**arg(69, 1150694))
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1150695)]' (**arg(70, 1150695))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1150696)]' (**arg(71, 1150696))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
get_char('c191') '[convertstrid(1150697)]' (**arg(72, 1150697))
hide p19
get_char('c12081') '[convertstrid(1150698)]' (**arg(73, 1150698))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1150699)]' (**arg(74, 1150699))
$ update_portrait('oc004_01 7', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(1150700)]' (**arg(75, 1150700))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1150701)]' (**arg(76, 1150701))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1150702)]' (**arg(77, 1150702))
return "avg12501"