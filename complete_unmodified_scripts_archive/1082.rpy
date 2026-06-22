label avg1082:

$ play_music("ed7202.ogg")
scene avg_bg_036
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(2101780)]' (**arg(1, 2101780))
play sfx2 "other_7060.ogg"
get_char('c0') '[convertstrid(2101781)]' (**arg(2, 2101781))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na03_b.ogg"
get_char('c13') '[convertstrid(2101782)]' (**arg(3, 2101782))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2101783)]' (**arg(4, 2101783))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2101784)]' (**arg(5, 2101784))
hide p2
$ update_portrait('oc004_01 1', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101785)]' (**arg(6, 2101785))
hide p4
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
get_char('c31') '[convertstrid(2101786)]' (**arg(7, 2101786))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(2101787)]' (**arg(8, 2101787))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(2101788)]' (**arg(9, 2101788))
hide p4
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2101789)]' (**arg(10, 2101789))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(2101790)]' (**arg(11, 2101790))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(2101791)]' (**arg(12, 2101791))
hide p3
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
get_char('c41') '[convertstrid(2101792)]' (**arg(13, 2101792))
hide p2
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101793)]' (**arg(14, 2101793))
hide p4
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(2101794)]' (**arg(15, 2101794))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101795)]' (**arg(16, 2101795))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101796)]' (**arg(17, 2101796))
hide p4
hide p1
$ update_narrator('c31')
with fade
$ update_portrait('oc003_01 2', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(2101797)]' (**arg(18, 2101797))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li03.ogg"
get_char('c43') '[convertstrid(2101798)]' (**arg(19, 2101798))
hide p3
hide p4
get_char('c0') '[convertstrid(2101799)]' (**arg(20, 2101799))
play sfx2 "fight_6016.ogg"
get_char('c0') '[convertstrid(2101800)]' (**arg(21, 2101800)) with shake
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7016.ogg"
get_char('c41') '[convertstrid(2101801)]' (**arg(22, 2101801))
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(2101802)]' (**arg(23, 2101802))
hide p2
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101803)]' (**arg(24, 2101803)) with shake
hide p4
hide p1
get_char('c0') '[convertstrid(2101804)]' (**arg(25, 2101804))
$ update_portrait('oc004_01 12', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li11.ogg"
get_char('c41') '[convertstrid(2101805)]' (**arg(26, 2101805))
$ update_portrait('oc004_01 12', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_c04_01.ogg"
get_char('c13') '[convertstrid(2101806)]' (**arg(27, 2101806)) with shake
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101807)]' (**arg(28, 2101807))
hide p4
$ update_portrait('oc003_01 8', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(2101808)]' (**arg(29, 2101808))
hide p3
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c21') '[convertstrid(2101809)]' (**arg(30, 2101809))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101810)]' (**arg(31, 2101810))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101811)]' (**arg(32, 2101811))
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101812)]' (**arg(33, 2101812))
hide p4
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(2101813)]' (**arg(34, 2101813))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101814)]' (**arg(35, 2101814))
hide p3
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 13', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2101815)]' (**arg(36, 2101815))
$ update_portrait('oc002_01 13', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101816)]' (**arg(37, 2101816))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101817)]' (**arg(38, 2101817))
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101818)]' (**arg(39, 2101818))
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro03.ogg"
get_char('c31') '[convertstrid(2101819)]' (**arg(40, 2101819))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c13') '[convertstrid(2101820)]' (**arg(41, 2101820))
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2101821)]' (**arg(42, 2101821))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101822)]' (**arg(43, 2101822))
return