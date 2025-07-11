label avg25293:

scene placeholderbackground
$ update_portrait('oc002_01 20', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfx2 "other_7007.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
c23 '[textdict[1211117]]'
hide p2
play sfx2 "other_7057.ogg"
c0 '[textdict[1211118]]'
c20153 '[textdict[1211119]]'
menu:
    extend ""
    "[textdict[1214995]]":
        call avg25294
    "[textdict[1214996]]":
        call avg25026
return