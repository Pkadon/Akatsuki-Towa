label avg25264:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1210984)]'
hide p2
c20133 '[convertstrid(1210985)]'
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na04.ogg"
c13 '[convertstrid(1210986)]'
hide p1
c20133 '[convertstrid(1210987)]'
$ update_portrait('oc002_01 18', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch04.ogg"
c23 '[convertstrid(1210988)]'
return