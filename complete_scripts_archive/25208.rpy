label avg25208:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7004.ogg"
play sfxvoice "avg_vocal_ch29.ogg"
c23 '[convertstrid(1210718)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1210719)]'
hide p1
$ update_portrait('oc002_01 19', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[convertstrid(1210720)]'
return