label avg29010:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[convertstrid(1007041)]'
hide p2
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na16.ogg"
c13 '[convertstrid(1007042)]'
return