label avg29117:
stop music

scene placeholderbackground
$ update_portrait('sc001_01 5', 'p9', [mid(-11), light], 5)
window show
with fade_in
c93 '[textdict[1218052]]'
hide p9
$ update_portrait('sc001_01 6', 'p9', [mid(-11), light], 5)
c93 '[textdict[1218053]]'
hide p9
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 5)
play sfxvoice "bcv_oc002_c05_01.ogg"
c13 '[textdict[1218054]]'
hide p1
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 5)
c93 '[textdict[1218055]]'
hide p9
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 5)
c93 '[textdict[1218056]]'
hide p9
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfxvoice "bcv_oc002_atk_01.ogg"
c13 '[textdict[1218057]]'
return