label avg25029:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_ch04.ogg"
c23 '[textdict[1210071]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1210072]]'
hide p1
$ update_portrait('uc001_01 1', 'p2000', [mid(-2), light], 5)
c20003 '[textdict[1210073]]'
return