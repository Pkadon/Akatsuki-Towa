label avg10564:

$ play_music("ED6303.ogg")
scene placeholderbackground
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
$ update_narrator('c43')
window show
with fade_in
get_char('c43') '[convertstrid(1154316)]' (**arg(1, 1154316))
$ update_portrait('oc004_01 11', 'p4', [r(-5), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l_entrance(-18), light, flip], 6)
play sfx2 "other_7088.ogg"
get_char('c161') '[convertstrid(1154317)]' (**arg(2, 1154317))
hide p4
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1154318)]' (**arg(3, 1154318))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154319)]' (**arg(4, 1154319))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1154320)]' (**arg(5, 1154320))
hide p1
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro10.ogg"
get_char('c33') '[convertstrid(1154321)]' (**arg(6, 1154321))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1154322)]' (**arg(7, 1154322))
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1154323)]' (**arg(8, 1154323))
hide p3
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1154324)]' (**arg(9, 1154324))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1154325)]' (**arg(10, 1154325))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1154326)]' (**arg(11, 1154326))
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1154327)]' (**arg(12, 1154327))
hide p4
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch24.ogg"
get_char('c23') '[convertstrid(1154328)]' (**arg(13, 1154328))
hide p16
hide p2
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
$ update_narrator('c161')
with fade
get_char('c161') '[convertstrid(1154329)]' (**arg(14, 1154329))
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1154330)]' (**arg(15, 1154330))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1154331)]' (**arg(16, 1154331))
$ update_portrait('sc008_01 4', 'p16', [l_exit(-18), light, flip], 6)
get_char('c161') '[convertstrid(1154332)]' (**arg(17, 1154332))
hide p16
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154333)]' (**arg(18, 1154333))
hide p1
$ update_portrait('oc004_01 4', 'p4', [r_entrance(-5), light], 6)
get_char('c43') '[convertstrid(1154334)]' (**arg(19, 1154334))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro11.ogg"
get_char('c31') '[convertstrid(1154335)]' (**arg(20, 1154335))
return