label avg22124:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1128247)]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[convertstrid(1128248)]'
return