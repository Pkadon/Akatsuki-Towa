label avg26018:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1215624)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1215625)]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1215626)]'
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1215627)]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1215628)]'
hide p2
play sfx2 "other_7002.ogg"
c0 '[convertstrid(1215748)]'
c0 '[convertstrid(1215629)]'
c0 '[convertstrid(1215630)]'
c0 '[convertstrid(1215631)]'
c0 '[convertstrid(1215632)]'
return