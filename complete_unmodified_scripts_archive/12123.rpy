label avg12123(trans=fade_in):

$ play_music("ED6104.ogg")
scene avg_bg_038
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_select.ogg"
get_char('c13') '[convertstrid(1128233)]' (**arg(1, 1128233))
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128234)]' (**arg(2, 1128234))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
get_char('c9591') '[convertstrid(1128235)]' (**arg(3, 1128235))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1128236)]' (**arg(4, 1128236))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c9591') '[convertstrid(1128237)]' (**arg(5, 1128237))
get_char('c9591') '[convertstrid(1128238)]' (**arg(6, 1128238))
get_char('c9591') '[convertstrid(1128239)]' (**arg(7, 1128239))
get_char('c9591') '[convertstrid(1128240)]' (**arg(8, 1128240))
get_char('c9591') '[convertstrid(1128241)]' (**arg(9, 1128241))
hide p1
play sfx2 "common_tag_2.ogg"
get_char('c0') '[convertstrid(1128242)]' (**arg(10, 1128242))
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1128243)]' (**arg(11, 1128243))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
get_char('c9591') '[convertstrid(1128244)]' (**arg(12, 1128244))
get_char('c9591') '[convertstrid(1128245)]' (**arg(13, 1128245))
play sfx2 "common_quest.ogg"
get_char('c9591') '[convertstrid(1128246)]' (**arg(14, 1128246))
return "avg12123"