label avg100101:
stop music

stop music
scene placeholderbackground
with fade
play sfxvoice "avg_vocal_na19.ogg"
show oc001_01 1 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1218002]]' with Shake((0, 0, 0, 0), 0.5, dist=20)
stop music
hide c1portrait
show sc001_01 6 as c9portrait at centerpos(-11), zorder 5
c92 '[textdict[1218003]]'
stop music
hide c9portrait
show sc001_01 2 as c9portrait at centerpos(-11), zorder 5
c92 '[textdict[1218004]]'
stop music
hide c9portrait
show sc001_01 1 as c9portrait at centerpos(-11), zorder 5
c92 '[textdict[1218005]]'
stop music
play sfxvoice "avg_vocal_na15.ogg"
hide c9portrait
show oc001_01 11 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1218006]]'
return