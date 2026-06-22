label avg12031:

$ play_music("ed7105.ogg")
scene avg_bg_022
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7020.ogg"
get_char('c13') '[convertstrid(1120142)]' (**arg(1, 1120142))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfx2 "other_7044.ogg"
get_char('c13') '[convertstrid(1120143)]' (**arg(2, 1120143))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
play sfx2 "other_7047.ogg"
get_char('c10081') '[convertstrid(1120144)]' (**arg(3, 1120144))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120145)]' (**arg(4, 1120145))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c10081') '[convertstrid(1120146)]' (**arg(5, 1120146))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120147)]' (**arg(6, 1120147))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120148)]' (**arg(7, 1120148))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c10091') '[convertstrid(1120149)]' (**arg(8, 1120149))
get_char('c10081') '[convertstrid(1120151)]' (**arg(9, 1120151))
play sfx2 "other_7020.ogg"
get_char('c10091') '[convertstrid(1120152)]' (**arg(10, 1120152))
play sfx2 "other_7048.ogg"
get_char('c10091') '[convertstrid(1120153)]' (**arg(11, 1120153))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04.ogg"
get_char('c13') '[convertstrid(1120154)]' (**arg(12, 1120154))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfx2 "other_7071.ogg"
get_char('c13') '[convertstrid(1120155)]' (**arg(13, 1120155))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
play sfx2 "other_7072.ogg"
get_char('c50051') '[convertstrid(1120156)]' (**arg(14, 1120156))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120157)]' (**arg(15, 1120157))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c50051') '[convertstrid(1120158)]' (**arg(16, 1120158))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120159)]' (**arg(17, 1120159))
return