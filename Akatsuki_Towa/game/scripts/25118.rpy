label avg25118:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfx2 "elc_5006.ogg"
play sfxvoice "avg_vocal_ch31.ogg"
c23 '[textdict[1210345]]'
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210346]]'
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 5)
play sfx2 "common_35rewardholy.ogg"
c13 '[textdict[1210347]]'
return