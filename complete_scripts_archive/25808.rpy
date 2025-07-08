label avg25808:
stop music

scene placeholderbackground
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfx2 "other_7034.ogg"
play sfxvoice "avg_vocal_ch27.ogg"
c23 '[textdict[1211272]]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
c13 '[textdict[1211273]]'
return