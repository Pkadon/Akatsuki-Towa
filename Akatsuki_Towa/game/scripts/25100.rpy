label avg25100:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1210280)]'
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
play sfx2 "fight_6025.ogg"
c13 '[convertstrid(1210281)]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[convertstrid(1210282)]'
hide p2
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210283)]'
return