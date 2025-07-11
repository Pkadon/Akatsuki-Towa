label avg25186:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1210617]]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[textdict[1210618]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1210619]]'
return