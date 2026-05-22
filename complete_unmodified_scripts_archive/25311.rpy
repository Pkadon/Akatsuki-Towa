label avg25311:

stop music
scene placeholderbackground
$ update_narrator('c6123')
window show
with fade_in
play sfx2 "other_7092.ogg"
c6123 '[convertstrid(1211191)]'
c6123 '[convertstrid(1211192)]'
play sfx2 "fight_6026.ogg"
c0 '[convertstrid(1211193)]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[convertstrid(1211194)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1211195)]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[convertstrid(1211196)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfx2 "common_quest.ogg"
play sfxvoice "avg_vocal_na03.ogg"
c13 '[convertstrid(1211197)]'
return