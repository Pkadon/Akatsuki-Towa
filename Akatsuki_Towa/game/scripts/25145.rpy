label avg25145:

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
play sfx2 "fight_6017.ogg"
c0 '[textdict[1210459]]'
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 5)
play sfx2 "other_7092.ogg"
play sfxvoice "avg_vocal_ch09.ogg"
c23 '[textdict[1210460]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1210461]]'
return