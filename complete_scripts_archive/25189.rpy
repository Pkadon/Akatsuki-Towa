label avg25189:
stop music

scene placeholderbackground
$ update_portrait('uc003_01 1', 'p2018', [mid(-26), light], 5)
window show
with fade_in
c20183 '[textdict[1210630]]'
hide p2018
$ update_portrait('oc002_01 19', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[textdict[1210631]]'
hide p2
$ update_portrait('uc003_01 3', 'p2018', [mid(-26), light], 5)
c20183 '[textdict[1210632]]'
hide p2018
play sfx2 "other_7086.ogg"
c0 '[textdict[1210633]]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_c02_01.ogg"
c23 '[textdict[1210634]]'
return