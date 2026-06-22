label avg12701:

$ play_music("ed9999.ogg")
scene avg_bg_050
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1170346)]' (**arg(1, 1170346))
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1170347)]' (**arg(2, 1170347))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1170348)]' (**arg(3, 1170348))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c14071') '[convertstrid(1170349)]' (**arg(4, 1170349))
$ update_portrait('oc001_01 12', 'p1', [r_exit(-2), light], 6)
get_char('c13') '[convertstrid(1170350)]' (**arg(5, 1170350))
hide p1
get_char('c14081') '[convertstrid(1170351)]' (**arg(6, 1170351))
get_char('c14093') '[convertstrid(1170352)]' (**arg(7, 1170352))
get_char('c14081') '[convertstrid(1170353)]' (**arg(8, 1170353))
$ update_portrait('oc001_01 8', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1170354)]' (**arg(9, 1170354))
$ play_music("ed7515.ogg")
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1170355)]' (**arg(10, 1170355))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1170356)]' (**arg(11, 1170356))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1170357)]' (**arg(12, 1170357))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
get_char('c14091') '[convertstrid(1170358)]' (**arg(13, 1170358))
hide p1
get_char('c14083') '[convertstrid(1170359)]' (**arg(14, 1170359))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1170360)]' (**arg(15, 1170360))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1170361)]' (**arg(16, 1170361))
$ update_portrait('oc001_01 4', 'p1', [r_exit(-2), light], 6)
get_char('c13') '[convertstrid(1170362)]' (**arg(17, 1170362))
hide p1
play sfx2 "other_7085.ogg"
get_char('c0') '[convertstrid(1170363)]' (**arg(18, 1170363))
return