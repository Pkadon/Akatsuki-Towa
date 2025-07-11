label avg25153:

scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "fight_6022.ogg"
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1210483]]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210484]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210485]]'
return