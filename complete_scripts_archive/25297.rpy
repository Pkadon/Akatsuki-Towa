label avg25297:

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7092.ogg"
c0 '[convertstrid(1211140)]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1211141)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1211142)]'
hide p1
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[convertstrid(1211143)]'
hide p2
play sfx2 "other_7092.ogg"
c0 '[convertstrid(1211144)]'
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 5)
play sfx2 "other_7080.ogg"
play sfxvoice "avg_vocal_na23.ogg"
c13 '[convertstrid(1211145)]'
return