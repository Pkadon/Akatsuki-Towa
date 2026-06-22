label avg12581:

$ play_music("ed7151.ogg")
scene avg_bg_080
$ update_narrator('c23')
window show
with fade_in
$ update_portrait('oc002_01 2', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1155400)]' (**arg(1, 1155400))
$ update_portrait('oc002_01 6', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1155401)]' (**arg(2, 1155401))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l_entrance(-17), light, flip], 6)
get_char('c291') '[convertstrid(1155402)]' (**arg(3, 1155402))
hide p2
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1155403)]' (**arg(4, 1155403))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('sc021_01 3', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1155404)]' (**arg(5, 1155404))
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1155405)]' (**arg(6, 1155405))
hide p3
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1155406)]' (**arg(7, 1155406))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1155407)]' (**arg(8, 1155407))
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1155408)]' (**arg(9, 1155408))
hide p4
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch24.ogg"
get_char('c23') '[convertstrid(1155409)]' (**arg(10, 1155409))
return