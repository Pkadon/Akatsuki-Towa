label avg10014(trans=fade_in):

$ play_music("ed7511.ogg")
scene avg_bg_010
$ update_narrator('c5303')
window show
with trans
$ update_portrait('uc002_03 1', 'p530', [r_entrance(-23), light], 6)
play sfx2 "other_7085.ogg"
get_char('c5303') '[convertstrid(1001318)]' (**arg(1, 1001318))
hide p530
$ update_portrait('uc002_03 2', 'p531', [r(-23), r_shake, light], 6)
get_char('c5313') '[convertstrid(1001319)]' (**arg(2, 1001319))
hide p531
$ update_portrait('uc002_03 4', 'p532', [r(-23), light], 6)
get_char('c5323') '[convertstrid(1001320)]' (**arg(3, 1001320))
hide p532
$ update_portrait('uc002_03 2', 'p530', [r(-23), light], 6)
get_char('c5303') '[convertstrid(1001321)]' (**arg(4, 1001321))
$ update_portrait('uc002_03 4', 'p530', [r(-23), light], 6)
get_char('c5303') '[convertstrid(1001322)]' (**arg(5, 1001322))
hide p530
$ update_portrait('uc002_03 2', 'p531', [r(-23), light], 6)
get_char('c5313') '[convertstrid(1001323)]' (**arg(6, 1001323))
hide p531
$ update_portrait('uc002_03 1', 'p530', [r(-23), light], 6)
get_char('c5303') '[convertstrid(1001324)]' (**arg(7, 1001324))
$ update_portrait('uc002_03 1', 'p530', [r(-23), dark], 5)
$ update_portrait('oc001_01 20', 'p1', [l_entrance(-2), light, flip], 6)
play sfx2 "other_7085.ogg"
get_char('c11') '[convertstrid(1001325)]' (**arg(8, 1001325))
hide p1
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001326)]' (**arg(9, 1001326))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('uc002_03 2', 'p530', [r(-23), r_shake, light], 6)
get_char('c5303') '[convertstrid(1001327)]' (**arg(10, 1001327))
hide p530
$ update_portrait('uc002_03 3', 'p531', [r(-23), light], 6)
get_char('c5313') '[convertstrid(1001328)]' (**arg(11, 1001328))
hide p2
$ update_portrait('uc002_03 3', 'p531', [r(-23), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001329)]' (**arg(12, 1001329))
hide p531
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('uc002_03 3', 'p530', [r(-23), r_shake, light], 6)
get_char('c5303') '[convertstrid(1001330)]' (**arg(13, 1001330))
hide p530
$ update_portrait('uc002_03 2', 'p531', [r(-23), light], 6)
get_char('c5313') '[convertstrid(1001331)]' (**arg(14, 1001331))
hide p531
$ update_portrait('uc002_03 4', 'p532', [r(-23), light], 6)
get_char('c5323') '[convertstrid(1001332)]' (**arg(15, 1001332))
hide p3
$ update_portrait('uc002_03 4', 'p532', [r(-23), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001333)]' (**arg(16, 1001333))
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001334)]' (**arg(17, 1001334))
hide p532
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('uc002_03 3', 'p530', [r(-23), light], 6)
get_char('c5303') '[convertstrid(1001335)]' (**arg(18, 1001335))
hide p530
$ update_portrait('uc002_03 4', 'p531', [r(-23), light], 6)
get_char('c5313') '[convertstrid(1001336)]' (**arg(19, 1001336))
hide p1
$ update_portrait('uc002_03 4', 'p531', [r(-23), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1001337)]' (**arg(20, 1001337))
hide p531
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('uc002_03 5', 'p532', [r(-23), light], 6)
get_char('c5323') '[convertstrid(1001338)]' (**arg(21, 1001338))
hide p3
$ update_portrait('uc002_03 5', 'p532', [r(-23), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001339)]' (**arg(22, 1001339))
hide p532
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1001340)]' (**arg(23, 1001340))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001341)]' (**arg(24, 1001341))
hide p3
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001342)]' (**arg(25, 1001342))
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001343)]' (**arg(26, 1001343))
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001344)]' (**arg(27, 1001344))
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001345)]' (**arg(28, 1001345))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 19', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001346)]' (**arg(29, 1001346))
hide p2
$ update_portrait('uc002_03 3', 'p530', [r(-23), light], 6)
get_char('c5303') '[convertstrid(1001347)]' (**arg(30, 1001347))
hide p530
$ update_portrait('uc002_03 3', 'p531', [r(-23), light], 6)
get_char('c5313') '[convertstrid(1001348)]' (**arg(31, 1001348))
hide p1
$ update_portrait('uc002_03 3', 'p531', [r(-23), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001349)]' (**arg(32, 1001349)) with shake
hide p531
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('uc002_03 3', 'p530', [r(-23), light], 6)
get_char('c5303') '[convertstrid(1001350)]' (**arg(33, 1001350))
hide p2
$ update_portrait('uc002_03 3', 'p530', [r(-23), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001351)]' (**arg(34, 1001351))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('uc002_03 3', 'p530', [r(-23), light], 6)
get_char('c5303') '[convertstrid(1001352)]' (**arg(35, 1001352))
$ update_portrait('uc002_03 2', 'p530', [r(-23), r_shake, light], 6)
get_char('c5303') '[convertstrid(1001353)]' (**arg(36, 1001353))
hide p530
$ update_portrait('uc002_03 3', 'p532', [r(-23), light], 6)
play sfx2 "other_7031.ogg"
get_char('c5323') '[convertstrid(1001354)]' (**arg(37, 1001354))
hide p532
play sfx2 "other_7079.ogg"
get_char('c5293') '[convertstrid(1001355)]' (**arg(38, 1001355))
play sfx2 "other_7080.ogg"
get_char('c5293') '[convertstrid(1001356)]' (**arg(39, 1001356))
hide p1
$ update_portrait('oc003_01 21', 'p3', [l(-6), light, flip], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_ro16.ogg"
get_char('c31') '[convertstrid(1001357)]' (**arg(40, 1001357))
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001358)]' (**arg(41, 1001358))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001359)]' (**arg(42, 1001359))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1001360)]' (**arg(43, 1001360))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001361)]' (**arg(44, 1001361))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001362)]' (**arg(45, 1001362))
hide p3
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001363)]' (**arg(46, 1001363))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1001364)]' (**arg(47, 1001364))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001365)]' (**arg(48, 1001365))
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('uc002_03 4', 'p530', [r_midback(-23), light], 6)
get_char('c5303') '[convertstrid(1001366)]' (**arg(49, 1001366))
return "avg10014"