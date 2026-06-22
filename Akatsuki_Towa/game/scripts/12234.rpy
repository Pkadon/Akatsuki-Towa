label avg12234:

$ play_music("ED6103.ogg")
scene avg_bg_038
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1121137)]' (**arg(1, 1121137))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c6871') '[convertstrid(1121138)]' (**arg(2, 1121138))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1121139)]' (**arg(3, 1121139))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
get_char('c6871') '[convertstrid(1121140)]' (**arg(4, 1121140))
$ update_portrait('oc002_01 16', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121141)]' (**arg(5, 1121141))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121142)]' (**arg(6, 1121142))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c6871') '[convertstrid(1121143)]' (**arg(7, 1121143))
hide p1
play sfx2 "other_7042.ogg"
get_char('c0') '[convertstrid(1121144)]' (**arg(8, 1121144))
get_char('c9951') '[convertstrid(1121145)]' (**arg(9, 1121145))
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121146)]' (**arg(10, 1121146))
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
get_char('c9951') '[convertstrid(1121147)]' (**arg(11, 1121147))
get_char('c9951') '[convertstrid(1121148)]' (**arg(12, 1121148))
hide p2
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121149)]' (**arg(13, 1121149))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
get_char('c9951') '[convertstrid(1121150)]' (**arg(14, 1121150))
get_char('c9951') '[convertstrid(1121151)]' (**arg(15, 1121151))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121152)]' (**arg(16, 1121152))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch16.ogg"
get_char('c21') '[convertstrid(1121153)]' (**arg(17, 1121153))
$ update_portrait('oc002_01 15', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121154)]' (**arg(18, 1121154))
return