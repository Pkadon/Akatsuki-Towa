label avg100102:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1218008]]'
hide p1
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 5)
c93 '[textdict[1218009]]'
hide p9
$ update_portrait('sc001_01 2', 'p9', [mid(-11), light], 5)
c93 '[textdict[1218010]]'
hide p9
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 5)
c93 '[textdict[1218011]]'
hide p9
$ update_portrait('sc001_01 2', 'p9', [mid(-11), light], 5)
c93 '[textdict[1218012]]'
hide p9
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[textdict[1218013]]'
return