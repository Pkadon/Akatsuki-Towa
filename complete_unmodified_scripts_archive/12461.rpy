label avg12461(trans=fade_in):

$ play_music("ed7300.ogg")
scene avg_bg_071
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1143778)]' (**arg(1, 1143778))
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch20.ogg"
get_char('c23') '[convertstrid(1143779)]' (**arg(2, 1143779))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143780)]' (**arg(3, 1143780))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
play sfx2 "other_7074.ogg"
get_char('c23') '[convertstrid(1143781)]' (**arg(4, 1143781))
stop music
hide p2
play sfx2 "other_7088.ogg"
get_char('c0') '[convertstrid(1143782)]' (**arg(5, 1143782))
play sfx2 "other_7034.ogg"
get_char('c11641') '[convertstrid(1143783)]' (**arg(6, 1143783))
$ play_music("ed7511.ogg")
get_char('c11641') '[convertstrid(1143784)]' (**arg(7, 1143784))
get_char('c11641') '[convertstrid(1143785)]' (**arg(8, 1143785))
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143786)]' (**arg(9, 1143786))
$ update_portrait('oc002_01 16', 'p2', [r(-3), r_shake, light], 6)
play sfx2 "other_7072.ogg"
get_char('c23') '[convertstrid(1143787)]' (**arg(10, 1143787))
$ update_portrait('oc002_01 16', 'p2', [r(-3), dark], 5)
get_char('c11651') '[convertstrid(1143788)]' (**arg(11, 1143788))
get_char('c11651') '[convertstrid(1143789)]' (**arg(12, 1143789))
get_char('c11651') '[convertstrid(1143790)]' (**arg(13, 1143790))
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143791)]' (**arg(14, 1143791))
return "avg12461"