label avg12798:

$ play_music("ed7120.ogg")
scene avg_bg_077
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1177689)]' (**arg(1, 1177689))
get_char('c14821') '[convertstrid(1177690)]' (**arg(2, 1177690))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1177691)]' (**arg(3, 1177691))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c14821') '[convertstrid(1177692)]' (**arg(4, 1177692))
get_char('c14821') '[convertstrid(1177693)]' (**arg(5, 1177693))
get_char('c14821') '[convertstrid(1177694)]' (**arg(6, 1177694))
hide p4
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1177695)]' (**arg(7, 1177695))
$ update_portrait('st061_01 5', 'p1304', [r(-2), dark], 5)
get_char('c14821') '[convertstrid(1177696)]' (**arg(8, 1177696))
hide p1304
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1177697)]' (**arg(9, 1177697))
return