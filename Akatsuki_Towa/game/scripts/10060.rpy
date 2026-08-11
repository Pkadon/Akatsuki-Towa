label avg10060(trans=fade_in):

$ play_music("ed7104.ogg")
scene avg_bg_023
$ update_narrator('c13')
window show
with trans
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7047.ogg"
get_char('c13') '[convertstrid(1004862)]' (**arg(1, 1004862))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l_entrance(-3), light, flip], 6)
play sfx2 "other_7048.ogg"
get_char('c21') '[convertstrid(1004863)]' (**arg(2, 1004863))
hide p2
get_char('c6901') '[convertstrid(1004864)]' (**arg(3, 1004864))
get_char('c6901') '[convertstrid(1004865)]' (**arg(4, 1004865))
hide p1
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1004866)]' (**arg(5, 1004866))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
get_char('c6891') '[convertstrid(1004867)]' (**arg(6, 1004867))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1004868)]' (**arg(7, 1004868))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c6891') '[convertstrid(1004869)]' (**arg(8, 1004869))
get_char('c6891') '[convertstrid(1004870)]' (**arg(9, 1004870))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1004871)]' (**arg(10, 1004871))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c6891') '[convertstrid(1004872)]' (**arg(11, 1004872))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1004873)]' (**arg(12, 1004873))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c6891') '[convertstrid(1004874)]' (**arg(13, 1004874))
get_char('c6891') '[convertstrid(1004875)]' (**arg(14, 1004875))
get_char('c6891') '[convertstrid(1004876)]' (**arg(15, 1004876))
hide p1
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1004877)]' (**arg(16, 1004877))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c6891') '[convertstrid(1004878)]' (**arg(17, 1004878))
hide p4
$ update_portrait('sc040_01 2', 'p47', [r(-9), light], 6)
get_char('c473') '[convertstrid(1004879)]' (**arg(18, 1004879))
$ update_portrait('sc040_01 2', 'p47', [r(-9), dark], 5)
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1004880)]' (**arg(19, 1004880))
$ update_portrait('sc039_01 1', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('sc040_01 2', 'p47', [r(-9), light], 6)
get_char('c473') '[convertstrid(1004881)]' (**arg(20, 1004881))
hide p46
$ update_portrait('sc040_01 2', 'p47', [r(-9), dark], 5)
get_char('c6891') '[convertstrid(1004882)]' (**arg(21, 1004882))
get_char('c6891') '[convertstrid(1004883)]' (**arg(22, 1004883))
hide p47
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1004884)]' (**arg(23, 1004884))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
get_char('c6891') '[convertstrid(1004885)]' (**arg(24, 1004885))
get_char('c6891') '[convertstrid(1004886)]' (**arg(25, 1004886))
hide p1
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1004887)]' (**arg(26, 1004887))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
get_char('c6891') '[convertstrid(1004888)]' (**arg(27, 1004888))
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch15.ogg"
get_char('c23') '[convertstrid(1004889)]' (**arg(28, 1004889))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
get_char('c6891') '[convertstrid(1004890)]' (**arg(29, 1004890))
play sfx2 "other_7004.ogg"
get_char('c6891') '[convertstrid(1004891)]' (**arg(30, 1004891))
hide p2
get_char('c0') '[convertstrid(1004893)]' (**arg(31, 1004893))
get_char('c0') '[convertstrid(1123028)]' (**arg(32, 1123028))
get_char('c6891') '[convertstrid(1004894)]' (**arg(33, 1004894))
$ update_portrait('sc039_01 5', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1004895)]' (**arg(34, 1004895))
$ update_portrait('sc039_01 5', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1004896)]' (**arg(35, 1004896))
hide p46
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c6891') '[convertstrid(1004897)]' (**arg(36, 1004897))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1004898)]' (**arg(37, 1004898))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c6891') '[convertstrid(1004899)]' (**arg(38, 1004899))
get_char('c6891') '[convertstrid(1004900)]' (**arg(39, 1004900))
get_char('c6891') '[convertstrid(1004901)]' (**arg(40, 1004901))
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1004902)]' (**arg(41, 1004902))
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1004903)]' (**arg(42, 1004903))
return "avg10060"