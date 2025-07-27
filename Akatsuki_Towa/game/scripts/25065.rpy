label avg25065:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_ch20.ogg"
c23 '[convertstrid(1210195)]'
hide p2
play sfx2 "fight_6016.ogg"
play sfxvoice "avg_vocal_ch27.ogg"
c0 '[convertstrid(1210196)]'
$ update_portrait('oc002_01 20', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch21.ogg"
c23 '[convertstrid(1210198)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210199)]'
hide p1
$ update_portrait('oc002_01 19', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1210200)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1210201)]'
return