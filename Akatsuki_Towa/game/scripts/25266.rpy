label avg25266:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7051.ogg"
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1210995)]' (**arg(1, 1210995))
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch28.ogg"
get_char('c23') '[convertstrid(1210996)]' (**arg(2, 1210996))
hide p2
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na07.ogg"
get_char('c13') '[convertstrid(1210997)]' (**arg(3, 1210997))
hide p1
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch17.ogg"
get_char('c23') '[convertstrid(1210998)]' (**arg(4, 1210998))
hide p2
play sfx2 "other_7037.ogg"
get_char('c20133') '[convertstrid(1210999)]' (**arg(5, 1210999))
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1211000)]' (**arg(6, 1211000))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1211001)]' (**arg(7, 1211001))
hide p2
get_char('c20133') '[convertstrid(1211002)]' (**arg(8, 1211002))
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na16.ogg"
get_char('c13') '[convertstrid(1211003)]' (**arg(9, 1211003))
return