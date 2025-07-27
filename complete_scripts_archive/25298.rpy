label avg25298:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch17.ogg"
c23 '[convertstrid(1211146)]'
hide p2
play sfx2 "other_7092.ogg"
c20203 '[convertstrid(1211147)]'
$ update_portrait('oc001_01 13', 'p1', [mid(-2), light], 5)
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na08.ogg"
c13 '[convertstrid(1211148)]'
hide p1
play sfx2 "other_7077.ogg"
c20203 '[convertstrid(1211149)]'
play sfx2 "other_7092.ogg"
c0 '[convertstrid(1211150)]'
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1211151)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[convertstrid(1211152)]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[convertstrid(1211153)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
play sfx2 "common_35rewardholy.ogg"
c13 '[convertstrid(1211154)]'
return