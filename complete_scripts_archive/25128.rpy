label avg25128:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1210382]]'
hide p1
play sfx2 "other_7004.ogg"
c0 '[textdict[1210383]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210384]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1210385]]'
return