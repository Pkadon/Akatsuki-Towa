label avg25162:

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
play sfx2 "common_tag_2.ogg"
c0 '[textdict[1210530]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210531]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfx2 "elc_5004.ogg"
c13 '[textdict[1210532]]'
return