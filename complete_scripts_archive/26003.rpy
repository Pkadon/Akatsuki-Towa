label avg26003:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1215512)]'
hide p2
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1215513)]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1215514)]'
hide p2
play sfx2 "other_7002.ogg"
c0 '[convertstrid(1215737)]'
c0 '[convertstrid(1215515)]'
c0 '[convertstrid(1215516)]'
c0 '[convertstrid(1215517)]'
return