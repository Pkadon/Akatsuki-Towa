label avg25293:
stop music

scene placeholderbackground
with fade
play sfx2 "other_7007.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
show oc002_01 20 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1211117]]'
play sfx2 "other_7057.ogg"
hide c2portrait
c00 '[textdict[1211118]]'
c20150 '[textdict[1211119]]'
menu:
    "[textdict[1214995]]":
        call avg25294
    "[textdict[1214996]]":
        call avg25026
return