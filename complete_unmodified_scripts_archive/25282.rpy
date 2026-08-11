label avg25282(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "fight_6025.ogg"
get_char('c13') '[convertstrid(1211068)]' (**arg(1, 1211068))
hide p1
get_char('c20153') '[convertstrid(1211069)]' (**arg(2, 1211069))
$ update_portrait('oc002_01 19', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6010.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
get_char('c23') '[convertstrid(1211070)]' (**arg(3, 1211070))
hide p2
play sfx2 "other_7057.ogg"
get_char('c20153') '[convertstrid(1211071)]' (**arg(4, 1211071))
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1211072)]' (**arg(5, 1211072))
hide p2
get_char('c20153') '[convertstrid(1211073)]' (**arg(6, 1211073))
play sfx2 "other_7086.ogg"
get_char('c0') '[convertstrid(1211074)]' (**arg(7, 1211074))
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1211075)]' (**arg(8, 1211075))
return "avg25282"