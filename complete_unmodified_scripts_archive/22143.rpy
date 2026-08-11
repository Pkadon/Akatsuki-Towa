label avg22143(trans=fade_in):

$ play_music("ED6200.ogg")
scene placeholderbackground
$ update_portrait('oc007_01 5', 'p7', [r(-24), light], 6)
$ update_narrator('c73')
window show
with trans
play sfxvoice "avg_vocal_ar06.ogg"
get_char('c73') '[convertstrid(1128310)]' (**arg(1, 1128310))
$ update_portrait('oc007_01 5', 'p7', [r(-24), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c11') '[convertstrid(1128311)]' (**arg(2, 1128311))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1128312)]' (**arg(3, 1128312))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc007_01 5', 'p7', [r(-24), r_shake, light], 6)
get_char('c73') '[convertstrid(1128313)]' (**arg(4, 1128313))
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1128314)]' (**arg(5, 1128314))
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1128315)]' (**arg(6, 1128315))
hide p2
$ update_portrait('oc007_01 1', 'p7', [r(-24), dark], 5)
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1128316)]' (**arg(7, 1128316))
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc007_01 2', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1128317)]' (**arg(8, 1128317))
$ update_portrait('oc007_01 5', 'p7', [r(-24), light], 6)
play sfxvoice "avg_vocal_ar05.ogg"
get_char('c73') '[convertstrid(1128318)]' (**arg(9, 1128318))
hide p4
$ update_portrait('oc007_01 5', 'p7', [r(-24), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128319)]' (**arg(10, 1128319))
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128320)]' (**arg(11, 1128320))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc007_01 2', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1128321)]' (**arg(12, 1128321))
$ update_portrait('oc007_01 5', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1128322)]' (**arg(13, 1128322))
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1128323)]' (**arg(14, 1128323))
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1128324)]' (**arg(15, 1128324))
$ update_portrait('oc007_01 5', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1128325)]' (**arg(16, 1128325))
hide p3
$ update_portrait('oc007_01 5', 'p7', [r(-24), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c11') '[convertstrid(1128326)]' (**arg(17, 1128326))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc007_01 5', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1128327)]' (**arg(18, 1128327))
hide p1
$ update_portrait('oc007_01 5', 'p7', [r(-24), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1128328)]' (**arg(19, 1128328))
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128329)]' (**arg(20, 1128329))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128330)]' (**arg(21, 1128330))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc007_01 5', 'p7', [r(-24), light], 6)
play sfx2 "common_quest.ogg"
play sfxvoice "avg_vocal_ar07.ogg"
get_char('c73') '[convertstrid(1128331)]' (**arg(22, 1128331))
return "avg22143"