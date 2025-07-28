label avg25282:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "fight_6025.ogg"
c13 '[convertstrid(1211068)]'
hide p1
c20153 '[convertstrid(1211069)]'
$ update_portrait('oc002_01 19', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6010.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[convertstrid(1211070)]'
hide p2
play sfx2 "other_7057.ogg"
c20153 '[convertstrid(1211071)]'
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[convertstrid(1211072)]'
hide p2
c20153 '[convertstrid(1211073)]'
play sfx2 "other_7086.ogg"
c0 '[convertstrid(1211074)]'
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1211075)]'
return