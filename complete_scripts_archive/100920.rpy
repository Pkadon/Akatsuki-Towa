label avg100920:

stop music
scene placeholderbackground
$ update_portrait('sc001_01 2', 'p9', [mid(-11), light], 5)
$ update_narrator('c93')
window show
with fade_in
c93 '[textdict[1218068]]'
hide p9
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
play sfxvoice "bcv_oc002_win_02.ogg"
c13 '[textdict[1218069]]'
hide p1
$ update_portrait('sc001_01 5', 'p9', [mid(-11), light], 5)
c93 '[textdict[1218070]]'
$ update_portrait('sc001_01 6', 'p9', [mid(-11), light], 5)
c93 '[textdict[1218071]]'
hide p9
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
play sfxvoice "bcv_oc002_c01_01.ogg"
c13 '[textdict[1218072]]'
return