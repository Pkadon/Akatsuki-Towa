label avg25276(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c20203')
window show
with trans
play sfx2 "other_7077.ogg"
get_char('c20203') '[convertstrid(1211045)]' (**arg(1, 1211045))
play sfx2 "other_7092.ogg"
get_char('c0') '[convertstrid(1211046)]' (**arg(2, 1211046))
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1211047)]' (**arg(3, 1211047))
hide p2
$ update_portrait('oc001_01 22', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na17.ogg"
get_char('c13') '[convertstrid(1211048)]' (**arg(4, 1211048))
hide p1
play sfx2 "other_7092.ogg"
get_char('c0') '[convertstrid(1211049)]' (**arg(5, 1211049))
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_ch09.ogg"
get_char('c23') '[convertstrid(1211050)]' (**arg(6, 1211050))
return "avg25276"