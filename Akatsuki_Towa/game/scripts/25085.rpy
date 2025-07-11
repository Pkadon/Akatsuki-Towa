label avg25085:

scene placeholderbackground
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 5)
window show
with fade_in
c23 '[textdict[1210247]]'
hide p2
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 5)
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na24.ogg"
c13 '[textdict[1210248]]'
return