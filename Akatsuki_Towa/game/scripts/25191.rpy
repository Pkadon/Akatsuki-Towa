label avg25191:

stop music
scene placeholderbackground
$ update_portrait('uc003_01 3', 'p2018', [mid(-26), light], 5)
$ update_narrator('c20183')
window show
with fade_in
c20183 '[textdict[1210638]]'
hide p2018
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1210639]]'
hide p2
$ update_portrait('uc003_01 3', 'p2018', [mid(-26), light], 5)
c20183 '[textdict[1210640]]'
hide p2018
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na11.ogg"
c13 '[textdict[1210641]]'
hide p1
$ update_portrait('uc003_01 3', 'p2018', [mid(-26), light], 5)
c20183 '[textdict[1210642]]'
hide p2018
play sfx2 "other_7086.ogg"
c0 '[textdict[1210643]]'
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
play sfx2 "common_36rewardsp.ogg"
c13 '[textdict[1210644]]'
return