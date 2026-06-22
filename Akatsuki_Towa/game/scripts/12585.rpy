label avg12585:

$ play_music("ed7151.ogg")
scene avg_bg_080
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1155443)]' (**arg(1, 1155443))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro11.ogg"
get_char('c31') '[convertstrid(1155444)]' (**arg(2, 1155444))
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfx2 "other_7017.ogg"
get_char('c23') '[convertstrid(1155445)]' (**arg(3, 1155445))
hide p3
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7085.ogg"
get_char('c41') '[convertstrid(1155446)]' (**arg(4, 1155446))
hide p4
$ update_portrait('sc021_01 4', 'p29', [l_entrance(-17), light, flip], 6)
get_char('c291') '[convertstrid(1155447)]' (**arg(5, 1155447))
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1155448)]' (**arg(6, 1155448))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1155449)]' (**arg(7, 1155449))
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1155450)]' (**arg(8, 1155450))
hide p2
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1155451)]' (**arg(9, 1155451))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1155452)]' (**arg(10, 1155452))
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1155453)]' (**arg(11, 1155453))
hide p4
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1155454)]' (**arg(12, 1155454))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1155455)]' (**arg(13, 1155455))
hide p3
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155456)]' (**arg(14, 1155456))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155457)]' (**arg(15, 1155457))
hide p29
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1155458)]' (**arg(16, 1155458))
hide p2
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li18.ogg"
get_char('c41') '[convertstrid(1155459)]' (**arg(17, 1155459))
hide p4
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1155460)]' (**arg(18, 1155460))
hide p1
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1155461)]' (**arg(19, 1155461))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1155462)]' (**arg(20, 1155462))
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1155463)]' (**arg(21, 1155463))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1155464)]' (**arg(22, 1155464))
return