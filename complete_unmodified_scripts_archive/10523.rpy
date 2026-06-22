label avg10523:

$ play_music("ED6303.ogg")
scene avg_bg_108
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
$ update_narrator('c71')
window show
with fade_in
get_char('c71') '[convertstrid(1152085)]' (**arg(1, 1152085))
$ update_portrait('oc007_01 1', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152086)]' (**arg(2, 1152086))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
get_char('c71') '[convertstrid(1152087)]' (**arg(3, 1152087))
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
get_char('c71') '[convertstrid(1152088)]' (**arg(4, 1152088))
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
get_char('c71') '[convertstrid(1152089)]' (**arg(5, 1152089))
hide p4
$ update_portrait('oc007_01 1', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152090)]' (**arg(6, 1152090))
hide p1
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152091)]' (**arg(7, 1152091))
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('oc007_01 2', 'p7', [l(-24), light, flip], 6)
get_char('c71') '[convertstrid(1152092)]' (**arg(8, 1152092))
hide p7
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
get_char('c31') '[convertstrid(1152093)]' (**arg(9, 1152093))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
get_char('c12293') '[convertstrid(1152094)]' (**arg(10, 1152094))
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152095)]' (**arg(11, 1152095))
$ update_portrait('oc004_01 11', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1152096)]' (**arg(12, 1152096))
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
get_char('c12293') '[convertstrid(1152097)]' (**arg(13, 1152097))
hide p3
$ update_portrait('oc004_01 4', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(1152098)]' (**arg(14, 1152098))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
get_char('c12293') '[convertstrid(1152099)]' (**arg(15, 1152099))
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1152100)]' (**arg(16, 1152100))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152101)]' (**arg(17, 1152101))
return