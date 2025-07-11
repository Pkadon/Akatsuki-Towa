label avg25310:

scene placeholderbackground
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_ch23.ogg"
c23 '[textdict[1211187]]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1211188]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[textdict[1211189]]'
return