label avg26026:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1215669)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1215670)]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1215671)]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1215672)]'
hide p2
play sfx2 "other_7002.ogg"
c0 '[convertstrid(1215750)]'
c0 '[convertstrid(1215673)]'
c0 '[convertstrid(1215674)]'
return