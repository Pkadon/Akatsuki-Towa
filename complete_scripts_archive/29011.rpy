label avg29011:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[convertstrid(1007043)]'
hide p2
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1007044)]'
hide p1
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch09.ogg"
c23 '[convertstrid(1007045)]'
return