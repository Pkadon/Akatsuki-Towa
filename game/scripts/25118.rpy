label avg25118:
stop music

scene placeholderbackground
with fade
play sfx2 "elc_5006.ogg"
play sfxvoice "avg_vocal_ch31.ogg"
show oc002_01 7 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210345)]]'
hide c2portrait
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210346)]]'
play sfx2 "common_35rewardholy.ogg"
hide c2portrait
show oc001_01 11 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210347)]]'
return