label avg26012:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[textdict[1215572]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215573]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
c23 '[textdict[1215574]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215575]]'
hide p1
play sfx2 "other_7002.ogg"
c0 '[textdict[1215743]]'
c0 '[textdict[1215576]]'
c0 '[textdict[1215577]]'
c0 '[textdict[1215578]]'
c0 '[textdict[1215579]]'
return