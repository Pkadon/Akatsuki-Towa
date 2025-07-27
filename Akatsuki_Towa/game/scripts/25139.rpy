label avg25139:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1210432)]'
hide p1
play sfx2 "other_7004.ogg"
c0 '[convertstrid(1210433)]'
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[convertstrid(1210434)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[convertstrid(1210435)]'
return