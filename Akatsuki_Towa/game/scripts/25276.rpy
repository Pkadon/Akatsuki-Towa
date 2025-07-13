label avg25276:

stop music
scene placeholderbackground
$ update_narrator('c20203')
window show
with fade_in
play sfx2 "other_7077.ogg"
c20203 '[textdict[1211045]]'
play sfx2 "other_7092.ogg"
c0 '[textdict[1211046]]'
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1211047]]'
hide p2
$ update_portrait('oc001_01 22', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na17.ogg"
c13 '[textdict[1211048]]'
hide p1
play sfx2 "other_7092.ogg"
c0 '[textdict[1211049]]'
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_ch09.ogg"
c23 '[textdict[1211050]]'
return