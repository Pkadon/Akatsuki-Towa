label avg20013:

play music "ed7150.ogg"
scene avg_bg_014
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1000935)]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch04_b.ogg"
c23 '[convertstrid(1000936)]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1000937)]'
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1000938)]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1000939)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1000940)]'
return