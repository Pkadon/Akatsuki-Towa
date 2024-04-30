label avg25069:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
play sfxvoice "avg_vocal_ch12.ogg"
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210220)]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210221)]]'
menu:
    "[textdict[str(1214997)]]":
        call avg25070
    "[textdict[str(1215000)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210223)]]'
hide c2portrait
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210224)]]'
menu:
    "[textdict[str(1210240)]]":
        call avg25072
    "[textdict[str(1210241)]]":
        call avg25072
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210227)]]'
play sfxvoice "avg_vocal_na10.ogg"
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210228)]]'
menu:
    "[textdict[str(1210240)]]":
        call avg25074
    "[textdict[str(1210241)]]":
        call avg25075
scene placeholderbackground
with fade
stop music
nobody "(Scene 4)"
stop music

scene placeholderbackground
with fade
play sfxvoice "avg_vocal_ch17.ogg"
show oc002_01 11 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210231)]]'
play sfx2 "elc_5005.ogg"
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210232)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 5)"
stop music

scene placeholderbackground
with fade
show oc002_01 17 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210233)]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210234)]]'
menu:
    "[textdict[str(1210240)]]":
        call avg25078
    "[textdict[str(1210241)]]":
        call avg25079
return