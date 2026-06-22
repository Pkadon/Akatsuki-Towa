label avg12371:

$ play_music("ed7111.ogg")
scene placeholderbackground
$ update_narrator('c5521')
window show
with fade_in
play sfx2 "other_7042.ogg"
get_char('c5521') '[convertstrid(1133882)]' (**arg(1, 1133882))
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1133883)]' (**arg(2, 1133883))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c5521') '[convertstrid(1133884)]' (**arg(3, 1133884))
hide p1
get_char('c10743') '[convertstrid(1133885)]' (**arg(4, 1133885))
play sfx2 "other_7004.ogg"
get_char('c5521') '[convertstrid(1133886)]' (**arg(5, 1133886))
get_char('c10743') '[convertstrid(1133887)]' (**arg(6, 1133887))
get_char('c10743') '[convertstrid(1133888)]' (**arg(7, 1133888))
$ update_portrait('oc004_01 20', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1133889)]' (**arg(8, 1133889))
$ update_portrait('oc004_01 20', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c33') '[convertstrid(1133890)]' (**arg(9, 1133890))
hide p4
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 20', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1133891)]' (**arg(10, 1133891)) with shake
hide p1
get_char('c5521') '[convertstrid(1133892)]' (**arg(11, 1133892))
play sfx2 "common_core.ogg"
get_char('c5521') '[convertstrid(1133893)]' (**arg(12, 1133893))
hide p3
play sfx2 "other_7043.ogg"
get_char('c10743') '[convertstrid(1133894)]' (**arg(13, 1133894))
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1133895)]' (**arg(14, 1133895))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
get_char('c10743') '[convertstrid(1133896)]' (**arg(15, 1133896))
get_char('c10743') '[convertstrid(1133897)]' (**arg(16, 1133897))
play sfx2 "other_7043.ogg"
get_char('c10743') '[convertstrid(1133898)]' (**arg(17, 1133898))
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c11') '[convertstrid(1133899)]' (**arg(18, 1133899))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
play sfx2 "fight_6025.ogg"
get_char('c10743') '[convertstrid(1133900)]' (**arg(19, 1133900)) with shake
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1133901)]' (**arg(20, 1133901))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li29.ogg"
get_char('c43') '[convertstrid(1133902)]' (**arg(21, 1133902))
hide p2
$ update_portrait('oc004_01 10', 'p4', [r(-5), dark], 5)
get_char('c10741') '[convertstrid(1133903)]' (**arg(22, 1133903))
hide p4
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133904)]' (**arg(23, 1133904))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
get_char('c10741') '[convertstrid(1133905)]' (**arg(24, 1133905))
hide p1
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133906)]' (**arg(25, 1133906))
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
get_char('c10741') '[convertstrid(1133907)]' (**arg(26, 1133907))
hide p3
get_char('c5523') '[convertstrid(1133908)]' (**arg(27, 1133908))
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1133909)]' (**arg(28, 1133909))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133910)]' (**arg(29, 1133910))
return