label avg25268:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_ch04.ogg"
c23 '[convertstrid(1211006)]'
hide p2
c20133 '[convertstrid(1211007)]'
return