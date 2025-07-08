label avg25280:
stop music

scene placeholderbackground
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfx2 "common_tag_2.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1211062]]'
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 5)
c13 '[textdict[1211063]]'
return