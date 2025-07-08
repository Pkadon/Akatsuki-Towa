label avg25147:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "common_tag_2.ogg"
c13 '[textdict[1210468]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch17.ogg"
c23 '[textdict[1210469]]'
return