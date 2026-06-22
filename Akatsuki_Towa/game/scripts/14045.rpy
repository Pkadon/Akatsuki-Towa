label avg14045:

$ play_music("ed7102.ogg")
scene avg_bg_023
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1202853)]' (**arg(1, 1202853))
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7047.ogg"
get_char('c13') '[convertstrid(1202854)]' (**arg(2, 1202854))
hide p1
get_char('c0') '[convertstrid(1202855)]' (**arg(3, 1202855))
$ update_portrait('oc002_01 6', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1202856)]' (**arg(4, 1202856))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('sc048_01 1', 'p55', [l_entrance(-7), light, flip], 6)
get_char('c551') '[convertstrid(1202857)]' (**arg(5, 1202857))
hide p2
$ update_portrait('sc048_01 1', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1202858)]' (**arg(6, 1202858))
hide p55
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1202859)]' (**arg(7, 1202859))
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1202860)]' (**arg(8, 1202860))
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1202861)]' (**arg(9, 1202861))
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202862)]' (**arg(10, 1202862))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1202863)]' (**arg(11, 1202863))
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1202864)]' (**arg(12, 1202864))
hide p239
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202865)]' (**arg(13, 1202865))
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202866)]' (**arg(14, 1202866))
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c21') '[convertstrid(1202867)]' (**arg(15, 1202867))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202868)]' (**arg(16, 1202868))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1202869)]' (**arg(17, 1202869))
$ update_portrait('sc048_01 1', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202870)]' (**arg(18, 1202870))
hide p55
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202871)]' (**arg(19, 1202871))
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202872)]' (**arg(20, 1202872))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202873)]' (**arg(21, 1202873))
return