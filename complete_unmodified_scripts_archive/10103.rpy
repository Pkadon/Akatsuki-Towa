label avg10103:

$ play_music("ed7102.ogg")
scene avg_bg_018
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch19.ogg"
get_char('c23') '[convertstrid(1005680)]' (**arg(1, 1005680))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005681)]' (**arg(2, 1005681))
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r_entrance(-5), light], 6)
get_char('c43') '[convertstrid(1005682)]' (**arg(3, 1005682))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1005683)]' (**arg(4, 1005683))
hide p1
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('sc039_01 4', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1005684)]' (**arg(5, 1005684))
hide p4
$ update_portrait('sc039_01 4', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('sc040_01 1', 'p47', [r(-9), light], 6)
get_char('c473') '[convertstrid(1005685)]' (**arg(6, 1005685))
$ play_music("ed7111.ogg")
scene avg_bg_047
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1005686)]' (**arg(7, 1005686))
$ update_portrait('sc044_01 1', 'p51', [l(-7), light, flip], 6)
play sfx2 "other_7047.ogg"
get_char('c511') '[convertstrid(1005687)]' (**arg(8, 1005687))
$ update_portrait('sc044_01 1', 'p51', [l(-7), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1001032)]' (**arg(9, 1001032))
hide p51
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1001032)]' (**arg(10, 1001032))
hide p45
$ update_portrait('sc044_01 2', 'p51', [l(-7), light, flip], 6)
play sfx2 "other_7004.ogg"
get_char('c511') '[convertstrid(1005690)]' (**arg(11, 1005690))
hide p3
$ update_portrait('sc044_01 2', 'p51', [l(-7), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1005691)]' (**arg(12, 1005691))
hide p51
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005692)]' (**arg(13, 1005692))
hide p2
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1005693)]' (**arg(14, 1005693))
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1005694)]' (**arg(15, 1005694))
$ update_portrait('oc003_01 7', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005695)]' (**arg(16, 1005695))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1005696)]' (**arg(17, 1005696))
$ update_portrait('oc003_01 11', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1005697)]' (**arg(18, 1005697))
$ update_portrait('oc003_01 10', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1005698)]' (**arg(19, 1005698))
$ update_portrait('oc003_01 10', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c11') '[convertstrid(1005699)]' (**arg(20, 1005699))
hide p3
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1005700)]' (**arg(21, 1005700))
hide p2
$ update_portrait('sc044_01 2', 'p51', [r(-7), light], 6)
get_char('c513') '[convertstrid(1005701)]' (**arg(22, 1005701))
$ update_portrait('sc044_01 1', 'p51', [r(-7), light], 6)
get_char('c513') '[convertstrid(1005702)]' (**arg(23, 1005702))
$ update_portrait('sc044_01 1', 'p51', [r(-7), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005703)]' (**arg(24, 1005703))
hide p51
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005704)]' (**arg(25, 1005704))
hide p2
$ update_portrait('sc044_01 1', 'p51', [r(-7), light], 6)
get_char('c513') '[convertstrid(1005705)]' (**arg(26, 1005705))
$ update_portrait('sc044_01 2', 'p51', [r(-7), light], 6)
get_char('c513') '[convertstrid(1005706)]' (**arg(27, 1005706))
$ update_portrait('sc044_01 1', 'p51', [r(-7), light], 6)
get_char('c513') '[convertstrid(1005707)]' (**arg(28, 1005707))
$ update_portrait('sc044_01 1', 'p51', [r(-7), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005708)]' (**arg(29, 1005708))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc044_01 3', 'p51', [r(-7), light], 6)
get_char('c513') '[convertstrid(1005709)]' (**arg(30, 1005709))
$ update_portrait('sc044_01 1', 'p51', [r(-7), light], 6)
get_char('c513') '[convertstrid(1005710)]' (**arg(31, 1005710))
hide p1
$ update_portrait('sc044_01 1', 'p51', [r(-7), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005711)]' (**arg(32, 1005711))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc044_01 2', 'p51', [r(-7), light], 6)
get_char('c513') '[convertstrid(1005712)]' (**arg(33, 1005712))
$ update_portrait('sc044_01 1', 'p51', [r(-7), light], 6)
get_char('c513') '[convertstrid(1005713)]' (**arg(34, 1005713))
hide p2
$ update_portrait('sc044_01 1', 'p51', [r(-7), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1005714)]' (**arg(35, 1005714))
hide p4
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c11') '[convertstrid(1005715)]' (**arg(36, 1005715))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005716)]' (**arg(37, 1005716))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc044_01 1', 'p51', [r(-7), light], 6)
get_char('c513') '[convertstrid(1005717)]' (**arg(38, 1005717))
$ update_portrait('sc044_01 2', 'p51', [r(-7), light], 6)
get_char('c513') '[convertstrid(1005718)]' (**arg(39, 1005718))
$ update_portrait('sc044_01 1', 'p51', [r(-7), light], 6)
get_char('c513') '[convertstrid(1005719)]' (**arg(40, 1005719))
$ update_portrait('sc044_01 1', 'p51', [r(-7), light], 6)
get_char('c513') '[convertstrid(1005720)]' (**arg(41, 1005720))
hide p1
$ update_portrait('sc044_01 1', 'p51', [r(-7), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1005721)]' (**arg(42, 1005721))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1005722)]' (**arg(43, 1005722))
hide p51
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r_midback(-2), light], 6)
play sfxvoice "avg_vocal_na11.ogg"
get_char('c13') '[convertstrid(1005723)]' (**arg(44, 1005723))
hide p3
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1005724)]' (**arg(45, 1005724))
$ update_portrait('sc038_01 4', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005725)]' (**arg(46, 1005725))
hide p45
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005726)]' (**arg(47, 1005726))
hide p1
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc044_01 2', 'p51', [r(-7), light], 6)
get_char('c513') '[convertstrid(1005727)]' (**arg(48, 1005727))
hide p2
$ update_portrait('sc044_01 2', 'p51', [r(-7), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005728)]' (**arg(49, 1005728))
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005729)]' (**arg(50, 1005729))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005730)]' (**arg(51, 1005730))
hide p51
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1005731)]' (**arg(52, 1005731))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1005732)]' (**arg(53, 1005732))
hide p2
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('sc044_01 1', 'p51', [r(-7), light], 6)
get_char('c513') '[convertstrid(1005733)]' (**arg(54, 1005733))
hide p4
$ update_portrait('sc044_01 1', 'p51', [r(-7), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001032)]' (**arg(55, 1001032))
hide p51
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005735)]' (**arg(56, 1005735))
hide p3
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005736)]' (**arg(57, 1005736))
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1005737)]' (**arg(58, 1005737))
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005738)]' (**arg(59, 1005738))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005739)]' (**arg(60, 1005739))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1005740)]' (**arg(61, 1005740))
hide p1
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch10.ogg"
get_char('c21') '[convertstrid(1005741)]' (**arg(62, 1005741))
return