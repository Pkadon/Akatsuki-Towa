label avg25140:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7079.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1210436)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210437)]'
return