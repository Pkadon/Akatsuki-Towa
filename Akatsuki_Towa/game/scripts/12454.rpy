label avg12454:

$ play_music("ed7515.ogg")
scene avg_bg_036
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1143545)]' (**arg(1, 1143545))
get_char('c0') '[convertstrid(1143546)]' (**arg(2, 1143546))
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1143547)]' (**arg(3, 1143547))
hide p4
play sfx2 "other_7088.ogg"
get_char('c0') '[convertstrid(1143548)]' (**arg(4, 1143548))
stop music
$ update_portrait('oc004_01 12', 'p4', [r(-5), r_shake, light], 6)
get_char('c43') '[convertstrid(1143549)]' (**arg(5, 1143549))
$ update_portrait('oc004_01 12', 'p4', [r(-5), dark], 5)
play sfx2 "other_7080.ogg"
get_char('c10531') '[convertstrid(1143550)]' (**arg(6, 1143550))
$ play_music("ed7511.ogg")
hide p4
get_char('c0') '[convertstrid(1143551)]' (**arg(7, 1143551))
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1143552)]' (**arg(8, 1143552))
return