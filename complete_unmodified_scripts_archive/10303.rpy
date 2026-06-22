label avg10303:

$ play_music("ed7116.ogg")
scene avg_bg_020
$ update_narrator('c5381')
window show
with fade_in
play sfx2 "other_7020.ogg"
get_char('c5381') '[convertstrid(1130125)]' (**arg(1, 1130125))
$ update_portrait('st033_01 2', 'p232', [r_entrance(-7), light], 6)
get_char('c2323') '[convertstrid(1130126)]' (**arg(2, 1130126))
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
get_char('c5381') '[convertstrid(1130127)]' (**arg(3, 1130127))
get_char('c5381') '[convertstrid(1130128)]' (**arg(4, 1130128))
$ update_portrait('st033_01 2', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1130129)]' (**arg(5, 1130129))
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
get_char('c5381') '[convertstrid(1130130)]' (**arg(6, 1130130))
get_char('c5381') '[convertstrid(1130131)]' (**arg(7, 1130131))
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1130132)]' (**arg(8, 1130132))
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
get_char('c5381') '[convertstrid(1130133)]' (**arg(9, 1130133))
$ update_portrait('st033_01 2', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1130134)]' (**arg(10, 1130134))
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
get_char('c5381') '[convertstrid(1130135)]' (**arg(11, 1130135))
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1130136)]' (**arg(12, 1130136))
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
get_char('c5381') '[convertstrid(1130137)]' (**arg(13, 1130137))
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1130138)]' (**arg(14, 1130138))
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
get_char('c5381') '[convertstrid(1130139)]' (**arg(15, 1130139))
get_char('c5381') '[convertstrid(1130140)]' (**arg(16, 1130140))
$ update_portrait('st033_01 6', 'p232', [r_exit(-7), light], 6)
play sfx2 "other_7020.ogg"
get_char('c2323') '[convertstrid(1130141)]' (**arg(17, 1130141))
hide p232
$ play_music("ed7101.ogg")
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro08.ogg"
get_char('c31') '[convertstrid(1130142)]' (**arg(18, 1130142))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r_entrance(-5), light], 6)
get_char('c43') '[convertstrid(1130143)]' (**arg(19, 1130143))
hide p4
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130144)]' (**arg(20, 1130144))
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130145)]' (**arg(21, 1130145))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1130146)]' (**arg(22, 1130146))
return